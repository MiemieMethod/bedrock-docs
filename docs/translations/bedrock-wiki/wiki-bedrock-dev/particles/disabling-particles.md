---
标题：禁用粒子
描述：移除游戏中显示的原版粒子。
类别：教程
显示大纲：false
标签：
    - 初学者
提及：
    - SirLich
    - Joelant05
    - MedicalJewel105
---

如果您想禁用某个粒子，建议直接在粒子文件中进行操作，而不是仅仅在`particles.png`中将粒子纹理设置为透明。此外，禁用粒子可能会比将其设置为透明提供略微的性能提升，因为透明粒子仍然会被发射（但不可见）。

禁用粒子发射的基本思路如下：

<代码头>RP/particles/some_vanilla_particle.json</代码头>

```json
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