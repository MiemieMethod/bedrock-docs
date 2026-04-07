# -*- coding: utf-8 -*-

from neteaseQuestScript.modCommon import dialogueConfig as modConfig
from .. import logger
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class DialogueScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        logger.info('==== %s ====' % 'init DialogueScreen')

        self.m_player_id = clientApi.GetLocalPlayerId()

        # '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel'
        # '/dialogue_panel'

        self.m_dialogue_board_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/dialogue_board_panel'
        self.m_dialogue_board_bg = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/dialogue_board_panel/dialogue_board_{}_bg'
        self.m_dialogue_title_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/dialogue_board_panel/title_text'
        self.m_dialogue_content_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/dialogue_board_panel/content_text'
        self.m_dialogue_option_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/dialogue_board_panel/option_{}_btn'
        self.m_dialogue_option_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/dialogue_board_panel/option_{0}_btn/option_{0}_icon'
        self.m_dialogue_option_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/dialogue_board_panel/option_{0}_btn/option_{0}_text'
        self.m_dialogue_close_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/dialogue_board_panel/close_btn'

        self.m_quest_board_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/quest_board_panel'
        self.m_quest_board_bg_pair = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/quest_board_panel/quest_board_single_bg', '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/quest_board_panel/quest_board_full_bg'
        self.m_quest_select_btn_pair = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/quest_board_panel/unfold_btn', '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/quest_board_panel/fold_btn'
        self.m_quest_info_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/quest_board_panel/quest_{}_panel'
        self.m_quest_info_status_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/quest_board_panel/quest_{0}_panel/quest_{0}_status_icon'
        self.m_quest_info_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/quest_board_panel/quest_{0}_panel/quest_{0}_text'

        self.m_quest_select_flag = False
        self.m_dialogue_replies = {}
        self.m_status_icons = {
            "continue": 'textures/ui/netease_quest/icon03@3x',
            "todo": 'textures/ui/netease_quest/icon01@3x',
            "done": 'textures/ui/netease_quest/icon02@3x',
            "shift": 'textures/ui/netease_quest/icon03@3x',
            'quit': 'textures/ui/netease_quest/icon04@3x',
        }

    # Create函数是继承自ScreenNode，会在UI创建完成后被调用
    def Create(self):
        self.AddTouchEventHandler(self.m_dialogue_option_btn.format(1), self.reply)
        self.AddTouchEventHandler(self.m_dialogue_option_btn.format(2), self.reply)
        self.AddTouchEventHandler(self.m_dialogue_option_btn.format(3), self.reply)
        self.AddTouchEventHandler(self.m_dialogue_close_btn, self.quit)
        self.AddTouchEventHandler(self.m_quest_select_btn_pair[0], self.select)
        self.AddTouchEventHandler(self.m_quest_select_btn_pair[-1], self.select)

    def initialize(self):
        self.SetVisible(self.m_dialogue_board_panel, False)
        self.SetVisible(self.m_quest_board_panel, False)

    def shift(self):
        self.SetVisible(self.m_quest_board_panel, clientApi.GetSystem(modConfig.ModName, modConfig.ClientSystemName).EnableUI)

    # 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
    def Update(self):
        pass

    def select(self, args):
        touch_event = args["TouchEvent"]
        touch_pos = args["TouchPosX"], args["TouchPosY"]

        touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
        if touch_event == touch_event_enum.TouchUp:
            # 触控在按钮范围内弹起时
            clientApi.SetResponse(True)
            self.m_quest_select_flag = not self.m_quest_select_flag
            for i in xrange(2, 6):
                self.SetVisible(self.m_quest_info_panel.format(i), self.m_quest_select_flag)
            self.SetVisible(self.m_quest_board_bg_pair[int(self.m_quest_select_flag)], True)
            self.SetVisible(self.m_quest_board_bg_pair[int(not self.m_quest_select_flag)], False)
            self.SetVisible(self.m_quest_select_btn_pair[int(self.m_quest_select_flag)], True)
            self.SetVisible(self.m_quest_select_btn_pair[int(not self.m_quest_select_flag)], False)
        elif touch_event == touch_event_enum.TouchDown:
            # 按钮按下时
            clientApi.SetResponse(False)
        elif touch_event == touch_event_enum.TouchCancel:
            # 触控在按钮范围外弹起时
            clientApi.SetResponse(True)

    def _quit(self):
        self.SetVisible(self.m_dialogue_board_panel, False)

    def quit(self, args):
        touch_event = args["TouchEvent"]
        touch_pos = args["TouchPosX"], args["TouchPosY"]

        touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
        if touch_event == touch_event_enum.TouchUp:
            # 触控在按钮范围内弹起时
            clientApi.SetResponse(True)
            self._quit()
        elif touch_event == touch_event_enum.TouchDown:
            # 按钮按下时
            clientApi.SetResponse(False)
        elif touch_event == touch_event_enum.TouchCancel:
            # 触控在按钮范围外弹起时
            clientApi.SetResponse(True)

    def reply(self, args):
        touch_event = args["TouchEvent"]
        touch_pos = args["TouchPosX"], args["TouchPosY"]

        touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
        if touch_event == touch_event_enum.TouchUp:
            # 触控在按钮范围内弹起时
            clientApi.SetResponse(True)
            if self.m_dialogue_replies.get(args['ButtonPath']):
                # 不让重复发
                # 万一没发出去就关了重新点出来
                clientApi.GetSystem(modConfig.ModName, modConfig.ClientSystemName).render(
                    self.m_dialogue_replies.pop(args['ButtonPath']))
            else:
                self._quit()
        elif touch_event == touch_event_enum.TouchDown:
            # 按钮按下时
            clientApi.SetResponse(False)
        elif touch_event == touch_event_enum.TouchCancel:
            # 触控在按钮范围外弹起时
            clientApi.SetResponse(True)

    def display_quest(self, progresses):
        # 展示左上角任务栏
        if not progresses:
            progresses = ((1, '§4暂无任务数据'),)
        l = len(progresses)
        for i in xrange(5):
            p1 = self.m_quest_info_status_icon.format(i + 1)
            p2 = self.m_quest_info_text.format(i + 1)
            if i < l:
                self.SetSprite(p1, self.m_status_icons[progresses[i][0] and 'todo' or 'done'])
                self.SetText(p2, progresses[i][1])
                if i:
                    self.SetVisible(p1, True)
                    self.SetVisible(p2, True)
            else:
                self.SetVisible(p1, False)
                self.SetVisible(p2, False)
        self.SetVisible(self.m_quest_board_panel, clientApi.GetSystem(modConfig.ModName, modConfig.ClientSystemName).EnableUI)

    def next_episode(self):
        self.m_dialogue_index += 1
        self._display_dialogue()

    def _display_dialogue(self):
        dialogue = modConfig.DialogueConfig[self.m_dialogue_id]
        compositions = dialogue.get('compositions')
        if not compositions:
            logger.error('==== 配置错误 144 ====')
            return self._quit()
        if self.m_dialogue_index >= len(compositions):
            logger.error('==== 配置错误 147 ====')
            return self._quit()
        select = compositions[self.m_dialogue_index]['select']
        l = len(select)
        if not l:
            logger.error('==== 配置错误 152 ====')
            return self._quit()
        self.SetText(self.m_dialogue_content_text, compositions[self.m_dialogue_index]['content'])
        self.m_dialogue_replies.clear()
        if l > 3:
            l = 3
        for i, o in enumerate(l == 3 and [3, 1, 2] or [1, 2, 3]):
            self.SetVisible(self.m_dialogue_board_bg.format(o), o == l)
            flag = o <= l
            p = self.m_dialogue_option_btn.format(o)
            if flag:
                for k, v in select[i]['option'].iteritems():
                    if v:
                        self.m_dialogue_replies[p] = (k, v)
                        self.SetSprite(self.m_dialogue_option_icon.format(o), self.m_status_icons[k])
                        break
                else:
                    self.SetSprite(self.m_dialogue_option_icon.format(o), self.m_status_icons['quit'])
                self.SetText(self.m_dialogue_option_text.format(o), select[i]['reply'])
            self.SetVisible(p, flag)
        self.SetVisible(self.m_dialogue_board_panel, True)

    def display_dialogue(self, dialogue_id, dialogue_title):
        dialogue = modConfig.DialogueConfig.get(dialogue_id)
        if not dialogue:
            logger.error('==== %s ====' % 'dialogue: %s 显示对话不存在' % dialogue_id)
            return self._quit()
        self.m_dialogue_id = dialogue_id
        self.m_dialogue_index = 0
        self.SetText(self.m_dialogue_title_text, dialogue_title)
        self._display_dialogue()
