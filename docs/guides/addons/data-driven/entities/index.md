# 自定义实体系列教程

自定义实体通常需要行为包和资源包同时配合。行为包负责服务端定义，例如组件、AI意向、碰撞箱、生命值、战利品和是否可召唤；资源包负责客户端定义，例如模型、纹理、渲染控制器、动画、粒子、声音和刷怪蛋颜色。

## 文件关系

/// html | div.treeview
- `demo_BP`
    - `entities`
        - `robot.json`
- `demo_RP`
    - `entity`
        - `robot.entity.json`
    - `models`
        - `entity`
            - `robot.geo.json`
    - `textures`
        - `entity`
            - `robot.png`
    - `texts`
        - `en_US.lang`
///

这些文件通过同一个标识符`demo:robot`关联。文件名本身不是最关键的，但统一命名能让项目更容易维护。

## 推荐顺序

1. 先做最小实体，只让`/summon demo:robot`能生成。
2. 再添加客户端实体、模型和纹理，让它不再隐形。
3. 添加本地化和刷怪蛋。
4. 添加组件、事件和AI意向。
5. 最后再加入动画、粒子、声音、战利品和生成规则。
6. 需要为实体存储自定义状态时，参考[实体属性](entity-properties.md)，了解如何用原生属性系统替代哑组件。

## 调试原则

如果实体无法生成，先看行为包；如果能生成但看不见，先看资源包。实体问题很容易同时出现在两边，因此建议每一步都进游戏测试，不要一次写完所有文件再排错。

## 进阶专题

掌握基础之后，可以继续探索以下专题：

/// html | div.grid.cards
- :material-ghost: [**虚拟实体**](dummy-entities.md)：无视觉、无行为的标记实体，常用于区域检测
- :material-shield: [**无敌实体**](invulnerable-entities.md)：使实体完全免疫所有伤害
- :material-cube: [**固体实体**](solid-entities.md)：让实体具有碰撞阻挡效果
- :material-timer: [**实体计时器**](timers.md)：基于时间触发事件的多种方法
- :material-eye: [**注视实体检测**](look-at-entity.md)：检测实体是否正在注视你
- :material-sword-off: [**禁用队伍伤害**](disabling-team-damage.md)：防止同族实体互相伤害
- :material-run-fast: [**实体移动**](entity-movement.md)：完整的移动系统配置指南
- :material-sword: [**实体攻击**](entity-attack.md)：目标选择与多种攻击类型
- :material-bed: [**睡眠实体**](sleeping-entities.md)：让实体使用床睡觉
- :material-hand-back-right: [**实体持物**](holding-items.md)：让实体在手中显示物品
- :material-radar: [**检测其他实体**](detecting-other-entities.md)：感知并响应附近的实体
- :material-airplane: [**飞行实体的骑乘控制**](flying-entities.md)：可骑乘的飞行实体实现方案
- :material-ferry: [**船型实体**](boat-entities.md)：在液体中漂浮的可骑乘实体
- :material-cloud: [**区域效果云**](area-effect-clouds.md)：高性能的静态标记与状态效果云
- :material-chat: [**NPC对话进阶**](npc-dialogue.md)：完整的多场景对话系统
- :material-heart-plus: [**生成已驯服实体**](spawning-tamed-entities.md)：预先与玩家绑定的驯服实体
- :material-village: [**仿村庄机制**](village-mechanic.md)：模拟居住、工作、聚集等村民行为
- :material-arrow-projectile: [**弹射物**](projectiles.md)：`minecraft:projectile`组件完整参考
- :material-axis-arrow: [**坐标空间变换**](coordinate-space-conversion.md)：世界、实体与骨骼空间的坐标转换
///
