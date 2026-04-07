# -*- coding: utf-8 -*-

from collections import Counter
from neteaseQuestScript.modCommon import questConfig as modConfig
# 用来打印规范格式的log
from .. import logger
from ..serverManager.coroutineMgr import CoroutineMgr
import time, json
import neteaseQuestScript.questConst as questConst
import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool
import neteaseQuestScript.timermanager as timermanager
import logout
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()

QUEST_TYPE_MAPPING = {  # redis中存储用字符串方便一些，所以做了一个studio配置到本逻辑判断key的映射
    modConfig.QUEST_KILL_MONSTER: questConst.QUEST_KILL_MONSTER,
    modConfig.QUEST_COLLECT_ITEM: questConst.QUEST_COLLECT_ITEM,
    modConfig.QUEST_ARRIVE_PLACE: questConst.QUEST_ARRIVE_PLACE,
    modConfig.QUEST_PLAYER_LEVEL: questConst.QUEST_PLAYER_LEVEL,
}


def post_json_loads(p_object):
    if isinstance(p_object, dict):
        return {post_json_loads(key): post_json_loads(value) for key, value in p_object.iteritems()}
    elif isinstance(p_object, list):
        return [post_json_loads(item) for item in p_object]
    elif isinstance(p_object, unicode):
        return p_object.encode('utf-8')
    else:
        return p_object

# 处理py2的json.loads字符串unicode格式编码问题，统一变成py2中str格式
json_loads = lambda s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kwargs: post_json_loads(json.loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kwargs))


