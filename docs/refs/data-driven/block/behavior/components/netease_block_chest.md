# 未命名

> 文档版本：1.21.0.24

用于给方块添加箱子功能，使用了该组件会创建一个block_entity方块，会与其他block_entity逻辑有冲突，请谨慎使用。
该组件会覆盖带有base_block及其相关组件的功能。
使用了这个组件后请勿再配置netease:face_directional。
使用SetBlockNew接口创建自定义箱子的时候，需要先调用一次SetBlockNew将目标位置方块设置为Air，再使用AddTimer延后调用SetBlockNew创建自定义箱子。

## 架构

```mcschema
netease:block_chest:
{
  string "custom_description" : opt
  integer "chest_capacity" : opt
  boolean "can_pair" : opt
  boolean "is_shulker_box" : opt
  boolean "mute" : opt
  boolean "can_be_blocked" : opt
}

```

/// html | div.result
//// define
`custom_description`：<samp>string</samp>

- 箱子UI上面显示的箱子名称，不填为空。


////


//// define
`chest_capacity`：<samp>integer</samp>

- 必填，箱子的容量行数，取值范围1-8，如果can_pair取值为true且该值大于4，将自动变为4。


////


//// define
`can_pair`：<samp>boolean</samp>

- 是否可以与隔壁箱子组合，合成一个大箱子。


////


//// define
`is_shulker_box`：<samp>boolean</samp>

- 是否为潜影盒箱子，如果开启摧毁方块将不会掉落，与原版潜影盒功能相同，无法与隔壁箱子进行组合。


////


//// define
`mute`：<samp>boolean</samp>

- 是否关闭箱子开启与关闭时的音效。


////


//// define
`can_be_blocked`：<samp>boolean</samp>

- 是否能被阻挡，即箱子上面有阻挡的方块时能否打开箱子。


////


///

