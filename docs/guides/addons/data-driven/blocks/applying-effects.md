# 方块效果

通过自定义组件，可以让方块在实体踩踏、站立或定时触发时对实体施加状态效果、造成伤害，或执行其他逻辑。

## 踩踏时施加状态效果

使用 `onStepOn` 事件钩子，当实体走上方块时触发：

```json title="BP/blocks/regeneration_pad.json > components"
"wiki:step_effect": {
    "effect": "regeneration",
    "duration": 60,
    "amplifier": 1
}
```

```js title="BP/scripts/step_effect.js"
import { system } from "@minecraft/server";

const StepEffectComponent = {
    onStepOn({ entity }, { params }) {
        if (!entity) return;
        entity.addEffect(params.effect, params.duration * 20, {
            amplifier: params.amplifier,
            showParticles: true
        });
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:step_effect", StepEffectComponent);
});
```

`duration` 参数是效果持续秒数，脚本中需要乘以20转换为刻数。

## 踩踏时造成伤害

使用 `onStepOn` 配合 `EntityDamageCause`：

```js
import { system, EntityDamageCause } from "@minecraft/server";

const DamagePadComponent = {
    onStepOn({ entity }, { params }) {
        entity?.applyDamage(params.damage, {
            cause: EntityDamageCause.magic
        });
    }
};
```

## 范围效果：定时检测附近实体

对于想要持续影响范围内实体的方块（类似信标），结合 `minecraft:tick` 组件和 `onTick` 钩子，使用 `dimension.getEntities()` 检测附近实体：

```json title="BP/blocks/aura_block.json > components"
"minecraft:tick": {
    "interval_range": [40, 40],
    "looping": true
},
"wiki:aura_effect": {
    "effect": "strength",
    "radius": 5
}
```

```js title="BP/scripts/aura_effect.js"
import { system } from "@minecraft/server";

const AuraEffectComponent = {
    onTick({ block }, { params }) {
        const entities = block.dimension.getEntities({
            location: block.center(),
            maxDistance: params.radius
        });
        for (const entity of entities) {
            entity.addEffect(params.effect, 60, { amplifier: 0, showParticles: false });
        }
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:aura_effect", AuraEffectComponent);
});
```

`getEntities` 的 `maxDistance` 是以方块中心为球心的半径范围（单位：方块）。

## 跌落伤害：跌落到方块时触发

`minecraft:entity_fall_on` 组件配合 `onEntityFallOn` 钩子，在实体跌落到方块上时触发：

```json title="BP/blocks/spike_block.json > components"
"minecraft:entity_fall_on": {
    "min_fall_distance": 0.5
},
"wiki:fall_damage": {
    "damage_multiplier": 2.0
}
```

```js
const FallDamageComponent = {
    onEntityFallOn({ entity, fallDistance }, { params }) {
        if (!entity) return;
        const damage = Math.floor(fallDistance * params.damage_multiplier);
        if (damage > 0) {
            entity.applyDamage(damage);
        }
    }
};
```

`fallDistance` 是实体在触发事件前的跌落距离（单位：方块）。

## 常用状态效果名称

| 中文名 | 效果ID |
|-------|--------|
| 生命恢复 | `regeneration` |
| 速度 | `speed` |
| 力量 | `strength` |
| 缓慢 | `slowness` |
| 虚弱 | `weakness` |
| 毒素 | `poison` |
| 夜视 | `night_vision` |
| 隐身 | `invisibility` |
| 瞬间伤害 | `instant_damage` |
| 瞬间治疗 | `instant_health` |
| 凋零 | `wither` |
| 饥饿 | `hunger` |
| 阻燃 | `fire_resistance` |
| 漂浮 | `levitation` |
