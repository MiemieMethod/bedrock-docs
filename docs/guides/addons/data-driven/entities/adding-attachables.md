# 添加附着物

附着物用于渲染“被实体拿着或穿着的物品”。它本质上是一个资源包JSON，包含标识符、材质、纹理、几何体、动画和渲染控制器。自定义武器、工具、背饰和可穿戴物品经常需要它。

## 准备物品和模型

先确保行为包中已经有一个物品，例如`demo:wrench`。再准备一个几何体`geometry.wrench`和纹理`textures/items/wrench.png`。

资源包结构如下：

/// html | div.treeview
- `demo_RP`
    - `attachables`
        - `wrench.player.json`
    - `models`
        - `entity`
            - `wrench.geo.json`
    - `textures`
        - `items`
            - `wrench.png`
///

## 定义附着物

```json title="attachables/wrench.player.json"
{
  "format_version": "1.20.30",
  "minecraft:attachable": {
    "description": {
      "identifier": "demo:wrench",
      "item": {
        "demo:wrench": "query.is_owner_identifier_any('minecraft:player')"
      },
      "materials": {
        "default": "entity",
        "enchanted": "entity_alphatest_glint"
      },
      "textures": {
        "default": "textures/items/wrench",
        "enchanted": "textures/misc/enchanted_item_glint"
      },
      "geometry": {
        "default": "geometry.wrench"
      },
      "render_controllers": [
        "controller.render.item_default"
      ]
    }
  }
}
```

`identifier`必须匹配已有物品标识符。`item`中的Molang条件用于限制这个附着物应用到哪个持有者；示例只应用到玩家。

## 绑定到手上

在几何体的骨骼中使用`binding`可以把模型绑定到持有者的物品槽。官方示例使用：

```json
"binding": "q.item_slot_to_bone_name(context.item_slot)"
```

这比直接写`rightItem`更灵活，因为它能根据主手、副手等槽位映射到正确骨骼。Blockbench也提供编辑绑定的界面，适合不想手写几何体JSON的情况。

## 测试

进入世界后运行：

```mcfunction
/give @s demo:wrench
```

切换第一人称和第三人称观察模型位置。如果位置不对，优先在Blockbench中调整几何体轴心点、旋转和绑定，而不是在物品定义中乱改。