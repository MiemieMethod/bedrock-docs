# 清单文件

**清单文件（Manifest File）**是每个附加包中最重要的文件，文件名须为{{file|manifest.json}}，位于附加包的根目录，与包内所有其他顶层文件处于同级目录。清单文件以JSON格式编写，用于向游戏引擎声明附加包的基本信息、类型、版本、依赖关系等元数据。游戏在导入和加载附加包时，首先读取并验证清单文件。

此外，游戏也接受以{{file|pack_manifest.json}}为文件名的旧式清单文件。当两者同时存在时，游戏优先读取{{file|manifest.json}}；若仅存在{{file|pack_manifest.json}}，则将其作为清单文件读取。在执行清单文件格式版本升级时，游戏会将旧版清单文件备份为{{file|manifest.json_old}}，并在附加包目录生成{{file|upgrade_report.log}}升级日志。

## 格式版本

清单文件通过顶层的`format_version`字段声明其格式版本。目前支持的格式版本包括（其他值将导致内容日志错误）：

- **0**：早期使用的清单文件格式，当前已基本废弃。格式版本`0`的清单文件在结构上与格式版本`1`和`2`存在差异：`header`中的`min_engine_version`默认值为`1.2.5`，且不强制要求大于或等于`1.13.0`。该格式版本下的`dependencies`字段语义上等同于格式版本`2`的`legacy_module_dependencies`字段。
- **1**：较早期的清单文件格式。`header`中的大部分字段与格式版本`2`相同，但`name`字段非必须，`min_engine_version`若大于或等于`1.13.0`会强制回退至`1.12.0`，`base_game_version`在此版本下不生效，且`lock_template_options`为可选字段。
- **2**：当前主流使用的格式版本，适用于资源包、行为包和世界模板。与格式版本`1`相比，`header`中的`name`字段为必填，`min_engine_version`必须大于或等于`1.13.0`，`base_game_version`对世界模板为必填字段，`lock_template_options`对世界模板包为必填字段。

## 结构

清单文件的主要结构如下：

/// html | div.treeview
- {{json|object|}}：根对象。
    - {{json|int|format_version|required=1}}：清单文件的格式版本。
    - {{json|object|header|required=1}}：标头信息。
        - {{json|string|name|required=1}}：附加包在游戏中显示的名称。
        - {{json|string|description}}：附加包的描述文本。
        - {{json|string|uuid|required=1}}：附加包的UUID，全局唯一标识符。
        - {{json|array|version|required=1}}：附加包版本，格式为`[主版本号, 次版本号, 补丁版本号]`。
        - {{json|array|min_engine_version}}：最低引擎版本。
        - {{json|string|pack_scope}}：包作用域，可选`world`、`global`或`any`（仅资源包）。
        - {{json|array|base_game_version}}：基游戏版本（仅世界模板）。
        - {{json|array|pack_optimization_version}}：包优化版本。
        - {{json|boolean|platform_locked}}：是否平台锁定。
        - {{json|boolean|lock_template_options}}：是否锁定模板选项。
        - {{json|boolean|allow_random_seed}}：是否允许随机种子。
    - {{json|array|modules|required=1}}：模块列表。
        - {{json|object|}}：一个模块。
            - {{json|string|type|required=1}}：模块类型。
            - {{json|string|uuid|required=1}}：模块的UUID。
            - {{json|array|version|required=1}}：模块版本。
            - {{json|string|description}}：模块描述。
            - {{json|string|language}}：脚本语言（仅脚本模块）。
            - {{json|string|entry}}：脚本入口文件路径（仅脚本模块）。
    - {{json|array|dependencies}}：依赖列表。
        - {{json|object|}}：一个依赖。
            - {{json|string|uuid}}：所依赖的附加包或模块的UUID。
            - {{json|string|module_name}}：所依赖的脚本API模块名称。
            - {{json|array|version}}：所依赖的版本。
    - {{json|array|capabilities}}：声明附加包需要的特殊功能。
    - {{json|object|metadata}}：附加包的元数据。
        - {{json|array|authors}}：作者列表。
        - {{json|string|license}}：许可证。
        - {{json|string|url}}：项目网址。
        - {{json|object|generated_with}}：生成工具信息。
        - {{json|string|product_type}}：产品类型。
    - {{json|array|settings}}：世界设置列表。
    - {{json|array|subpacks}}：子包列表。
    - {{json|boolean|has_education_metadata}}：是否包含教育版元数据。<!-- md:flag edu -->
