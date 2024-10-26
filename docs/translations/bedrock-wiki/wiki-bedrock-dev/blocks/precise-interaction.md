---
title: 精确交互
description: 学习如何与同一块的不同部分进行交互。
category: 教程
tags:
    - 实验性
    - 专家
    - 脚本
mentions:
    - QuazChick
    - SmokeyStack
---

::: tip 格式 & 最低引擎版本 `1.21.40`
本教程假设您对区块和脚本有高级理解。在开始之前，请先查看 [区块](/blocks/blocks-intro) 和 [脚本](/scripting/starting-scripts) 指南。
:::

创建玩家可以互动的自定义区块的能力从实现上可能非常基础，但仍然允许复杂的功能。然而，有时基于简单右键点击或轻敲区块而没有位置特定条件的默认交互模式不足以实现所需的功能。

例如，如果您想创建一个在一侧有多个按钮的区块，每个按钮触发不同的动作，该怎么办？或者一个分段显示器，其中多个单独点亮的灯可以包含在一个区块内。

这就是精确交互发挥作用的地方！以下的精确交互方法允许您在一个区块中定义多个可以单独交互的区域，并为每个区域分配不同的功能。在本教程中，我们将向您展示如何使用脚本为您的区块添加精确交互，并提供每种方法的示例。

