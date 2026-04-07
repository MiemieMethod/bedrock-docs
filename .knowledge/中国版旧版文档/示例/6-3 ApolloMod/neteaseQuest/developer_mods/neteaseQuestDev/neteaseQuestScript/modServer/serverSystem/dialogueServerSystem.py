# -*- coding: utf-8 -*-

from neteaseQuestScript.modCommon import dialogueConfig as modConfig
# 用来打印规范格式的log
from .. import logger
from ..serverManager.coroutineMgr import CoroutineMgr
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()
# 编辑器任务状态配置数字，头顶ui的贴图资源名称，两者的映射关系
DIALOGUE_TYPE_MAPPING = {modConfig.APPEAR_CONDITION_DONE: 'done', modConfig.APPEAR_CONDITION_DOING: 'doing', modConfig.APPEAR_CONDITION_TODO: 'todo'}


class DialogueServerSystem(ServerSystem):
    def __init__(self, namespace, system_name):
        ServerSystem.__init__(self, namespace, system_name)
        logger.info('==== %s ====' % 'init dialogueServerSystem')
        self.listen_event()

        self.m_coroutine_mgr = CoroutineMgr()
        self.m_quest_server_system_cache = None  # 任务系统类
        self.m_player_aoi_monitor = False  # 查询玩家身边NPC状态，用于显示头顶图标的标志位

    def get_coroutine_mgr(self):
        return self.m_coroutine_mgr

    def Destroy(self):
        self.m_quest_server_system_cache = None
        self.m_coroutine_mgr.destroy()
        self.un_listen_event()

    def listen_event(self):
        self.DefineEvent(modConfig.DisplayDialogueEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            modConfig.OnScriptTickServer, self, self.on_script_tick_server)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            modConfig.PlayerAttackEntityEvent, self, self.on_player_attack_entity)
        self.ListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.ShiftDialogueEvent, self,
                            self.on_shift_dialogue)

    def un_listen_event(self):
        self.UnDefineEvent(modConfig.DisplayDialogueEvent)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                              modConfig.OnScriptTickServer, self, self.on_script_tick_server)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                              modConfig.PlayerAttackEntityEvent, self, self.on_player_attack_entity)
        self.UnListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.ShiftDialogueEvent, self,
                              self.on_shift_dialogue)

    def detect_player_aoi(self):
        """
        隔16帧执行一次
        取得存在本服的所有玩家id
        获取各自身边100格范围内的实体
        判断是否存在npc并根据任务状态判断该npc头顶应该显示什么状态的ui
        """

        yield -16
        try:
            if not self.m_quest_server_system_cache:
                instance = serverApi.GetSystem(modConfig.QuestModName, modConfig.QuestServerSystemName)
                if instance:
                    self.m_quest_server_system_cache = instance
            if not self.m_quest_server_system_cache:
                self.m_player_aoi_monitor = False
                return
            for player_id in self.m_quest_server_system_cache.get_quest_available_players():
                comp = self.CreateComponent(player_id, modConfig.Minecraft, 'game')
                semaphores = {}
                try:
                    entity_id_list = comp.GetEntitiesAround(player_id, 100, {})
                    for npc_entity_id in [entity_id for entity_id in entity_id_list if entity_id in modConfig.NPC_ENTITY_ID_DICT]:
                        dialogue_id = self.trigger(player_id, npc_entity_id)  # 直接复用接触该npc应该返回什么类型的对话来判断显示什么状态
                        if dialogue_id is None:
                            continue
                        dialogue = modConfig.DialogueConfig.get(dialogue_id)
                        if dialogue:
                            phrase = DIALOGUE_TYPE_MAPPING.get(dialogue['appearCondition'], 'gossip')  # 其余都是闲谈图标
                        else:
                            phrase = 'gossip'
                        semaphores[npc_entity_id] = phrase
                except:
                    import traceback
                    traceback.print_exc()
                    print 'Exception in detect_aoi player_id: {}'.format(player_id)
                self.NotifyToClient(player_id, 'HighlightEvent', {'semaphores': semaphores})
        except:
            import traceback
            traceback.print_exc()
        self.m_player_aoi_monitor = False

    def suspect(self, dialogue, name, engine_identifier):
        if not (None in (name, dialogue.get('npcName')) or dialogue['npcName'] == name):
            return True
        if not (None in (engine_identifier, dialogue.get('npcEngineIdentifier')) or dialogue['npcEngineIdentifier'] == engine_identifier):
            return True

    def trigger(self, player_id, npc_entity_id):
        """
        先找玩家进度的任务
        没有的话找该npc绑定的第一个符合的对话
        无论什么情况
        最多只能返回一个
        :param player_id: player entity id
        :param npc_entity_id: npc entity id
        :return: proper phrase or None
        """
        if not self.m_quest_server_system_cache:
            instance = serverApi.GetSystem(modConfig.QuestModName, modConfig.QuestServerSystemName)
            if instance:
                self.m_quest_server_system_cache = instance
        name = None
        comp = self.CreateComponent(npc_entity_id, modConfig.Minecraft, modConfig.NameComponent)
        if comp:
            name = comp.GetName()
        engine_identifier = None
        comp = self.CreateComponent(npc_entity_id, modConfig.Minecraft, modConfig.EngineTypeComponent)
        if comp:
            engine_identifier = comp.GetEngineTypeStr()
        # TODO: 后续再补细节
        if self.m_quest_server_system_cache:
            for dialogue_id in modConfig.NPC_ENTITY_ID_DICT[npc_entity_id][modConfig.APPEAR_CONDITION_DONE]:
                dialogue = modConfig.DialogueConfig[dialogue_id]
                if self.suspect(dialogue, name, engine_identifier):
                    continue
                quest_id = dialogue['postAppearDone']
                if self.m_quest_server_system_cache.can_submit(player_id, quest_id):
                    return dialogue_id
            for dialogue_id in modConfig.NPC_ENTITY_ID_DICT[npc_entity_id][modConfig.APPEAR_CONDITION_DOING]:
                dialogue = modConfig.DialogueConfig[dialogue_id]
                if self.suspect(dialogue, name, engine_identifier):
                    continue
                quest_id = dialogue['postAppearDoing']
                if self.m_quest_server_system_cache.get_progress(player_id, quest_id):  # TODO: 是否要进行中且未完成
                    return dialogue_id
            for dialogue_id in modConfig.NPC_ENTITY_ID_DICT[npc_entity_id][modConfig.APPEAR_CONDITION_TODO]:
                dialogue = modConfig.DialogueConfig[dialogue_id]
                if self.suspect(dialogue, name, engine_identifier):
                    continue
                quest_id = dialogue['postAppearTodo']
                if self.m_quest_server_system_cache.can_accept(player_id, quest_id):
                    return dialogue_id
        for dialogue_id in modConfig.NPC_ENTITY_ID_DICT[npc_entity_id][modConfig.APPEAR_CONDITION_NONE]:
            dialogue = modConfig.DialogueConfig[dialogue_id]
            if self.suspect(dialogue, name, engine_identifier):
                continue
            return dialogue_id

    def on_shift_dialogue(self, data):
        """
        选项为跳转对话
        需要获取npc名称
        上发到服务端处理后推送
        """

        # player_id, phrase, name = data.get('id'), data.get('phrase'), data.get('dialogue_title')
        player_id, dialogue_id = data.get('id'), data.get('phrase')
        # if not player_id or not phrase:
        if not player_id or not dialogue_id:
            return
        dialogue = modConfig.DialogueConfig.get(dialogue_id)
        if not dialogue:
            logger.error('==== %s ====' % 'dialogue: %s 跳转对话不存在' % dialogue_id)
            return
        comp = self.CreateComponent(dialogue['npcEntityId'], modConfig.Minecraft, modConfig.NameComponent)
        self.push_dialogue(player_id, dialogue_id, (comp.GetName() or '') if comp else '')

    def on_player_attack_entity(self, args):
        """
        玩家攻击实体事件
        判断是不是攻击了配置的npc
        是的话显示配置的对话
        """

        victim_id, player_id = args.get('victimId'), args.get('playerId')
        if victim_id and player_id:
            if victim_id in modConfig.NPC_ENTITY_ID_DICT:
                # 的确是个npc
                args['cancel'] = True
                args['isKnockBack'] = False
                phrase = self.trigger(player_id, victim_id)  # 找对话id，暂时都应该只有对话
                if phrase:
                    comp = self.CreateComponent(victim_id, modConfig.Minecraft, modConfig.NameComponent)
                    self.push_dialogue(player_id, phrase, (comp.GetName() or '') if comp else '')

    def on_script_tick_server(self, *args):
        """
        服务端的逻辑帧，用于驱动协程管理器与定时任务
        """
        self.m_coroutine_mgr.tick()

        if not self.m_player_aoi_monitor:
            self.m_player_aoi_monitor = True
            self.m_coroutine_mgr.start_coroutine(self.detect_player_aoi())

    def push_dialogue(self, player_id, dialogue_id, name=''):
        """
        通知客户端显示对话
        """
        event_data = self.CreateEventData()
        event_data['dialogue_id'] = dialogue_id
        if name:
            event_data['dialogue_title'] = name
        self.NotifyToClient(player_id, modConfig.DisplayDialogueEvent, event_data)
