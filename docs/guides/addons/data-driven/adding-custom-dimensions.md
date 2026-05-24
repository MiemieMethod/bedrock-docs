# 自定义维度

这篇教程只做“能落地验证的最小练习”。目前的国际版维度JSON资料主要来自自动导出参考，存在根对象命名不一致和字段说明缺失的问题，所以这里不把它当作稳定生产方案。

/// warning | 不要混用中国版字段
国际版维度文件位于行为包`dimensions/`目录，使用`minecraft:`命名空间字段。中国版`netease:dimension_info`、`netease:biome_source`和模组SDK接口属于另一套体系，不能写进国际版维度文件。
///

## 第一步：准备目录

先在行为包创建`dimensions/`目录：

/// html | div.treeview
- `demo_BP`
    - `dimensions`
        - `demo_dimension.json`
///

## 第二步：写一个最小文件

先用`minecraft:dimension`形态做最小验证：

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

当前能确认的核心字段只有三组：

- `description.identifier`使用`namespace:name`格式。
- `minecraft:dimension_bounds`定义维度垂直边界。
- `minecraft:generation.generator_type`指定生成器类型。

/// note | 生成器取值仍缺资料
缺少`generator_type`的官方完整取值清单。本教程无法给出“所有版本都可用”的枚举表，实际项目请在目标版本中逐项验证。
///

## 第三步：了解另一种根对象记载

同一批自动导出资料还记录了`minecraft:dimension_type`形态，结构与上面的`minecraft:dimension`非常接近：

```json title="demo_BP/dimensions/demo_dimension_alt.json"
{
  "format_version": "1.20.0",
  "minecraft:dimension_type": {
    "description": {
      "identifier": "demo:sky_dimension_alt"
    },
    "components": {
      "minecraft:dimension_bounds": {
        "min": 0,
        "max": 256
      },
      "minecraft:generation": {
        "generator_type": "待目标版本验证"
      }
    }
  }
}
```

这表示当前资料存在命名差异。维护时应优先相信“目标版本是否实际可加载”，而不是只看自动导出的字段名。

## 第四步：把验证做完整

建议按下面顺序检查：

1. 开启内容日志并导入包，确认维度文件被解析。
2. 新建测试世界，确认不会出现维度定义报错。
3. 如果目标玩法依赖真实新维度传送与运行时逻辑，再评估是否改用脚本API方案。

国际版维度能力边界与字段汇总可分别参见[维度](../../../docs/addon/dimension.md)和[维度定义](../../../refs/addon/dimension.md)。