**注意：** 精确交互并不能使区块拥有多个/自定义形状的 [`minecraft:selection_box`](/blocks/block-components#selection-box) 组件。选择框必须位于所有定义的区域内，以确保精确交互正常工作。

![展示图像显示示例鸽槽和双花盆区块](/assets/images/blocks/precise-interaction/showcase.png)

## 工作原理

提供的精确交互方法使用 [`player interact event`](https://learn.microsoft.com/minecraft/creator/scriptapi/minecraft/server/blockcomponentplayerinteractevent?view=minecraft-bedrock-experimental) 的 `faceLocation` 属性。

这个值告诉我们在区块的 `minecraft:selection_box` 上的哪个位置被选择/点击，这是精确交互所依赖的。

**注意：** `faceLocation` 本应相对于被交互区块的左下西角，但当前相对于世界原点，这意味着我们需要进行额外的计算以使其相对。当此问题解决后，将不再需要此计算。

## FaceSelectionPlains 类

此类允许您在区块的表面定义二维区域并获取被选择的平面。

要使用此方法进行精确交互，请创建文件 `BP/scripts/utilities/face_selection_plains.js` 并将以下代码粘贴到其中。

<details>
<summary>FaceSelectionPlains 代码</summary>

<pre><code>BP/scripts/utilities/face_selection_plains.js
```js
import { Direction } from "@minecraft/server";

const isInRange = (value, min, max) => value >= min && value <= max;

export default class FaceSelectionPlains {
    /**
     * 允许您在区块的表面定义二维区域并获取被选择的平面。
     *
     * @param {Object[]} plains 定义区块表面上可能被选择的二维区域的数组。
     * @param {[number, number]} plains[].origin [U, V] 数组定义平面相对于区块表面左上角的偏移量（像素）。
     * @param {[number, number]} plains[].size [U, V] 数组定义平面的大小，从左上角延伸（像素）。
     * @param {string} [plains[].name] 自定义名称，以便在选择时轻松识别此平面。
     */
    constructor(...plains) {
        this.plains = plains;
    }
    /**
     * @param {Object} selection
     * @param {Direction} selection.face
     * @param {import("@minecraft/server").Vector3} selection.faceLocation
     *
     * @param {Object} [options]
     * @param {boolean} [options.invertU] 如果为 true，水平轴从 `右 -> 左` 延伸而不是 `左 -> 右`。
     * @param {boolean} [options.invertV] 如果为 true，垂直轴从 `下 -> 上` 延伸而不是 `上 -> 下`。
     *
     * @returns 选定的平面 ID，或如果未提供 ID 则返回平面索引。如果没有平面适用于选择，则返回 `undefined`。
     */
    getSelected(selection, options) {
        const { face, faceLocation } = selection;

        // 创建一个新对象，以免修改原始对象
        let location = { ...faceLocation };

        const horizontalAxis = face === Direction.East || face === Direction.West ? "z" : "x";
        const verticalAxis = face === Direction.Up || face === Direction.Down ? "z" : "y";

        if (face !== Direction.Down) location[verticalAxis] = 1 - location[verticalAxis];
        if (face !== Direction.South && face !== Direction.West)
            location[horizontalAxis] = 1 - location[horizontalAxis];

        if (options?.invertU) location[horizontalAxis] = 1 - location[horizontalAxis];
        if (options?.invertV) location[verticalAxis] = 1 - location[verticalAxis];

        for (let i = 0; i < this.plains.length; i++) {
            const plain = this.plains[i];

            const inHorizontalRange = isInRange(
                location[horizontalAxis],
                plain.origin[0] / 16,
                (plain.origin[0] + plain.size[0]) / 16
            );
            const inVerticalRange = isInRange(
                location[verticalAxis],
                plain.origin[1] / 16,
                (plain.origin[1] + plain.size[1]) / 16
            );

            if (inHorizontalRange && inVerticalRange) return plain.name ?? i;
        }
    }
}
```
</code></pre>

</details>

### 方法

- #### constructor

    ```ts
    new FaceSelectionPlains(...plains: { origin: [number, number]; size: [number, number]; name?: string }[])
    ```

    创建一个新的 `FaceSelectionPlains` 实例。

    <details>
    <summary>参数</summary>

    - **plains**: `Object[]`

        定义区块表面上可能被选择的二维区域的数组。

        - **origin**: `[number, number]`

            [U, V] 数组定义平面相对于区块表面左上角的偏移量。

        - **size**: `[number, number]`

            [U, V] 数组定义平面的大小，从左上角延伸。

        - **name**?: `string`

            自定义名称，以便在选择时轻松识别此平面。

    </details>

- #### getSelected

    ```ts
    getSelected(selection: { face: Direction; faceLocation: Vector3 }, options?: { invertU?: boolean; invertV?: boolean }): number | string | undefined
    ```

    返回相关平面的数组索引或提供的名称。如果没有选择平面，则返回 `undefined`。

    <details>
    <summary>参数</summary>

    - **selection**: `Object`

        包含选择详情的对象。

        - **face**: [`Direction`](https://learn.microsoft.com/minecraft/creator/scriptapi/minecraft/server/direction)

            被选择的区块面。

        - **faceLocation**: [`Vector3`](https://learn.microsoft.com/minecraft/creator/scriptapi/minecraft/server/vector3)

            相对于区块左下西角的选择位置。

    - **options**?: `Object`

        可选地配置选定平面的计算方式。

        - **invertU**?: `boolean`

            如果为 true，水平轴从 `右 -> 左` 延伸而不是 `左 -> 右`。

        - **invertV**?: `boolean`

            如果为 true，垂直轴从 `下 -> 上` 延伸而不是 `上 -> 下`。

    </details>

### 使用

以下示例将目标区块面分成四个部分：

<pre><code>BP/scripts/blocks/example.js</code></pre>

```js
import { world } from "@minecraft/server";
import FaceSelectionPlains from "../utilities/face_selection_plains";

const quadrants = new FaceSelectionPlains(
    { origin: [0, 0], size: [8, 8] },
    { origin: [8, 0], size: [8, 8] },
    { origin: [0, 8], size: [8, 8] },
    { origin: [8, 8], size: [8, 8] }
);
```

此外，可以提供名称以便轻松识别每个平面：

```js
const quadrants = new FaceSelectionPlains(
    { origin: [0, 0], size: [8, 8], name: "top_left" },
    { origin: [8, 0], size: [8, 8], name: "top_right" },
    { origin: [0, 8], size: [8, 8], name: "bottom_left" },
    { origin: [8, 8], size: [8, 8], name: "bottom_right" }
);
```

这可以在一个 [自定义组件](/blocks/block-events) 中使用，以获取所选的象限：

```js
const QuadrantInteractionBlockComponent = {
    onPlayerInteract({ block, face, faceLocation }) {
        // 解决 faceLocation 错误 - 获取相对于区块的位置
        const relativeFaceLocation = {
            x: faceLocation.x - block.location.x,
            y: faceLocation.y - block.location.y,
            z: faceLocation.z - block.location.z,
        };

        // 返回选定区域的索引（0、1、2 或 3），或如果提供了名称（例如 "top_left"）。
        // 如果没有选择平面，则返回 `undefined`。
        const selectedQuadrant = quadrants.getSelected({
            face,
            faceLocation: relativeFaceLocation,
        });

        world.sendMessage(`选择了象限 ${selectedQuadrant}！`);
    },
};
```

## SelectionBoxes 类

::: warning
与 `minecraft:selection_box` 和 `minecraft:collision_box` 组件一样，在设置您的选择框时，请勿使用 Blockbench 显示的位置值，因为它们是从西北方向测量的，而不是东北方向。请改用导出 `.geo.json` 文件中的 origin 值。

如果您希望使用 Blockbench 的值，应该在 [`getSelected`](#getselected-1) 中将 `invertX` 选项设置为 true。
:::

此类允许您在区块中定义三维区域，并获取面选择所在的盒子。

要使用此方法进行精确交互，请创建文件 `BP/scripts/utilities/selection_boxes.js` 并将以下代码粘贴到其中。

<details>
<summary>SelectionBoxes 代码</summary>

<pre><code>BP/scripts/utilities/selection_boxes.js</code></pre>

```js
const isInRange = (value, min, max) => value >= min && value <= max;

export default class SelectionBoxes {
    /**
     * 允许您在区块中定义三维区域，并获取面选择所在的盒子。
     *
     * @param {Object[]} boxes 定义区块内可能被选择的三维区域的数组。
     * @param {[number, number, number]} boxes[].origin [X, Y, Z] 数组定义盒子相对于区块水平中线和垂直底部的偏移量（像素），从东北方向延伸。
     * @param {[number, number, number]} boxes[].size [X, Y, Z] 数组定义盒子的大小（像素），从东北方向延伸。
     * @param {string} [boxes[].name] 自定义名称，以便在选择时轻松识别此盒子。
     */
    constructor(...boxes) {
        this.boxes = boxes;
    }
    /**
     * 获取 `faceLocation` 所在的盒子。
     *
     * @param {import("@minecraft/server").Vector3} faceLocation 相对于区块左下西角的选择位置。
     *
     * @param {Object} [options] 可选地配置选定盒子的计算方式。
     * @param {boolean} [options.invertX] 如果为 true，X 轴从 `西 -> 东` 延伸而不是 `东 -> 西`，遵循 [Blockbench](https://blockbench.net) 的显示位置。
     * @param {boolean} [options.invertY] 如果为 true，Y 轴从 `上 -> 下` 延伸而不是 `下 -> 上`。
     * @param {boolean} [options.invertZ] 如果为 true，Z 轴从 `南 -> 北` 延伸而不是 `北 -> 南`。
     *
     * @returns {(string|number|undefined)} 选定盒子的名称，或如果未提供名称，则为盒子索引。如果没有盒子适用于选择，则返回 `undefined`。
     */
    getSelected(faceLocation, options) {
        // 创建一个新对象，以免修改原始对象
        let location = { ...faceLocation };

        // X 轴被反转以确保测量相对于区块左下东。
        if (!options?.invertX) location.x = 1 - location.x;
        if (options?.invertY) location.y = 1 - location.y;
        if (options?.invertZ) location.z = 1 - location.z;

        for (let i = 0; i < this.boxes.length; i++) {
            const box = this.boxes[i];

            const from = {
                x: box.origin[0] + 8,
                y: box.origin[1],
                z: box.origin[2] + 8,
            };
            const to = {
                x: from.x + box.size[0],
                y: from.y + box.size[1],
                z: from.z + box.size[2],
            };

            const inXRange = isInRange(location.x, from.x / 16, to.x / 16);
            const inYRange = isInRange(location.y, from.y / 16, to.y / 16);
            const inZRange = isInRange(location.z, from.z / 16, to.z / 16);

            if (inXRange && inYRange && inZRange) return box.name ?? i;
        }
    }
}
```

</details>

### 方法

- #### constructor

    ```ts
    new SelectionBoxes(...boxes: { origin: [number, number, number]; size: [number, number, number]; name?: string }[])
    ```

    创建一个新的 `SelectionBoxes` 实例。

    <details>
    <summary>参数</summary>

    - **boxes**: `Object[]`

        定义区块内可能被选择的三维区域的数组。

        - **origin**: `[number, number, number]`

            [X, Y, Z] 数组定义盒子相对于区块水平中线和垂直底部的偏移量（像素），从东北方向延伸。

        - **size**: `[number, number, number]`

            [X, Y, Z] 数组定义盒子的大小（像素），从东北方向延伸。

        - **name**?: `string`

            自定义名称，以便在选择时轻松识别此盒子。

    </details>

- #### getSelected

    ```ts
    getSelected(faceLocation: Vector3, options?: { invertX?: boolean; invertY?: boolean; invertZ?: boolean }): number | string | undefined
    ```

    获取 `faceLocation` 所在的盒子。

    返回相关盒子的数组索引或提供的名称。如果没有选择盒子，则返回 `undefined`。

    <details>
    <summary>参数</summary>

    - **faceLocation**: [`Vector3`](https://learn.microsoft.com/minecraft/creator/scriptapi/minecraft/server/vector3)

        相对于区块左下西角的选择位置。

    - **options**?: `Object`

        可选地配置选定盒子的计算方式。

        - **invertX**?: `boolean`

            如果为 true，X 轴从 `西 -> 东` 延伸而不是 `东 -> 西`，遵循 [Blockbench](https://blockbench.net) 的显示位置。

        - **invertY**?: `boolean`

            如果为 true，Y 轴从 `上 -> 下` 延伸而不是 `下 -> 上`。

        - **invertZ**?: `boolean`

            如果为 true，Z 轴从 `南 -> 北` 延伸而不是 `北 -> 南`。

    </details>

### 使用

以下示例将目标区块分成垂直两半：

<pre><code>BP/scripts/blocks/example.js</code></pre>

```js
import { world } from "@minecraft/server";
import SelectionBoxes from "../utilities/selection_boxes";

const verticalHalves = new SelectionBoxes(
    { origin: [-8, 8, -8], size: [16, 8, 16], name: "top" },
    { origin: [-8, 0, -8], size: [16, 8, 16], name: "bottom" }
);
```

这可以与 [`itemUseOn` 后事件](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemuseonafterevent) 一起使用，以获取选定的盒子：

```js
world.afterEvents.itemUseOn.subscribe((e) => {
    // 如果目标区块不是 "wiki:example_block"，则不执行任何操作
    if (e.block.typeId !== "wiki:example_block") return;

    // 返回选定的垂直半部分（"top" 或 "bottom"）。
    const selectedVerticalHalf = verticalHalves.getSelected(e.faceLocation);

    world.sendMessage(`选择了区块的 ${selectedVerticalHalf} 部分！`);
});
```

## 鸽槽示例

使用我们的 [FaceSelectionPlains](#faceselectionplains-类) 类，我们可以创建一个功能类似雕刻书架的区块。其他资源（纹理等）包含在 [示例附加包](#下载示例附加包) 中。

与纸张互动将填充选定的槽。销毁区块会释放所有存储的纸张物品。

![鸽槽展示](/assets/images/blocks/precise-interaction/pigeonholes.png)

<Button link="https://github.com/Bedrock-OSS/wiki-addon/blob/main/ma-precise_interaction/rp/models/blocks/pigeonholes.geo.json">
    下载鸽槽模型
</Button>

<details>
<summary>区块 JSON</summary>

<pre><code>BP/blocks/pigeonholes.json</code></pre>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:pigeonholes",
            "menu_category": {
                "category": "items"
            },
            "states": {
                "wiki:slot_0_occupied": [false, true],
                "wiki:slot_1_occupied": [false, true],
                "wiki:slot_2_occupied": [false, true],
                "wiki:slot_3_occupied": [false, true],
                "wiki:slot_4_occupied": [false, true],
                "wiki:slot_5_occupied": [false, true]
            },
            "traits": {
                "minecraft:placement_direction": {
                    "enabled_states": ["minecraft:cardinal_direction"],
                    "y_rotation_offset": 180
                }
            }
        },
        "components": {
            "minecraft:custom_components": ["wiki:pigeonholes_storage"],
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": 1.5
            },
            "minecraft:geometry": {
                "identifier": "geometry.pigeonholes",
                "culling": "wiki:pigeonholes_culling",
                "bone_visibility": {
                    // 根据槽是否被占用显示每个槽
                    "empty_slot_0": "!q.block_state('wiki:slot_0_occupied')",
                    "empty_slot_1": "!q.block_state('wiki:slot_1_occupied')",
                    "empty_slot_2": "!q.block_state('wiki:slot_2_occupied')",
                    "empty_slot_3": "!q.block_state('wiki:slot_3_occupied')",
                    "empty_slot_4": "!q.block_state('wiki:slot_4_occupied')",
                    "empty_slot_5": "!q.block_state('wiki:slot_5_occupied')",
                    "occupied_slot_0": "q.block_state('wiki:slot_0_occupied')",
                    "occupied_slot_1": "q.block_state('wiki:slot_1_occupied')",
                    "occupied_slot_2": "q.block_state('wiki:slot_2_occupied')",
                    "occupied_slot_3": "q.block_state('wiki:slot_3_occupied')",
                    "occupied_slot_4": "q.block_state('wiki:slot_4_occupied')",
                    "occupied_slot_5": "q.block_state('wiki:slot_5_occupied')"
                }
            },
            "minecraft:material_instances": {
                "*": {
                    "texture": "stripped_bamboo_block_top"
                },
                // 在模型中定义的材质实例：
                "side": {
                    "texture": "stripped_bamboo_block"
                },
                "empty_slot": {
                    "texture": "pigeonholes_empty"
                },
                "occupied_slot": {
                    "texture": "pigeonholes_occupied"
                }
            }
        },
        "permutations": [
            // 朝北
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'north'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 0, 0] }
                }
            },
            // 朝西
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'west'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 90, 0] }
                }
            },
            // 朝南
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'south'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 180, 0] }
                }
            },
            // 朝东
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'east'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, -90, 0] }
                }
            }
        ]
    }
}
```

</details>

<details>
<summary>精确交互脚本</summary>

<pre><code>BP/scripts/blocks/pigeonholes.js</code></pre>

```js
import { world, EquipmentSlot, GameMode, ItemStack } from "@minecraft/server";
import FaceSelectionPlains from "../utilities/face_selection_plains"; // 导入 FaceSelectionPlains 类

