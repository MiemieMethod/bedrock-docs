# bridge.进阶功能

bridge.的进阶能力主要围绕项目配置、Dash编译器和扩展系统展开。它们能让一个附加包项目拥有更强的创建、补全、转换和打包能力，但多数功能只在bridge.项目内生效。发布给Minecraft前，必须经过Dash或相应导出流程转换为游戏能够读取的普通文件。

/// warning | 区分工具语法和游戏语法
Dash自定义命令、Dash自定义组件、`.molang`文件和生成器脚本不是Minecraft原生API。它们不能直接复制到游戏世界中使用，也不能作为其他编辑器一定能识别的标准格式。
///

## 项目配置

bridge.项目根目录中的`config.json`保存工具层项目配置。它遵循Bedrock OSS组织提出的项目配置标准，主要告诉bridge.项目名称、作者、命名空间、目标版本、实验性玩法开关和各类包的位置。

常见字段包括：

| 字段 | 用途 |
| --- | --- |
| `type` | 指定项目类型，基岩版项目通常为`minecraftBedrock`。 |
| `name`和`description` | 指定项目在bridge.界面和相关工具中显示的名称与描述。 |
| `authors` | 记录作者名称，也可以为作者附加图标路径。 |
| `namespace` | 指定项目默认命名空间，用于生成标识符和提供补全。 |
| `targetVersion` | 指定开发目标Minecraft版本，影响可创建文件、补全和校验。 |
| `experimentalGameplay` | 记录实验性玩法开关，bridge.会据此筛选可用功能。 |
| `packs` | 把`behaviorPack`、`resourcePack`、`skinPack`和`worldTemplate`等包类型映射到项目内路径。 |
| `worlds` | 通过glob模式记录项目内世界文件夹。 |
| `bdsProject` | 标记项目是否面向BDS，以便显示相关脚本模块。 |
| `compiler` | 配置Dash默认构建配置；设为`false`可以禁用Dash。 |

如果项目从`Local Project`转换而来，或从`.mcaddon`、`.mcpack`导入而来，建议先检查`packs`、`namespace`和`targetVersion`是否符合真实项目结构。

## Dash编译器

Dash是bridge.内置的项目编译器。它负责把项目源文件转换为开发输出或发布输出，并为自定义命令、自定义组件、`.molang`文件、生成器脚本和格式版本修正等功能提供转换流程。

日常开发中，内置Dash通常以监视模式运行：保存源文件后，受影响文件会重新编译到输出目录。如果已经设置`com.mojang`同步，开发输出会直接进入Minecraft开发包目录。导出项目时，bridge.会使用Dash生成生产构建，再写入`.mcaddon`、`.mcworld`或`.mctemplate`。

Dash的构建配置由插件数组组成。插件顺序会影响转换结果，数组中越靠前的插件越早运行。官方文档列出的内置插件包括：

- `typeScript`：把TypeScript转译为JavaScript。
- `customEntityComponents`、`customItemComponents`和`customBlockComponents`：处理Dash自定义组件。
- `customCommands`：处理Dash自定义命令。
- `molang`：处理`.molang`文件并可压缩Molang表达式。
- `generatorScripts`：启用生成器脚本。
- `formatVersionCorrection`：修正部分JSON文件的格式版本处理。
- `simpleRewrite`：把开发输出写入目标目录。
- `rewriteForPackaging`：为打包格式重写输出文件。

熟悉终端的用户还可以使用独立Dash。官方文档将独立Dash描述为基于Deno的命令行构建，适合需要脱离bridge.界面进行自动化构建的项目。

## 自定义命令

Dash自定义命令存放在行为包的`commands/`文件夹中，每个JavaScript或TypeScript文件导出一个命令定义。命令定义通常包含三个部分：

1. `name`指定在bridge.补全列表中出现的命令名。
2. `schema`描述命令参数，供补全和校验使用。
3. `template`根据用户输入的参数生成一个或多个普通Minecraft命令。

自定义命令会出现在`.mcfunction`和部分JSON命令位置的补全中。编译后，Dash会把它们展开为普通命令。因此，自定义命令不能直接在游戏聊天栏或命令方块中输入。

