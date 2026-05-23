# 制作模型

模型决定实体、方块或附着物在三维空间中的形状。基岩版模型通常由几何体JSON和纹理图片共同组成；几何体描述骨骼、立方体、轴心点和UV，纹理提供表面颜色。

## 使用Blockbench新建模型

打开Blockbench，选择适合目标内容的项目类型。实体和附着物通常使用Bedrock Model；方块如果要使用自定义几何体，也可以导出Bedrock几何体。

新建项目时先确定几何体标识符。例如本系列使用：

```text
geometry.demo_robot
```

官方教程建议骨骼和动画标识符使用小写字母、数字、下划线和点。不要在动画标识符中使用冒号或短横线。

## 组织骨骼

建议给模型创建一个根骨骼，再把头、身体、手臂、轮子等部件放在根骨骼下面。骨骼本身不可见，但它能包含立方体并参与动画。

制作可动画部件时，要提前把轴心点放在真正旋转的位置。例如门板的轴心点应在铰链侧，轮子的轴心点应在轮心。

## 绘制纹理

最简单的做法是让Blockbench生成纹理模板，再在Paint页或外部像素画软件中绘制。普通方块常用16×16像素纹理；实体和复杂模型可以使用更大尺寸，但不要无意义地提高分辨率。

保存后把文件放入资源包：

/// html | div.treeview
- `demo_RP`
    - `models`
        - `entity`
            - `demo_robot.geo.json`
    - `textures`
        - `entity`
            - `demo_robot.png`
///

## 在客户端实体中引用

模型不会自动显示。你需要在客户端实体文件中把材质、纹理、几何体和渲染控制器连起来：

```json title="entity/demo_robot.entity.json"
{
  "format_version": "1.10.0",
  "minecraft:client_entity": {
    "description": {
      "identifier": "demo:robot",
      "materials": {
        "default": "entity"
      },
      "textures": {
        "default": "textures/entity/demo_robot"
      },
      "geometry": {
        "default": "geometry.demo_robot"
      },
      "render_controllers": [
        "controller.render.default"
      ]
    }
  }
}
```

纹理路径不写`.png`扩展名。几何体引用写的是模型文件内部的`description.identifier`，不是文件名。

## 导出前检查

- 几何体标识符是否和引用一致。
- 纹理是否保存在资源包内正确路径。
- 透明纹理是否使用了合适材质，例如`entity_alphatest`或`entity_alphablend`。
- 骨骼名是否和动画中使用的骨骼名一致。
- 模型保存后是否重新进入世界测试。

完成模型后，就可以进入动画和动画控制器部分，让模型动起来。
