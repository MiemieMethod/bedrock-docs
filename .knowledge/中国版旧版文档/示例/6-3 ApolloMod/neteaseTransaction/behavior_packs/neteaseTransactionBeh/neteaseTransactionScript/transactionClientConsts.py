# -*- coding: utf-8 -*-

ModName = 'NeteaseTransaction'
ModVersion = '1.0.1'
ServerSystemClsPath = 'neteaseTransactionScript.transactionServerSystem.TransactionServerSystem'
ClientSystemClsPath = 'neteaseTransactionScript.transactionClientSystem.TransactionClientSystem'
ClientSystemName = 'NeteaseTransactionClientSystem'
ServerSystemName = 'NeteaseTransactionServerSystem'

TableUserTransactionInfo = "neteaseTransactionInfo"

# 服务端自定义事件
SyncConfigEvent = "ServerSyncConfig"
InitiateTransactionEvent = "InitiateTransaction"
ShowTipsEvent = "ShowTips"
PartnerLockEvent = "PartnerLock"
PartnerConfirmEvent = "PartnerConfirm"
TransactionCompleteEvent = "TransactionComplete"
RequestTransactionServerEvent = "RequestTransactionServer"
CancelTransactionEvent = "CancelTransaction"

# 客户端自定义事件
ConfirmRequestEvent = "ConfirmRequest"
CloseTransactionEvent = "CloseTransaction"
LockTransactionEvent = "LockTransaction"
ConfirmTransactionEvent = "ConfirmTransaction"
RequestTransactionClientEvent = "RequestTransactionClient"