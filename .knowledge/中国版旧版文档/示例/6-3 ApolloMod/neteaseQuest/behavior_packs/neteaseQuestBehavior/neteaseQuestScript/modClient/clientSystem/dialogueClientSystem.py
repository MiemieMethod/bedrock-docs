# -*- coding: utf-8 -*-

from collections import OrderedDict
from neteaseQuestScript.modCommon import dialogueConfig as modConfig
# 用来打印规范的log
from .. import logger
from ..clientManager.coroutineMgr import CoroutineMgr
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class DialogueClientSystem(ClientSystem):
    """
    该mod的客户端类
    根据服务端推送下来的数据显示任务进度
    根据服务端判断交互的npc通知显示响应对话
    探索是否已经到达关心的地点（寻路型任务）
    根据服务端推送下来的玩家附近的npc位置显示各npc头顶的状态图标
    """

    @property
    def EnableUI(self):
        # 这个标记影响了是否显示本界面预实现的UI
        # 若使用者有自行制作UI的意向，在mod.json中配置屏蔽UI即可，详见mod.json
        return self.mEnableUI

    @EnableUI.setter
    def EnableUI(self, flag):
        self.mEnableUI = flag
        if self.m_dialogue_ui_node:
            self.m_dialogue_ui_node.shift()

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        logger.info('==== %s ====' % 'init dialogueClientSystem')
        self.mEnableUI = False
        self.listen_event()

        self.m_player_id = clientApi.GetLocalPlayerId()
        self.m_attentive_positions = {}  # 任务id与任务点的映射
        self.m_pos_monitor = False  # 控制探测位置逻辑的标志
        # 保存ui界面节点
        self.m_dialogue_ui_node = None
        self.m_semaphore_ui_nodes = OrderedDict()  # 使用了OrderedDict数据结构，用于管理npc头顶状态图标
        self.m_coroutine_mgr = CoroutineMgr()  # 生成器函数管理
        self.m_dialogue_option_handlers = {  # 预设了点击会话各类型选项的执行方法
            "continue": lambda *args: self.m_dialogue_ui_node.next_episode(),
            "todo": lambda *args: self.NotifyToServer(modConfig.AcceptQuestEvent, *args),
            "done": lambda *args: self.NotifyToServer(modConfig.SubmitQuestEvent, *args),
            "shift": lambda *args: self.NotifyToServer(modConfig.ShiftDialogueEvent, *args)
        }

    def get_coroutine_mgr(self):
        return self.m_coroutine_mgr

    def Destroy(self):
        self.m_coroutine_mgr.destroy()
        self.un_listen_event()

    def listen_event(self):
        # self.DefineEvent(modConfig.PassPhraseEvent)
        # self.DefineEvent(modConfig.GetQuestProgressesEvent)
        # self.DefineEvent(modConfig.ArriveEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                            modConfig.UiInitFinishedEvent, self, self.on_ui_init_finished)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                            modConfig.OnScriptTickClient, self, self.on_script_tick_client)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.DisplayDialogueEvent, self,
                            self.on_display_dialogue)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, 'HighlightEvent', self, self.on_highlight)
        self.ListenForEvent(modConfig.QuestModName, modConfig.QuestServerSystemName, modConfig.DisplayQuestEvent, self,
                            self.on_display_quest)

    def un_listen_event(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                              modConfig.UiInitFinishedEvent, self, self.on_ui_init_finished)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                              modConfig.OnScriptTickClient, self, self.on_script_tick_client)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.DisplayDialogueEvent, self,
                              self.on_display_dialogue)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, 'HighlightEvent', self, self.on_highlight)
        self.UnListenForEvent(modConfig.QuestModName, modConfig.QuestServerSystemName, modConfig.DisplayQuestEvent,
                              self, self.on_display_quest)

    def on_ui_init_finished(self, args):
        logger.info('==== %s ====' % '"init UI done": %s' % args)
        # 注册UI 详细解释参照《UI API》
        clientApi.RegisterUI(modConfig.ModName, modConfig.dialogueUIName, modConfig.dialogueUIClsPath,
                             modConfig.dialogueUIScreenDef)
        clientApi.RegisterUI(modConfig.ModName, 'semaphoreUI', 'neteaseQuestScript.modClient.ui.semaphoreClientUI.SemaphoreScreen', 'semaphoreUI.main')
        # 创建UI 详细解释参照《UI API》
        clientApi.CreateUI(modConfig.ModName, modConfig.dialogueUIName, {"isHud": 1})
        self.m_dialogue_ui_node = clientApi.GetUI(modConfig.ModName, modConfig.dialogueUIName)
        if self.m_dialogue_ui_node:
            self.m_dialogue_ui_node.initialize()
        else:
            logger.error('==== %s ====' % 'create UI: %s failed' % modConfig.dialogueUIScreenDef)
        # 这里取任务进度
        event_data = self.CreateEventData()
        event_data["id"] = self.m_player_id
        self.NotifyToServer(modConfig.GetQuestProgressesEvent, event_data)
        comp = self.CreateComponent(clientApi.GetLevelId(), modConfig.Minecraft, 'game')
        comp.ShowHealthBar(True)
        self.supply()

    # 监听引擎ScriptTickClientEvent事件，引擎会执行该tick回调，1秒钟30帧
    def on_script_tick_client(self, *args):
        """
        客户端的逻辑帧，用于驱动协程管理器与定时任务
        """
        self.m_coroutine_mgr.tick()

        if not self.m_pos_monitor:
            self.m_pos_monitor = True
            self.m_coroutine_mgr.start_coroutine(self.detect_pos())  # 生成器函数的最末尾会将标志设置为False，又会重新执行一轮逻辑

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        pass

    def supply(self):
        """
        附近的NPC变多了
        创建一个头顶UI的节点
        """
        semaphore_ui_node = clientApi.CreateUI(modConfig.ModName, "semaphoreUI", {
            "bindEntityId": self.m_player_id,  # 先绑玩家头上，后续有逻辑转移挂接的实体，字典其余字段请查阅modsdk文档中对创建ui的说明
            "bindOffset": (0, 2.33, 0),
            "autoScale": 0
        })
        if semaphore_ui_node:
            self.m_semaphore_ui_nodes[len(self.m_semaphore_ui_nodes)] = semaphore_ui_node  # key使用字典的长度一定不会重复，因为只增不减

    def on_highlight(self, data):
        """
        服务端推下来附近的NPC状态
        根据这个状态显示NPC头顶的UI
        """

        # print 'on_highlight', data
        if not self.m_semaphore_ui_nodes:
            return
        semaphores = data['semaphores']
        demand = len(semaphores)
        for _ in xrange(min(demand - len(self.m_semaphore_ui_nodes), 10)):  # 最多也只创建10条
            self.supply()
        total = len(self.m_semaphore_ui_nodes)
        d = total - demand
        count = 0
        for npc_entity_id in semaphores.keys():
            if npc_entity_id in self.m_semaphore_ui_nodes:
                count += 1
                semaphore_ui_node = self.m_semaphore_ui_nodes.pop(npc_entity_id)  # 从OrderedDict弹出，为了下面插入时在最尾部
                phrase = semaphores[npc_entity_id]
                if semaphore_ui_node.get_icon() != phrase:
                    # 状态改变了才换图标
                    semaphore_ui_node.set_icon(phrase)
                semaphore_ui_node.show()  # 可能以前离开较远隐藏过显示
                self.m_semaphore_ui_nodes[npc_entity_id] = semaphore_ui_node  # 在队尾
                semaphores.pop(npc_entity_id)  # 处理好的npc丢掉
        for npc_entity_id in semaphores.keys():
            count += 1
            if count > total:
                # 没有可用节点了
                return
            k, semaphore_ui_node = self.m_semaphore_ui_nodes.popitem(0)  # 头部弹出可用节点
            if semaphore_ui_node.ChangeBindEntityId(npc_entity_id):
                semaphore_ui_node.set_icon(semaphores[npc_entity_id])
                self.m_semaphore_ui_nodes[npc_entity_id] = semaphore_ui_node  # 放置于队尾
            else:
                print 'abnormal on_highlight'
                self.m_semaphore_ui_nodes[k] = semaphore_ui_node
        while d > 0:
            # 有剩余的节点
            d -= 1
            k, semaphore_ui_node = self.m_semaphore_ui_nodes.popitem(0)
            semaphore_ui_node.hide()  # 隐藏显示
            self.m_semaphore_ui_nodes[k] = semaphore_ui_node

    def on_display_quest(self, data):
        """
        接收到任务数据
        """
        print 'on_display_quest', data
        progresses = data.get('progresses')
        if self.m_dialogue_ui_node:
            self.EnableUI = data.get('EnableUI') or False  # 客户端玩家进入会请求任务数据，顺带返回mod.json中的是否显示UI配置
            self.m_dialogue_ui_node.display_quest(progresses)
        positions = data.get('positions', {})
        self.m_attentive_positions = positions  # 关心的地点
        destination = data.get('destination')
        if destination:
            # 导航
            try:
                destination = tuple(destination)
                print clientApi.StartNavTo(destination, 'textures/ui/netease_quest/navi', lambda *args: logger.info('navi cut args: {}'.format(args)))
            except:
                logger.warning('abnormal on_display_quest')
                import traceback
                traceback.print_exc()
        else:
            clientApi.StopNav()

    def on_display_dialogue(self, data):
        """
        显示任务对话
        """
        dialogue_id = data['dialogue_id']
        dialogue_title = data.get('dialogue_title', '')
        self.m_dialogue_ui_node.display_dialogue(dialogue_id, dialogue_title)

    def chk(self, pos1, pos2, r, omit_altitude=False):
        """
        检查pos1与pos2之间的距离
        是否小于等于r
        """

        abs1 = abs(pos1[0] - pos2[0])
        if abs1 > r:
            return False
        abs2 = abs(pos1[2] - pos2[2])
        if abs2 > r:
            return False
        if omit_altitude:
            return abs1 ** 2 + abs2 ** 2 <= r ** 2
        else:
            h = abs(pos1[1] - pos2[1])
            return h <= r and abs1 ** 2 + abs2 ** 2 + h ** 2 <= r ** 2

    def detect_pos(self):
        """
        检查“到达地点”类型任务，每隔一定逻辑帧执行一次
        """
        yield -16  # 每隔16帧执行一次
        if self.m_attentive_positions:
            comp = self.CreateComponent(self.m_player_id, modConfig.Minecraft, modConfig.PosComponent)
            pos = comp.GetPos()
            if pos:
                matches = []
                for k, v in self.m_attentive_positions.copy().iteritems():
                    if self.chk(pos, v['spot'], v['radius']):
                        matches.append(k)
                event_data = self.CreateEventData()
                event_data["id"] = self.m_player_id
                event_data['matches'] = matches  # 到达了任务配置点附近的任务id列表
                self.NotifyToServer(modConfig.ArriveEvent, event_data)
        self.m_pos_monitor = False  # 解开标志位，表示可以开始执行下一次了

    def render(self, option):
        """
        对话框选项点击后会走到这里
        """
        k, v = option
        event_data = self.CreateEventData()
        event_data["id"] = self.m_player_id
        event_data['phrase'] = v  # 四种选项的配置值，如果是任务相关则为任务id，若为跳转对话则为对话id，若为继续本对话则为True（保持参数一致性，虽然下面没有使用）
        self.m_coroutine_mgr.delay_exec_func(self.m_dialogue_option_handlers[k], 0, event_data)  # 四种选项的后续执行不同，self.m_dialogue_option_handlers字典中的值则为不同的执行方法
        # 选什么都关闭对话
        self.m_dialogue_ui_node._quit()
