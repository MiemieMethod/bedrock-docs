# 渲染控制器

**渲染控制器（Render Controller）**是Minecraft基岩版资源包中控制实体和附着物视觉渲染方式的定义文件。渲染控制器将几何体、纹理和材质组装在一起，决定游戏实际渲染时使用哪些资源以及如何组合它们。

## 概述

渲染控制器是实体渲染管线中的关键环节。客户端实体定义中通过`render_controllers`字段引用一个或多个渲染控制器，每个渲染控制器指定了当前应使用的几何体、纹理、材质和渲染设置。渲染控制器中的大部分字段都支持Molang表达式，使得渲染行为能够根据实体的状态动态变化。

渲染控制器定义文件位于资源包的`render_controllers/`目录中。

## 基本结构

一个渲染控制器的定义通常包含以下核心字段：

- **`geometry`**：指定要使用的几何体，值为Molang表达式，通过`Geometry.`前缀引用客户端实体中定义的几何体短名称。
- **`textures`**：指定要使用的纹理数组，每个元素通过`Texture.`前缀引用纹理短名称。
- **`materials`**：指定要使用的材质映射，将骨骼或通配符映射到`Material.`前缀引用的材质短名称。

```json title="渲染控制器示例"
{
  "format_version": "1.10.0",
  "render_controllers": {
    "controller.render.example": {
      "geometry": "Geometry.default",
      "textures": ["Texture.default"],
      "materials": [{"*": "Material.default"}]
    }
  }
}
```

## 纹理数组

渲染控制器支持定义纹理数组，配合Molang表达式实现纹理的动态选择。数组在渲染控制器的`arrays`字段中定义：

```json
"arrays": {
  "textures": {
    "Array.skins": ["Texture.skin0", "Texture.skin1", "Texture.skin2"]
  }
}
```

然后在`textures`字段中使用Molang索引数组：

```json
"textures": ["Array.skins[query.variant]"]
```

类似地，也可以定义几何体数组和材质数组。

## 材质映射

`materials`字段是一个数组，每个元素为一个键值对。键为骨骼名称或通配符`*`，值为材质引用。引擎按数组顺序匹配骨骼名称，第一个匹配的条目生效。通配符`*`匹配所有未被前面条目匹配的骨骼。

```json
"materials": [
  {"hand*": "Material.alpha"},
  {"*": "Material.default"}
]
```

上述示例中，以`hand`开头的骨骼使用半透明材质，其余骨骼使用默认材质。

## 覆盖色与光照

渲染控制器还可以控制以下渲染属性：

- **`overlay_color`**：设置实体的覆盖色，使用Molang表达式控制RGBA四个通道。常用于实体受伤时的红色闪烁效果。
- **`on_fire_color`**：设置实体着火时的颜色。
- **`is_hurt_color`**：设置实体受伤时的颜色。
- **`light_color_multiplier`**：光照颜色乘数，影响实体对环境光照的反应。
- **`ignore_lighting`**：是否忽略环境光照，为`true`时实体始终以最大亮度渲染。

## 部件可见性

通过`part_visibility`字段可以控制模型中每个骨骼的可见性。该字段为一组骨骼名称到布尔Molang表达式的映射，当表达式求值为`false`时对应骨骼不会被渲染。

```json
"part_visibility": [
  {"hat_layer": "!query.is_invisible"},
  {"cape": "query.has_cape"}
]
```
