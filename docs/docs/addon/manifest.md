# 清单文件

**清单文件（Manifest File）**是每个附加包中最重要的文件，文件名必须为{{file|manifest.json}}，位于附加包的根目录。清单文件以JSON格式编写，用于向游戏引擎声明附加包的基本信息、类型、版本、依赖关系等元数据。游戏在导入和加载附加包时，首先读取并验证清单文件。

## 格式版本

清单文件通过顶层的`format_version`字段声明其格式版本。目前支持的格式版本包括：

- **1**：最早期的清单文件格式，主要用于皮肤包。
- **2**：当前主流使用的格式版本，适用于资源包、行为包和世界模板。

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

`modules`数组中每个模块的`type`字段定义了模块的类型，决定了游戏引擎如何处理附加包中的内容：

| 类型 | 描述 |
|------|------|
| `resources` | 资源包模块，包含纹理、模型、音效等客户端资源 |
| `data` | 行为包模块，包含实体行为、配方、战利品表等服务端数据 |
| `world_template` | 世界模板模块 |
| `script` | 脚本模块，包含JavaScript脚本代码 |
| `client_data` | 客户端数据模块 |

## 依赖声明

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
