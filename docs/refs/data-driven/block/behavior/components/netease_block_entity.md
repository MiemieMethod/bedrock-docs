# 未命名

> 文档版本：1.21.0.24

用于给自定义方块添加自定义方块实体。

## 架构

```mcschema
netease:block_entity:
{
  boolean "tick" : opt
  boolean "client_tick" : opt
  boolean "movable" : opt
}

```

/// html | div.result
//// define
`tick`：<samp>boolean</samp>

- 为true时，当玩家进入方块tick范围时，该方块每秒会发送20次ServerBlockEntityTickEvent事件
为false时，该方块不会发送ServerBlockEntityTickEvent事件


////


//// define
`client_tick`：<samp>boolean</samp>

- 为true时，当玩家进入方块tick范围时，该方块每秒会发送20次ModBlockEntityTickClientEvent事件
为false时，该方块不会发送ModBlockEntityTickClientEvent事件


////


//// define
`movable`：<samp>boolean</samp>

- 为true时，该方块可被粘性活塞拉回
为false时，该方块不可被粘性活塞拉回


////


///