///

## UUID

**UUID（Universally Unique Identifier）**是清单文件中用于唯一标识附加包和模块的通用唯一标识符。UUID的标准格式为`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`，由32位十六进制数字和4个连字符组成。

每个附加包的标头UUID必须全局唯一，两个不同的附加包不应使用相同的标头UUID。同一附加包中的不同模块也应各自拥有独立的UUID。UUID可以通过在线生成器或开发工具生成。

## 模块类型

`modules`数组中每个模块的`type`字段定义了模块的类型，决定了游戏引擎如何处理附加包中的内容。`type`为`invalid`或其他非法字符串时将导致内容日志错误：

| 类型 | 别名 | 描述 |
|------|------|------|
| `resources` | `resourcepack` | 资源包模块，包含纹理、模型、音效等客户端资源 |
| `data` | — | 行为包模块，包含实体行为、配方、战利品表等服务端数据 |
| `world_template` | `worldtemplate` | 世界模板模块 |
| `script` | — | 脚本模块，包含JavaScript脚本代码，需同时设置`language`和`entry`字段 |
| `client_data` | — | 客户端数据模块 |
| `client_script` | — | 客户端脚本模块 |
| `interface` | — | 界面模块 |
| `plugin` | — | 插件模块 |
| `skin_pack` | `skinpack` | 皮肤包模块 |
| `persona_piece` | — | 角色部件模块 |
| `invalid` | — | 无效类型（将导致内容日志错误） |

## 世界设置控件

`settings`数组中，每个控件对象须包含`type`字段以指定控件类型，以及`text`和`name`字段。`name`字段用于存储该控件的设置值，`text`字段用于在界面中显示标签文字。支持的控件类型如下：

| 类型 | 描述 | 专有字段 |
|------|------|---------|
| `label` | 纯文本标签，不可交互 | 无 |
| `toggle` | 开关切换，存储布尔值 | `default`（布尔，默认值）、`control_locked`（枚举，可选） |
| `slider` | 连续滑块，存储浮点数 | `default`、`min`、`max`（浮点数）、`step`（步长，可选，默认为`1`）、`control_locked`（可选） |
| `step_slider` | 步进滑块，存储步数索引（整数） | `default`（整数，默认索引）、`steps`（字符串数组，各步文本）、`control_locked`（可选） |
| `dropdown` | 下拉菜单，存储选项索引（整数） | `default`（整数，默认索引）、`options`（字符串数组，各选项文本） |
| `input` | 文本输入框，存储字符串 | `default`（字符串）、`placeholder`（占位文本，可选）、`control_locked`（可选） |

`control_locked`字段控制该控件何时被锁定，可选值为`"none"`（从不锁定）、`"pregame"`（游戏开始前锁定）或`"ingame"`（游戏进行中锁定）。



`dependencies`数组用于声明附加包所依赖的其他包或脚本API模块。依赖可以通过UUID指向另一个附加包，也可以通过`module_name`指向一个内置的脚本API模块（如`@minecraft/server`）。

游戏在加载附加包时会检查所有声明的依赖是否满足。如果某个依赖的附加包未安装或版本不匹配，游戏可能会拒绝加载当前附加包或产生警告。

## 功能声明

`capabilities`数组用于声明附加包需要的特殊功能支持。如果在创建世界时未开启对应的功能开关，声明了该功能的附加包可能无法正常工作。可用的功能包括：

- `chemistry`：化学功能。<!-- md:flag edu -->
- `editorExtension`：编辑器扩展功能。
- `experimental_custom_ui`：实验性自定义UI。
- `raytraced`：光线追踪支持。

## 参考阅读

- [清单文件架构参考](../../refs/addon/manifest-schema.md)
- [清单标头参考](../../refs/addon/manifest-header.md)
- [清单模块参考](../../refs/addon/manifest-module.md)
- [清单依赖参考](../../refs/addon/manifest-dependency.md)
- [世界设置参考](../../refs/addon/world-setting.md)