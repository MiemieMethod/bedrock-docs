# 禁用原版粒子

有时，资源包需要移除或替换原版粒子特效——例如在建立极简画风的材质包时去掉爆炸或魔法粒子，或者在优化性能时彻底停止某些高频粒子的发射。

## 推荐做法

**正确做法是覆盖粒子定义文件，而不是将粒子纹理改为透明。**

将粒子纹理改透明看似有效，但发射器依然正常工作——每次触发时仍然创建粒子实例、执行运动计算，只是最终不可见。这既不能带来性能收益，也不彻底。

通过覆盖粒子定义，可以让发射器在激活条件上直接返回0，从根本上阻止粒子发射。

## 操作步骤

1. 在资源包的`particles`文件夹中创建与目标粒子**同名**的JSON文件。
2. 在文件中写入如下结构，将`identifier`替换为目标粒子的完整赋命名空间标识符。

```json title="RP/particles/minecraft__some_vanilla_particle.json"
{
    "format_version": "1.10.0",
    "particle_effect": {
        "description": {
            "identifier": "minecraft:some_vanilla_particle",
            "basic_render_parameters": {
                "material": "particles_alpha",
                "texture": "textures/particle/particles"
            }
        },
        "components": {
            "minecraft:emitter_lifetime_expression": {
                "activation_expression": 0,
                "expiration_expression": 1
            },
            "minecraft:emitter_rate_manual": {
                "max_particles": 0
            }
        }
    }
}
```

/// tip | 说明
- `activation_expression: 0`：发射器激活条件永远为假，发射器不会进入激活状态。
- `expiration_expression: 1`：发射器立即过期。
- `max_particles: 0`：即使激活，也不发射任何粒子。

两个组件同时使用是双重保险，任意一个即可阻止粒子发射。
///

## 文件命名

粒子定义覆盖依靠`identifier`字段而非文件名。文件名和目录结构可以自由选择，但建议与原版粒子标识符保持对应关系，方便维护。例如，禁用`minecraft:huge_explosion_emitter`时，可以将文件命名为`minecraft__huge_explosion_emitter.json`（用双下划线替代命名空间分隔符，因为文件名不能包含冒号）。

/// warning | 命名空间冲突
覆盖文件的`identifier`必须与原版粒子完全一致（含`minecraft:`命名空间），否则覆盖无效，原版粒子将照常播放。
///

## 常见使用场景

- **极简画风材质包**：禁用爆炸、魔法、水花等视觉噪声粒子。
- **性能优化**：停用在大规模战斗中产生大量粒子实例的效果（如暴击、爆炸粒子）。
- **视觉替换**：先禁用原版粒子，再用自定义粒子定义实现替换效果（此时`identifier`相同，整个文件即为替换后的新粒子）。

## 延伸阅读

- [自定义粒子](adding-custom-particles.md)
- [原版粒子列表](../../../refs/tables/particles/vanilla_particles.md)