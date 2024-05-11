# 未命名

> 文档版本：1.21.0.24

用于给自定义方块定义是否可以随机tick，并且设置该tick事件是否发送到脚本层。

## 架构

```mcschema
netease:fuel:
{
  boolean "enable" : opt
  boolean "tick_to_script" : opt
}

```

/// html | div.result
//// define
`enable`：<samp>boolean</samp>

- 方块是否随机tick。


////


//// define
`tick_to_script`：<samp>boolean</samp>

- 是否发送事件 BlockRandomTickServerEvent 到python脚本。


////


///

