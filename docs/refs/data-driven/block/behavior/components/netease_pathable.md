# 未命名

> 文档版本：1.21.0.24

用于设置游戏内AI在进行寻路时，方块是否被当作障碍物。

## 架构

```mcschema
netease:pathable:
{
  boolean "value" : opt
}

```

/// html | div.result
//// define
`value`：<samp>boolean</samp>

- 为true时，寻路时被当作空气
为false时，寻路时被当作障碍物，并且可在其上方行走


////


///