## 自定义组件

Dash自定义组件用于把实体、方块和物品文件中的重复JSON逻辑抽成可复用组件。组件文件按类型分别放在行为包的`components/entity/`、`components/block/`和`components/item/`文件夹中。

一个组件定义通常包含：

- `name`：组件名，建议使用项目命名空间。
- `schema`：组件属性的JSON架构，用于补全和校验。
- `template`：把组件属性转换为实际要合并到文件中的JSON。

例如，项目可以把一组固定生命值、碰撞箱和事件响应封装成组件，再在多个实体文件中使用。编译后，最终输出仍应是Minecraft能够读取的普通实体、方块或物品JSON。

## `.molang`文件

bridge.允许把常用Molang逻辑放进专门的`.molang`文件。`molang`编译插件会从`BP/molang/`和`RP/molang/`读取这些文件，并在项目中提供可复用函数。

`.molang`文件可以定义函数。调用时可使用`f.<函数名>(...)`或`function.<函数名>(...)`。官方文档示例中，函数参数通过`a.<参数名>`或`arg.<参数名>`访问，临时变量会自动限定在当前函数体内。

/// tip | 适合封装重复表达式
如果同一段Molang条件反复出现在动画控制器、客户端实体或物品文件中，可以考虑把它移入`.molang`文件。这样更容易统一修改，但也意味着项目必须经过Dash编译后才能发布。
///

## 生成器脚本

生成器脚本是放在项目内的JavaScript或TypeScript文件，用于生成JSON、`.mcfunction`或其他文件。使用它之前，需要在Dash配置中启用`generatorScripts`插件。

简单生成器可以直接默认导出要写入的对象或字符串。复杂生成器可以使用`@bridge/generate`模块：

- `useTemplate`读取一个模板文件，并可选择不把模板输出到构建结果。
- `createCollection`创建文件合集，让一个脚本生成多个文件。

生成器脚本适合生成大量规则相似的文件。例如，按照同一模板批量生成物品定义、函数文件或本地化条目。

## 扩展系统

bridge.扩展可以全局安装，也可以安装到项目的`.bridge/extensions`文件夹中。全局扩展可用于所有项目，本地扩展只对当前项目生效，更适合团队项目随源码一起管理。

每个扩展都需要清单文件。清单通常包含`name`、`description`、`author`、`version`、`id`、`tags`和`target`等字段。扩展可以提供多种能力：

| 能力 | 说明 |
| --- | --- |
| 预设 | 在新建文件窗口中提供表单化文件创建流程。 |
| 代码片段 | 在文本编辑器或树编辑器中快速插入JSON或文本。 |
| 主题 | 修改bridge.界面、语法高亮和编辑器配色。 |
| 编译器插件 | 扩展Dash构建流程。 |
| 脚本模块 | 通过`@bridge/*`模块访问文件系统、标签页、通知、窗口和项目数据。 |
| iframe API | 把外部网页工具嵌入bridge.标签页，并通过通信通道访问部分bridge.的API。 |

官方资料中的若干脚本模块页面仍包含`TODO`或未完成说明。实际编写扩展时，建议同时查看bridge.源码和官方扩展仓库中的示例。

## 预设与代码片段

预设用于从表单创建一组文件。一个预设通常位于扩展的`presets/`目录中，并包含自己的`manifest.json`。预设清单可以声明名称、图标、分类、启用条件、输入字段、要创建的文件和要扩展的文件。复杂预设还可以通过预设脚本处理文件输入、开关、选择器和批量生成逻辑。

代码片段则更轻量。片段JSON通常声明`name`、`description`、`fileTypes`、`locations`和`data`。`fileTypes`使用bridge.文件类型ID，`locations`使用JSON路径glob模式，决定片段能插入到哪些文件位置。

## 何时谨慎使用

如果项目必须能被任意代码编辑器直接维护，或者发布前不希望依赖专门构建流程，就应减少Dash自定义语法的使用。相反，如果团队统一使用bridge.，并且项目已经使用版本管理和固定构建配置，Dash和扩展系统可以显著减少重复工作。
