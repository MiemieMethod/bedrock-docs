# 红石方块

自定义方块默认不参与红石信号的导通。通过几个专用组件，可以让自定义方块成为红石绝缘体、导体、消费者或产生者。

## 红石绝缘体（默认）

自定义方块默认就是红石绝缘体——不导通也不阻断红石信号，红石粉可以绕过它传播。无需任何额外配置。

如果需要显式声明（例如在某个置换中覆盖导体配置），可以将 `propagates_power` 设为 `false`：

```json title="components"
"minecraft:redstone_conductivity": {
    "redstone_conductor": false,
    "propagates_power": false
}
```

## 红石导体

要让方块像石头和金属块一样导通红石信号，添加 `minecraft:redstone_conductivity` 组件并开启 `redstone_conductor`：

```json title="BP/blocks/metal_block.json > components"
"minecraft:redstone_conductivity": {
    "redstone_conductor": true
}
```

/// note
默认情况下 `propagates_power` 也为 `true`，表示方块侧面可以作为红石粉的传播路径（像石头一样）。
///

## 红石消费者（接收信号）

红石消费者在接收到红石信号时可以触发自定义组件事件。配置 `minecraft:redstone_consumer` 组件并监听 `onRedstoneUpdate` 钩子：

```json title="BP/blocks/powered_light.json > components"
"minecraft:redstone_consumer": {
    "direction": "all"
},
"wiki:redstone_light": {}
```

```js title="BP/scripts/powered_light.js"
import { system } from "@minecraft/server";

const RedstoneLight = {
    onRedstoneUpdate({ block }) {
        const power = block.getRedstonePower() ?? 0;
        block.setPermutation(
            block.permutation.withState("wiki:is_on", power > 0)
        );
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:redstone_light", RedstoneLight);
});
```

/// warning | 已知问题（MCPE-232715）
添加 `minecraft:redstone_consumer` 后，方块的导体性能会被禁用。如果你的方块同时需要是导体，必须在 `minecraft:redstone_conductivity` 中显式设置 `propagates_power: true`：

```json
"minecraft:redstone_conductivity": {
    "redstone_conductor": true,
    "propagates_power": true
}
```
///

`onRedstoneUpdate` 事件中，可以用 `block.getRedstonePower()` 获取方块当前接收到的红石信号强度（0～15）。

## 红石产生者（输出信号）

红石产生者可以向相邻方块输出红石信号。使用 `minecraft:redstone_producer` 组件配置输出方向和信号强度的计算方式：

```json title="BP/blocks/detector.json > components"
"minecraft:redstone_producer": {
    "direction": "all",
    "signal_strength": "q.block_state('wiki:power_level')"
}
```

- `direction`：输出方向，可选 `"all"` 或具体面列表。
- `signal_strength`：信号强度，支持固定整数或Molang表达式（0～15）。

`signal_strength` 使用Molang时，可以根据方块状态动态调整输出信号强度，实现类似原版压力板的效果。