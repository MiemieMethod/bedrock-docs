# `BlockSignComponent`

> 文档版本：1.21.0.20

`BlockSignComponent`类，扩展自`BlockComponent`。

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:sign";
```


## 属性

/// define
`isWaxed`


///

```js
read-only isWaxed: boolean;
```


## 方法

/// define
`getRawText`


///

```js
getRawText(side: SignSide): RawText | undefined
```

/// html | div.result
//// define
`side`：[`SignSide`](./signside.md)

- 参数1。


////

//// define
返回值：[`RawText`](./rawtext.md)|`undefined`

- 返回值。


////

///


/// define
`getText`


///

```js
getText(side: SignSide): string | undefined
```

/// html | div.result
//// define
`side`：[`SignSide`](./signside.md)

- 参数1。


////

//// define
返回值：`string`|`undefined`

- 返回值。


////

///


/// define
`getTextDyeColor`


///

```js
getTextDyeColor(side: SignSide): DyeColor | undefined
```

/// html | div.result
//// define
`side`：[`SignSide`](./signside.md)

- 参数1。


////

//// define
返回值：[`DyeColor`](./dyecolor.md)|`undefined`

- 返回值。


////

///


/// define
`setText`


///

```js
setText(message: RawMessage | RawText | string, side: SignSide): void
```

/// html | div.result
//// define
`message`：RawMessage|RawText|string

- 参数1。


////

//// define
`side`：[`SignSide`](./signside.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setTextDyeColor`


///

```js
setTextDyeColor(color?: DyeColor, side: SignSide): void
```

/// html | div.result
//// define
`color`：[`DyeColor`](./dyecolor.md)|`undefined`

- 参数1。


////

//// define
`side`：[`SignSide`](./signside.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setWaxed`


///

```js
setWaxed(waxed: boolean): void
```

/// html | div.result
//// define
`waxed`：`boolean`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