class QuestServerSystem(ServerSystem):
    """
    该mod的服务端类
    持久化玩家的任务数据
    提供正常判断任务完成的逻辑
    """

    def __init__(self, namespace, system_name):
        ServerSystem.__init__(self, namespace, system_name)
        logger.info('==== %s ====' % 'init QuestServerSystem')
        if not self.InitMysqlPool():
            return
        if not self.InitRedisPool():
            return
        if not self.InitQuestCfg():
            return
        self.listen_event()

        self.m_quest_available_players = {}  # 双标记，由于玩家刚连进本服需要查询数据库，处于该字典内的玩家表示已经正常查询完毕且已将任务数据加到内存中
        self.m_quest_online_players = {}  # 双标记，连进本服的玩家，但未必已经正常查询返回，理论上位于上方字典的也会存在此字典

        self.m_doing_records = {}  # 进行中
        self.m_done_records = {}  # 已完成
        self.m_player_level_dict = {}  # 等级映射

        self.m_player_attentive_items = {}  # 搜寻物品类型的任务所需关心玩家的物品
        self.m_player_attentive_holding_dict = {}  # 缓存上一次查询的任务道具持有数，用于有变化就触发事件检查（即使完成了但没有提交的任务依旧可以看到有变化）
        self.m_player_item_monitor = False

        self.m_coroutine_mgr = CoroutineMgr()
        self.m_cache_quest_data_timer = timermanager.timerManager.addRepeatTimer(4, self.cache_quest_data)  # 每4s（该频率为综合考虑后的较优值）将玩家的任务数据刷进redis
        self.m_persist_quest_data_timer = timermanager.timerManager.addRepeatTimer(444, self.persist_quest_data)  # 每444s（该频率为综合考虑后的较优值）将玩家的任务数据从redis中读出来刷进mysql

    def get_quest_available_players(self):
        return self.m_quest_available_players.keys()

    def get_coroutine_mgr(self):
        return self.m_coroutine_mgr

    def InitMysqlPool(self):
        try:
            mysqlPool.InitDB(20)
        except:
            logout.error("Exception in InitMysqlPool")
            return False
        return True

    def InitRedisPool(self):
        try:
            redisPool.InitDB(20)
        except:
            logout.error("Exception in InitRedisPool")
            return False
        return True

    def InitQuestCfg(self):
        self.m_quest_enable_default_navi = False
        cfg = commonNetgameApi.GetModJsonConfig("neteaseQuestScript")
        if not cfg:
            logout.warning("nothing in InitQuestCfg")
        else:
            self.m_quest_enable_default_navi = bool(cfg.get('QuestEnableDefaultNavi'))
        return True

    def Destroy(self):
        if self.m_cache_quest_data_timer:
            timermanager.timerManager.delTimer(self.m_cache_quest_data_timer)
            self.m_cache_quest_data_timer = None
        if self.m_persist_quest_data_timer:
            timermanager.timerManager.delTimer(self.m_persist_quest_data_timer)
            self.m_persist_quest_data_timer = None
        # comp = self.CreateComponent(serverApi.GetLevelId(), modConfig.Minecraft, modConfig.ExtraDataComponent)
        # comp.SetExtraData("doing_records", self.m_doing_records)
        # comp.SetExtraData("done_records", self.m_done_records)
        # comp.SetExtraData("player_level_dict", self.m_player_level_dict)
        self.un_listen_event()
        mysqlPool.Finish()
        redisPool.Finish()

    def listen_event(self):
        self.DefineEvent(modConfig.DisplayQuestEvent)
        self.DefineEvent(modConfig.HustleEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            modConfig.LoadServerAddonScriptsAfter, self, self.on_load_server_addon_scripts_after)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            modConfig.OnScriptTickServer, self, self.on_script_tick_server)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.MobDieEvent,
                            self, self.on_mob_die)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddLevelEvent,
                            self, self.on_add_level)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            questConst.AddServerPlayerEvent, self, self.on_add_server_player)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            questConst.DelServerPlayerEvent, self, self.on_del_server_player)
        self.ListenForEvent(modConfig.DialogueModName, modConfig.DialogueClientSystemName, modConfig.AcceptQuestEvent,
                            self, self.on_accept_quest)
        self.ListenForEvent(modConfig.DialogueModName, modConfig.DialogueClientSystemName, modConfig.SubmitQuestEvent,
                            self, self.on_submit_quest)
        self.ListenForEvent(modConfig.DialogueModName, modConfig.DialogueClientSystemName,
                            modConfig.GetQuestProgressesEvent, self, self.on_get_quest_progresses)
        self.ListenForEvent(modConfig.DialogueModName, modConfig.DialogueClientSystemName, modConfig.ArriveEvent, self,
                            self.on_arrive)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.HustleEvent, self, self.on_hustle)
        self.ListenForEvent(questConst.ModName, questConst.ServiceSystemName, questConst.PushQuestDataEvent, self,
                            self.on_push_quest_data)
        self.ListenForEvent(questConst.ModName, questConst.ServiceSystemName, questConst.QueryQuestDataEvent, self,
                            self.on_master_query_quest_data)
        self.ListenForEvent(questConst.ModName, questConst.ServiceSystemName, questConst.UpdateQuestDataEvent, self,
                            self.on_master_update_quest_data)

    def un_listen_event(self):
        self.UnDefineEvent(modConfig.DisplayQuestEvent)
        self.UnDefineEvent(modConfig.HustleEvent)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                              modConfig.LoadServerAddonScriptsAfter, self, self.on_load_server_addon_scripts_after)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                              modConfig.OnScriptTickServer, self, self.on_script_tick_server)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.MobDieEvent,
                              self, self.on_mob_die)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddLevelEvent,
                              self, self.on_add_level)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                              questConst.AddServerPlayerEvent, self, self.on_add_server_player)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                              questConst.DelServerPlayerEvent, self, self.on_del_server_player)
        self.UnListenForEvent(modConfig.DialogueModName, modConfig.DialogueClientSystemName, modConfig.AcceptQuestEvent,
                              self, self.on_accept_quest)
        self.UnListenForEvent(modConfig.DialogueModName, modConfig.DialogueClientSystemName, modConfig.SubmitQuestEvent,
                              self, self.on_submit_quest)
        self.UnListenForEvent(modConfig.DialogueModName, modConfig.DialogueClientSystemName,
                              modConfig.GetQuestProgressesEvent, self, self.on_get_quest_progresses)
        self.UnListenForEvent(modConfig.DialogueModName, modConfig.DialogueClientSystemName, modConfig.ArriveEvent,
                              self, self.on_arrive)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.HustleEvent, self,
                              self.on_hustle)
        self.UnListenForEvent(questConst.ModName, questConst.ServiceSystemName, questConst.PushQuestDataEvent, self,
                              self.on_push_quest_data)
        self.UnListenForEvent(questConst.ModName, questConst.ServiceSystemName, questConst.QueryQuestDataEvent, self,
                              self.on_master_query_quest_data)
        self.UnListenForEvent(questConst.ModName, questConst.ServiceSystemName, questConst.UpdateQuestDataEvent, self,
                              self.on_master_update_quest_data)

    def on_master_update_quest_data(self, data):
        """
        master的运营指令修改修改任务
        """

        print 'on_master_update_quest_data', data
        try:
            req_data = json_loads(data['requestBody'])
            success, msg = self.UpdateQuestData(req_data['uid'], req_data['mod'])
            if success:
                self.NotifyToMaster(questConst.UpdateQuestDataEvent, {'clientId': data['clientId']})
        except:
            import traceback
            traceback.print_exc()

    def on_master_query_quest_data(self, data):
        """
        master的运营指令查询玩家任务
        """

        print 'on_master_query_quest_data', data
        uid = data.get('uid')
        player_id = netgameApi.GetPlayerIdByUid(uid)
        if not player_id:
            print 'can not get player_id by uid: %s' % uid
            return
        if player_id in self.m_doing_records and player_id in self.m_done_records:
            self.NotifyToMaster(questConst.QueryQuestDataEvent, {
                'clientId': data['clientId'],
                'uid': uid,
                'doing': self.m_doing_records[player_id],
                'done': self.m_done_records[player_id]
            })

    def quest_server_render(self, player_id, event_name, resp_data):
        """
        请求service的回调统一入口
        """

        print player_id, event_name, resp_data
        if event_name == questConst.PullQuestDataEvent:
            if resp_data['code'] == questConst.RespCodeSuccess:
                uid = resp_data['entity']['uid']
                if player_id not in self.m_quest_online_players:
                    logout.warning('quest_server_render player be offline uid: {} player_id: {}'.format(uid, player_id))
                    self.RequestToService(
                        questConst.ModName,
                        questConst.PushQuestDataEvent,
                        resp_data['entity'],
                        lambda rtn, data: rtn or logout.error('玩家 {} 可能无法获取任务数据'.format(uid))
                    )
                    return
                if resp_data['entity'].get('debut'):
                    # 取数据库的
                    sql = 'SELECT done, rec FROM {} WHERE uid=%s'.format(questConst.TableQuestData)
                    mysqlPool.AsyncQueryWithOrderKey('QUERY_PLAYER_%s_QUEST_DATA' % uid, sql, (uid,), lambda result_set: self.on_query_quest_data(result_set, uid, player_id))
                else:
                    keys = ['{}:quest:doing'.format(uid), '{}:quest:done'.format(uid)]
                    redisPool.AsyncMget(keys, lambda values: self.post_push_quest_data(keys, values))

    def on_hustle(self, data):
        """
        收集道具相关任务
        玩家的相关道具发生变化
        """

        player_id, item_id = data.get('id'), data.get('item_id')
        self.update_quest(player_id, questConst.QUEST_COLLECT_ITEM, item_id)

    def on_arrive(self, data):
        """
        到达地点任务
        """

        player_id, matches = data.get('id'), data.get('matches')
        if player_id and matches:
            for quest_id in matches:
                self.update_quest(player_id, questConst.QUEST_ARRIVE_PLACE, quest_id, 1)

    def on_get_quest_progresses(self, data):
        """
        客户端玩家进入后请求左上角任务栏显示数据
        """

        player_id = data.get('id')
        if player_id:
            self.push_quest(player_id)

    def on_accept_quest(self, data):
        """
        接任务
        """
        player_id, quest_id = data.get('id'), data.get('phrase')
        if not player_id or not quest_id:
            return
        self.accept_quest(player_id, quest_id)

    def on_submit_quest(self, data):
        """
        交任务
        """
        player_id, quest_id = data.get('id'), data.get('phrase')
        if not player_id or not quest_id:
            return
        self.submit_quest(player_id, quest_id)

    def post_push_quest_data(self, keys, values):
        uid = int(keys[0].split(':', 1)[0])
        player_id = netgameApi.GetPlayerIdByUid(uid)
        if player_id not in self.m_quest_online_players:
            logout.warning('post_push_quest_data player be offline uid: {} player_id: {}'.format(uid, player_id))
            self.RequestToService(
                questConst.ModName,
                questConst.PushQuestDataEvent,
                {'uid': uid},
                lambda rtn, data: rtn or logout.error('玩家 {} 可能无法获取任务数据'.format(uid))
            )
            return
        for i, k in enumerate(keys):
            rec = values[i]
            if k.endswith('done'):
                try:
                    self.m_done_records[player_id] = Counter(json_loads(rec))
                except:
                    logout.error('corrupted data keys: {} values: {}'.format(keys, values))
                    self.m_doing_records.pop(player_id, -1)
                    self.m_done_records.pop(player_id, -1)
                    return
            else:
                try:
                    self.m_doing_records[player_id] = json_loads(rec)
                except:
                    logout.error('corrupted data keys: {} values: {}'.format(keys, values))
                    self.m_doing_records.pop(player_id, -1)
                    self.m_done_records.pop(player_id, -1)
                    return
        self.m_quest_available_players[player_id] = uid
        self.push_quest(player_id)

    def on_push_quest_data(self, data):
        print 'on_push_quest_data', data
        uid = data.get('uid')
        player_id = netgameApi.GetPlayerIdByUid(uid)
        if player_id not in self.m_quest_online_players:
            logout.warning('on_push_quest_data player be offline uid: {} player_id: {}'.format(uid, player_id))
            self.RequestToService(
                questConst.ModName,
                questConst.PushQuestDataEvent,
                data,
                lambda rtn, data: rtn or logout.error('玩家 {} 可能无法获取任务数据'.format(uid))
            )
            return
        if data.get('debut'):
            # 取数据库的
            sql = 'SELECT done, rec FROM {} WHERE uid=%s'.format(questConst.TableQuestData)
            mysqlPool.AsyncQueryWithOrderKey('QUERY_PLAYER_%s_QUEST_DATA' % uid, sql, (uid,), lambda result_set: self.on_query_quest_data(result_set, uid, player_id))
        else:
            keys = ['{}:quest:doing'.format(uid), '{}:quest:done'.format(uid)]
            redisPool.AsyncMget(keys, lambda values: self.post_push_quest_data(keys, values))

    def on_query_quest_data(self, result_set, uid, player_id):
        if result_set is None:
            logout.error('玩家 {} 登录获取任务进度失败'.format(uid))
            return
        if player_id in self.m_quest_online_players:
            for row in result_set:
                if row[0]:
                    try:
                        self.m_done_records[player_id] = Counter(json_loads(row[-1]))
                    except:
                        logout.error('corrupted data result_set: {} uid: {}'.format(result_set, uid))
                        self.m_doing_records.pop(player_id, -1)
                        self.m_done_records.pop(player_id, -1)
                        return
                else:
                    try:
                        self.m_doing_records[player_id] = json_loads(row[-1])
                    except:
                        logout.error('corrupted data result_set: {} uid: {}'.format(result_set, uid))
                        self.m_doing_records.pop(player_id, -1)
                        self.m_done_records.pop(player_id, -1)
                        return
            if player_id not in self.m_doing_records:
                self.m_doing_records.setdefault(player_id, {})
            if player_id not in self.m_done_records:
                self.m_done_records.setdefault(player_id, Counter())
            self.m_quest_available_players[player_id] = uid
            self.push_quest(player_id)
        else:
            self.RequestToService(
                questConst.ModName,
                questConst.PushQuestDataEvent,
                {'uid': uid, 'debut': 1},
                lambda rtn, data: rtn or logout.error('玩家 {} 可能无法获取任务数据'.format(uid))
            )

    def on_add_server_player(self, args):
        """
        玩家进入本服
        """

        player_id = args.get('id')
        uid = netgameApi.GetPlayerUid(player_id)
        if not uid:
            print 'can not get uid by player_id: %s' % player_id
            logout.error('[neteaseQuest] can not get uid by player_id: %s' % player_id)
            return
        self.m_quest_online_players[player_id] = uid  # 进入本服标记
        if args.get('isTransfer'):
            self.RequestToService(
                questConst.ModName,
                questConst.PullQuestDataEvent,
                {'uid': uid},
                lambda rtn, data: self.quest_server_render(player_id, questConst.PullQuestDataEvent, data) if rtn else logout.error('玩家 {} 无法获取任务数据'.format(uid))
            )
        else:
            # 第一次登进游戏，告诉service本服有部署任务系统
            self.RequestToService(
                questConst.ModName,
                questConst.PullQuestDataEvent,
                {'uid': uid, 'debut': 1}
            )
            # 取数据库的
            sql = 'SELECT done, rec FROM {} WHERE uid=%s'.format(questConst.TableQuestData)
            mysqlPool.AsyncQueryWithOrderKey('QUERY_PLAYER_%s_QUEST_DATA' % uid, sql, (uid,), lambda result_set: self.on_query_quest_data(result_set, uid, player_id))
        comp = self.CreateComponent(player_id, modConfig.Minecraft, "lv")
        if comp:
            self.m_player_level_dict[player_id] = comp.GetPlayerLevel()

    def on_del_server_player(self, args):
        # 玩家退出本服
        player_id = args.get('id')
        self.m_quest_online_players.pop(player_id, -1)
        uid = self.m_quest_available_players.pop(player_id, None)
        if uid is not None and player_id in self.m_doing_records and player_id in self.m_done_records:
            # 玩家登出，刷一次他的任务数据到数据库
            lines = []
            data = {'{}:quest:doing'.format(uid): '{}', '{}:quest:done'.format(uid): '{}'}
            quest_data = self.m_doing_records.pop(player_id, None)
            if quest_data:
                try:
                    rec = json.dumps(quest_data)
                    lines.append((uid, 0, rec))
                    data['{}:quest:doing'.format(uid)] = rec
                except:
                    logout.warning('on_del_server_player invalid line: {}'.format((uid, player_id, quest_data)))
            quest_data = self.m_done_records.pop(player_id, None)
            if quest_data:
                try:
                    rec = json.dumps(quest_data)
                    lines.append((uid, 1, rec))
                    data['{}:quest:done'.format(uid)] = rec
                except:
                    logout.warning('on_del_server_player invalid line: {}'.format((uid, player_id, quest_data)))
            if lines:
                sql = 'INSERT INTO {} (uid, done, rec) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE rec = VALUES(rec)'.format(questConst.TableQuestData)
                self.m_coroutine_mgr.delay_exec_func(lambda: mysqlPool.AsyncExecutemanyWithOrderKey('PERSIST_QUEST_DATA', sql, lines, lambda rtn: rtn or logout.error('PERSIST_QUEST_DATA failed lines: {}'.format(lines))), 0)
            if data:
                logout.info('on_del_server_player data: {}'.format(data))
                self.m_coroutine_mgr.delay_exec_func(lambda: redisPool.AsyncFuncWithKey(self.mset, "cache_quest_data", lambda success: self.post_cache_quest_data(uid, data, not args.get('isTransfer'), success), data), 0)

    def on_add_level(self, args):
        # 升级
        player_id, new_level = args.get('id'), args.get('newLevel')
        self.m_player_level_dict[player_id] = new_level
        self.update_quest(player_id, questConst.QUEST_PLAYER_LEVEL, 'player_level', new_level)

    def on_mob_die(self, args):
        # 怪物死亡
        victim_id, attacker_id = args.get('id'), args.get('attacker')
        # 暂时先一个一个更新
        self.update_quest(attacker_id, questConst.QUEST_KILL_MONSTER, self.CreateComponent(victim_id, modConfig.Minecraft, modConfig.EngineTypeComponent).GetEngineTypeStr(), 1)

    def on_load_server_addon_scripts_after(self, *args):
        # logger.info('==== %s ====' % 'restore dialogueServerSystem')
        # comp = self.CreateComponent(serverApi.GetLevelId(), modConfig.Minecraft, modConfig.ExtraDataComponent)
        # doing_records = comp.GetExtraData("doing_records")
        # done_records = comp.GetExtraData("done_records")
        # player_level_dict = comp.GetExtraData("player_level_dict")
        # if doing_records:
        #     self.m_doing_records = doing_records
        # else:
        #     logger.warning('==== %s ====' % 'restore dialogueServerSystem missing doing_records')
        # if done_records:
        #     self.m_done_records = done_records
        # else:
        #     logger.warning('==== %s ====' % 'restore dialogueServerSystem missing done_records')
        # if player_level_dict:
        #     self.m_player_level_dict = player_level_dict
        # else:
        #     logger.warning('==== %s ====' % 'restore dialogueServerSystem missing player_level_dict')
        pass

    def on_persist_quest_data(self, keys, values):
        print 'on_persist_quest_data', keys, values
        lines = []
        for i, k in enumerate(keys):
            rec = values[i]
            if isinstance(rec, str):
                try:
                    uid = int(k.split(':', 1)[0])
                    lines.append((uid, k.endswith('done') and 1 or 0, rec))
                    continue
                except:
                    pass
            logout.warning('on_persist_quest_data invalid line: {}'.format((k, rec)))
        if lines:
            sql = 'INSERT INTO {} (uid, done, rec) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE rec = VALUES(rec)'.format(questConst.TableQuestData)
            mysqlPool.AsyncExecutemanyWithOrderKey('PERSIST_QUEST_DATA', sql, lines, lambda rtn: rtn or logout.error('PERSIST_QUEST_DATA failed lines: {}'.format(lines)))

    def persist_quest_data(self):
        self.m_coroutine_mgr.delay_exec_func(self.pre_persist_quest_data, 0)
        # redisPool.AsyncFuncWithKey(self.mget, "persist_quest_data", lambda args: logout.error('persist_quest_data failed') if args is None else self.on_persist_quest_data(*args))
        pass

    def pre_persist_quest_data(self):
        keys = []
        for uid in self.m_quest_available_players.values():
            keys.append('{}:quest:doing'.format(uid))
            keys.append('{}:quest:done'.format(uid))
        redisPool.AsyncMget(keys, lambda values: self.on_persist_quest_data(keys, values))

    # def mget(self, conn):
    #     keys = conn.keys('*:quest:do*')
    #     values = conn.mget(keys)
    #     return keys, values

    def mset(self, conn, data):
        conn.mset(data)
        return True

    def post_cache_quest_data(self, uid, data, leave, success):
        if not success:
            logout.error('on_cache_quest_data failed data: {}'.format(data))
        elif not leave:
            self.RequestToService(
                questConst.ModName,
                questConst.PushQuestDataEvent,
                {'uid': uid},
                lambda rtn, data: rtn or logout.error('玩家 {} 可能无法获取任务数据'.format(uid))
            )

    def cache_quest_data(self):
        self.m_coroutine_mgr.delay_exec_func(self.pre_cache_quest_data, 0)

    def pre_cache_quest_data(self):
        data = {}
        for player_id in self.m_doing_records.keys():
            uid = self.m_quest_available_players.get(player_id)
            quest_data = self.m_doing_records.get(player_id)
            if uid and quest_data:
                try:
                    data['{}:quest:doing'.format(uid)] = json.dumps(quest_data)
                except:
                    logout.warning('cache_quest_data invalid line: {}'.format((uid, player_id, quest_data)))
        for player_id in self.m_done_records.keys():
            uid = self.m_quest_available_players.get(player_id)
            quest_data = self.m_done_records.get(player_id)
            if uid and quest_data:
                try:
                    data['{}:quest:done'.format(uid)] = json.dumps(quest_data)
                except:
                    logout.warning('cache_quest_data invalid line: {}'.format((uid, player_id, quest_data)))
        if data:
            logout.info('cache_quest_data data: {}'.format(data))
            redisPool.AsyncFuncWithKey(self.mset, "cache_quest_data", lambda success: success or logout.error('pre_cache_quest_data failed data: {}'.format(data)), data)

    def on_script_tick_server(self, *args):
        """
        服务端的逻辑帧，用于驱动协程管理器与定时任务
        """
        timermanager.timerManager.tick()
        self.m_coroutine_mgr.tick()

        if not self.m_player_item_monitor:
            self.m_player_item_monitor = True
            self.m_coroutine_mgr.start_coroutine(self.detect_player_item())

    def detect_player_item(self):
        """
        隔44帧执行一次
        查询玩家的物品
        任务相关道具若有变化
        则发送事件
        """

        yield -44
        try:
            for player_id, attentive_items in self.m_player_attentive_items.iteritems():
                holding_dict = {item_id: 0 for item_id in attentive_items}
                comp = self.CreateComponent(player_id, modConfig.Minecraft, modConfig.ItemComponent)
                inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
                for i in range(36):
                    try:
                        slot_data = comp.GetPlayerItem(inv, i) or {}
                        item_id = '{}:{}'.format(slot_data.get('itemName'), slot_data.get('auxValue'))
                        if item_id and item_id in attentive_items:
                            count = slot_data.get('count')
                            if count:
                                # holding_dict[item_id] = holding_dict.setdefault(item_id, 0) + count
                                holding_dict[item_id] += count
                    except:
                        continue
                for item_id, n in holding_dict.iteritems():
                    if n != self.m_player_attentive_holding_dict.setdefault(player_id, {}).setdefault(item_id, 0):
                        self.m_player_attentive_holding_dict[player_id][item_id] = n
                        event_data = self.CreateEventData()
                        event_data["id"] = player_id
                        event_data['item_id'] = item_id
                        self.BroadcastEvent(modConfig.HustleEvent, event_data)
        except:
            import traceback
            traceback.print_exc()
        self.m_player_item_monitor = False

    def update_quest(self, entity_id, kind, k, v=0):
        """
        任务更新的统一入口
        """

        flag = False
        autos = []
        server_type = commonNetgameApi.GetServerType()
        for quest_id, progress in self.m_doing_records.get(entity_id, {}).get(kind, {}).iteritems():
            quest = modConfig.QuestConfig.get(quest_id)
            if not quest:
                logger.error('==== %s ====' % '"update quest 不存在": %s' % quest_id)
                continue
            if kind == questConst.QUEST_KILL_MONSTER:
                # entity_type = getattr(self.ENTITY_TYPE, quest['questMobType'].capitalize(), False)
                # if not entity_type:
                #     logger.error('==== 这任务更新不了因为怪物类型为空 %s ====', quest)
                # if k == entity_type:
                if k == quest['questMobType']:
                    progress[0] += v
                    flag = True  # 改了就要通知
            elif kind == questConst.QUEST_COLLECT_ITEM:
                item_id = reduce(lambda x, y: '{}:{}'.format(x, y), quest['questItemType'])
                if not item_id:
                    logger.error('==== 这任务更新不了因为道具id为空 %s ====', quest)
                if k == item_id:
                    cur = self.get_default(entity_id, quest)[0]
                    if progress[0] != cur:
                        progress[0] = cur
                        flag = True  # 改了就要通知
            elif kind == questConst.QUEST_ARRIVE_PLACE:
                if k == quest_id and quest.get('spotServerType', server_type) == server_type:
                    if not progress[0]:
                        progress[0] += v
                    flag = True  # 改了就要通知
            elif kind == questConst.QUEST_PLAYER_LEVEL:
                cur = self.get_default(entity_id, quest)[0]
                if progress[0] != cur:
                    progress[0] = cur
                    flag = True  # 改了就要通知
            if self._can_submit(quest_id, progress) and not quest.get('npcEntityId'):
                autos.append(quest_id)
        for quest_id in autos:
            self.submit_quest(entity_id, quest_id)
        if flag:
            self.m_coroutine_mgr.delay_exec_func(self.push_quest, 2, entity_id)

    def accept_quest(self, player_id, quest_id, name=''):
        """
        接任务
        """

        quest = modConfig.QuestConfig.get(quest_id)
        if not quest:
            logger.error('==== %s ====' % '"accept quest 不存在": %s' % quest_id)
            return
        if player_id not in self.m_doing_records:
            logout.warning('accept_quest no quest data player_id: {}'.format(player_id))
            return
        quest_data = self.m_doing_records[player_id]
        holding_dict = self.can_accept(player_id, quest_id, True)
        if holding_dict:
            kind = QUEST_TYPE_MAPPING[quest['questType']]
            preconditions = quest.get('preconditions', {})
            # if preconditions.get('cost'):
            stuff = preconditions.get('stuff')
            if stuff:
                # 此时holding_dict是位置
                stuff_dict = Counter()
                for item in stuff:
                    item_id = reduce(lambda x, y: '{}:{}'.format(x, y), item['type'])
                    if not item_id:
                        logger.error('==== 走到这里居然还有道具id为空 %s ====', item)
                    if item['cost']:
                        stuff_dict.update({item_id: item['n']})
                if stuff_dict:
                    if not self.cost_stuff(player_id, stuff_dict, holding_dict):
                        # 没扣成功
                        logger.error('==== %s ====' % '"accept quest 扣材料失败": (%s, %s, %s, %s)' % (
                            player_id, quest_id, stuff, holding_dict))
                    else:
                        for item_id in holding_dict.keys():
                            self.m_coroutine_mgr.delay_exec_func(
                                self.update_quest, 0, player_id, questConst.QUEST_COLLECT_ITEM, item_id)
            quest_data.setdefault(kind, {})[quest_id] = self.get_default(player_id, quest)
            self.push_quest(player_id)
            # self.notify(player_id, '成功接受任务')
            self.notify(player_id, '系统：成功接受任务`{}`'.format(quest['questName']))
            # accept_proceeds = quest.get('accept_proceeds')
            # if not accept_proceeds:
            #     return self.push_dialogue(player_id, -1)
            # for phrase in accept_proceeds:
            #     self.on_accept_quest({'id': player_id, 'phrase': phrase, 'dialogue_title': name})
            pass
        else:
            # self.notify(player_id, '接受任务失败')
            self.notify(player_id, '§c系统：接受任务`{}`失败'.format(quest['questName']))

    def submit_quest(self, player_id, quest_id, name=''):
        """
        提交任务
        """

        quest = modConfig.QuestConfig.get(quest_id)
        if not quest:
            logger.error('==== %s ====' % '"submit quest 不存在": %s' % quest_id)
            return
        if player_id not in self.m_doing_records:
            logout.warning('submit_quest no quest data player_id: {}'.format(player_id))
            return
        quest_data = self.m_doing_records[player_id]
        kind = QUEST_TYPE_MAPPING.get(quest.get('questType'))
        if not kind:
            logger.error('==== %s ====' % '"submit quest 不能没类型": %s' % quest_id)
            return
        if quest_id not in quest_data.get(kind, {}):
            logger.warning('==== %s ====' % '"submit quest 未接取": %s' % quest_id)
            return
        if self._can_submit(quest_id, quest_data[kind][quest_id]):
            if quest.get('cost') and kind == questConst.QUEST_COLLECT_ITEM:
                stuff = {reduce(lambda x, y: '{}:{}'.format(x, y), quest['questItemType']): quest['amount']}
                if stuff:
                    holding_dict = self.can_cost_stuff(player_id, stuff)
                    if not holding_dict:
                        logger.error('==== %s ====' % '"submit quest 完成了却无法扣材料": %s' % quest_id)
                        return
                    elif not self.cost_stuff(player_id, stuff, holding_dict):
                        # 没扣成功
                        logger.error('==== %s ====' % '"submit quest 完成了却扣材料失败": (%s, %s, %s, %s)' % (
                            player_id, quest_id, stuff, holding_dict))
                    else:
                        for item_id in holding_dict.keys():
                            self.m_coroutine_mgr.delay_exec_func(
                                self.update_quest, 0, player_id, questConst.QUEST_COLLECT_ITEM, item_id)
            del quest_data[kind][quest_id]
            rewards = self.post_submit_quest(player_id, quest, quest_id)
            self.push_quest(player_id)
            # self.notify(player_id, '成功完成任务')
            self.notify(player_id, '系统：完成任务`{}`'.format(quest['questName']))
            if rewards:
                self.notify(player_id, '系统：获得任务奖励——{}{}'.format('经验*{}'.format(rewards['exp']) if rewards.get('exp') else '', '{}物品*{}'.format(rewards.get('exp') and '、' or '', len(rewards['drugs'])) if rewards.get('drugs') else ''))
            # commit_proceeds = quest.get('commit_proceeds')
            # if not commit_proceeds:
            #     return self.push_dialogue(player_id, -1)
            # for phrase in commit_proceeds:
            #     self.on_accept_quest({'id': player_id, 'phrase': phrase, 'dialogue_title': name})
            pass
        else:
            logger.warning('==== %s ====' % '"submit quest 未完成": %s' % quest_data[kind][quest_id])
            # self.notify(player_id, '完成任务失败')
            self.notify(player_id, '§c系统：完成任务`{}`失败'.format(quest['questName']))

    def post_submit_quest(self, player_id, quest, quest_id):
        """
        完成任务加经验给奖励
        """

        self.m_done_records[player_id].update([quest_id])
        rewards = quest.get('rewards')
        if rewards:
            if rewards.get('exp'):
                # 处理加经验
                comp = self.CreateComponent(player_id, modConfig.Minecraft, modConfig.CommandComponent)
                comp.SetCommand('/xp {} @s'.format(rewards['exp']), player_id)
            drugs = rewards.get('drugs')
            if drugs:
                comp = self.CreateComponent(player_id, modConfig.Minecraft, modConfig.ItemComponent)
                demand = len(drugs)
                free = []
                if len(free) < demand:
                    inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
                    for i in range(36):
                        if comp.GetPlayerItem(inv, i) is None:
                            free.append(i)
                            if len(free) >= demand:
                                break
                for item in drugs:
                    if item['n'] > 0:
                        item_dict = {
                            'itemName': item['type'][0],
                            'count': item['n'],
                            'enchantData': [],
                            'auxValue': item['type'][1],
                            'extraId': ''
                        }
                        if free:
                            comp.SpawnItemToPlayerInv(item_dict, player_id, free.pop(0))
                        else:
                            self.notify(player_id, '§c系统：背包已满掉落在地')
                            comp.SpawnItemToLevel(item_dict, self.CreateComponent(player_id, modConfig.Minecraft, "dimension").GetPlayerDimensionId(), self.CreateComponent(player_id, modConfig.Minecraft, modConfig.PosComponent).GetPos())
        return rewards

    def get_default(self, player_id, quest):
        """
        获取一个任务的初始进度
        """

        default = [0, time.time()]
        kind = QUEST_TYPE_MAPPING[quest['questType']]
        if kind == questConst.QUEST_COLLECT_ITEM:
            item_id = reduce(lambda x, y: '{}:{}'.format(x, y), quest['questItemType'])
            if not item_id:
                logger.error('==== 这任务完不成了因为道具id为空 %s ====', quest)
            else:
                comp = self.CreateComponent(player_id, modConfig.Minecraft, modConfig.ItemComponent)
                inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
                for i in range(36):
                    try:
                        slot_data = comp.GetPlayerItem(inv, i) or {}
                        if '{}:{}'.format(slot_data.get('itemName'), slot_data.get('auxValue')) == item_id:
                            count = slot_data.get('count')
                            if count:
                                default[0] += count
                    except:
                        continue
        elif kind == questConst.QUEST_PLAYER_LEVEL:
            default[0] = self.m_player_level_dict.get(player_id, 0)
        return default

    def can_cost_stuff(self, player_id, stuff):
        """
        如果够材料返回材料位置
        不够反空
        :param player_id:
        :param stuff: 不能是空
        :type stuff: dict
        :return:
        """
        comp = self.CreateComponent(player_id, modConfig.Minecraft, modConfig.ItemComponent)
        inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
        holding_dict = {}
        for item_id, n in stuff.iteritems():
            # 暂时先这样因为dict不能重key所以不会多算
            holding_dict[item_id] = []
            if n > 0:
                for i in range(36):
                    try:
                        slot_data = comp.GetPlayerItem(inv, i) or {}
                        if '{}:{}'.format(slot_data.get('itemName'), slot_data.get('auxValue')) == item_id:
                            count = slot_data.get('count')
                            if count:
                                holding_dict[item_id].append((count, i))
                                if reduce(lambda x, y: (x[0] + y[0], 0), holding_dict[item_id])[0] >= n:
                                    break
                    except:
                        continue
                if not holding_dict[item_id] or reduce(lambda x, y: (x[0] + y[0], 0), holding_dict[item_id])[0] < n:
                    # logger.warning('==== %s ====' % '"%s 材料不足": %s' % (quest_id, item_id))
                    return
        return holding_dict

    def cost_stuff(self, player_id, stuff, holding_dict):
        """
        真正执行消耗材料的方法
        理论上都是查出来够才扣
        """
        try:
            costing_stuff = dict(stuff)
            comp = self.CreateComponent(player_id, modConfig.Minecraft, modConfig.ItemComponent)
            for item_id, distributions in holding_dict.iteritems():
                for count, slot_pos in distributions:
                    n = min(costing_stuff[item_id], count)
                    if not comp.SetInvItemNum(slot_pos, count - n):
                        logger.error('==== cost stuff 扣材料失败 位置 %s 有 %s 个扣 %s 个 ====', slot_pos, count, n)
                        return
                    costing_stuff[item_id] -= n
                    if costing_stuff[item_id] <= 0:
                        break
            return True
        except:
            pass

    def can_accept(self, player_id, quest_id, alert=False):
        """
        接取任务前的判断
        """

        holding_dict = {}
        quest = modConfig.QuestConfig.get(quest_id)
        if not quest:
            logger.error('==== %s ====' % '"can accept quest 不存在": %s' % quest_id)
            return
        if player_id not in self.m_doing_records:
            logout.warning('can_accept no quest data player_id: {}'.format(player_id))
            return
        quest_data = self.m_doing_records[player_id]
        kind = QUEST_TYPE_MAPPING.get(quest.get('questType'))
        if not kind:
            logger.error('==== %s ====' % '"can accept quest 不能没类型": %s' % quest_id)
            return
        if quest_id in quest_data.get(kind, {}):
            logger.warning('==== %s ====' % '"can accept quest 已存在": %s' % quest_data[kind][quest_id])
            return
        limit = quest['limit']
        # if limit and self.m_done_records.get(player_id, {}).get(quest_id, 0) >= limit:
        if 0 <= limit <= self.m_done_records.get(player_id, {}).get(quest_id, 0):
            logger.warning('==== %s ====' % '"can accept quest 完成达上限": %s' % quest_id)
            if alert:
                self.notify(player_id, '§c`{}`：完成次数已达上限'.format(quest['questName']))
            return
        preconditions = quest.get('preconditions', {})
        if preconditions:
            lv = preconditions.get('lv', 0)
            stuff = preconditions.get('stuff', [])
            pre_quest_id = preconditions.get('preQuest')
            if self.m_player_level_dict.get(player_id, 0) < lv:
                logger.warning('==== %s ====' % '"can accept quest 等级不足": %s' % quest_id)
                if alert:
                    self.notify(player_id, '§c`{}`：等级不足'.format(quest['questName']))
                return
            if stuff:
                stuff_dict = Counter()
                for item in stuff:
                    item_id = reduce(lambda x, y: '{}:{}'.format(x, y), item['type'])
                    if not item_id:
                        logger.warning('==== 道具id为空 %s ====', item)
                    stuff_dict.update({item_id: item['n']})
                holding_dict = self.can_cost_stuff(player_id, stuff_dict)
                if not holding_dict:
                    logger.warning('==== %s ====' % '"can accept quest 材料不足": %s' % quest_id)
                    if alert:
                        self.notify(player_id, '§c`{}`：材料不足'.format(quest['questName']))
                    return
            if pre_quest_id:
                if pre_quest_id not in self.m_done_records.get(player_id, {}):
                    logger.warning('==== %s ====' % '"can accept quest 前置任务未完成": %s' % quest_id)
                    if alert:
                        self.notify(player_id, '§c`{}`：未完成前置任务'.format(quest['questName']))
                    return
        return holding_dict or True

    def _can_submit(self, quest_id, progress):
        """
        提交任务前的判断
        """

        quest = modConfig.QuestConfig.get(quest_id)
        if not quest:
            logger.error('==== %s ====' % '"can submit quest 不存在": %s' % quest_id)
            return
        kind = QUEST_TYPE_MAPPING.get(quest.get('questType'))
        if not kind:
            logger.error('==== %s ====' % '"can submit quest 不能没类型": %s' % quest_id)
            return
        if kind in (questConst.QUEST_KILL_MONSTER, questConst.QUEST_COLLECT_ITEM,) and progress[0] >= quest['amount']:
            return True
        if kind in (questConst.QUEST_PLAYER_LEVEL,) and progress[0] >= quest['goal']:
            return True
        if kind in (questConst.QUEST_ARRIVE_PLACE,) and progress[0] > 0:
            return True

    def get_progress(self, player_id, quest_id):
        """
        获取玩家某任务的进度
        """

        quest = modConfig.QuestConfig.get(quest_id)
        if not quest:
            logger.error('==== %s ====' % '"get progress quest 不存在": %s' % quest_id)
            return
        kind = QUEST_TYPE_MAPPING.get(quest.get('questType'))
        if not kind:
            logger.error('==== %s ====' % '"get progress quest 不能没类型": %s' % quest_id)
            return
        return self.m_doing_records.get(player_id, {}).get(kind, {}).get(quest_id)

    def can_submit(self, player_id, quest_id):
        """
        判断能否提交一个任务
        高层级的调用
        因为可能没有进度
        """

        progress = self.get_progress(player_id, quest_id)
        if not progress:
            logger.info('==== %s ====' % '"can submit quest 无进度": %s' % quest_id)
            return
        return self._can_submit(quest_id, progress)

    def generate_desc(self, quest_id, progress):
        """
        任务进度描述文本
        """

        quest = modConfig.QuestConfig.get(quest_id)
        if not quest:
            logger.error('==== %s ====' % '"generate desc quest 不存在": %s' % quest_id)
            return
        kind = QUEST_TYPE_MAPPING.get(quest.get('questType'))
        if not kind:
            logger.error('==== %s ====' % '"generate desc quest 不能没类型": %s' % quest_id)
            return
        desc = quest['desc']
        if not desc:
            desc = quest['questName']
        situation = '§r({}{}§r/{})'.format(
            self._can_submit(quest_id, progress) and '§a' or '§c',
            progress[0],
            kind in (questConst.QUEST_KILL_MONSTER, questConst.QUEST_COLLECT_ITEM,) and quest['amount'] or (kind == questConst.QUEST_PLAYER_LEVEL and quest['goal'] or 1))
        pretty = desc.replace('%p', situation, 1)
        if pretty == desc:
            return desc + situation
        return pretty

    def push_quest(self, player_id):
        """
        下放任务数据
        """

        if player_id not in self.m_doing_records:
            return
        quest_data = self.m_doing_records[player_id]
        event_data = self.CreateEventData()
        try:
            import apolloCommon.commonNetgameApi as commonNetgameApi
            cfg = commonNetgameApi.GetModJsonConfig("neteaseQuestScript")
            if not cfg:
                print 'nuthang'
            else:
                event_data['EnableUI'] = cfg.get('EnableUI', True)
        except:
            import traceback
            traceback.print_exc()
        details = reduce(lambda x, y: x + y, map(lambda kind: [(
            0 if self._can_submit(quest_id, progress) else 1,
            progress[-1],
            quest_id,
            self.generate_desc(quest_id, progress),
        ) for quest_id, progress in quest_data[kind].iteritems()], quest_data) or [[]])
        details.sort(key=lambda t: (t[0], t[1]))  # 感觉要优化每次推都查可能不好
        event_data['progresses'] = map(lambda t: (t[0], t[-1]), details[:5])
        server_type = commonNetgameApi.GetServerType()
        self.fill(event_data, quest_data, 'positions', questConst.QUEST_ARRIVE_PLACE, server_type)
        if self.m_quest_enable_default_navi and details:
            quest = modConfig.QuestConfig.get(details[0][2], {})
            destination = quest.get(details[0][0] and 'naviDestinationDoing' or 'naviDestinationDone')
            if destination:
                destination_server_type = quest.get(details[0][0] and 'naviDestinationDoingServerType' or 'naviDestinationDoneServerType')
                print 'push_quest server_type: {} destination_server_type: {}'.format(server_type, destination_server_type)
                if destination_server_type is None or destination_server_type == server_type:
                    event_data['destination'] = destination
        self.NotifyToClient(player_id, modConfig.DisplayQuestEvent, event_data)
        pre = self.m_player_attentive_items.get(player_id)
        self.fill(self.m_player_attentive_items, quest_data, player_id, questConst.QUEST_COLLECT_ITEM)
        if pre != self.m_player_attentive_items.get(player_id):
            self.m_player_attentive_holding_dict.setdefault(player_id, {}).clear()

    def fill(self, event_data, quest_data, key, kind, server_type=''):
        if kind == questConst.QUEST_ARRIVE_PLACE:
            event_data[key] = {quest_id: {
                'spot': modConfig.QuestConfig[quest_id]['spot'],
                'radius': modConfig.QuestConfig[quest_id]['radius']
            } for quest_id, progress in quest_data.get(kind, {}).iteritems() if not self._can_submit(quest_id, progress) and modConfig.QuestConfig[quest_id].get('spotServerType', server_type) == server_type}
        elif kind == questConst.QUEST_COLLECT_ITEM:
            event_data[key] = {reduce(lambda x, y: '{}:{}'.format(x, y), modConfig.QuestConfig[quest_id]['questItemType']) for quest_id in quest_data.get(kind, {})}
        if not event_data[key]:
            del event_data[key]

    def notify(self, player_id, msg):
        if not msg:
            return
        comp = self.CreateComponent(player_id, modConfig.Minecraft, modConfig.CommandComponent)
        # comp.SetCommand("title @s title %s" % msg, player_id)
        comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % msg, player_id)

    def UpdateQuestData(self, uid, mod):
        """
        更改一个玩家的任务数据
        """
        for quest_id, o in mod.iteritems():
            quest = modConfig.QuestConfig.get(quest_id)
            if not quest:
                return False, '不存在任务id为`{}`的任务'.format(quest_id)
            if o not in (-1, 0, 1):
                return False, '操作码`{}`不合法'.format(o)
        player_id = netgameApi.GetPlayerIdByUid(uid)
        if not (player_id in self.m_quest_available_players and player_id in self.m_quest_online_players and player_id in self.m_doing_records and player_id in self.m_done_records):
            return False, '玩家不在本服'
        flag = False
        for quest_id, o in mod.iteritems():
            quest = modConfig.QuestConfig.get(quest_id)
            if o > 0:
                self.m_doing_records.get(player_id, {}).get(QUEST_TYPE_MAPPING[quest['questType']], {}).pop(quest_id, -1)
                rewards = self.post_submit_quest(player_id, quest, quest_id)
                self.notify(player_id, '系统：完成任务`{}`'.format(quest['questName']))
                if rewards:
                    self.notify(player_id, '系统：获得任务奖励——{}{}'.format('经验*{}'.format(rewards['exp']) if rewards.get('exp') else '', '{}物品*{}'.format(rewards.get('exp') and '、' or '', len(rewards['drugs'])) if rewards.get('drugs') else ''))
            elif o < 0:
                self.m_doing_records.get(player_id, {}).get(QUEST_TYPE_MAPPING[quest['questType']], {}).pop(quest_id, -1)
            else:
                data = self.m_doing_records.get(player_id, {}).setdefault(QUEST_TYPE_MAPPING[quest['questType']], {})
                if quest_id not in data:
                    data[quest_id] = self.get_default(player_id, quest)
                    self.notify(player_id, '系统：成功接受任务`{}`'.format(quest['questName']))
            flag = True
        if flag:
            self.push_quest(player_id)
        return True, '操作成功'
