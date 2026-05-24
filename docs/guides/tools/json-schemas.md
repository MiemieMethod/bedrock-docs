# 配置JSON架构校验

如果你不使用bridge.，仍然可以让Visual Studio Code、Neovim、JetBrains IDE或Sublime Text根据JSON架构检查附加包文件。Blockception维护的`Minecraft-bedrock-json-schemas`项目提供了一组社区JSON架构，并在仓库中给出了多种编辑器的配置方式。

/// warning | 架构不是游戏本身
社区JSON架构适合用来减少拼写错误、补全常见字段和快速发现无效JSON，但它不是Minecraft基岩版引擎，也不是官方参考。遇到架构提示和文档、游戏导出资料或实际内容日志冲突时，应以官方资料和游戏实际行为为准。
///

## 什么时候需要配置

建议在这些情况下配置JSON架构：

- 你使用Visual Studio Code、Neovim、JetBrains IDE或Sublime Text直接编辑附加包。
- 你希望在保存前发现少写逗号、字段拼错、字段类型错误等问题。
- 你需要在不打开bridge.的情况下获得一部分字段提示。
- 你正在维护已经纳入Git的包目录，希望把编辑器设置和项目一起保存。

如果你主要使用bridge.，通常不需要额外配置。bridge.已经内置面向项目目标版本的补全与校验。

## 架构能覆盖哪些文件

Blockception仓库的说明页和IDE设置指南列出了常见架构。下面只列出适合附加包开发时优先配置的部分：

| 范围 | 常见文件 | 架构用途 |
| --- | --- | --- |
| 通用 | `manifest.json` | 校验清单文件、模块、依赖和包元数据。 |
| 语言 | `languages.json`、`language_names.json` | 校验语言索引和语言名称文件。 |
| 皮肤包 | `skins.json` | 校验皮肤包中的皮肤列表。 |
| 资源包 | `animations`、`animation_controllers`、`attachables`、`entity`、`models/entity`、`particles`、`render_controllers`、`textures`、`sounds`、`fogs` | 校验客户端资源定义。 |
| 行为包 | `blocks`、`entities`、`features`、`feature_rules`、`items`、`loot_tables`、`recipes`、`spawn_rules`、`trading`、`volumes`、`functions/tick.json` | 校验服务端数据定义。 |

这些架构依赖文件名或路径匹配。若你的项目使用非常规文件名，例如把实体定义命名为`zombie_custom.json`而不放在`entities`文件夹中，编辑器可能不会自动套用正确架构。

## Visual Studio Code

Visual Studio Code支持通过`json.schemas`设置绑定远程JSON架构。最简单的做法是在项目根目录创建`.vscode/settings.json`，然后加入需要的映射：

```json title=".vscode/settings.json"
{
  "json.schemas": [
    {
      "description": "Minecraft Bedrock Manifest",
      "fileMatch": [
        "manifest.json",
        "manifest.jsonc",
        "manifest.json5"
      ],
      "url": "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/manifest.json"
    },
    {
      "description": "Minecraft Bedrock Behavior Entities",
      "fileMatch": [
        "behavior_packs/*/entities/*.json",
        "*BP*/entities/*.json",
        "*.entity.bp.json",
        "*.behavior.json"
      ],
      "url": "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/entities/entities.json"
    },
    {
      "description": "Minecraft Bedrock Client Entity",
      "fileMatch": [
        "resource_packs/*/entity/*.json",
        "*RP*/entity/*.json",
        "*.entity.rp.json",
        "*.entity.json"
      ],
      "url": "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/entity/entity.json"
    }
  ]
}
```

如果项目使用工作区文件，也可以把同样的`json.schemas`数组放入`.code-workspace`的`settings`对象中。Blockception仓库根目录还提供了完整的`vscode-settings.json`，适合在需要覆盖大多数附加包文件类型时复制。

/// tip | 先少后多
初学时可以只配置`manifest.json`、实体、方块、物品和配方。等项目需要粒子、渲染控制器、地物或交易表时，再添加对应架构。过长的全量配置不一定更易维护。
///

