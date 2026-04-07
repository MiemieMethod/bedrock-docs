# -*- coding:utf-8 -*-

def IsSameItem(item1, item2):
    """判断是否为同一item，只有itemName和auxValue均相同才返回True"""
    if not item1 or not item2:
        return False
    if item1.get("itemName", "item1") != item2.get("itemName", "item2"):
        return False
    if item1.get("auxValue") != item2.get("auxValue"):
        return False
    if item1.get("userData") != item2.get("userData"):
        return False
    if item1.get("durability") != item2.get("durability"):
        return False
    return True