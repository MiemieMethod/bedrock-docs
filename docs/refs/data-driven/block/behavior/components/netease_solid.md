# 未命名

> 文档版本：1.21.0.24

用于设置方块是否为实心方块主要与生物在方块内时是否受到窒息伤害有关。
使用了这个组件，自定义方块将不会产生阴影。

## 架构

```mcschema
netease:solid:
{
  boolean "value" : opt
}

```

/// html | div.result
//// define
`value`：<samp>boolean</samp>

- 为true时，生物在方块内会受到窒息伤害
为false时，生物在方块内不会受到窒息伤害


////


///

