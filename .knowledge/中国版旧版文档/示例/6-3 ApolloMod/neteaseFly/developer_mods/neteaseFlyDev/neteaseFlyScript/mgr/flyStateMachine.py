# -*- coding: utf-8 -*-

import logout

class NodeId(object):
    Default = 0
    Fly = 1

class EventType(object):
    CloseFly = 0
    OpenFly = 1
    Hungry = 2
    TransferServer = 3
    TransferDim = 4
    FlyEnabledChange = 5
    APICall = 6

class Node(object):
    def __init__(self, onEnter, onExit):
        super(Node, self).__init__()
        self.mOnEnter = onEnter
        self.mOnExit = onExit

    def OnEnter(self, eventType, playerUid):
        if self.mOnEnter:
            self.mOnEnter(eventType, playerUid)

    def OnExit(self, eventType, playerUid):
        if self.mOnExit:
            self.mOnExit(eventType, playerUid)

class Edge(object):
    def __init__(self, target, requirement, priority):
        super(Edge, self).__init__()
        self.mRequirement = requirement
        self.mTargetNodeId = target
        self.mPriority = priority

    def Requirement(self, enableFly, eventType, playerUid):
        if self.mRequirement:
            return self.mRequirement(enableFly, eventType, playerUid)
        return False

    def GetTargetNodeId(self):
        return self.mTargetNodeId

    def GetPriority(self):
        return self.mPriority

class FlyStateMachine(object):
    def __init__(self):
        super(FlyStateMachine, self).__init__()
        self.mCurrentNode = None
        self.mCurrentNodeId = None
        self.mDefaultNodeId = NodeId.Default
        self.mNodes = {}
        self.mEdges = {}

    def AddNode(self, nodeId, onEnter=None, onExit=None, defaultNode = False):
        """
        添加状态节点
        param: nodeId 节点名称
        param: onEnter 进入该状态节点执行函数
        param: onExit 离开该状态节点执行函数
        """
        if self.mNodes.get(nodeId) != None:
            logout.error("{0} Node with the same name already exists in the state machine!".format(nodeId))
            return
        node = Node(onEnter, onExit)
        self.mNodes[nodeId] = node
        self.mEdges[nodeId] = []
        if defaultNode or self.mCurrentNodeId == None:
            self.mCurrentNode = node
            self.mCurrentNodeId = nodeId
            self.mDefaultNodeId = nodeId

    def AddEdge(self, source, target, requirement=None, priority = 0):
        """
        添加转移条件
        param: source 原状态
        param: target 目标状态
        param: requirement 边界条件函数，返回True时执行状态转移
        param: priority 优先级，当同时满足多个转移条件时按优先级转移
        """
        edges = self.mEdges.get(source)
        if not isinstance(edges, list):
            logout.error("there is no node named {0}".format(source))
            return
        targetIndex = -1
        for i in range(len(edges)):
            if edges[i].GetPriority() < priority:
                targetIndex = i
        if targetIndex == -1:
            edges.append(Edge(target, requirement, priority))
        else:
            edges.insert(targetIndex, Edge(target, requirement, priority))

    def ReceiveEvent(self, enableFly, eventType, playerUid):
        """
        接受事件，收到事件后根据当前状态遍历转移条件，满足转移条件时执行状态转移
        param: enableFly 是否允许飞行
        param: eventType 事件类型
        param: playerUid 玩家Uid
        """
        edges = self.mEdges.get(self.mCurrentNodeId)
        if edges:
            for edge in edges:
                if edge.Requirement(enableFly, eventType, playerUid):
                    self.ChangeState(edge.GetTargetNodeId(), eventType, playerUid)
                    break

    def ResetToDefaut(self):
        """将状态重置为初始状态"""
        if self.mCurrentNodeId != self.mDefaultNodeId:
            self.ChangeState(self.mDefaultNodeId)

    def ChangeState(self, target, eventType=None, playerUid=None):
        """
        改变状态，执行当前状态的OnExit函数，然后执行目标状态的OnEnter函数
        param: target 目标状态
        param: eventType 事件类型
        param: playerUid 玩家Uid
        """
        node = self.mNodes.get(target)
        if not node:
            logout.error("Tried to change to a nonexistant state!")
        self.mCurrentNode.OnExit(eventType, playerUid)
        self.mCurrentNodeId = target
        self.mCurrentNode = self.mNodes[target]
        self.mCurrentNode.OnEnter(eventType, playerUid)

    def GetCurrentNodeId(self):
        """获取当前状态节点"""
        return self.mCurrentNodeId