# 未命名

> 文档版本：1.21.0.24

定义物品描述信息。

## 架构

```mcschema
netease:cooldown:
{
  integer "duration" : opt
  string "category" : opt
}

```

/// html | div.result
//// define
`duration`：<samp>integer</samp>

- 可填，这个物品能够再次使用前的冷却时间。


////


//// define
`category`：<samp>string</samp>

- 可填，物品的冷却类型。


////


///

