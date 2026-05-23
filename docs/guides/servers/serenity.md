# SerenityJS入门

SerenityJS是一个面向Node.js生态的Minecraft基岩版自实现服务端。它适合想用TypeScript或JavaScript组织服务器逻辑，或者想把基岩版服务器嵌入到普通Node.js/Bun项目中的开发者。想先了解定位和边界，可以阅读[SerenityJS](../../docs/server/serenity.md)。

/// warning | 不要把SerenityJS能力当成BDS能力
SerenityJS的事件、命令、自定义方块和插件系统都属于SerenityJS自身。BDS插件、LeviLamina模组、Endstone插件、Allay插件、Nukkit插件和PocketMine-MP插件不能直接放到SerenityJS中运行。
///

## 准备环境

使用SerenityJS前，先安装Node.js的LTS版本，并准备一个代码编辑器。SerenityJS资料推荐Visual Studio Code。若只运行预构建服务器，可从项目发行页下载对应版本；若希望创建可编程项目，使用包管理器创建项目更合适。

```bash
npm create serenity
yarn create serenity
pnpm create serenity
```

创建过程会根据交互提示初始化项目，并安装SerenityJS相关包。完成后，应优先阅读生成项目中的说明文件，因为模板内容可能随SerenityJS版本更新。

## 连接本机服务器

如果服务器已经启动，但Windows版Minecraft客户端无法在服务器列表中发现或连接本机服务器，通常需要解除Minecraft客户端的回环限制。以管理员身份打开终端后运行：

```powershell
CheckNetIsolation.exe LoopbackExempt -a -p=S-1-15-2-1958404141-86561845-1752920682-3514627264-368642714-62675701-733520436
```

终端返回`Ok.`后，再尝试从客户端连接。该步骤只影响Windows本机调试，不是SerenityJS服务器协议或插件功能的一部分。

## 嵌入服务器

`@serenityjs/core`允许在代码中创建服务器实例。下面的示例展示了一个最小结构：创建`Serenity`实例、监听玩家初始化事件、注册LevelDB世界提供器，并启动服务器。

```typescript title="src/index.ts"
import { Serenity, LevelDBProvider, WorldEvent } from "@serenityjs/core";

const serenity = new Serenity({
  path: "./properties.json",
  serenity: {
    permissions: "./permissions.json",
    resources: "./resource_packs",
  },
});

serenity.on(WorldEvent.PlayerInitialized, ({ player }) => {
  player.sendMessage("欢迎来到服务器！");
});

serenity.registerProvider(LevelDBProvider, { path: "./worlds" });

serenity.start();
```

`properties.json`、`permissions.json`、`resource_packs`和`worlds`是SerenityJS项目使用的路径，不应直接等同于BDS目录结构。实际项目中应根据模板和当前版本文档确认配置文件格式。

## 监听事件阶段

SerenityJS事件有`before`、`on`和`after`三类监听阶段。`before`适合做前置检查，并可以通过返回布尔值影响后续处理；`on`用于常规事件响应；`after`用于读取事件完成后的状态。

```typescript
import { WorldEvent } from "@serenityjs/core";

serenity.before(WorldEvent.PlayerChat, ({ message }) => {
  if (message === "cancel") return false;
  return true;
});
```

不要假设这些阶段与官方脚本API或其他服务端插件API完全一致。移植代码时，应重新检查事件触发时机和可取消性。

## 注册世界命令

SerenityJS命令按世界注册。拿到`World`实例后，可以通过`world.commandPalette.register()`注册命令。下面的`ping`命令在没有参数时返回`Pong!`。

```typescript
import { World } from "@serenityjs/core";

function register(world: World): void {
  world.commandPalette.register(
    "ping",
    "Ping the server to check if it's responsive.",
    () => {
      return {
        message: "Pong!",
      };
    },
  );
}
```

如果命令需要权限、调试标记或参数重载，可以加入注册器函数：

```typescript
import { TargetEnum, World } from "@serenityjs/core";

function register(world: World): void {
  world.commandPalette.register(
    "ping",
    "Ping the server to check if it's responsive.",
    (registry) => {
      registry.permissions = ["example.ping"];
      registry.debug = true;

      registry.overload(
        {
          target: [TargetEnum, false],
        },
        ({ target }) => {
          if (!target.result || target.result.length !== 1) {
            throw new Error("Invalid target argument, expected a single value.");
          }

          const entity = target.result[0];
          const value = entity.isPlayer() ? entity.username : entity.type.identifier;

          return {
            message: `Pong, ${value}!`,
          };
        },
      );
    },
    () => {
      return {
        message: "Pong!",
      };
    },
  );
}
```

重载参数和权限字符串属于SerenityJS命令系统。不要把它们写入原版函数、命令方块或BDS配置中。

## 创建自定义方块

SerenityJS可以用`CustomBlockType`定义自定义方块类型，并用组件、方块置换和方块萃取描述表现与行为。

```typescript
import { BlockTrait, CustomBlockType } from "@serenityjs/core";
import { MaterialRenderMethod } from "@serenityjs/protocol";

const exampleBlockType = new CustomBlockType("serenity:example_block", {
  solid: true,
});

exampleBlockType.components.setLightEmission(15);
exampleBlockType.components.setIsInteractable(true);

const geometry = exampleBlockType.components.getGeometry();
geometry.setModelIdentifier("geometry.example_block");

const materials = exampleBlockType.components.getMaterialInstances();
materials.createMaterialInstance("*", {
  texture: "example_block",
  render_method: MaterialRenderMethod.AlphaTest,
});

const powered = exampleBlockType.createPermutation({ powered: true });
powered.components.setLightEmission(15);

const unpowered = exampleBlockType.createPermutation({ powered: false });
unpowered.components.setLightEmission(0);

class ExampleBlockTrait extends BlockTrait {
  public static readonly identifier = "serenity:example_block_trait";

  public onInteract(): void {
    const state = this.block.getState("powered");
    this.block.setState("powered", !state);
  }
}
```

定义完成后，还需要把方块类型注册到世界的方块调色板：

```typescript
world.blockPalette.registerType(exampleBlockType);
world.blockPalette.registerTrait(ExampleBlockTrait);
```

这些自定义方块能力只在SerenityJS服务端运行时中成立。若要制作普通附加包自定义方块，应改读附加包数据驱动教程，而不是照搬SerenityJS代码。

## 创建插件项目

SerenityJS提供`sample-plugin`模板仓库。创建插件时，通常先使用模板生成自己的仓库，再在其中编写TypeScript或JavaScript代码。资料中提到创建模板项目时可以选择仓库名称、描述，并可按需包含模板中的不同分支。

插件适合分发可复用的服务端扩展；直接嵌入`Serenity`实例的代码则适合把服务器作为应用程序的一部分。两种组织方式都属于SerenityJS生态，选择时应看项目是否需要独立发布和安装。

## 修改SerenityJS本体

如果目标是修改SerenityJS仓库本身，而不是开发服务器项目或插件，需要安装Yarn并构建整个工作区：

```bash
yarn install
yarn build
cd devapp
yarn dev
```

这会编译SerenityJS的TypeScript源码并启动开发应用。普通服主和插件开发者通常不需要执行这组步骤。
