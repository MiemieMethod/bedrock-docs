# 区域效果云

区域效果云（即`minecraft:area_effect_cloud`实体）是基岩版中一类特殊实体，原版通过投掷滞留型药水产生，但通过结构文件和NBT编辑，可以将其用于地图制作中许多精妙的场景。

## 特点与用途

区域效果云具有以下独特特性：

- **高性能**：类似虚拟实体，与世界和其他实体没有碰撞，适合在玩家或实体附近大量放置
- **完全静止**：只能通过命令移动，适合需要精确定位的场合
- **可施加状态效果**：持续时间可精确到刻，可控制环境音效、屏幕提示、粒子等
- **继承特性**：运行时标识符设为`minecraft:area_effect_cloud`的实体会继承上述所有特性

## 放置区域效果云

区域效果云必须通过结构文件中的特定NBT数据来正确创建。

### NBT编辑工具

推荐使用以下工具编辑结构文件：

- [NBT Studio](https://github.com/tryashtar/nbt-studio)（独立程序）
- [NBT Viewer](https://marketplace.visualstudio.com/items?itemName=Misodee.vscode-nbt)（VS Code扩展）

### NBT格式

以下是区域效果云实体根标签中的关键标签：

| 标签 | 类型 | 说明 |
|---|---|---|
| `Duration` | Integer | 存在时间（刻），值为0时立即消失 |
| `DurationOnUse` | Integer | 每次施加效果后存在时间的变化量 |
| `InitialRadius` | Float | 创建时的半径；小于0.5时立即消失 |
| `RadiusChangeOnPickup` | Float | 被玻璃瓶收集时半径的变化量（原版末影龙的呼吸云使用此功能） |
| `RadiusOnUse` | Float | 每次施加效果后半径的变化量 |
| `RadiusPerTick` | Float | 每刻半径的变化量 |
| `ParticleColor` | Integer | 粒子颜色（十进制整数） |
| `ReapplicationDelay` | Integer | 效果施加的间隔（刻） |
| `mobEffects` | List | 施加的状态效果列表 |

`mobEffects`标签下每个效果条目的参数：

| 标签 | 类型 | 说明 |
|---|---|---|
| `Id` | Byte | 状态效果ID |
| `Amplifier` | Byte | 效果等级（0为一级） |
| `Duration` | Integer | 效果持续时间（刻） |
| `DurationEasy` | Integer | 简单难度下的持续时间（刻） |
| `DurationNormal` | Integer | 普通难度下的持续时间（刻） |
| `DurationHard` | Integer | 困难难度下的持续时间（刻） |
| `Ambient` | Byte | 粒子是否半透明 |
| `ShowParticles` | Byte | 是否显示粒子 |
| `DisplayOnScreenTextureAnimation` | Byte | 是否显示获得效果时的屏幕动画（如不祥之兆、图腾等） |

### 预制结构文件

可以手动制作一个包含区域效果云的结构文件作为模板：最小半径为0.5格，存在时间为最大值（2^31 - 1刻，约29826小时），将此结构文件放置在`BP/structures/wiki/area_effect_cloud.mcstructure`，之后通过`/structure load`或脚本API放置即可。

## 使用区域效果云

放置后，区域效果云可以像其他标记实体一样使用。

**注意事项**：

- 云会发出`minecraft:mobspell_lingering`粒子效果。若不希望显示粒子，需通过资源包修改该粒子发射器
- 区域效果云不向客户端更新位置信息，因此它在视觉上固定在最初生成的位置，但实际上可以用`/tp`移动

### 脚本API使用示例

通过脚本API动态放置并操作区域效果云：

```js title="BP/scripts/marker.js"
import { world } from "@minecraft/server";

function spawnMarker(location) {
    const structureLocation = {
        x: Math.floor(location.x),
        y: Math.floor(location.y),
        z: Math.floor(location.z),
    };

    // 放置存储在BP/structures/wiki/area_effect_cloud.mcstructure的结构
    world.structureManager.place("wiki:area_effect_cloud", location.dimension, structureLocation);
}
```

/// tip | 监听实体加载
由于结构放置是异步的，如需在区域效果云生成后立即对其操作，可以监听`world.afterEvents.entityLoad`事件，在回调中通过标签或类型筛选到刚生成的实体进行处理。
///