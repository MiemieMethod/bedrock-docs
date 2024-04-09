# `ActionFormData`

> 文档版本：1.21.0.20

`ActionFormData`类。script_api.@minecraft/server-ui.actionformdata.description

## 方法

/// define
`body`


///

script_api.@minecraft/server-ui.actionformdata.body.description

```js
body(bodyText: RawMessage | string): ActionFormData
```

/// html | div.result
//// define
`bodyText`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.actionformdata.bodytext.body.description


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.@minecraft/server-ui.actionformdata.body.return


////

///


/// define
`button`


///

script_api.@minecraft/server-ui.actionformdata.button.description

```js
button(text: RawMessage | string, iconPath?: string): ActionFormData
```

/// html | div.result
//// define
`text`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.actionformdata.text.button.description


////

//// define
`iconPath`：`string`|`undefined`

- script_api.@minecraft/server-ui.actionformdata.iconpath.button.description


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.@minecraft/server-ui.actionformdata.button.return


////

///


/// define
`constructor`


///

script_api.@minecraft/server-ui.actionformdata.constructor.description

```js
new constructor(): ActionFormData
```

/// html | div.result
//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.@minecraft/server-ui.actionformdata.constructor.return


////

///


/// define
`show`


///

script_api.@minecraft/server-ui.actionformdata.show.description

```js
show(player: Player): Promise<ActionFormResponse>
```

/// html | div.result
//// define
`player`：[`Player`](../../server/1.8.0/player.md)

- script_api.@minecraft/server-ui.actionformdata.player.show.description


////

//// define
返回值：<code>Promise&lt;<a href="../actionformresponse/">ActionFormResponse</a>&gt;</code>

- script_api.@minecraft/server-ui.actionformdata.show.return


////

///


/// define
`title`


///

script_api.@minecraft/server-ui.actionformdata.title.description

```js
title(titleText: RawMessage | string): ActionFormData
```

/// html | div.result
//// define
`titleText`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.actionformdata.titletext.title.description


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.@minecraft/server-ui.actionformdata.title.return


////

///

