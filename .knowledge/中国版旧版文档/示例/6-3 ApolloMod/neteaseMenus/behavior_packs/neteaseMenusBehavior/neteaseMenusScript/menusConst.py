# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.4"
ModName = "neteaseMenus"
ClientSystemName = "neteaseMenusBeh"
ClientSystemClsPath = "neteaseMenusScript.menusClientSystem.MenusClientSystem"
ServerSystemName = "neteaseMenusDev"
ServerSystemClsPath = "neteaseMenusScript.menusServerSystem.MenusServerSystem"

# UI
menusUIName = "menusUI"
menusUIClsPath = "neteaseMenusScript.menusClientUI.MenusScreen"
menusUIScreenDef = "netease_menus_UI.main"

# 配置文件中的配置
ConfigParams = {}

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"

# 事件
DisplayMenusEvent = 'DisplayMenusEvent'

# 抛出的事件
class OutputEvent(object):
    MenusNavigateEvent = 'MenusNavigateEvent' # 菜单被点击时
