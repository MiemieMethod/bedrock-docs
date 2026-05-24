# 准备环境与项目结构

ICMod开发以Android设备上的Horizon启动器为入口。Nernar维护的InnerCore文档把整体关系描述为“Horizon加载InnerCore包，InnerCore包加载CoreEngine，模组再通过CoreEngine与Minecraft交互”。这个体系属于第三方旧客户端模组生态，不是当前国际版原生支持的开发方式。

/// warning | 先确认目标环境
资料中提到的InnerCore主线长期围绕Android版Minecraft、Horizon启动器和特定游戏版本运行。维护旧项目时，应先确认目标设备的Android版本、CPU架构、InnerCore包版本、模组依赖库版本和目标Minecraft版本。
///

## 安装与包

Nernar文档将InnerCore相关环境分为启动器、包和引擎：

- Horizon是启动器，负责预加载游戏、下载和管理包、管理模组与模组包。
- InnerCore是Minecraft相关包，提供模组运行环境。
- CoreEngine是模组直接接触的主要接口层。

Horizon中的包通常包含普通InnerCore、InnerCore Test和InnerCore Legacy。普通InnerCore面向多数项目；Test用于测试实验性变化；Legacy用于旧项目兼容。旧的独立InnerCore应用已经属于更早的生态，文档也不建议把它当作新项目目标。

在Android11及以下设备上，Horizon目录通常更容易通过`games/horizon`访问；较新的Android版本因存储权限限制，需要通过文件管理器进入`Android/data/com.zheka.horizon/files/horizon`。资料反复提醒：日志通常位于Horizon的`logs`目录或InnerCore包的`innercore`目录，向旧模组作者反馈问题时应优先提供完整日志。

## 包目录

Horizon目录下的核心内容大致如下：

/// html | div.treeview
- `horizon`
    - `packs`：已安装的包。
    - `logs`：启动器、引擎和崩溃日志。
    - `resource_packs`：启动器级资源包缓存。
    - `behavior_packs`：启动器级行为包缓存。
    - `packs/Inner_Core`
        - `modpacks`：模组包。
        - `innercore`：默认模组包和引擎设置。
        - `innercore/mods`：默认安装的模组。
        - `worlds`：该包独立使用的世界。
        - `assets`：该游戏版本的内置资源副本。
///

不要直接编辑包内的`assets`目录。附加包资源应放入Minecraft的开发资源包或开发行为包目录；InnerCore模组资源则应由模组自己的`build.config`描述并加载。

## 模组目录

一个典型InnerCore模组是一个文件夹。它不仅包含脚本，也包含资源、配置、图标、构建输出和可能的Java或C++代码。

/// html | div.treeview
- 模组文件夹
    - `.dex`：发布构建文件。
    - `dev`
        - `.includes`：构建到目标脚本的文件列表。
        - `header.js`：常见的头部脚本。
    - `assets`
        - `resources`
            - `terrain-atlas`：方块纹理。
            - `items-opaque`：物品纹理。
        - `gui`：界面资源。
    - `launcher.js`：加载阶段脚本。
    - `build.config`：核心构建配置。
    - `mod.info`：模组名称、作者、版本和简介。
    - `mod_icon.png`：模组图标。
    - `config.json`：模组设置。
    - `config.info.json`：设置界面描述。
///

`mod.info`是JSON文件。资料建议至少填写`name`、`author`、`version`和`description`。`description`应保持短小，因为旧模组浏览器界面的显示空间有限。

```json title="mod.info"
{
  "name": "Name me",
  "author": "ICDocs",
  "version": "1.0",
  "description": "Short description."
}
```

`config.json`默认可只包含`enabled`。当`enabled`为`false`时，模组脚本可以不启动，但资源仍可能被加载，因此依赖关系和资源副作用需要单独考虑。

```json title="config.json"
{
  "enabled": true
}
```

## 构建配置

`build.config`描述资源、脚本、构建目录、库目录、Java目录和原生目录。资料中给出的常见字段包括：

/// define
`defaultConfig`

- 设定构建类型、API、库目录、资源包目录和行为包目录。InnerCore模组通常使用CoreEngine作为主要API。

`resources`

- 设定资源目录和资源类型。`resource`用于普通资源，`gui`用于旧界面资源。

`compile`

- 设定要加载的脚本以及`sourceType`。常见类型有`preloader`、`launcher`、`main`、`custom`和`library`。

`buildDirs`

- 设定要把多个脚本构建到哪个目标脚本。目录中通常需要`.includes`。

`javaDirs`和`nativeDirs`

- 设定Java代码和C++原生代码目录。它们属于旧客户端模组生态的能力，不是附加包能力。
///

```json title="build.config"
{
  "defaultConfig": {
    "buildType": "develop",
    "api": "CoreEngine",
    "libraryDir": "lib/"
  },
  "resources": [
    {
      "path": "assets/resources/",
      "resourceType": "resource"
    },
    {
      "path": "assets/gui/",
      "resourceType": "gui"
    }
  ],
  "buildDirs": [
    {
      "dir": "dev/",
      "targetSource": "main.js"
    }
  ],
  "compile": [
    {
      "path": "main.js",
      "sourceType": "main"
    },
    {
      "path": "launcher.js",
      "sourceType": "launcher"
    }
  ]
}
```

`.includes`按顺序列出参与构建的脚本。空行和注释会被忽略；不存在的文件通常只产生警告。工具链版本还会读取注释中的TypeScript编译选项，支持目录、排除项和部分通配写法。

```gitignore title="dev/.includes"
# comments can describe why a file is included
header.js
api/tests.js
api/globals.js
module/.
```

## 脚本生命周期

InnerCore文档把脚本生命周期分为几个阶段：

1. 启动器启动后，InnerCore扫描模组、收集脚本并决定要加载的资源。
2. `preloader`脚本可在游戏资源加载前处理资源，例如生成或重染纹理。
3. 游戏进入加载阶段后，`launcher`脚本运行。它通常设置多人信息，然后调用`Launch()`。
4. `Launch()`启动`main`脚本，模组的物品、方块、配方、事件和主要逻辑通常在这里注册。
5. `custom`脚本可通过`runCustomSource`按需运行，并可接收额外上下文。

```javascript title="launcher.js"
ConfigureMultiplayer({
  name: "Name me",
  version: "auto",
  isClientOnly: false
});

Launch();
```

/// warning | 不要重复启动
资料明确指出，每个模组只能启动一次。重复调用`Launch()`会导致错误。
///

## 开发工具

Nernar文档推荐使用Visual Studio Code或IntelliJ IDEA一类环境编写脚本、Java和C++代码；移动设备上可使用Spck Code Editor。若需要TypeScript、Java、C++和从电脑推送代码到设备，InnerCore Mod Toolchain会统一处理TypeScript编译器、Java编译器、C/C++编译器和Android调试桥等工具。

这些工具建议只适用于维护旧ICMod项目。新项目若不依赖旧客户端能力，应优先评估附加包、脚本API、中国版模组SDK或服务端插件。
