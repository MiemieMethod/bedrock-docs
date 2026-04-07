
# -*- coding: utf-8 -*-

from mod_log import logger

class NodeId(object):
    Idle = 1
    SelectSlot = 2
    UnSelectSlot = 3
    Swap = 4
    TouchProgressiveSelect = 5
    TouchProgressiveSelectComplete = 6
    TouchProgressiveSelectCancel = 7
    DropAll = 8
    Coalesce = 9

class ButtonEventType(object):
    Clicked = 0
    Pressed = 1
    Released = 2
    DoubleClick = 3

class Node(object):
    def __init__(self, onEnter, onExit):
        super(Node, self).__init__()
        self.mOnEnter = onEnter
        self.mOnExit = onExit

    def OnEnter(self, buttonPath):
        if self.mOnEnter:
            self.mOnEnter(buttonPath)

    def OnExit(self, buttonPath):
        if self.mOnExit:
            self.mOnExit(buttonPath)

class ButtonEdge(object):
    def __init__(self, target, requirement, priority):
        super(ButtonEdge, self).__init__()
        self.mRequirement = requirement
        self.mTargetNodeId = target
        self.mPriority = priority

    def Requirement(self, buttonPath, buttonEventType):
        if self.mRequirement:
            return self.mRequirement(buttonPath, buttonEventType)
        return False

    def GetTargetNodeId(self):
        return self.mTargetNodeId

    def GetPriority(self):
        return self.mPriority

class ContainerInteractionStateMachine(object):
    def __init__(self):
        super(ContainerInteractionStateMachine, self).__init__()
        self.mCurrentNode = None
        self.mCurrentNodeId = None
        self.mDefaultNodeId = NodeId.Idle
        self.mNodes = {}
        self.mButtonEdges = {}

    def AddNode(self, nodeId, onEnter=None, onExit=None, defaultNode = False):
        if self.mNodes.get(nodeId) != None:
            logger.error("{0} Node with the same name already exists in the state machine!".format(nodeId))
            return
        node = Node(onEnter, onExit)
        self.mNodes[nodeId] = node
        self.mButtonEdges[nodeId] = []
        if defaultNode or self.mCurrentNodeId == None:
            self.mCurrentNode = node
            self.mCurrentNodeId = nodeId
            self.mDefaultNodeId = nodeId

    def AddEdge(self, source, target, requirement=None, priority = 0):
        edges = self.mButtonEdges.get(source)
        if not isinstance(edges, list):
            logger.error("there is no node named {0}".format(source))
            return
        targetIndex = -1
        for i in range(len(edges)):
            if edges[i].GetPriority() < priority:
                targetIndex = i
        if targetIndex == -1:
            edges.append(ButtonEdge(target, requirement, priority))
        else:
            edges.insert(targetIndex, ButtonEdge(target, requirement, priority))

    def ReceiveEvent(self, buttonPath, buttonEventType):
        edges = self.mButtonEdges.get(self.mCurrentNodeId)
        if edges:
            for edge in edges:
                if edge.Requirement(buttonPath, buttonEventType):
                    self.ChangeState(edge.GetTargetNodeId(), buttonPath)
                    break

    def ResetToDefaut(self):
        if self.mCurrentNodeId != self.mDefaultNodeId:
            self.ChangeState(self.mDefaultNodeId)

    def ChangeState(self, target, buttonPath=None):
        node = self.mNodes.get(target)
        if not node:
            logger.error("Tried to change to a nonexistant state!")
        self.mCurrentNode.OnExit(buttonPath)
        self.mCurrentNodeId = target
        self.mCurrentNode = self.mNodes[target]
        self.mCurrentNode.OnEnter(buttonPath)

    def GetCurrentNodeId(self):
        return self.mCurrentNodeId