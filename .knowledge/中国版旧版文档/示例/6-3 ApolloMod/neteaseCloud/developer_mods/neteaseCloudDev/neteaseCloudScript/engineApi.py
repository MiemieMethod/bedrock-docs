# -*- coding: utf-8 -*-
# 这个文件的函数均为modsdk的组件操作
# 具体各组件功能与方法请查阅mc.163.com/mcstudio/mc-dev

import lobbyGame.netgameApi as lobbyGameApi
import server.extraServerApi as serverApi
import logout
AirName = 'minecraft:air'

def CleanWholeExtraData(entityId, uid):
    dataDict = GetWholeExtraData(entityId)
    entitycomp = serverApi.CreateComponent(entityId, "Minecraft", "extraData")
    for k in dataDict.keys():
        if not entitycomp.CleanExtraData(k):
            logout.error('CleanWholeExtraData fail!uid:%s, data:%s' % (uid, dataDict[k]))

def GetWholeExtraData(entityId):
    comp = serverApi.CreateComponent(entityId, "Minecraft", "extraData")
    dataDict = comp.GetWholeExtraData()
    if not dataDict:
        return {}
    return dataDict

def SetExtraData(dataDict, playerId):
    entitycomp = serverApi.CreateComponent(playerId, "Minecraft", "extraData")
    for k, v in dataDict.iteritems():
        entitycomp.SetExtraData(k, v)

def GetUserInventories(playerId):
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
    slotDict = {}
    for slot in xrange(36):
        itemDict = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
        if not itemDict:
            continue
        slotDict[slot] = itemDict
    return slotDict

def GetUserArmors(playerId):
    equipTypeLst = [
        serverApi.GetMinecraftEnum().ArmorSlotType.HEAD,
        serverApi.GetMinecraftEnum().ArmorSlotType.BODY,
        serverApi.GetMinecraftEnum().ArmorSlotType.LEG,
        serverApi.GetMinecraftEnum().ArmorSlotType.FOOT
    ]
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
    typeDict = {}
    for equipType in equipTypeLst:
        itemDict = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.ARMOR, equipType)
        if itemDict:
            typeDict[equipType] = itemDict
    return typeDict
    # comp = serverApi.CreateComponent(playerId, 'Minecraft', 'armorSlot')
    # typeDict = {}
    # for equipType in equipTypeLst:
    #     info = comp.GetArmorNew(equipType)
    #     if info is None:
    #         continue
    #     itemName, auxValue, extraId = info
    #     if AirName == itemName:
    #         continue
    #     typeDict[equipType] = (itemName, auxValue, extraId)
    # return typeDict

def GetLeftHandItem(playerId):
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
    itemDict = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.OFFHAND, 0)
    return itemDict

def GetAllEffects(playerId):
    comp = serverApi.CreateComponent(playerId, "Minecraft", "effect")
    return comp.GetAllEffects()

def ClearUserInventories(playerId):
    '''
    airDict = {
        'itemName' : AirName,
        'count' : 0
    }
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
    for slot in xrange(36):
        if not comp.SpawnItemToPlayerInv(airDict, playerId, slot):
            logout.error('ClearUserInventories fail!playerid:%s, slot:%s, item:%s' % (playerId, slot, airDict))
    '''
    comp = serverApi.CreateComponent(playerId, "Minecraft", "command")
    comp.SetCommand("/clear @s", playerId)
    return

def ClearUserArmors(playerId):
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'armorSlot')
    comp.SetArmorNew(serverApi.GetMinecraftEnum().ArmorSlotType.HEAD, '')
    comp.SetArmorNew(serverApi.GetMinecraftEnum().ArmorSlotType.BODY, '')
    comp.SetArmorNew(serverApi.GetMinecraftEnum().ArmorSlotType.LEG, '')
    comp.SetArmorNew(serverApi.GetMinecraftEnum().ArmorSlotType.FOOT, '')

def ClearLeftHandItem(playerId):
    itemDict = {
        'itemName': AirName,
        'count': 0,
    }
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
    comp.SpawnItemToPlayerOffHand(itemDict, playerId)

