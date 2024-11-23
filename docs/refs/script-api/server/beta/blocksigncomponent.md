# `BlockSignComponent`

> 文档版本：1.21.60.21

`BlockSignComponent`类，扩展自[`BlockComponent`](./blockcomponent.md)。script_api.@minecraft/server.blocksigncomponent.description

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

/// html | div.result
//// define
`isWaxed`：`boolean`

- script_api.@minecraft/server.blocksigncomponent.iswaxed.description


////

///


## 方法

/// define
`getRawText`


///

script_api.@minecraft/server.blocksigncomponent.getrawtext.description

```js
getRawText(side: SignSide): RawText | undefined
```

/// html | div.result
//// define
`side`：[`SignSide`](./signside.md)＝`0`

- script_api.@minecraft/server.blocksigncomponent.getrawtext.side.description


////

//// define
返回值：[`RawText`](./rawtext.md)|`undefined`

- script_api.@minecraft/server.blocksigncomponent.getrawtext.return


////

///


/// define
`getText`


///

script_api.@minecraft/server.blocksigncomponent.gettext.description

```js
getText(side: SignSide): string | undefined
```

/// html | div.result
//// define
`side`：[`SignSide`](./signside.md)＝`0`

- script_api.@minecraft/server.blocksigncomponent.gettext.side.description


////

//// define
返回值：`string`|`undefined`

- script_api.@minecraft/server.blocksigncomponent.gettext.return


////

///


/// define
`getTextDyeColor`


///

script_api.@minecraft/server.blocksigncomponent.gettextdyecolor.description

```js
getTextDyeColor(side: SignSide): DyeColor | undefined
```

/// html | div.result
//// define
`side`：[`SignSide`](./signside.md)＝`0`

- script_api.@minecraft/server.blocksigncomponent.gettextdyecolor.side.description


////

//// define
返回值：[`DyeColor`](./dyecolor.md)|`undefined`

- script_api.@minecraft/server.blocksigncomponent.gettextdyecolor.return


////

///


/// define
`setText`


///

script_api.@minecraft/server.blocksigncomponent.settext.description

```js
setText(message: RawMessage | RawText | string, side: SignSide): void
```

/// html | div.result
//// define
`message`：[`RawMessage`](./rawmessage.md)|[`RawText`](./rawtext.md)|`string`

- script_api.@minecraft/server.blocksigncomponent.settext.message.description


////

//// define
`side`：[`SignSide`](./signside.md)＝`0`

- script_api.@minecraft/server.blocksigncomponent.settext.side.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.blocksigncomponent.settext.return


////

///


/// define
`setTextDyeColor`


///

script_api.@minecraft/server.blocksigncomponent.settextdyecolor.description

```js
setTextDyeColor(color?: DyeColor, side: SignSide): void
```

/// html | div.result
//// define
`color`?：[`DyeColor`](./dyecolor.md)＝`null`

- script_api.@minecraft/server.blocksigncomponent.settextdyecolor.color.description


////

//// define
`side`：[`SignSide`](./signside.md)＝`0`

- script_api.@minecraft/server.blocksigncomponent.settextdyecolor.side.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.blocksigncomponent.settextdyecolor.return


////

///


/// define
`setWaxed`


///

script_api.@minecraft/server.blocksigncomponent.setwaxed.description

```js
setWaxed(waxed: boolean): void
```

/// html | div.result
//// define
`waxed`：`boolean`

- script_api.@minecraft/server.blocksigncomponent.setwaxed.waxed.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.blocksigncomponent.setwaxed.return


////

///

