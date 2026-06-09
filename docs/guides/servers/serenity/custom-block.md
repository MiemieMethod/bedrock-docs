# 创建自定义方块

SerenityJS提供了强大的工具来创建自定义方块，可以在服务器实例中使用。本指南将指导你完成创建自定义方块的全过程，包括定义其属性、行为和在服务器中的使用方式。

## 自定义方块基础

要创建自定义方块，首先需要定义其基本属性。这通过创建`CustomBlockType`类的新实例来完成，该类由`@serenityjs/core`包提供。下面是创建简单自定义方块的示例。

```typescript
import { CustomBlockType } from '@serenityjs/core';

// 定义一个自定义方块类型
// 第一个参数是方块ID，第二个参数是包含附加选项的对象
const exampleBlockType = new CustomBlockType("serenity:example_block", { solid: true });
```

一旦自定义方块类型被创建，你可以通过访问`components`属性来定义其组件。每个组件都可以有自己的一组属性，这些属性可以在创建方块类型之前或之后定义。这些组件与原版Minecraft附加包系统中使用的组件相同，这使其易于使用和理解。原版Minecraft的自定义方块可以轻松转换为Serenity中的自定义方块。

在下一个示例中，我们将为基础方块类型分配一个组件。这意味着所有置换都将继承此组件，除非被覆盖。

```typescript
import { MaterialRenderMethod } from '@serenityjs/protocol';

// 基础类型将发出光级为15的光线
exampleBlockType.components.setLightEmission(15);

// 获取基础几何体组件并设置模型标识符
const geometry = exampleBlockType.components.getGeometry();
geometry.setModelIdentifier("geometry.example_block");

// 获取基础材质实例组件并创建一个默认材质实例
const materials = exampleBlockType.components.getMaterialInstances();
materials.createMaterialInstance("*", {
  texture: "example_block",
  render_method: MaterialRenderMethod.AlphaTest
});
```

## 方块置换

方块置换是一种定义方块不同变种的方式，这些变种被称为状态。每个置换都可以有自己的一组组件属性。要创建置换，可以在`CustomBlockType`实例上使用`createPermutation`方法。置换的状态可以是字符串、数字或布尔值。

```typescript
const permutation = exampleBlockType.createPermutation({
  boolean_state: true,
  number_state: 42,
  string_state: "example",
});
```

置换可以覆盖方块类型的基础组件。在下一个示例中，我们将创建方块类型的2个置换。第一个置换的光发射级别将为零，第二个置换的光发射级别将为15。这将创建两个不同的方块变种，其中一个发光，另一个不发光。

```typescript
// 创建一个具有不同光发射级别的置换
const permutation1 = exampleBlockType.createPermutation({ powered: false });
permutation1.components.setLightEmission(0); // 级别0将不发出光线

// 创建另一个具有不同光发射级别的置换
const permutation2 = exampleBlockType.createPermutation({ powered: true });
permutation2.components.setLightEmission(15); // 级别15将发出光线
```

## 方块特质

方块特质是一种为方块定义额外属性的方式。这些特质可用于定义方块在游戏中的行为。例如，你可以定义一个特质，使方块在与之交互时发出光线。要创建特质，需要创建一个扩展`BlockTrait`类的新类。下面是创建简单方块特质的示例，该特质使方块在与之交互时发出光线。

首先，我们需要扩展上面的代码，我们需要使基础方块类型可交互。这通过在方块类型的`components`属性内调用`setIsInteractable`方法来完成。这将允许我们在游戏中正确与方块交互。

```typescript
// 这将使方块类型可交互
exampleBlockType.components.setIsInteractable(true);
```

接下来，我们可以创建一个扩展`BlockTrait`类的新类。此类将定义方块在与之交互时的行为。在本例中，我们将创建一个特质，使方块在与之交互时切换其发光状态。特质增加了代码的可重用性，因为它们可以用于多个方块。这类似于如何在方块类型中使用组件。

```typescript
import { BlockTrait } from '@serenityjs/core';

class ExampleBlockTrait extends BlockTrait {
  // 每个特质都必须有一个唯一的标识符
  public static readonly identifier = "serenity:example_block_trait";

  public onInteract(): void {
    // 获取我们在置换中定义的方块的"powered"状态
    const state = this.block.getState("powered");

    // 切换方块的"powered"状态
    this.block.setState("powered", !state);
  }
}
```

一旦特质被定义，你可以将其注册到方块类型。这意味着当方块初始时，它将应用该特质。你可以通过在方块类型实例上调用`registerTrait`方法来注册特质。

```typescript
// 方块类型现在将应用该特质
exampleBlockType.registerTrait(ExampleBlockTrait);
```

## 总结

在本指南中，我们介绍了在Serenity中创建自定义方块的基础知识。我们定义了一个自定义方块类型、创建了置换，并添加了特质来定义方块的行为。完成这些步骤后，你还需要将方块类型注册到世界实例。这通过在世界实例的`blockPalette`属性上调用`registerType`方法来完成。

```typescript
world.blockPalette.registerType(exampleBlockType);

// 可选地，你也可以注册方块特质
world.blockPalette.registerTrait(ExampleBlockTrait);
```

如果你对完整的代码片段感兴趣，可以在[这里](https://github.com/SerenityJS/serenity/tree/main/docs/custom-block/code.ts)找到！