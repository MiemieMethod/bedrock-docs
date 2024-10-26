---
title: TypeScript
category: 文档
mentions:
  - BlueFrog130
  - sermah
  - SmokeyStack
  - SirLich
  - Fabrimat
  - JaylyDev
  - Herobrine643928
  - ThomasOrs
description: 在Minecraft基岩版附加包开发中的TypeScript。
---

[TypeScript](https://www.typescriptlang.org/) 是由微软开发和维护的一种编程语言。它是JavaScript的严格语法超集，并为语言添加了可选的静态类型。TypeScript旨在用于大型应用程序的开发，并会转译为JavaScript。由于TypeScript是JavaScript的超集，现有的JavaScript程序也是有效的TypeScript程序。

在开发Minecraft附加包的脚本时，使用TypeScript非常有益。存在一些库可以帮助开发Minecraft附加包，提供智能感知和类型安全，以便于广播和监听事件。

## 工作原理

TypeScript是一种需要编译为JavaScript的语言。Minecraft无法处理`.ts`文件。因此，需要设置一些工具，以便利用TypeScript构建附加包。

首先，需要将TypeScript文件编译为JavaScript，这可以通过使用[TypeScript编译器](https://www.npmjs.com/package/typescript)来完成。然后，这些文件可以被Minecraft的脚本系统使用。

由于已经有了构建步骤，我们不妨结合其他系统，以便于文件分离和代码共享。Minecraft的脚本系统只会对各自文件夹中的脚本文件进行操作，利用的是Mojang自己的JavaScript解释器。因此，跨多个文件的任何逻辑必须合并为一个大型文件。这就是像[webpack](https://webpack.js.org/)和[browserify](https://browserify.org/)这样的工具派上用场的地方。

## 脚本API

## 前提条件

1. Minecraft基岩版（Windows 10）
2. 一个代码编辑器，比如Visual Studio Code（虽然记事本在技术上是足够的，但我们将假设使用VSCode）
3. 基础的JavaScript知识（本教程不会教授如何编写JavaScript，假设你具备基本知识）
4. 安装工具和将TypeScript编译为JavaScript需要[Node.js](https://nodejs.org/en/)。
5. 对TypeScript的了解

## 设置指南

本指南用于使用TypeScript编译器设置脚本API TypeScript项目。

### 开始

打开终端（Windows的命令提示符），导航到项目应位于的位置。它可以是任何地方。对于Windows 10，你也可以在文件资源管理器中按`Shift + 右键`并选择`在PowerShell中打开`。

如果你还没有这样做，运行`cd`命令将终端的目录设置为项目所在的目录。

```bash
cd path/to/project
```

接下来，我们需要安装TypeScript以创建附加包。为此，输入以下命令。

以下命令全局安装TypeScript。

```bash
npm install -g typescript
```

以下命令在当前目录创建一个package.json文件。

```bash
npm init -y
```

以下命令安装脚本API模块。本示例中使用的是Beta API。

```bash
npm install @minecraft/server@beta
npm install @minecraft/server-ui@beta
npm install @minecraft/server-gametest@beta
npm install @minecraft/server-admin@beta
npm install @minecraft/server-net@beta
```

现在你的文件夹结构应包含以下目录：

<FolderView :paths="[
	'node_modules',
  'package-lock.json',
  'package.json',
]"></FolderView>

::: tip

如果你收到`command npm not found`的错误，请确保你已安装Node.js并将其添加到PATH中。

:::

现在可以初始化项目。下一步是在当前目录创建一个`tsconfig.json`文件，内容如下，模拟Minecraft脚本API文件系统。

<CodeHeader>tsconfig.json</CodeHeader>

```json
{
  "compilerOptions": {
    "module": "ES2020",
    "target": "ES2021",
    "moduleResolution": "Node",
    "allowSyntheticDefaultImports": true,
    "baseUrl": "./src",
    "rootDir": "./src",
    "outDir": "./scripts"
  },
  "exclude": [ "node_modules" ],
  "include": [ "src" ]
}
```

现在你已经创建了项目，可以在你选择的IDE中打开它。如果你使用VS Code，可以`cd`进入项目目录并运行`code .`来打开项目。

### 项目结构

<FolderView :paths="[
	'node_modules',
  'src/Main.ts',
	'manifest.json',
	'pack_icon.png',
  'package-lock.json',
  'package.json',
  'tsconfig.json',
]"></FolderView>

除非你知道自己在做什么，否则项目中唯一需要关注的部分是`src`文件夹中的所有内容。所有开发工作都应在此进行。

### 编写脚本

现在在`src`目录中编写你的第一个TypeScript代码，例如如下所示：

<CodeHeader>BP/src/Main.ts</CodeHeader>

```ts
import { Player, EntityQueryOptions, GameMode, Vector3, world } from '@minecraft/server';

// 使用提供的类型的示例函数
function findPlayersInSurvivalMode(location: Vector3): Player[] {
  const options: EntityQueryOptions = {
    gameMode: GameMode.survival,
    location: location,
  };

  const players: Player[] = world.getPlayers(options);
  return players;
}

// 示例用法
const playerLocation: Vector3 = { x: 10, y: 20, z: 30 };
const playersInSurvivalMode: Player[] = findPlayersInSurvivalMode(playerLocation);
console.log(playersInSurvivalMode);
```

### 命令

以下命令在开发项目时最常用。

```bash
tsc
```

`tsc`将编译`scripts`文件夹中的所有TS文件到你的行为包文件夹中。

```bash
tsc --watch
```

`--watch`将监视你在`src`目录中所做的任何更改，并自动重新安装附加包。

<FolderView :paths="[
	'node_modules',
  'scripts/Main.js',
  'src/Main.ts',
	'manifest.json',
	'pack_icon.png',
  'package-lock.json',
  'package.json',
  'tsconfig.json',
]"></FolderView>

现在`src/Main.ts`文件应已转译为`scripts/Main.js`，其代码如下：

<CodeHeader>BP/scripts/Main.js</CodeHeader>

```js
import { GameMode, world } from '@minecraft/server';
// 使用提供的类型的示例函数
function findPlayersInSurvivalMode(location) {
    const options = {
        gameMode: GameMode.survival,
        location: location,
    };
    const players = world.getPlayers(options);
    return players;
}
// 示例用法
const playerLocation = { x: 10, y: 20, z: 30 };
const playersInSurvivalMode = findPlayersInSurvivalMode(playerLocation);
console.log(playersInSurvivalMode);
```

### 打包

要在Minecraft中运行代码，请将行为包压缩并导入到Minecraft世界中。在你的行为包中应仅包含以下文件，其余文件不必包含在`.mcpack`压缩文件中。

<FolderView :paths="[
  'scripts/Main.js',
	'manifest.json',
	'pack_icon.png',
]"></FolderView>

恭喜你，你已经创建了第一个TypeScript项目用于脚本API。