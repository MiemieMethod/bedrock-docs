# 未命名

> 文档版本：1.21.0.24

可燃类物品组件。允许该物品作为燃料在熔炉中燃烧。

## 架构

```mcschema
netease:tier:
{
  string "digger" : opt
  boolean "destroy_special" : opt
  integer "level" : opt
}

```

/// html | div.result
//// define
`digger`：<samp>string</samp>

- 必须设置。表示方块使用此工具挖掘时有速度加成。可选的值有：
shovel：铲
pickaxe：镐
hatchet：斧


////


//// define
`destroy_special`：<samp>boolean</samp>

- 可选。
当设置为true时，表示只有使用digger设置的工具进行挖掘才会产生掉落物。


////


//// define
`level`：<samp>integer</samp>

- 可选。
当destroy_special为true时才会生效。表示挖掘所需的工具等级，若手持工具等级小于该值，则不会产生掉落物。
原版工具的等级：
空手/其他非工具物品：0
木制/金制工具：0
石制工具：1
铁制工具：2
钻石工具：3


////


///

