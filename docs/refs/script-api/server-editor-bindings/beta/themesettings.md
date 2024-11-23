# `ThemeSettings`

> 文档版本：1.21.60.21

`ThemeSettings`类。script_api.@minecraft/server-editor-bindings.themesettings.description

## 方法

/// define
`addNewTheme`


///

script_api.@minecraft/server-editor-bindings.themesettings.addnewtheme.description

```js
addNewTheme(id: string, name?: string, sourceThemeId?: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.addnewtheme.id.description


////

//// define
`name`?：`string`＝`null`

- script_api.@minecraft/server-editor-bindings.themesettings.addnewtheme.name.description


////

//// define
`sourceThemeId`?：`string`＝`null`

- script_api.@minecraft/server-editor-bindings.themesettings.addnewtheme.sourcethemeid.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.themesettings.addnewtheme.return


////

///


/// define
`canThemeBeModified`


///

script_api.@minecraft/server-editor-bindings.themesettings.canthemebemodified.description

```js
canThemeBeModified(id: string): boolean
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.canthemebemodified.id.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.themesettings.canthemebemodified.return


////

///


/// define
`deleteTheme`


///

script_api.@minecraft/server-editor-bindings.themesettings.deletetheme.description

```js
deleteTheme(id: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.deletetheme.id.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.themesettings.deletetheme.return


////

///


/// define
`getCurrentTheme`


///

script_api.@minecraft/server-editor-bindings.themesettings.getcurrenttheme.description

```js
getCurrentTheme(): string
```

/// html | div.result
//// define
返回值：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.getcurrenttheme.return


////

///


/// define
`getThemeColors`


///

script_api.@minecraft/server-editor-bindings.themesettings.getthemecolors.description

```js
getThemeColors(id: string): Record<string, RGBA> | undefined
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.getthemecolors.id.description


////

//// define
返回值：<code>Record&lt;string, <a href="../../../server/beta/rgba/">RGBA</a>&gt;</code>|`undefined`

- script_api.@minecraft/server-editor-bindings.themesettings.getthemecolors.return


////

///


/// define
`getThemeIdList`


///

script_api.@minecraft/server-editor-bindings.themesettings.getthemeidlist.description

```js
getThemeIdList(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server-editor-bindings.themesettings.getthemeidlist.return


////

///


/// define
`getThemeName`


///

script_api.@minecraft/server-editor-bindings.themesettings.getthemename.description

```js
getThemeName(id: string): string
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.getthemename.id.description


////

//// define
返回值：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.getthemename.return


////

///


/// define
`resolveColorKey`


///

script_api.@minecraft/server-editor-bindings.themesettings.resolvecolorkey.description

```js
resolveColorKey(key: ThemeSettingsColorKey): RGBA
```

/// html | div.result
//// define
`key`：[`ThemeSettingsColorKey`](./themesettingscolorkey.md)

- script_api.@minecraft/server-editor-bindings.themesettings.resolvecolorkey.key.description


////

//// define
返回值：[`RGBA`](../../server/beta/rgba.md)

- script_api.@minecraft/server-editor-bindings.themesettings.resolvecolorkey.return


////

///


/// define
`setCurrentTheme`


///

script_api.@minecraft/server-editor-bindings.themesettings.setcurrenttheme.description

```js
setCurrentTheme(id: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.setcurrenttheme.id.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.themesettings.setcurrenttheme.return


////

///


/// define
`setThemeName`


///

script_api.@minecraft/server-editor-bindings.themesettings.setthemename.description

```js
setThemeName(id: string, name: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.setthemename.id.description


////

//// define
`name`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.setthemename.name.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.themesettings.setthemename.return


////

///


/// define
`updateThemeColor`


///

script_api.@minecraft/server-editor-bindings.themesettings.updatethemecolor.description

```js
updateThemeColor(id: string, key: ThemeSettingsColorKey, newColor: RGBA): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.themesettings.updatethemecolor.id.description


////

//// define
`key`：[`ThemeSettingsColorKey`](./themesettingscolorkey.md)

- script_api.@minecraft/server-editor-bindings.themesettings.updatethemecolor.key.description


////

//// define
`newColor`：[`RGBA`](../../server/beta/rgba.md)

- script_api.@minecraft/server-editor-bindings.themesettings.updatethemecolor.newcolor.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.themesettings.updatethemecolor.return


////

///