// 槽位边界
const slots = new FaceSelectionPlains(
    { origin: [0, 0], size: [6, 8] },
    { origin: [6, 0], size: [5, 8] },
    { origin: [11, 0], size: [5, 8] },
    { origin: [0, 8], size: [6, 8] },
    { origin: [6, 8], size: [5, 8] },
    { origin: [11, 8], size: [5, 8] }
);

const isFrontFace = (block, face) =>
    block.permutation.getState("minecraft:cardinal_direction") === face.toLowerCase();

const isSlotOccupied = (block, slot) => block.permutation.getState(`wiki:slot_${slot}_occupied`);

const occupySlot = (block, slot) =>
    block.setPermutation(block.permutation.withState(`wiki:slot_${slot}_occupied`, true));

const emptySlot = (block, slot) =>
    block.setPermutation(block.permutation.withState(`wiki:slot_${slot}_occupied`, false));

function handleInteract({ block, face, faceLocation, dimension, player }) {
    if (!player || !isFrontFace(block, face)) return;

    const equippable = player.getComponent("minecraft:equippable");
    if (!equippable) return;

    const relativeFaceLocation = {
        x: faceLocation.x - block.location.x,
        y: faceLocation.y - block.location.y,
        z: faceLocation.z - block.location.z,
    };

    const selectedSlot = slots.getSelected({ face, faceLocation: relativeFaceLocation });
    if (selectedSlot === undefined) return;

    const mainhand = equippable.getEquipmentSlot(EquipmentSlot.Mainhand);
    const isHoldingPaper = mainhand.hasItem() && mainhand.typeId === "minecraft:paper";

    if (isHoldingPaper && !isSlotOccupied(block, selectedSlot)) {
        if (player.getGameMode() !== GameMode.creative) {
            if (mainhand.amount > 1) mainhand.amount--;
            else mainhand.setItem(undefined);
        }

        occupySlot(block, selectedSlot);
        dimension.playSound("insert.chiseled_bookshelf", block.center());
    } else if (isSlotOccupied(block, selectedSlot)) {
        emptySlot(block, selectedSlot);

        const itemLocation = { ...faceLocation };
        itemLocation.y -= 0.5;
        dimension.spawnItem(new ItemStack("minecraft:paper"), itemLocation).clearVelocity();

        dimension.playSound("pickup.chiseled_bookshelf", block.center());
    }
}

