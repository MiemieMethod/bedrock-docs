# 第一个实体

这一页会创建一个最小机器人实体。它没有复杂AI，只用于确认实体服务端定义、客户端定义、模型、纹理和本地化能正确连起来。

## 行为包实体

创建文件：

```json title="demo_BP/entities/robot.json"
{
  "format_version": "1.20.80",
  "minecraft:entity": {
    "description": {
      "identifier": "demo:robot",
      "is_spawnable": true,
      "is_summonable": true
    },
    "components": {
      "minecraft:physics": {},
      "minecraft:nameable": {},
      "minecraft:collision_box": {
        "width": 0.9,
        "height": 1.8
      },
      "minecraft:health": {
        "value": 20,
        "max": 20
      }
    }
  }
}
```

`is_spawnable`会让实体有刷怪蛋，`is_summonable`会让`/summon`可用。`minecraft:physics`提供重力和常规碰撞。

## 资源包客户端实体

创建文件：

```json title="demo_RP/entity/robot.entity.json"
{
  "format_version": "1.10.0",
  "minecraft:client_entity": {
    "description": {
      "identifier": "demo:robot",
      "materials": {
        "default": "entity"
      },
      "textures": {
        "default": "textures/entity/robot"
      },
      "geometry": {
        "default": "geometry.robot"
      },
      "render_controllers": [
        "controller.render.default"
      ],
      "spawn_egg": {
        "base_color": "#505152",
        "overlay_color": "#3b9dff"
      }
    }
  }
}
```

接着把`robot.geo.json`放入`demo_RP/models/entity`，把`robot.png`放入`demo_RP/textures/entity`。模型内部的几何体标识符必须是`geometry.robot`。

## 添加名称

```text title="demo_RP/texts/en_US.lang"
entity.demo:robot.name=Robot
item.spawn_egg.entity.demo:robot.name=Spawn Robot
```

## 测试

进入启用两个包的世界，运行：

```mcfunction
/summon demo:robot ~ ~ ~
```

如果实体生成但不可见，检查资源包是否激活、客户端实体标识符是否一致、模型几何体标识符是否一致、纹理路径是否没有写`.png`。如果命令提示实体不存在，先检查行为包实体文件。
