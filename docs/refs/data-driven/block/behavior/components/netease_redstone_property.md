# 未命名

> 文档版本：1.21.0.24

用于给自定义方块添加自定义方块实体。

## 架构

```mcschema
netease:redstone_property:
{
  string "value" : opt
}

```

/// html | div.result
//// define
`value`：<samp>string</samp>

- 目前只支持break_on_push，设置之后，方块可以被活塞破坏变成掉落物，否则，方块会被活塞推动而不破坏。


////


///