// ------------------------------
//  销毁时释放纸张
// ------------------------------
function releasePaper({ block, destroyedBlockPermutation, dimension }) {
    const states = destroyedBlockPermutation.getAllStates();

    for (const state in states) {
        const value = states[state];
        const isPaper = value === true;

        if (!isPaper) continue;

        dimension.spawnItem(new ItemStack("minecraft:paper"), block.center());
    }
}

/** @type {import("@minecraft/server").BlockCustomComponent} */
const PigeonholesStorageBlockComponent = {
    onPlayerInteract: handleInteract,
    onPlayerDestroy: releasePaper,
};

world.beforeEvents.worldInitialize.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent(
        "wiki:pigeonholes_storage",
        PigeonholesStorageBlockComponent
    );
});
```

</details>

## 双花盆示例

使用我们的 [SelectionBoxes](#selectionboxes-类) 类，玩家可以分别与每个花盆进行交互。以下文件是实现新的双花盆区块的基础，其他资源（纹理等）包含在 [示例附加包](#下载示例附加包) 中。

**注意**：此示例中的花盆仅支持种植蒲公英和仙人掌，简单起见——您可以自行进一步扩展。

![双花盆展示](/assets/images/blocks/precise-interaction/double_flower_pot.png)

<Button link="https://github.com/Bedrock-OSS/wiki-addon/blob/main/ma-precise_interaction/rp/models/blocks/double_flower_pot.geo.json">
    下载双花盆模型
</Button>

<details>
<summary>区块 JSON</summary>

<pre><code>BP/blocks/double_flower_pot.json</code></pre>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:double_flower_pot",
            "menu_category": {
                "category": "items"
            },
            "states": {
                "wiki:pot_0_plant": ["none", "dandelion", "cactus"],
                "wiki:pot_1_plant": ["none", "dandelion", "cactus"]
            },
            "traits": {
                "minecraft:placement_direction": {
                    "enabled_states": ["minecraft:cardinal_direction"]
                }
            }
        },
        "components": {
            "minecraft:custom_components": ["wiki:double_flower_pot"],
            "minecraft:collision_box": {
                "origin": [-7, 0, -3],
                "size": [14, 6, 6]
            },
            // 必须覆盖精确交互脚本中的所有盒子
            "minecraft:selection_box": {
                "origin": [-7, 0, -3],
                "size": [14, 6, 6]
            },
            "minecraft:geometry": {
                "identifier": "geometry.double_flower_pot",
                // 条件性显示花盆中的植物
                "bone_visibility": {
                    "dandelion_0": "q.block_state('wiki:pot_0_plant') == 'dandelion'",
                    "dandelion_1": "q.block_state('wiki:pot_1_plant') == 'dandelion'",
                    "cactus_0": "q.block_state('wiki:pot_0_plant') == 'cactus'",
                    "cactus_1": "q.block_state('wiki:pot_1_plant') == 'cactus'"
                }
            },
            "minecraft:material_instances": {
                "*": {
                    "texture": "flower_pot",
                    "render_method": "alpha_test",
                    "ambient_occlusion": false
                },
                // 在模型中定义的材质实例：
                "dirt": {
                    "texture": "double_flower_pot_dirt",
                    "render_method": "alpha_test",
                    "ambient_occlusion": false
                },
                "handle": {
                    "texture": "double_flower_pot_handle",
                    "render_method": "alpha_test"
                },
                "dandelion": {
                    "texture": "yellow_flower",
                    "render_method": "alpha_test",
                    "face_dimming": false,
                    "ambient_occlusion": false
                },
                "cactus_side": {
                    "texture": "cactus_side",
                    "render_method": "alpha_test"
                },
                "cactus_top": {
                    "texture": "cactus_top",
                    "render_method": "alpha_test"
                }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'west' || q.block_state('minecraft:cardinal_direction') == 'east'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 90, 0] } // 模型前方朝东
                }
            }
        ]
    }
}
```

