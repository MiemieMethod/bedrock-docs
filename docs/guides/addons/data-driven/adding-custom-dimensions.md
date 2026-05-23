# 自定义维度

知识库中关于自定义维度的内容主要来自官方自动参考架构，缺少完整教程、示例包和稳定生成器取值说明。因此，本页只整理能确认的文件形态和学习注意事项，不把它作为完整可发布流程。

## 能确认的维度文档结构

官方参考中记录了维度定义文档包含`format_version`和维度定义对象。维度定义需要描述和组件，描述中声明命名空间标识符，组件中可包含维度边界和生成设置。

/// warning | 参考资料仍不一致
知识库中的自动生成维度参考同时出现了`minecraft:dimension`和`minecraft:dimension_type`两种根对象记载，且后者的字段类型说明存在明显生成错误。因此，下面示例只能说明旧参考中可见的结构形态，不能视为已经验证可直接发布的完整文件。
///

```json title="demo_BP/dimensions/demo_dimension.json"
{
  "format_version": "1.20.0",
  "minecraft:dimension": {
    "description": {
      "identifier": "demo:sky_dimension"
    },
    "components": {
      "minecraft:dimension_bounds": {
        "min": 0,
        "max": 256
      },
      "minecraft:generation": {
        "generator_type": "需要按目标版本参考确认"
      }
    }
  }
}
```

参考文档说明：

- `description.identifier`使用`namespace:name`格式。
- `minecraft:dimension_bounds`定义维度垂直边界。
- `minecraft:generation.generator_type`指定世界生成器类型，但当前知识库没有足够内容说明可用取值和正式用法。

## 不建议现在直接依赖

如果你的目标是发布稳定附加包，建议先使用已有三大维度配合生物群系、地物、结构和函数实现玩法。等你能确认目标版本中自定义维度的创建、进入方式、生成器和兼容性后，再把它加入项目。

## 可先练习的替代方案

- 用世界模板提供预制区域。
- 用结构和地物生成特殊区域。
- 用迷雾、声音和资源包改变区域氛围。
- 用函数或命令检测玩家位置并模拟维度规则。

这样做虽然不是真正的新维度，但在知识库缺少完整内容时更可靠。
