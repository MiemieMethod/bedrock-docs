# `/hud`

> 文档版本：1.21.0.20

`/hud`命令command.hud.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/hud <target:target> <visible:HudVisibility> [hud_element:HudElement]
```

//// html | div.result
command.hud.1.description

///// define
`target`：<!-- md:samp target -->

- 基本类型。command.hud.target.description

`visible`：<!-- md:samp HudVisibility -->

- 枚举类型。command.enum.hudvisibility.description枚举值如下：

  |值|描述|
  |---|---|
  |`hide`|command.enum.hudvisibility.hide|
  |`reset`|command.enum.hudvisibility.reset|


`hud_element`：<!-- md:samp HudElement -->

- 枚举类型，可选。command.enum.hudelement.description枚举值如下：

  |值|描述|
  |---|---|
  |`hunger`|command.enum.hudelement.hunger|
  |`all`|command.enum.hudelement.all|
  |`paperdoll`|command.enum.hudelement.paperdoll|
  |`armor`|command.enum.hudelement.armor|
  |`tooltips`|command.enum.hudelement.tooltips|
  |`touch_controls`|command.enum.hudelement.touch_controls|
  |`crosshair`|command.enum.hudelement.crosshair|
  |`hotbar`|command.enum.hudelement.hotbar|
  |`health`|command.enum.hudelement.health|
  |`progress_bar`|command.enum.hudelement.progress_bar|
  |`air_bubbles`|command.enum.hudelement.air_bubbles|
  |`horse_health`|command.enum.hudelement.horse_health|
  |`status_effects`|command.enum.hudelement.status_effects|
  |`item_text`|command.enum.hudelement.item_text|



/////

////

///
