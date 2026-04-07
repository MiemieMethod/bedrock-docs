# -*- coding: utf-8 -*-
import time
import mod.client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()
import math

compFactory = clientApi.GetEngineCompFactory()

# 客户端类
class Main(ClientSystem):
    def __init__(self, namespace, system):
        ClientSystem.__init__(self, namespace, system)
        self.playerID = clientApi.GetLocalPlayerId()

        self.global0Area =[(0,0), (5,5)]    # 矩形区域0的最小点与最大点，玩家在内时播放music.global0全局音乐
        self.global1Area =[(-5,-5), (0,0)]  # 矩形区域1的最小点与最大点，玩家在内时播放music.global1全局音乐
        
        self.campPoint = (20,4,20)          # 圆形区域的圆心
        self.campRadius = 5                 # 圆形区域的半径。玩家在内时播放music.custom音效
        
        self.lastPlayMusic = None

    def Update(self):
        posComp = compFactory.CreatePos(self.playerID)
        auComp =  compFactory.CreateCustomAudio(self.playerID)
        playerPos = posComp.GetPos()
        # 矩形区域0
        if self.IsInSquareArea((playerPos[0],playerPos[2]),self.global0Area):
            if self.lastPlayMusic is not "music.global0":
                auComp.DisableOriginMusic(True)
                auComp.PlayGlobalCustomMusic("music.global0",1,True)
                self.lastPlayMusic = "music.global0"
                print self.lastPlayMusic
        # 矩形区域1
        elif self.IsInSquareArea((playerPos[0],playerPos[2]),self.global1Area):
            if self.lastPlayMusic is not "music.global1":
                auComp.DisableOriginMusic(True)
                auComp.PlayGlobalCustomMusic("music.global1",1,True)
                self.lastPlayMusic = "music.global1"
                print self.lastPlayMusic
        # 圆形区域
        elif self.IsInCampArea((playerPos[0],playerPos[2]),(self.campPoint[0],self.campPoint[2]),5):
            if self.lastPlayMusic is not "music.custom":
                auComp.DisableOriginMusic(True)
                if self.lastPlayMusic:
                    auComp.StopCustomMusic(self.lastPlayMusic)
                auComp.PlayCustomMusic("music.custom",self.campPoint,1,1,True)
                self.lastPlayMusic = "music.custom"
                print self.lastPlayMusic
        else:
            if self.lastPlayMusic:
                auComp.StopCustomMusic(self.lastPlayMusic,2)
                self.lastPlayMusic = None
                auComp.DisableOriginMusic(False)
                print "stop play"    

    def IsInSquareArea(self,playerPos,areaPoints):
        x,z = playerPos
        minX, minZ = areaPoints[0]
        maxX, maxZ = areaPoints[1]
        return minX <= x <= maxZ and minZ <= z <= maxZ


    def IsInCampArea(self,playerPos,targetPos,radius):
        disSqr = math.pow(playerPos[0]-targetPos[0],2)+math.pow(playerPos[1]-targetPos[1],2)
        if disSqr > radius**2:
            return False
        return True
    #endregion

    