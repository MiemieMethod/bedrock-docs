# `@minecraft/server-admin`

> 文档版本：1.21.60.21

`@minecraft/server-admin`模块的`1.0.0-beta`版本，UUID为`53d7f2bf-bf9c-49c4-ad1f-7c803d947920`。该模块是script_api.@minecraft/server-admin.description

/// info | 依赖
该模块依赖于以下模块：

- `@minecraft/common`|`1.0.0`|`77ec12b4-1b2b-4c98-8d34-d1cd63f849d5`
- `@minecraft/server`|`1.0.0`|`b26a4d4c-afdf-4690-88f8-931846312678`
///

## 对象

/// define
`secrets`


///

```js
static read-only secrets: ServerSecrets;
```

/// html | div.result
//// define
`secrets`：[`ServerSecrets`](./serversecrets.md)

- script_api.@minecraft/server-admin.secrets.description


////

///


/// define
`variables`


///

```js
static read-only variables: ServerVariables;
```

/// html | div.result
//// define
`variables`：[`ServerVariables`](./servervariables.md)

- script_api.@minecraft/server-admin.variables.description


////

///


## 函数

/// define
`transferPlayer`


///

script_api.@minecraft/server-admin.transferplayer.description

```js
static transferPlayer(player: Player, host: string, port: uint16): void
```

/// html | div.result
//// define
`player`：[`Player`](../../server/1.0.0/player.md)

- script_api.@minecraft/server-admin.transferplayer.player.description


////

//// define
`host`：`string`

- script_api.@minecraft/server-admin.transferplayer.host.description


////

//// define
`port`：`uint16`∈[`1`, `65535`]

- script_api.@minecraft/server-admin.transferplayer.port.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-admin.transferplayer.return


////

///


## 类

|类|描述|
|---|---|
|[`SecretString`](./secretstring.md)||
|[`ServerSecrets`](./serversecrets.md)||
|[`ServerVariables`](./servervariables.md)||
