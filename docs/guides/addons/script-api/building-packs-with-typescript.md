# 使用TypeScript构建包<!-- md:flag vanilla -->

JavaScript足够写出脚本，但当项目变大时，TypeScript会更舒服：编辑器能提示类型，编译器能提前发现一部分错误，调试器也能通过源映射把运行中的JavaScript对应回`main.ts`。这一课会把上一课的脚本项目升级成“编写TypeScript、编译JavaScript、部署到游戏”的工作流。

## 安装工具

你需要准备以下工具：

- __Node.js__：安装官方长期支持版本，NPM会随Node.js一起安装。
- __Visual Studio Code__：用于编辑TypeScript和调试脚本。
- __Minecraft Bedrock Edition Debugger__：可选，但推荐安装；它可以让Visual Studio Code附加到正在运行的Minecraft脚本。

官方TypeScript教程使用`minecraft-scripting-samples`仓库中的`ts-starter`作为起点。这个启动项目已经包含常见的构建和部署脚本，适合第一次学习时直接使用。

## 取得启动项目

1. 打开`https://github.com/microsoft/minecraft-scripting-samples/`。
2. 下载仓库压缩包，解压后找到`ts-starter`文件夹。
3. 把`ts-starter`复制到你的项目目录，例如`C:\projects\cotta`。
4. 在PowerShell中进入项目目录：

```powershell
cd C:\projects\cotta
```

安装项目依赖：

```powershell
npm i
```

然后用Visual Studio Code打开当前目录：

```powershell
code .
```

## 配置部署目标

打开项目根目录的`.env`。常见配置如下：

```ini title=".env"
PROJECT_NAME="starter"
MINECRAFT_PRODUCT="BedrockGDK"
CUSTOM_DEPLOYMENT_PATH=""
```

- `PROJECT_NAME`决定部署到游戏开发目录时使用的文件夹名。
- `MINECRAFT_PRODUCT`可以选择正式版或预览版安装位置；官方示例使用`BedrockGDK`和`PreviewGDK`。
- `CUSTOM_DEPLOYMENT_PATH`用于非标准安装位置。

然后打开行为包中的`manifest.json`，修改名称、描述和UUID。不要直接复用模板UUID，否则多个包同时存在时会互相冲突。

## 本地部署

第一次运行部署脚本前，如果PowerShell阻止脚本执行，可以只对当前进程放宽策略：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

执行本地部署：

```powershell
npx just-scripts local-deploy
```

这个命令会编译TypeScript，并把生成结果复制到`.env`指定的Minecraft开发目录。启动游戏、创建测试世界并启用行为包后，如果模板脚本输出类似`Hello starter!`的消息，就说明工具链已经工作。

开发时可以使用监听模式：

```powershell
npx just-scripts local-deploy --watch
```

监听模式会在文件变化后自动重新编译和部署。你仍然需要在游戏内执行`/reload`，或在不支持热重载的改动后重新进入世界。

## 编写TypeScript脚本

打开`scripts/main.ts`，可以先写一个和上一课等价的版本：

```typescript title="scripts/main.ts"
import { world, system } from "@minecraft/server";

system.runInterval(() => {
  world.sendMessage(`TypeScript脚本正在运行。当前刻：${system.currentTick}`);
}, 200);
```

保存后，监听模式会把它编译成Minecraft可以执行的JavaScript。TypeScript项目通常还会生成源映射文件，以便调试器把运行位置对应回原始`.ts`文件。

## 调试与检查

如果脚本没有按预期运行，按这个顺序排查：

1. 看终端中的TypeScript编译错误。
2. 看Minecraft内容日志中的包加载和脚本运行错误。
3. 确认`package.json`中安装了项目实际使用的`@minecraft/*`模块。
4. 确认`manifest.json`中的脚本模块依赖和`package.json`里的NPM依赖没有遗漏。

官方校验规则会检查行为包清单和`package.json`之间的脚本模块注册关系：清单里用了某个`@minecraft/*`模块，但`package.json`没有注册时，会被视为缺少包注册；包名不存在时，也会报错。

/// tip | 什么时候使用调试器
打印日志适合快速确认代码是否执行；当你需要看变量、单步执行、检查调用栈时，再使用Minecraft Bedrock Edition Debugger。调试脚本时，Visual Studio Code的`launch.json`通常会使用`minecraft-js`调试类型和`19144`端口。
///
