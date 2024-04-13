# `ScreenDisplay`

> 文档版本：1.21.0.21

`ScreenDisplay`类。script_api.@minecraft/server.screendisplay.description

## 方法

/// define
`getHiddenHudElements`


///

script_api.@minecraft/server.screendisplay.gethiddenhudelements.description

```js
getHiddenHudElements(): HudElement[]
```

/// html | div.result
//// define
返回值：<code><a href="../hudelement/">HudElement</a>[]</code>

- script_api.@minecraft/server.screendisplay.gethiddenhudelements.return


////

///


/// define
`hideAllExcept`


///

script_api.@minecraft/server.screendisplay.hideallexcept.description

```js
hideAllExcept(hudElements?: HudElement[]): void
```

/// html | div.result
//// define
`hudElements`：<code><a href="../hudelement/">HudElement</a>[]</code>|`undefined`

- script_api.@minecraft/server.screendisplay.hideallexcept.hudelements.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.screendisplay.hideallexcept.return


////

///


/// define
`isForcedHidden`


///

script_api.@minecraft/server.screendisplay.isforcedhidden.description

```js
isForcedHidden(hudElement: HudElement): boolean
```

/// html | div.result
//// define
`hudElement`：[`HudElement`](./hudelement.md)

- script_api.@minecraft/server.screendisplay.isforcedhidden.hudelement.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.screendisplay.isforcedhidden.return


////

///


/// define
`isValid`


///

script_api.@minecraft/server.screendisplay.isvalid.description

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.screendisplay.isvalid.return


////

///


/// define
`resetHudElements`


///

script_api.@minecraft/server.screendisplay.resethudelements.description

```js
resetHudElements(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.screendisplay.resethudelements.return


////

///


/// define
`setActionBar`


///

script_api.@minecraft/server.screendisplay.setactionbar.description

```js
setActionBar(text: (RawMessage | string)[] | RawMessage | string): void
```

/// html | div.result
//// define
`text`：`(RawMessage | string)[]`|[`RawMessage`](./rawmessage.md)|`string`

- script_api.@minecraft/server.screendisplay.setactionbar.text.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.screendisplay.setactionbar.return


////

///


/// define
`setHudVisibility`


///

script_api.@minecraft/server.screendisplay.sethudvisibility.description

```js
setHudVisibility(visible: HudVisibility, hudElements?: HudElement[]): void
```

/// html | div.result
//// define
`visible`：[`HudVisibility`](./hudvisibility.md)

- script_api.@minecraft/server.screendisplay.sethudvisibility.visible.description


////

//// define
`hudElements`：<code><a href="../hudelement/">HudElement</a>[]</code>|`undefined`

- script_api.@minecraft/server.screendisplay.sethudvisibility.hudelements.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.screendisplay.sethudvisibility.return


////

///


/// define
`setTitle`


///

script_api.@minecraft/server.screendisplay.settitle.description

```js
setTitle(title: (RawMessage | string)[] | RawMessage | string, options?: TitleDisplayOptions): void
```

/// html | div.result
//// define
`title`：`(RawMessage | string)[]`|[`RawMessage`](./rawmessage.md)|`string`

- script_api.@minecraft/server.screendisplay.settitle.title.description


////

//// define
`options`：[`TitleDisplayOptions`](./titledisplayoptions.md)|`undefined`

- script_api.@minecraft/server.screendisplay.settitle.options.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.screendisplay.settitle.return


////

///


/// define
`updateSubtitle`


///

script_api.@minecraft/server.screendisplay.updatesubtitle.description

```js
updateSubtitle(subtitle: (RawMessage | string)[] | RawMessage | string): void
```

/// html | div.result
//// define
`subtitle`：`(RawMessage | string)[]`|[`RawMessage`](./rawmessage.md)|`string`

- script_api.@minecraft/server.screendisplay.updatesubtitle.subtitle.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.screendisplay.updatesubtitle.return


////

///

