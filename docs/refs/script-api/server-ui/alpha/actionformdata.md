# `ActionFormData`

> 文档版本：1.21.60.21

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
`bodyText`：[`RawMessage`](../../server/alpha/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.actionformdata.body.bodytext.description


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
`text`：[`RawMessage`](../../server/alpha/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.actionformdata.button.text.description


////

//// define
`iconPath`?：`string`＝`null`

- script_api.@minecraft/server-ui.actionformdata.button.iconpath.description


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
`player`：[`Player`](../../server/alpha/player.md)

- script_api.@minecraft/server-ui.actionformdata.show.player.description


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
`titleText`：[`RawMessage`](../../server/alpha/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.actionformdata.title.titletext.description


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.@minecraft/server-ui.actionformdata.title.return


////

///

