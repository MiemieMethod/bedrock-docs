# `ScreenDisplay`

> 文档版本：1.21.0.20

`ScreenDisplay`类。

## 方法

/// define
`getHiddenHudElements`


///

```js
getHiddenHudElements(): HudElement[]
```

/// html | div.result

///


/// define
`hideAllExcept`


///

```js
hideAllExcept(hudElements?: HudElement[]): void
```

/// html | div.result
//// define
`hudElements`：<code><a href="./hudelement.md">HudElement</a>[]</code>|`undefined`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`isForcedHidden`


///

```js
isForcedHidden(hudElement: HudElement): boolean
```

/// html | div.result
//// define
`hudElement`：[`HudElement`](./hudelement.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isValid`


///

```js
isValid(): boolean
```

/// html | div.result

///


/// define
`resetHudElements`


///

```js
resetHudElements(): void
```

/// html | div.result

///


/// define
`setActionBar`


///

```js
setActionBar(text: RawMessage | string[] | RawMessage | string): void
```

/// html | div.result
//// define
`text`：RawMessage | string[]|RawMessage|string

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setHudVisibility`


///

```js
setHudVisibility(visible: HudVisibility, hudElements?: HudElement[]): void
```

/// html | div.result
//// define
`visible`：[`HudVisibility`](./hudvisibility.md)

- 参数1。


////

//// define
`hudElements`：<code><a href="./hudelement.md">HudElement</a>[]</code>|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setTitle`


///

```js
setTitle(title: RawMessage | string[] | RawMessage | string, options?: TitleDisplayOptions): void
```

/// html | div.result
//// define
`title`：RawMessage | string[]|RawMessage|string

- 参数1。


////

//// define
`options`：[`TitleDisplayOptions`](./titledisplayoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`updateSubtitle`


///

```js
updateSubtitle(subtitle: RawMessage | string[] | RawMessage | string): void
```

/// html | div.result
//// define
`subtitle`：RawMessage | string[]|RawMessage|string

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

