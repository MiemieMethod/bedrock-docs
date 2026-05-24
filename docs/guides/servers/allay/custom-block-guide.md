---
comments: true
---

# 自定义方块

自定义方块是Allay里风险较高但也最强的一组高级接口。它允许你为方块生成客户端定义，控制几何体、材质、变换和按状态切换的渲染结果。

## 先确认前提

这套接口需要访问Allay的服务端模块，所以构建配置里必须关闭`apiOnly`：

```kotlin title="build.gradle.kts"
allay {
    apiOnly = false
}
```

/// warning | 内部API风险
`apiOnly = false`意味着你的插件开始接触Allay服务端实现层，而不是只依赖稳定API层。这类接口在版本升级时更容易发生破坏性变更。
///

## 最简单的写法：只给一个纹理

如果你只想先做一个简单的自定义方块，直接从`ofTexture()`开始：

```java linenums="1"
import org.allaymc.server.block.type.AllayBlockType;
import org.allaymc.server.block.type.CustomBlockDefinitionGenerator;

AllayBlockType.builder(MyBlockImpl.class)
    .identifier("myplugin:ruby_block")
    .blockDefinitionGenerator(
        CustomBlockDefinitionGenerator.ofTexture("ruby_block"))
    .build();
```

这适合“外观简单，只要一个贴图”的方块。

## 给方块指定固定几何体和材质

如果你已经有资源包里的模型，可以使用`ofConstant()`：

```java linenums="1"
import org.allaymc.server.block.type.BlockStateDefinition;
import org.allaymc.server.block.type.BlockStateDefinition.Geometry;
import org.allaymc.server.block.type.BlockStateDefinition.Materials;
import org.allaymc.server.block.type.CustomBlockDefinitionGenerator;

AllayBlockType.builder(MyLampImpl.class)
    .identifier("myplugin:custom_lamp")
    .blockDefinitionGenerator(
        CustomBlockDefinitionGenerator.ofConstant(
            BlockStateDefinition.builder()
                .geometry(Geometry.of("geometry.custom_lamp"))
                .materials(Materials.builder().any("lamp_texture"))
                .displayName("自定义灯")
                .build()))
    .build();
```

这里最核心的对象是`BlockStateDefinition`。它描述的是“某个方块状态在客户端应该怎样渲染”。

## 按方块状态切换外观

如果一个方块会随状态变化切换模型或贴图，就用`of(state -> ...)`：

```java linenums="1"
import org.allaymc.api.block.property.type.BlockPropertyTypes;
import org.allaymc.server.block.type.BlockStateDefinition;
import org.allaymc.server.block.type.BlockStateDefinition.Geometry;
import org.allaymc.server.block.type.BlockStateDefinition.Materials;
import org.allaymc.server.block.type.CustomBlockDefinitionGenerator;

AllayBlockType.builder(MyDoorImpl.class)
    .identifier("myplugin:custom_door")
    .setProperties(BlockPropertyTypes.OPEN_BIT)
    .blockDefinitionGenerator(
        CustomBlockDefinitionGenerator.of(state -> {
            boolean open = state.getPropertyValue(BlockPropertyTypes.OPEN_BIT);
            return BlockStateDefinition.builder()
                .geometry(Geometry.of(open ? "geometry.door_open" : "geometry.door_closed"))
                .materials(Materials.builder().any("door_texture"))
                .build();
        }))
    .build();
```

这类写法很适合门、机器、作物、指示灯等“状态决定表现”的方块。

## 材质怎么配

`Materials.builder()`可以按面分配贴图：

```java linenums="1"
import org.allaymc.api.block.data.BlockFace;
import org.allaymc.server.block.type.BlockStateDefinition.Materials;

Materials.builder()
    .any("log_side")
    .face(BlockFace.UP, "log_top")
    .face(BlockFace.DOWN, "log_top");
```

如果你需要透明、双面或更复杂的渲染方式，就改用`MaterialInstance`：

```java linenums="1"
import org.allaymc.server.block.type.BlockStateDefinition.MaterialInstance;
import org.allaymc.server.block.type.BlockStateDefinition.Materials;

Materials.builder().any(MaterialInstance.alphaTest("leaves_texture"));
```

常见工厂方法包括：

- `opaque(...)`
- `alphaTest(...)`
- `alphaTestSingleSided(...)`
- `blend(...)`
- `doubleSided(...)`

## 变换和旋转

如果模型需要旋转、缩放或平移，可以设置`Transformation`：

```java linenums="1"
import org.allaymc.server.block.type.BlockStateDefinition.Transformation;

Transformation.builder()
    .ry(90)
    .sx(1.0f).sy(1.0f).sz(1.0f)
    .tx(0.0f).ty(0.0f).tz(0.0f)
    .build();
```

/// warning | 旋转值限制
资料中给出的旋转值是`0`、`90`、`180`和`270`。超出这个集合时，客户端渲染结果并没有可靠保证。
///

## 几何体还能做什么

除了最简单的`Geometry.of("geometry.xxx")`外，高级写法还支持：

- 控制骨骼可见性。
- 设置剔除规则与剔除图层。
- 对全部或指定骨骼启用UV锁定。

这些能力更适合已经有成熟资源包模型、并且确实需要按状态隐藏某些骨骼的插件。

## 记住：渲染定义不等于物理行为

`BlockStateDefinition`主要描述客户端渲染。碰撞箱、选择框、发光、摩擦等物理性质并不是在这里写死的，而是来自方块本身的数据与组件。

## 实战建议

- 第一次做自定义方块时，先用`ofTexture()`跑通整条链路。
- 只有真的需要按状态切模型时，再升级到`of(state -> ...)`。
- 几何体标识符和贴图名必须和资源包里的实际文件保持一致。
- 如果你还没熟悉基础方块接口，先回头看[方块API](block-guide.md)。
