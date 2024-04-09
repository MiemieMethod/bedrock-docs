# `Player`

> 文档版本：1.21.0.20

`Player`类，扩展自[`Entity`](./entity.md)。script_api.mojang-minecraft.player.description

## 属性

/// define
`name`


///

```js
read-only name: string;
```

/// html | div.result
//// define
`name`：`string`

- script_api.mojang-minecraft.player.name.description


////

///


/// define
`selectedSlot`


///

```js
selectedSlot: int32;
```

/// html | div.result
//// define
`selectedSlot`：`int32`

- script_api.mojang-minecraft.player.selectedslot.description


////

///


## 方法

/// define
`getItemCooldown`


///

script_api.mojang-minecraft.player.getitemcooldown.description

```js
getItemCooldown(cooldownCategory: string): int32
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- script_api.mojang-minecraft.player.cooldowncategory.getitemcooldown.description


////

//// define
返回值：`int32`

- script_api.mojang-minecraft.player.getitemcooldown.return


////

///


/// define
`playSound`


///

script_api.mojang-minecraft.player.playsound.description

```js
playSound(soundId: string, soundOptions?: SoundOptions): void
```

/// html | div.result
//// define
`soundId`：`string`

- script_api.mojang-minecraft.player.soundid.playsound.description


////

//// define
`soundOptions`：[`SoundOptions`](./soundoptions.md)|`undefined`

- script_api.mojang-minecraft.player.soundoptions.playsound.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.player.playsound.return


////

///


/// define
`postClientMessage`


///

script_api.mojang-minecraft.player.postclientmessage.description

```js
postClientMessage(id: string, value: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.mojang-minecraft.player.id.postclientmessage.description


////

//// define
`value`：`string`

- script_api.mojang-minecraft.player.value.postclientmessage.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.player.postclientmessage.return


////

///


/// define
`startItemCooldown`


///

script_api.mojang-minecraft.player.startitemcooldown.description

```js
startItemCooldown(cooldownCategory: string, tickDuration: int32): void
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- script_api.mojang-minecraft.player.cooldowncategory.startitemcooldown.description


////

//// define
`tickDuration`：`int32`

- script_api.mojang-minecraft.player.tickduration.startitemcooldown.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.player.startitemcooldown.return


////

///

