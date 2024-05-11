# 未命名

> 文档版本：1.21.0.24

用于配置自定义红石源与自定义红石机械元件；
可以配置自定义红石的类型，如红石源或者红石机械元件；
可以配置初始信号强度，默认为15。

## 架构

```mcschema
netease:redstone:
{
  string "type" : opt
  integer "strength" : opt
}

```

/// html | div.result
//// define
`type`：<samp>string</samp>

- 红石类型：
producer：红石源
consumer：红石机械元件


////


//// define
`strength`：<samp>integer</samp>


////


///

