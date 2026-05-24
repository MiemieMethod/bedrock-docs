# 自定义声音

声音文件属于资源包。你可以覆盖原版声音，也可以新增声音事件，再通过`/playsound`、实体事件、动画控制器或其他内容触发。

## 覆盖原版声音

如果只是替换原版声音，目录和文件名要与原版资源包对应。示例：替换开箱声音。

/// html | div.treeview
- `demo_RP`
    - `sounds`
        - `random`
            - `chestopen.ogg`
///

官方教程指出，替换声音时文件扩展名不必和原版完全相同，但扩展名前的文件名必须一致。例如可以用`chestopen.ogg`替换同名原版声音。

## 新增声音事件

创建`demo_RP/sounds.json`：

```json title="sounds.json"
{
  "individual_event_sounds": {
    "events": {
      "demo.chime": {
        "sound": "demo.chime",
        "volume": 1.0,
        "pitch": [0.9, 1.1]
      }
    }
  }
}
```

再创建`demo_RP/sounds/sound_definitions.json`：

```json title="sounds/sound_definitions.json"
{
  "format_version": "1.20.20",
  "sound_definitions": {
    "demo.chime": {
      "__use_legacy_max_distance": "true",
      "category": "block",
      "sounds": [
        "sounds/demo/chime"
      ]
    }
  }
}
```

声音文件路径为：

```text
demo_RP/sounds/demo/chime.ogg
```

## 测试

```mcfunction
/playsound demo.chime @s
```

如果听不到声音，先检查文件是否为OGG格式，再检查`sound_definitions.json`中的路径是否不带扩展名。声音和纹理一样，通常需要重新进入世界才能可靠刷新。

## 给实体或动画使用

客户端实体可以定义短名：

```json
"sound_effects": {
  "phase_change": "demo.chime"
}
```

动画控制器状态中再调用：

```json
"sound_effects": [
  {
    "effect": "phase_change"
  }
]
```

这样声音就能和动画、粒子一起作为实体状态变化的反馈。