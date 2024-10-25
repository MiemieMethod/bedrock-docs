# `InputInfo`

> 文档版本：1.21.50.25

`InputInfo`类。script_api.@minecraft/server.inputinfo.description

## 属性

/// define
`lastInputModeUsed`


///

```js
read-only lastInputModeUsed: InputMode;
```

/// html | div.result
//// define
`lastInputModeUsed`：[`InputMode`](./inputmode.md)

- script_api.@minecraft/server.inputinfo.lastinputmodeused.description


////

///


/// define
`touchOnlyAffectsHotbar`


///

```js
read-only touchOnlyAffectsHotbar: boolean;
```

/// html | div.result
//// define
`touchOnlyAffectsHotbar`：`boolean`

- script_api.@minecraft/server.inputinfo.touchonlyaffectshotbar.description


////

///


## 方法

/// define
`getButtonState`


///

script_api.@minecraft/server.inputinfo.getbuttonstate.description

```js
getButtonState(button: InputButton): ButtonState
```

/// html | div.result
//// define
`button`：[`InputButton`](./inputbutton.md)

- script_api.@minecraft/server.inputinfo.getbuttonstate.button.description


////

//// define
返回值：[`ButtonState`](./buttonstate.md)

- script_api.@minecraft/server.inputinfo.getbuttonstate.return


////

///


/// define
`getMovementVector`


///

script_api.@minecraft/server.inputinfo.getmovementvector.description

```js
getMovementVector(): Vector2
```

/// html | div.result
//// define
返回值：[`Vector2`](./vector2.md)

- script_api.@minecraft/server.inputinfo.getmovementvector.return


////

///

