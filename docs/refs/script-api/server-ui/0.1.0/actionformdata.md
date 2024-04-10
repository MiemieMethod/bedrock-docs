# `ActionFormData`

> 文档版本：1.21.0.20

`ActionFormData`类。script_api.mojang-minecraft-ui.actionformdata.description

## 方法

/// define
`body`


///

script_api.mojang-minecraft-ui.actionformdata.body.description

```js
body(bodyText: string): ActionFormData
```

/// html | div.result
//// define
`bodyText`：`string`

- script_api.mojang-minecraft-ui.actionformdata.body.bodytext.description


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.mojang-minecraft-ui.actionformdata.body.return


////

///


/// define
`button`


///

script_api.mojang-minecraft-ui.actionformdata.button.description

```js
button(text: string, iconPath?: string): ActionFormData
```

/// html | div.result
//// define
`text`：`string`

- script_api.mojang-minecraft-ui.actionformdata.button.text.description


////

//// define
`iconPath`：`string`|`undefined`

- script_api.mojang-minecraft-ui.actionformdata.button.iconpath.description


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.mojang-minecraft-ui.actionformdata.button.return


////

///


/// define
`constructor`


///

script_api.mojang-minecraft-ui.actionformdata.constructor.description

```js
new constructor(): ActionFormData
```

/// html | div.result
//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.mojang-minecraft-ui.actionformdata.constructor.return


////

///


/// define
`show`


///

script_api.mojang-minecraft-ui.actionformdata.show.description

```js
show(player: Player): Promise<ActionFormResponse>
```

/// html | div.result
//// define
`player`：[`Player`](../../server/0.1.0/player.md)

- script_api.mojang-minecraft-ui.actionformdata.show.player.description


////

//// define
返回值：<code>Promise&lt;<a href="../actionformresponse/">ActionFormResponse</a>&gt;</code>

- script_api.mojang-minecraft-ui.actionformdata.show.return


////

///


/// define
`title`


///

script_api.mojang-minecraft-ui.actionformdata.title.description

```js
title(titleText: string): ActionFormData
```

/// html | div.result
//// define
`titleText`：`string`

- script_api.mojang-minecraft-ui.actionformdata.title.titletext.description


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- script_api.mojang-minecraft-ui.actionformdata.title.return


////

///

