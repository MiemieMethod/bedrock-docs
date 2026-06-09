# SerenityJS API概览

本文列出SerenityJS出现的主要包、事件阶段、命令注册接口和自定义方块接口。以下内容均属于SerenityJS第三方自实现服务端，不是BDS、官方脚本API或原版附加包系统的原生能力。

/// warning | 版本提示
当前工作区中的`@serenityjs/core`、`@serenityjs/data`和`@serenityjs/plugins`均为`0.8.20`，且根工作区要求Node.js25或Bun1.3.0以上，说明项目仍处于1.0前的快速迭代阶段。具体类名、方法签名和可用能力应以当前NPM包、类型定义和发行说明为准。
///

## 包

| 包 | 说明 |
|----|------|
| `@serenityjs/core` | 核心服务端结构、`Serenity`实例、世界、事件、方块类型、区块、子区块和LevelDB世界提供器。 |
| `@serenityjs/protocol` | 基岩版协议结构和协议相关枚举，例如用于材质实例的`MaterialRenderMethod`。 |
| `@serenityjs/raknet` | RakNet传输层实现。 |
| `@serenityjs/nbt` | NBT数据处理。 |
| `@serenityjs/data` | 运行所需数据。 |
| `@serenityjs/emitter` | 事件基础设施。 |
| `@serenityjs/logger` | 日志工具。 |
| `@serenityjs/plugins` | 插件系统工具。 |
| `@serenityjs/internal-config` | 内部配置工具。 |

上述核心工作区包当前统一使用`0.8.20`版本号。

## `Serenity`实例

`Serenity`实例是嵌入式服务端的入口。构造选项示例如下：

```typescript
const serenity = new Serenity({
  path: "./properties.json",
  serenity: {
    permissions: "./permissions.json",
    resources: "./resource_packs",
  },
});
```

| 字段 | 说明 |
|------|------|
| `path` | 服务器属性配置路径。 |
| `serenity.permissions` | 权限配置路径。 |
| `serenity.resources` | 资源包目录路径。 |

常见方法：

| 方法 | 说明 |
|------|------|
| `registerProvider(LevelDBProvider, { path })` | 注册LevelDB世界提供器，并指定世界目录。 |
| `start()` | 启动服务器。 |
| `before(event, listener)` | 注册前置事件监听器。 |
| `on(event, listener)` | 注册常规事件监听器。 |
| `after(event, listener)` | 注册后置事件监听器。 |

## 事件阶段

| 阶段 | 说明 |
|------|------|
| `before` | 在其他监听器前执行。返回`false`时可取消后续事件循环，返回`true`时继续处理。 |
| `on` | 在同一进程刻中、`before`阶段之后执行；该阶段本身不用于取消事件。 |
| `after` | 在其他处理完成后、后续进程刻中执行。 |

出现的事件包括：

| 事件 | 用途 |
|------|------|
| `WorldEvent.PlayerInitialized` | 玩家初始化后发送欢迎消息。 |
| `WorldEvent.PlayerChat` | 监听玩家聊天并可在`before`阶段进行前置判断。 |
| `WorldEvent.PlayerPlaceBlock` | 在方块放置前后读取原位置方块和即将放置的方块置换。 |

## 命令注册

SerenityJS命令按世界注册，入口是世界实例的`commandPalette`。

```typescript
world.commandPalette.register(name, description, registry?, executor);
```

| 参数 | 说明 |
|------|------|
| `name` | 命令名称。 |
| `description` | 命令描述。 |
| `registry` | 可选的注册器函数，用于设置权限、调试标记和重载。 |
| `executor` | 默认执行器。当没有重载匹配时执行。 |

### 注册器字段

| 字段或方法 | 说明 |
|------------|------|
| `registry.permissions` | 命令所需权限字符串数组。 |
| `registry.debug` | 是否在游戏内命令列表中以调试样式显示。该标记不改变命令功能。 |
| `registry.overload(arguments, executor)` | 注册一个参数重载及其执行器。 |

### 参数类型

| 类型 | 说明 |
|------|------|
| `TargetEnum` | 目标参数。`[TargetEnum, false]`表示非可选目标参数。 |
| `CustomEnum` | 自定义枚举参数的基类。子类通过静态`identifier`和`options`定义枚举标识符与可选值。 |

### 执行器上下文

执行器示例读取了以下上下文值：

| 值 | 说明 |
|----|------|
| `origin` | 命令发送者。示例中通过`origin instanceof Player`限制玩家执行。 |
| `target.result` | 目标参数解析结果。 |
| `kit.result` | 自定义枚举参数解析结果。 |

执行器可以返回包含`message`字段的对象，也可以抛出错误表示参数或执行条件无效。

## 自定义方块

`CustomBlockType`用于定义SerenityJS自定义方块类型。

```typescript
const blockType = new CustomBlockType("serenity:example_block", {
  solid: true,
});
```

### 基础组件

出现的组件方法包括：

| 方法 | 说明 |
|------|------|
| `components.setLightEmission(level)` | 设置发光等级。`0`表示不发光，`15`表示最大发光等级。 |
| `components.setIsInteractable(value)` | 设置方块是否可交互。交互型方块才能触发示例中的交互方块特质。 |
| `components.getGeometry()` | 获取几何体组件。 |
| `geometry.setModelIdentifier(identifier)` | 设置几何体标识符。 |
| `components.getMaterialInstances()` | 获取材质实例组件。 |
| `materials.createMaterialInstance(face, options)` | 为指定面创建材质实例。`"*"`表示全部面。 |

材质实例选项示例：

| 字段 | 说明 |
|------|------|
| `texture` | 纹理名称。 |
| `render_method` | 渲染方法。常见值包括`MaterialRenderMethod.AlphaTest`。 |

### 方块置换

```typescript
const permutation = blockType.createPermutation({
  boolean_state: true,
  number_state: 42,
  string_state: "example",
});
```

方块置换的状态值可以是字符串、数字或布尔值。置换可以覆盖基础方块组件，例如为不同`powered`状态设置不同发光等级。

### 方块特质

方块特质通过继承`BlockTrait`定义。

| 成员 | 说明 |
|------|------|
| `static identifier` | 方块特质的唯一标识符。 |
| `onInteract()` | 交互回调。常见用法是在其中读取并切换`powered`状态。 |
| `this.block.getState(name)` | 读取方块状态值。 |
| `this.block.setState(name, value)` | 设置方块状态值。 |

### 注册

| 方法 | 说明 |
|------|------|
| `world.blockPalette.registerType(blockType)` | 将自定义方块类型注册到世界方块调色板。 |
| `world.blockPalette.registerTrait(traitClass)` | 注册方块特质类。 |

## 插件模板

SerenityJS当前工作区单独提供`@serenityjs/plugins`包。创建插件时，至少需要准备Node.js或Bun运行时与代码编辑器，并确认项目安装了插件包及其依赖的核心包。

插件模板只适用于SerenityJS插件生态；它不是BDS、LeviLamina、Endstone、Allay、Nukkit或PocketMine-MP插件模板。

## 本体开发命令

SerenityJS仓库使用Yarn工作区。修改SerenityJS本体时，常用命令为：

| 命令 | 说明 |
|------|------|
| `yarn install` | 初始化工作区依赖。 |
| `yarn build` | 将TypeScript编译为JavaScript。 |
| `cd devapp` | 进入开发应用目录。 |
| `yarn dev` | 启动开发服务器。 |

这些命令面向SerenityJS项目本体开发，不是普通服务器部署或插件安装的必要步骤。