def ClearEffects(playerId):
    effectDictList = GetAllEffects(playerId)
    if not effectDictList:
        return
    comp = serverApi.CreateComponent(playerId, "Minecraft", "effect")
    for effectDict in effectDictList:
        name = effectDict['effectName']
        if not comp.RemoveEffectFromEntity(name):
            logout.error('ClearEffects error!playerid:%s, effect name:%s' % (playerId, name))

def AddEffectsToUser(effectLst, playerId, uid):
    comp = serverApi.CreateComponent(playerId, "Minecraft", "effect")
    for effect in effectLst:
        res = comp.AddEffectToEntity(effect['effectName'], effect['duration'], effect['amplifier'], True)
        if not res:
            logout.error('AddEffectsToUser fail!uid:%s, effect:%s' % (uid, effect))

def SpawnItemsToPlayerInv(itemsDict, playerId, uid):
    suc = True
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
    gameComp = serverApi.CreateComponent(serverApi.GetLevelId(), 'Minecraft', 'game')
    for slot, itemDict in itemsDict.iteritems():
        exist = gameComp.LookupItemByName(str(itemDict['itemName']))
        if not exist:
            logout.warning('SpawnItemsToPlayerInv fail!inventory item not exist!player:%s, item:%s' % (uid, itemsDict))
            continue
        itemDict['enchantData'] = [tuple(lst) for lst in itemDict['enchantData']]
        if not comp.SpawnItemToPlayerInv(itemDict, playerId, slot):
            logout.error('SpawnItemsToPlayerInv fail!uid:%s, item:%s' % (uid, itemDict))
            suc = False
    return suc

def SetUserArmors(armors, playerId, uid):
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'armorSlot')
    gameComp = serverApi.CreateComponent(serverApi.GetLevelId(), 'Minecraft', 'game')
    itemComp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
    for _type, armorInfo in armors.iteritems():
        if tuple == type(armorInfo):
            #兼容上个版本
            itemName, auxValue, extraId = armorInfo
            exist = gameComp.LookupItemByName(str(itemName))
            if not exist:
                logout.warning('SetUserArmors fail!armor not exist!player:%s, armor:%s' % (uid, armorInfo))
                continue
            if not comp.SetArmorNew(_type, itemName, extraId, []):
                logout.error('SetUserArmors fail!uid:%s, armor:%s' % (uid, armorInfo))
        else:
            itemName = str(armorInfo['itemName'])
            exist = gameComp.LookupItemByName(str(itemName))
            if not exist:
                logout.warning('SetUserArmors fail!armor not exist!player:%s, armor:%s' % (uid, armorInfo))
                continue
            armorInfo['enchantData'] = [tuple(lst) for lst in armorInfo['enchantData']]
            if not itemComp.SpawnItemToArmor(armorInfo, playerId, _type):
                logout.error('SpawnItemToArmor fail!uid:%s, armor:%s' % (uid, armorInfo))

def SpawnItemToPlayerLeftHand(itemDict, playerId, uid):
    gameComp = serverApi.CreateComponent(serverApi.GetLevelId(), 'Minecraft', 'game')
    exist = gameComp.LookupItemByName(str(itemDict['itemName']))
    if not exist:
        logout.warning('SpawnItemToPlayerLeftHand fail!item not exist!player:%s, item:%s' % (uid, itemDict))
        return
    comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
    if not comp.SpawnItemToPlayerOffHand(itemDict, playerId):
        logout.error('SpawnItemToPlayerLeftHand fail!uid:%s, item:%s' % (uid, itemDict))

def ChangeSelectSlot(slot, playerId, uid):
    comp = serverApi.CreateComponent(playerId, "Minecraft", "player")
    if not comp.ChangeSelectSlot(slot):
        logout.error('ChangeSelectSlot fail.uid:%s, right hand slot:%s' % (uid, slot))


# 简易单例
serverSystemInstance = None
def SetServerSystem(serverSys):
    global  serverSystemInstance
    serverSystemInstance = serverSys

# 服务端本地事件通知
def BroadcastEvent(eventName, data):
    global serverSystemInstance
    serverSystemInstance.BroadcastEvent(eventName, data)
