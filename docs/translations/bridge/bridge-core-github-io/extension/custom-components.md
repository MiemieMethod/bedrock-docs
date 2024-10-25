# 自定义组件

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/custom-components/](https://bridge-core.github.io/extension-docs/custom-components/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/custom-components.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/custom-components.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@613e4f17d0beb90ee05a08784717545189da51fd -->
///

## 概述

bridge.允许你定义新的实体、区块和物品组件，以便更快速地编写冗长、复杂和重复的行为。要开始使用，请导航到预设窗口中的“自定义组件”选项卡，并填写选项，包括你希望使用TypeScript还是JavaScript编写组件、文件名，以及你希望创建的是物品、实体还是区块组件。如果你在bridge.之外或在扩展中创建组件，则需要在`BP/components/<组件类型>`或`<扩展名称>/components/<组件类型>`文件夹中创建js或ts文件。

## 执行范围

### `defineComponent`

自定义组件可以访问`defineComponent`函数，其格式如下：

`#!ts defineComponent({ name: (name: string) => void, schema: (schema: any) => void, template: (templateFunction: (componentArgs: T, opts: TemplateContext) => void) => void }): void`

参数：

- `#!ts name(name: string): void`
  自定义组件的名称，将在自动补全中显示。

- `#!ts schema(schema: any): void`
  组件的模式。这用于为自定义组件参数创建自动补全，应该采用[标准JSON模式](https://json-schema.org)。你还可以使用`$ref`属性访问bridge.的内置自动补全。它们可以在[这里](https://github.com/bridge-core/editor-packages/tree/main/packages/minecraftBedrock/schema)找到，并应从`data`文件夹根目录引用，例如`#!ts $ref: '/data/packages/minecraftBedrock/schema/general/slotType.json'`将访问插槽类型的自动补全。

- `#!ts template(templateFunction: (componentArgs: any, opts: TemplateContext) => void): void`
  `templateFunction`接收`componentArgs`，这是用户定义的组件参数，`opts`提供函数，允许你将数据与组件创建所在的文件合并，并允许你创建动画和动画控制器。

### `TemplateContext`

#### 通用

- `#!ts compilerMode: 'build' | 'dev'`
  让你访问当前编译器模式。

- `#!ts create(template: any, location?: string, operation?: (deepMerge: (oldData: any, newData: any) => any, oldData: any, newData: any) => any): void`
  允许你在组件所在的实体/区块/物品内部创建数据。`template`应该是一个JavaScript对象，包含要与给定`location`的文件合并的数据。`location`应该是用`'/'`分隔的路径，指向你希望创建`template`的位置。例如：`minecraft:entity/description`。默认的合并行为可以选择性地通过`operation`被覆盖，`operation`应该是一个函数，接受默认合并函数`deepMerge`、`location`处的数据(`oldData`)和要合并的新数据(`newData`)。它应返回自定义合并的结果。例如：`(deepMerge, oldData, newData) => newData`将覆盖`location`处的数据。

- `#!ts location: string`
  让你访问组件在实体/区块/物品文件中的位置。

- `#!ts identifier: string`
  让你访问组件所在的实体/区块/物品的标识符。

#### 实体

```ts
interface TemplateContext {
  compilerMode: 'build' | 'dev'
  create: (
    template: any,
    location?: string,
    operation?: (
      deepMerge: (oldData: any, newData: any) => any,
      oldData: any,
      newData: any
    ) => any
  ) => void
  sourceEntity: () => any
  animation: (animation: any, condition?: string | false) => void
  animationController: (
    animationController: any,
    condition?: string | false
  ) => void
  location: string
  identifier: string
  projectNamespace: string
  client: {
    create: (clientEntity: any, formatVersion = "1.10.0") => void
  }
  dialogueScene: (sceneDefinition: any, openDialogue = true) => void
  onActivated: (eventResponse: any) => void
  onDeactivated: (eventResponse: any) => void
  lootTable: (lootTable: any) => string
  tradeTable: (tradeTable: any) => string
  spawnRule: (spawnRule: any) => void
}
```

- `#!ts sourceEntity(): any`
  访问当前应用于你的组件的源实体。

- `#!ts animation(animation: any, condition?: string | false): void`
  允许你创建一个自动链接到实体的BP动画。`animation`应该是一个包含应添加到动画名称的动画数据的JavaScript对象。`condition`是一个可选参数，允许你为动画运行设置一个molang条件。

- `#!ts animationController(animationController: any, condition?: string | false): void`
  允许你创建一个自动链接到实体的BP动画控制器。`animationController`应该是一个包含应添加到动画控制器名称的动画控制器数据的JavaScript对象。`condition`是一个可选参数，允许你为动画控制器运行设置一个molang条件。

- `#!ts client.create(clientEntity: any, formatVersion?: string): void`
  为使用自定义组件的实体创建一个新的客户端实体文件。

- `#!ts onActivated(eventResponse: any): void`
  每当你的组件应用于此实体时触发事件响应。

- `#!ts onDeactivated(eventResponse: any): void`
  每当你的组件从此实体中移除时触发事件响应。

- `#!ts dialogueScene(sceneDefinition: any, openDialogue?: boolean): void`
  创建一个新的对话场景以在你的附加包中使用。此函数仅在你的项目目标版本至少为"1.17.40"时可用。

- `#!ts lootTable(lootTable: any): string`
  为实体创建一个掉落表，并返回一个指向此掉落表的字符串。

- `#!ts tradeTable(tradeTable: any): string`
  为实体创建一个交易表，并返回一个指向此交易表的字符串。

- `#!ts spawnRule(spawnRule: any): void`
  为使用自定义组件的实体创建一个新的生成规则文件。

#### 物品

```ts
interface TemplateContext {
  compilerMode: 'build' | 'dev'
  create: (
    template: any,
    location?: string,
    operation?: (
      deepMerge: (oldData: any, newData: any) => any,
      oldData: any,
      newData: any
    ) => any
  ) => void
  location: string
  identifier: string
  projectNamespace: string
  sourceItem: () => any
  lootTable: (lootTable: any) => string
  recipe: (recipe: any) => void
  player: {
    create: (
      template: any,
      location?: string,
      operation?: (
        deepMerge: (oldData: any, newData: any) => any,
        oldData: any,
        newData: any
      ) => any
    ) => void
    animation: (animation: any, condition?: string | false) => void
    animationController: (
      animationController: any,
      condition?: string | false
    ) => void
  }
}
```

- `#!ts sourceItem(): any`
  访问当前应用于你的组件的源物品。

- `#!ts lootTable(lootTable: any): string`
  为物品创建一个掉落表，并返回一个指向此掉落表的字符串。

- `#!ts recipe(recipe: any): void`
  为使用自定义组件的物品创建一个新配方。

`player` 对象提供对以下函数的访问：

- `#!ts animation(animation: any, condition?: string | false): void`
  允许你创建一个自动链接到玩家的BP动画。`animation`应该是一个包含应添加到动画名称的动画数据的JavaScript对象。`condition`是一个可选参数，允许你为动画运行设置一个molang条件。

- `#!ts animationController(animationController: any, condition?: string | false): void`
  允许你创建一个自动链接到玩家的BP动画控制器。`animationController`应该是一个包含应添加到动画控制器名称的动画控制器数据的JavaScript对象。`condition`是一个可选参数，允许你为动画控制器运行设置一个molang条件。

- `#!ts create(template: any, location?: string): void`
  允许你在玩家内部创建数据。`template`应该是一个JavaScript对象，包含要合并到玩家行为文件中的数据，位于给定的`location`。`location`应该是用`'/'`分隔的路径，指向你希望创建`template`的位置。例如：`minecraft:entity/description`。默认的合并行为可以选择性地通过`operation`被覆盖，`operation`应该是一个函数，接受默认合并函数`deepMerge`、`location`处的数据(`oldData`)和要合并的新数据(`newData`)。它应返回自定义合并的结果。例如：`(deepMerge, oldData, newData) => newData`将覆盖`location`处的数据。

#### 区块

```ts
interface TemplateContext {
  compilerMode: 'build' | 'dev'
  create: (
    template: any,
    location?: string,
    operation?: (
      deepMerge: (oldData: any, newData: any) => any,
      oldData: any,
      newData: any
    ) => any
  ) => void
  sourceBlock: () => any
  location: string
  identifier: string
  projectNamespace: string
  onActivated: (eventResponse: any) => void
  onDeactivated: (eventResponse: any) => void
  lootTable: (lootTable: any) => string
  recipe: (recipe: any) => void
}
```

- `#!ts sourceBlock(): any`
  访问当前应用于你的组件的源区块。

- `#!ts onActivated(eventResponse: any): void`
  每当你的组件应用于此区块时触发事件响应。

- `#!ts onDeactivated(eventResponse: any): void`
  每当你的组件从此区块中移除时触发事件响应。

- `#!ts lootTable(lootTable: any): string`
  为区块创建一个掉落表，并返回一个指向此掉落表的字符串。

- `#!ts recipe(recipe: any): void`
  为使用自定义组件的区块创建一个新配方。

### 创建文件

文件也可以通过自定义组件自动创建。可以调用以下函数来创建文件：

- `#!ts animation(animation: any, condition: string | false): string`返回动画的名称。

- `#!ts animationController(animationController: any, condition: string | false): string`返回动画控制器的名称。

- `#!ts client.create(clientEntity: any, formatVersion?: string): void`

- `#!ts dialogueScene(sceneDefinition: any, openDialogue?: boolean): void`

## 扩展清单

在扩展中创建自定义组件时，你需要在扩展清单中指定它应该安装的位置，使用[`contributeFiles`](./extension-manifest.md#contributefiles)字段。

## 示例

示例可以在以下位置找到：

- [ItemEquippedSensor](https://github.com/bridge-core/plugins/tree/master/plugins/ItemEquippedSensorV2)
- [SimpleBlockRotation](https://github.com/bridge-core/plugins/tree/master/plugins/BlockRotationV2)