# 方块声音

自定义方块可以使用原版内置的声音类型，也可以定义完全自定义的声音。

## 使用内置音效类型

在资源包的 `blocks.json` 中，可以为自定义方块指定一个声音类型：

```json title="RP/blocks.json"
{
    "wiki:my_block": {
        "sound": "stone"
    }
}
```

这里的 `"stone"` 是声音类型标识符，对应游戏中石头方块放置、破坏、踩踏等时的音效。游戏内置了数十种声音类型，完整列表见[原版方块音效类型参考表](../../../refs/tables/blocks/block_sound_types.md)。

## 自定义方块音效

如果内置声音类型不满足需求，可以在 `sounds/sound_definitions.json` 中定义新的音效，然后在 `sounds.json` 中关联到方块：

### 第一步：定义音效

```json title="RP/sounds/sound_definitions.json"
{
    "wiki.my_block.break": {
        "category": "block",
        "sounds": [
            "sounds/wiki/blocks/my_block_break"
        ]
    },
    "wiki.my_block.place": {
        "category": "block",
        "sounds": [
            "sounds/wiki/blocks/my_block_place"
        ]
    },
    "wiki.my_block.step": {
        "category": "block",
        "sounds": [
            "sounds/wiki/blocks/my_block_step"
        ]
    },
    "wiki.my_block.hit": {
        "category": "block",
        "sounds": [
            "sounds/wiki/blocks/my_block_hit"
        ]
    }
}
```

音效文件（`.ogg` 或 `.fsb` 格式）放在 `sounds/wiki/blocks/` 目录下。

### 第二步：在sounds.json中注册方块音效

```json title="RP/sounds.json"
{
    "block_sounds": {
        "wiki:custom_sound": {
            "events": {
                "break": "wiki.my_block.break",
                "place": "wiki.my_block.place",
                "step": "wiki.my_block.step",
                "hit": "wiki.my_block.hit",
                "fall": "wiki.my_block.step",
                "jump": "wiki.my_block.step",
                "land": "wiki.my_block.step"
            },
            "pitch": [0.8, 1.2],
            "volume": 1.0
        }
    }
}
```

### 第三步：在blocks.json中指定

```json title="RP/blocks.json"
{
    "wiki:my_block": {
        "sound": "wiki:custom_sound"
    }
}
```

## 音效事件说明

方块音效共有7种事件类型：

/// define
`break`

- 方块被破坏时播放。

`place`

- 方块被放置时播放。

`hit`

- 玩家对方块持续挖掘（蓄力中）时循环播放。

`step`

- 实体在方块上行走时播放。

`fall`

- 实体从高处跌落到方块上时播放。

`jump`

- 实体从方块上起跳时播放。

`land`

- 实体落地到方块上时播放。

///

/// note | 最低配置
最常用的是 `break`、`place`、`hit`、`step`。`fall`、`jump`、`land` 如果不单独指定，默认回退到 `step` 的音效。
///

## 通过脚本API播放声音 <!-- md:flag vanilla -->

在自定义组件事件中，可以手动在方块位置播放音效：

```js
onPlayerInteract({ block }) {
    block.dimension.playSound("random.click", block.center(), {
        pitch: 1.0,
        volume: 1.0
    });
}
```