## Neovim

Neovim通常通过`jsonls`语言服务器使用JSON架构。需要先安装并启用LSP配置插件，然后把架构加入`jsonls`的`settings.json.schemas`：

```lua title="jsonls.lua"
local lspconfig = require("lspconfig")

lspconfig.jsonls.setup({
  settings = {
    json = {
      schemas = {
        {
          description = "Minecraft Bedrock Manifest",
          fileMatch = { "manifest.json", "manifest.jsonc", "manifest.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/manifest.json"
        },
        {
          description = "Minecraft Bedrock Recipes",
          fileMatch = { "recipes/*.json", "*.recipe.json" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/recipes/recipes.json"
        }
      }
    }
  }
})
```

如果使用`lazy.nvim`，可以把上述`jsonls.setup`调用放入`nvim-lspconfig`的配置函数。不同Neovim配置框架的文件路径不完全一致，但关键都是把`schemas`数组传给`jsonls`。

## JetBrains IDE

JetBrains IDE内置JSON架构映射功能，可以逐个添加远程架构：

1. 打开设置或首选项。
2. 进入**Languages & Frameworks**→**Schemas and DTDs**→**JSON Schema Mappings**。
3. 点击添加按钮。
4. 填写名称，例如`Minecraft Bedrock Manifest`。
5. 在架构文件或URL中填入Blockception的原始JSON地址，例如`https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/manifest.json`。
6. 添加文件路径模式，例如`manifest.json`或`behavior_packs/*/entities/*.json`。

常用映射可以从清单文件、行为包实体和资源包客户端实体开始。若某个IDE版本不能很好处理通配路径，可以把映射限制到项目中的具体目录。

## Sublime Text

Sublime Text通常通过LSP和`LSP-json`获得JSON架构支持。安装Package Control、LSP和`LSP-json`后，可以在LSP设置中加入：

```json title="LSP设置"
{
  "clients": {
    "LSP-json": {
      "enabled": true,
      "settings": {
        "json": {
          "schemas": [
            {
              "fileMatch": [
                "manifest.json"
              ],
              "url": "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/manifest.json"
            },
            {
              "fileMatch": [
                "behavior_packs/*/entities/*.json",
                "*.entity.bp.json"
              ],
              "url": "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/entities/entities.json"
            }
          ]
        }
      }
    }
  }
}
```

保存设置后，重新打开JSON文件或重启语言服务器即可重新加载映射。

## 排查问题

如果编辑器没有出现补全或校验，可以按顺序检查：

1. 当前文件是否被识别为JSON、JSONC或JSON5。
2. 文件路径是否匹配`fileMatch`。路径匹配失败是最常见原因。
3. 设备是否能访问`raw.githubusercontent.com`。
4. 远程架构URL是否拼写正确。
5. 编辑器的JSON语言服务器是否已经启动。
6. 当前文件本身是否为有效JSON；语法错误可能阻止架构继续校验字段。

若远程URL无法访问，可以把架构文件下载到项目或本机固定目录，再把`url`改为本地文件路径。这样做能减少网络依赖，但也需要自行更新架构文件。

## 使用时的限制

JSON架构只能描述静态结构，不能完全判断游戏运行时行为。例如，架构可以提示`minecraft:entity`中某个组件的字段类型，却不能保证该组件在当前游戏版本、实验性开关、目标平台或中国版环境下确实可用。发布前仍然需要在目标版本中测试，并查看内容日志。

另外，Blockception贡献说明要求架构描述尽量与Microsoft原文保持一致；没有官方描述或未公开的功能可能会被标注为`UNDOCUMENTED`，或由维护者补写概述。看到这类提示时，不要把它当作完整机制说明，应继续查阅文档、导出资料或本站对应页面。

## 完整架构参考

Blockception维护的仓库提供了完整的JSON架构列表和IDE配置指南。如需查看所有可用的架构及其URL，或了解更多IDE和编辑器的配置方法，请参阅[IDE设置指南](../../translations/blockception/ide-setup.md)。