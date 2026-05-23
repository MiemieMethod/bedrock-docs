# 渲染控制器

本页列出国际版资源包`render_controllers/`目录中渲染控制器定义文件的主要结构。渲染控制器用于为客户端实体和附着物选择几何体、材质、纹理和部分渲染属性。本页不包含中国版网易ModSDK接口。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 渲染控制器文件使用的格式版本。官方示例使用`1.8.0`。 |
| `render_controllers` | 对象 | 未设置 | 渲染控制器定义字典。键为控制器标识符，值为控制器对象。 |

## 控制器对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `arrays` | 对象 | 未设置 | 定义可由Molang表达式索引的资源数组。可包含纹理、几何体和材质数组。 |
| `geometry` | Molang表达式 | 未设置 | 选择客户端实体定义中`Geometry.`前缀的几何体短名称。 |
| `materials` | 数组 | 未设置 | 将骨骼名称或通配符映射到`Material.`前缀的材质短名称。 |
| `textures` | 数组 | 未设置 | 选择一个或多个`Texture.`前缀的纹理短名称，或选择纹理数组中的元素。 |
| `part_visibility` | 数组 | 未设置 | 按骨骼名称控制模型部件可见性。 |
| `overlay_color` | Molang表达式或数组 | 未设置 | 控制覆盖色，通常用于实体受伤、着火等效果。 |
| `light_color_multiplier` | Molang表达式或数组 | 未设置 | 控制光照颜色乘数。 |
| `ignore_lighting` | 布尔值或Molang表达式 | 未设置 | 控制实体渲染是否忽略环境光照。 |

## 资源数组

`arrays`可为同一资源类型声明多个候选值，并在`geometry`、`materials`或`textures`中使用Molang索引选择。数组元素应引用客户端实体定义中已经声明的短名称。

```json title="纹理数组示例"
{
  "arrays": {
    "textures": {
      "Array.skins": [
        "Texture.wild",
        "Texture.black",
        "Texture.red",
        "Texture.siamese"
      ]
    }
  },
  "textures": [
    "Array.skins[query.variant]"
  ]
}
```

## 材质映射

`materials`数组中的每个元素为一个键值对。键可以是骨骼名称、带通配符的骨骼匹配模式或`*`，值为材质短名称。引擎按数组顺序匹配，通常将更具体的骨骼规则放在通配符之前。

```json
"materials": [
  { "hand*": "Material.alpha" },
  { "*": "Material.default" }
]
```

## 示例

```json title="豹猫渲染控制器示例"
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.ocelot": {
      "arrays": {
        "textures": {
          "Array.skins": [
            "Texture.wild",
            "Texture.black",
            "Texture.red",
            "Texture.siamese"
          ]
        }
      },
      "geometry": "Geometry.default",
      "materials": [
        { "*": "Material.default" }
      ],
      "textures": [
        "Array.skins[query.variant]"
      ]
    }
  }
}
```

## 挂接位置

渲染控制器标识符通常在客户端实体定义的`description.render_controllers`数组中引用。控制器内部使用的`Geometry.`、`Texture.`和`Material.`短名称来自同一客户端实体定义的`geometry`、`textures`和`materials`映射。

## 相关参考

- [客户端实体定义](client-entity.md)