</details>

<details>
<summary>精确交互脚本</summary>

<pre><code>BP/scripts/blocks/double_flower_pot.js</code></pre>

```js
import { world, ItemStack } from "@minecraft/server";
import SelectionBoxes from "../utilities/selection_boxes"; // 导入 SelectionBoxes 类

// 支持沿两个水平轴的方向
const pots = {
    x: new SelectionBoxes(
        { origin: [-7, 0, -3], size: [6, 6, 6] },
        { origin: [1, 0, -3], size: [6, 6, 6] }
    ),
    z: new SelectionBoxes(
        { origin: [-3, 0, -7], size: [6, 6, 6] },
        { origin: [-3, 0, 1], size: [6, 6, 6] }
    ),
};

// 每种植物的状态值和关联的声音
const plants = {
    "minecraft:yellow_flower": {
        value: "dandelion",
        sound: "dig.grass",
    },
    "minecraft:cactus": {
        value: "cactus",
        sound: "dig.cloth",
    },
};

// 获取适当轴线的选定花盆
const getSelectedPot = (e) =>
    pots[e.block.permutation.getState("wiki:axis")].getSelected(e.faceLocation);

const isPotOccupied = (block, pot) =>
    block.permutation.getState(`wiki:pot_${pot}_plant`) !== "none";

const setPotPlant = (block, pot, plant) =>
    block.setPermutation(block.permutation.withState(`wiki:pot_${pot}_plant`, plant));

const playPlantSound = (dimension, location, sound) =>
    dimension.runCommand(`playsound ${sound} @a ${location.x} ${location.y} ${location.z} 0.5`);

// 如果未选择花盆（目标为中间区域）或已被填充，则取消物品使用
world.beforeEvents.itemUseOn.subscribe((e) => {
    if (e.block.typeId !== "wiki:double_flower_pot" || !plants[e.itemStack.typeId]) return;

    const selectedPot = getSelectedPot(e);

    if (selectedPot === undefined || isPotOccupied(e.block, selectedPot)) e.cancel = true;
});

// -------------------------------
//    在选定花盆中种植
// -------------------------------
world.afterEvents.itemUseOn.subscribe((e) => {
    if (
        e.block.typeId !== "wiki:double_flower_pot" ||
        !plants[e.itemStack.typeId] ||
        e.source.isSneaking
    )
        return;

    const selectedPot = getSelectedPot(e);
    const plant = plants[e.itemStack.typeId];

    setPotPlant(e.block, selectedPot, plant.value);
    playPlantSound(e.block.dimension, e.block.location, plant.sound);
});

// -------------------------------
//  销毁时释放植物
// -------------------------------
function releasePlants(e) {
    const states = (e.brokenBlockPermutation ?? e.explodedBlockPermutation).getAllStates();

    // 存储的植物状态值数组，如 ["cactus", "dandelion"]
    const storedPlants = Object.entries(states)
        .filter(([state, value]) => state.startsWith("wiki:pot") && value !== "none")
        .map(([state, value]) => value);

    if (storedPlants.length === 0) return;

    // 将掉落物中心定位在区块中心
    const lootLocation = {
        x: e.block.location.x + 0.5,
        y: e.block.location.y + 0.5,
        z: e.block.location.z + 0.5,
    };

    // 为每个花盆植物创建一个物品实体
    for (const plant of storedPlants) {
        const plantId = Object.keys(plants).find((key) => plants[key].value === plant);

        e.dimension.spawnItem(new ItemStack(plantId), lootLocation);
        playPlantSound(e.dimension, e.block.location, plants[plantId].sound);
    }
}

world.afterEvents.playerBreakBlock.subscribe((e) => {
    if (e.brokenBlockPermutation.type.id === "wiki:double_flower_pot") releasePlants(e);
});
world.afterEvents.blockExplode.subscribe((e) => {
    if (e.explodedBlockPermutation.type.id === "wiki:double_flower_pot") releasePlants(e);
});
```

</details>

## 导入脚本

别忘了将您的脚本导入到附加包的入口文件中！

<pre><code>BP/manifest.json</code></pre>

```json
{
    "modules": [
        {
            "type": "script",
            "language": "javascript",
            "entry": "index.js", // 您定义的入口文件
            "uuid": "...",
            "version": "1.0.0"
        }
    ],
    "dependencies": [
        {
            "module_name": "@minecraft/server",
            "version": "1.15.0"
        }
    ]
}
```

<pre><code>BP/scripts/index.js</code></pre>

```js
// 在此处导入您的精确交互脚本...
import "./blocks/pigeonholes";
import "./blocks/double_flower_pot";
```

## 下载示例附加包

根据本教程创建的模板附加包，将鸽槽和双花盆区块添加到 `物品` 标签中。

<Button link="https://github.com/Bedrock-OSS/wiki-addon/releases/download/download/precise_interaction.mcaddon">
    下载 MCADDON
</Button>

如果您在精确交互方面需要额外的帮助，欢迎在 [Bedrock Add-Ons Discord](/discord) 中提问！记得在提问时包含此页面的链接，因为此处提供的类并未内置到 Minecraft 中。