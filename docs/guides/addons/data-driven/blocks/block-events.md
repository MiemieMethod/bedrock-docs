# 自定义组件与方块事件

基岩版通过**自定义组件**机制，让脚本API<!-- md:flag vanilla -->可以响应方块上发生的各种事件，例如玩家交互、踩踏、随机刻等。

## 注册自定义组件

自定义组件必须在世界加载之前注册，要使用 `system.beforeEvents.startup` 事件：

```js title="BP/scripts/my_block.js"
import { system } from "@minecraft/server";

/** @type {import("@minecraft/server").BlockCustomComponent} */
const MyBlockComponent = {
    onPlayerInteract({ block, player }) {
        player?.sendMessage(`你点击了 ${block.typeId}！`);
    },
    onTick({ block }) {
        // 每次刻触发
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:my_component", MyBlockComponent);
});
```

注册之后，在方块JSON中声明使用这个组件：

```json title="BP/blocks/my_block.json > components"
"wiki:my_component": {}
```

## 参数化自定义组件

自定义组件可以接受参数，让同一套逻辑适配不同方块：

```json title="BP/blocks/my_block.json > components"
"wiki:reward_on_break": {
    "item": "minecraft:diamond",
    "count": 3
}
```

在脚本中通过事件对象的 `params` 字段读取参数：

```js
const RewardOnBreakComponent = {
    onPlayerBreak({ block, dimension }, { params }) {
        const { item, count } = params;
        dimension.spawnItem(
            new ItemStack(item, count),
            block.center()
        );
    }
};
```

## 事件钩子一览

以下是 `BlockCustomComponent` 支持的所有事件钩子：

/// define
`beforeOnPlayerPlace`

- 玩家**将要放置**该方块之前触发。可通过 `event.cancel = true` 取消放置。

`onBreak`

- 方块以**任何方式被破坏**时触发（玩家、爆炸、命令等）。

`onEntityFallOn`

- 实体**跌落到**该方块上时触发。需配合 `minecraft:entity_fall_on` 组件，可设置触发所需的最小跌落高度。

`onPlace`

- 方块以**任何方式被放置**后触发。

`onPlayerBreak`

- **玩家破坏**该方块时触发（不含爆炸、命令等方式）。

`onPlayerInteract`

- **玩家右键交互**该方块时触发。

`onRandomTick`

- **随机刻**触发时调用。需配合 `minecraft:tick` 组件并设置 `interval_range` 和 `looping: true`。

`onRedstoneUpdate`

- 该方块接收到的**红石信号发生变化**时触发。

`onStepOff`

- 实体**走出**该方块时触发。

`onStepOn`

- 实体**走上**该方块时触发。

`onTick`

- 按 `minecraft:tick` 组件设定的**固定间隔**触发。

///

## 完整示例：交互开关灯

这个例子展示了一个可以交互切换开关状态的灯：

```json title="BP/blocks/toggle_lamp.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:toggle_lamp",
            "states": {
                "wiki:is_on": [false, true]
            }
        },
        "components": {
            "wiki:toggle": {
                "state": "wiki:is_on",
                "on_sound": "random.click",
                "off_sound": "random.click"
            },
            "minecraft:material_instances": {
                "*": { "texture": "wiki:lamp_off" }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('wiki:is_on')",
                "components": {
                    "minecraft:light_emission": 15,
                    "minecraft:material_instances": {
                        "*": { "texture": "wiki:lamp_on" }
                    }
                }
            }
        ]
    }
}
```

```js title="BP/scripts/toggle_lamp.js"
import { system } from "@minecraft/server";

const ToggleComponent = {
    onPlayerInteract({ block }, { params }) {
        const currentState = block.permutation.getState(params.state);
        block.setPermutation(
            block.permutation.withState(params.state, !currentState)
        );
        block.dimension.playSound(
            currentState ? params.off_sound : params.on_sound,
            block.center()
        );
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:toggle", ToggleComponent);
});
```

## 定时触发：minecraft:tick

`minecraft:tick` 组件配合 `onTick` 钩子，可以实现按固定间隔执行逻辑：

```json title="components"
"minecraft:tick": {
    "interval_range": [20, 20],
    "looping": true,
    "looping_deadline": 0
}
```

- `interval_range`：触发间隔的随机范围（单位：刻）。设为 `[20, 20]` 表示每1秒触发一次。
- `looping`：是否循环触发。
- `looping_deadline`：循环最大触发次数，0表示无限。

`onRandomTick` 类似，但依赖游戏的随机刻机制（需要 `interval_range` 和 `looping: true`）。

## 旧版JSON事件迁移

在格式版本1.20.0之前，自定义方块事件使用JSON响应定义。这种旧式事件已被废弃，不应在新方块中使用。以下是几个常见旧式响应的Script API等效写法：

/// tab | 添加状态效果
旧式：`add_mob_effect`

```js
onStepOn({ entity }) {
    entity?.addEffect("regeneration", 30, { amplifier: 10, showParticles: false });
}
```
///

/// tab | 对实体造成伤害
旧式：`damage`

```js
import { EntityDamageCause } from "@minecraft/server";

// ...
onStepOn({ entity }) {
    entity?.applyDamage(2, { cause: EntityDamageCause.drowning });
}
```
///

/// tab | 运行命令
旧式：`run_command`

```js
onPlayerInteract({ block }) {
    block.dimension.runCommand(`say 命令在此运行！`);
}
```
///