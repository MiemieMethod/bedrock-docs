# -*- coding: utf-8 -*-
import apolloCommon.mysqlPool as mysqlPool
import ujson as json

# 辅助函数 -- 把unicode编码的字符串、字典或列表转换成utf8编码
def UnicodeConvert(input):
    if isinstance(input, dict):
        return {UnicodeConvert(key): UnicodeConvert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [UnicodeConvert(element) for element in input]
    elif isinstance(input, tuple):
        tmp = [UnicodeConvert(element) for element in input]
        return tuple(tmp)
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def GetCloudItems(uid, apply_tag, cb = None):
    # 查询
    sql = 'select cloud_items from neteaseCloudItems where uid = %s and apply_tag = %s'
    params = (uid, apply_tag, )
    mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, params, cb)

def InsertCloudItems(uid, cloudItemDict, apply_tag, cb = None):
    # 插入
    itemJson = json.dumps(cloudItemDict)
    sql = 'insert into neteaseCloudItems (uid, cloud_items, apply_tag) values (%s, %s, %s)'
    params = (uid, itemJson, apply_tag, )
    mysqlPool.AsyncInsertOneWithOrderKey(str(uid), sql, params, cb)

def UpdateCloudItems(uid, cloudItemDict, apply_tag, cb = None):
    # 更新
    itemJson = json.dumps(cloudItemDict)
    sql = 'update neteaseCloudItems set cloud_items = %s where uid = %s and apply_tag = %s'
    params = (itemJson, uid, apply_tag, )
    mysqlPool.AsyncExecuteWithOrderKey(str(uid), sql, params, cb)
