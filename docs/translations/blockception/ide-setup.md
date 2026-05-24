# IDE设置指南

本指南提供了在各种IDE和编辑器中配置Minecraft基岩版JSON架构的说明。

/// note | 翻译来源
本文档翻译自[Blockception维护的Minecraft-bedrock-json-schemas](https://github.com/Blockception/Minecraft-bedrock-json-schemas)项目的官方指南。
///

## 目录

- [Neovim与LSP](#neovim与lsp)
- [Visual Studio Code](#visual-studio-code)
- [JetBrains IDE](#jetbrains-ide)
- [Sublime Text](#sublime-text)

---

## Neovim与LSP

要在Neovim和`jsonls`语言服务器中使用这些JSON架构，需要配置LSP设置。

### 前置条件

- 支持LSP的Neovim
- `nvim-lspconfig`插件
- 已安装`jsonls`语言服务器

### 配置

将以下配置添加到Neovim的LSP配置中（通常在`~/.config/nvim/lua/lsp/jsonls.lua`或你的LSP配置文件中）：

```lua
local lspconfig = require('lspconfig')

lspconfig.jsonls.setup({
  settings = {
    json = {
      schemas = {
        -- 通用架构
        {
          description = "Minecraft基岩版清单",
          fileMatch = { "manifest.json", "manifest.jsonc", "manifest.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/manifest.json"
        },
        {
          description = "Minecraft基岩版世界附加包",
          fileMatch = { "world_behavior_packs.json", "world_behavior_packs.jsonc", "world_behavior_packs.json5", "world_resource_packs.json", "world_resource_packs.jsonc", "world_resource_packs.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/world_x_packs.json"
        },
        
        -- 语言架构
        {
          description = "Minecraft基岩版语言名称",
          fileMatch = { "language_names.json", "language_names.jsonc", "language_names.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/language/language_names.json"
        },
        {
          description = "Minecraft基岩版语言",
          fileMatch = { "languages.json", "languages.jsonc", "languages.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/language/languages.json"
        },
        
        -- 皮肤包架构
        {
          description = "Minecraft基岩版皮肤包",
          fileMatch = { "skin_pack/skins.json", "skin_pack/skins.jsonc", "skin_pack/skins.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/skinpacks/skins.json"
        },
        
        -- 资源包架构
        {
          description = "Minecraft基岩版资源包动画控制器",
          fileMatch = {
            "resource_packs/*/animation_controllers/*.json",
            "resource_packs/*/animation_controllers/*.jsonc",
            "resource_packs/*/animation_controllers/*.json5",
            "*resource*pack*/animation_controllers/*.json",
            "*resource*pack*/animation_controllers/*.jsonc",
            "*resource*pack*/animation_controllers/*.json5",
            "*Resource*Pack*/animation_controllers/*.json",
            "*RP*/animation_controllers/*.json",
            "*rp*/animation_controllers/*.json",
            "*.animation_controller.rp.json",
            "*.rpac.json",
            "*.ac.rp.json",
            "*.rp_ac.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/animation_controllers/animation_controller.json"
        },
        {
          description = "Minecraft基岩版资源包动画",
          fileMatch = {
            "resource_packs/*/animations/*.json",
            "*resource*pack*/animations/*.json",
            "*Resource*Pack*/animations/*.json",
            "*RP*/animations/*.json",
            "*rp*/animations/*.json",
            "*.animation.rp.json",
            "*.anim.rp.json",
            "*.a.rp.json",
            "*.rpa.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/animations/actor_animation.json"
        },
        {
          description = "Minecraft基岩版附着物",
          fileMatch = {
            "attachables/*.json",
            "*.attachable.json",
            "*.attach.json",
            "*.at.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/attachables/attachables.json"
        },
        {
          description = "Minecraft基岩版客户端生物群系",
          fileMatch = { "biomes_client.json", "biomes_client.jsonc", "biomes_client.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/biomes_client.json"
        },
        {
          description = "Minecraft基岩版资源包方块",
          fileMatch = { "blocks.json", "blocks.jsonc", "blocks.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/blocks.json"
        },
        {
          description = "Minecraft基岩版客户端实体",
          fileMatch = {
            "entity/*.json",
            "*.entity.rp.json",
            "*.e.rp.json",
            "*.ce.json",
            "*.rpe.json",
            "*.entity.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/entity/entity.json"
        },
        {
          description = "Minecraft基岩版迷雾",
          fileMatch = {
            "fogs/*.json",
            "*.fog.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/fog/fog.json"
        },
        {
          description = "Minecraft基岩版翻书动画纹理",
          fileMatch = { "flipbook_textures.json", "flipbook_textures.jsonc", "flipbook_textures.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/textures/flipbook_textures.json"
        },
        {
          description = "Minecraft基岩版物品纹理",
          fileMatch = { "item_texture.json", "item_texture.jsonc", "item_texture.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/textures/item_texture.json"
        },
        {
          description = "Minecraft基岩版纹理列表",
          fileMatch = { "texture_list.json", "texture_list.jsonc", "texture_list.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/textures/texture_list.json"
        },
        {
          description = "Minecraft基岩版资源包物品",
          fileMatch = {
            "resource_packs/*/items/*.json",
            "*resource*pack*/items/*.json",
            "*RP*/items/*.json",
            "*.item.rp.json",
            "*.i.rp.json",
            "*.rpi.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/items/items.json"
        },
        {
          description = "Minecraft基岩版实体模型",
          fileMatch = {
            "models/entity/*.json",
            "*.geo.json",
            "*.geometry.json",
            "*.model.json",
            "*.g.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/models/entity/model_entity.json"
        },
        {
          description = "Minecraft基岩版材质",
          fileMatch = { "materials/*.material" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/materials/materials.json"
        },
        {
          description = "Minecraft基岩版音乐定义",
          fileMatch = { "music_definitions.json" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/sounds/music_definitions.json"
        },
        {
          description = "Minecraft基岩版粒子",
          fileMatch = {
            "particles/*.json",
            "*.particle.json",
            "*.p.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/particles/particles.json"
        },
        {
          description = "Minecraft基岩版渲染控制器",
          fileMatch = {
            "render_controllers/*.json",
            "*.render.json",
            "*.render_controller.json",
            "*.rc.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/render_controllers/render_controllers.json"
        },
        {
          description = "Minecraft基岩版音效定义",
          fileMatch = { "sound_definitions.json", "sound_definitions.jsonc", "sound_definitions.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/sounds/sound_definitions.json"
        },
        {
          description = "Minecraft基岩版音效",
          fileMatch = { "sounds.json", "sounds.jsonc", "sounds.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/sounds.json"
        },
        {
          description = "Minecraft基岩版地形纹理",
          fileMatch = { "terrain_texture.json", "terrain_texture.jsonc", "terrain_texture.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/textures/terrain_texture.json"
        },
        
        -- 行为包架构
        {
          description = "Minecraft基岩版行为包动画控制器",
          fileMatch = {
            "behavior_packs/*/animation_controllers/*.json",
            "*behavior*pack*/animation_controllers/*.json",
            "*Behavior*Pack*/animation_controllers/*.json",
            "*BP*/animation_controllers/*.json",
            "*bp*/animation_controllers/*.json",
            "*.animation_controller.bp.json",
            "*.bpac.json",
            "*.ac.bp.json",
            "*.bp_ac.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/animation_controllers/animation_controller.json"
        },
        {
          description = "Minecraft基岩版行为包动画",
          fileMatch = {
            "behavior_packs/*/animations/*.json",
            "*behavior*pack*/animations/*.json",
            "*BP*/animations/*.json",
            "*.animation.bp.json",
            "*.anim.bp.json",
            "*.a.bp.json",
            "*.bpa.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/animations/animations.json"
        },
        {
          description = "Minecraft基岩版生物群系",
          fileMatch = {
            "behavior_packs/*/biomes/*.json",
            "*behavior*pack*/biomes/*.json",
            "*BP*/biomes/*.json",
            "*.biome.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/biomes/biomes.json"
        },
        {
          description = "Minecraft基岩版对话",
          fileMatch = {
            "behavior_packs/*/dialogue/*.json",
            "*behavior*pack*/dialogue/*.json",
            "*BP*/dialogue/*.json",
            "*.diag.json",
            "*.dialogue.json",
            "*.dialog.json",
            "*.d.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/dialogue/dialogue.json"
        },
        {
          description = "Minecraft基岩版函数刻",
          fileMatch = { "functions/tick.json", "functions/tick.jsonc", "functions/tick.json5" },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/functions/tick.json"
        },
        {
          description = "Minecraft基岩版战利品表",
          fileMatch = {
            "behavior_packs/*/loot_tables/*.json",
            "*behavior*pack*/loot_tables/*.json",
            "*BP*/loot_tables/*.json",
            "*.loot.json",
            "*.loot_table.json",
            "*.lt.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/loot_tables/loot_tables.json"
        },
        {
          description = "Minecraft基岩版行为包方块",
          fileMatch = {
            "behavior_packs/*/blocks/*.json",
            "*behavior*pack*/blocks/*.json",
            "*BP*/blocks/*.json",
            "*.block.json",
            "*.b.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/blocks/blocks.json"
        },
        {
          description = "Minecraft基岩版行为包实体",
          fileMatch = {
            "behavior_packs/*/entities/*.json",
            "*behavior*pack*/entities/*.json",
            "*BP*/entities/*.json",
            "*.entity.bp.json",
            "*.e.bp.json",
            "*.se.json",
            "*.bpe.json",
            "*.behavior.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/entities/entities.json"
        },
        {
          description = "Minecraft基岩版地物",
          fileMatch = {
            "behavior_packs/*/features/*.json",
            "*behavior*pack*/features/*.json",
            "*BP*/features/*.json",
            "*.feature.json",
            "*.f.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/features/features.json"
        },
        {
          description = "Minecraft基岩版地物规则",
          fileMatch = {
            "behavior_packs/*/feature_rules/*.json",
            "*behavior*pack*/feature_rules/*.json",
            "*BP*/feature_rules/*.json",
            "*.feature_rule.json",
            "*.fr.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/feature_rules/feature_rules.json"
        },
        {
          description = "Minecraft基岩版行为包物品",
          fileMatch = {
            "behavior_packs/*/items/*.json",
            "*behavior*pack*/items/*.json",
            "*BP*/items/*.json",
            "*.item.bp.json",
            "*.i.bp.json",
            "*.bpi.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/items/items.json"
        },
        {
          description = "Minecraft基岩版配方",
          fileMatch = {
            "recipes/*.json",
            "*.recipe.json",
            "*.crafting_recipe.json",
            "*.cr.json",
            "*.r.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/recipes/recipes.json"
        },
        {
          description = "Minecraft基岩版生成规则",
          fileMatch = {
            "spawn_rules/*.json",
            "*.spawn.json",
            "*.sr.json",
            "*.spawn_rule.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/spawn_rules/spawn_rules.json"
        },
        {
          description = "Minecraft基岩版交易",
          fileMatch = {
            "behavior_packs/*/trading/*.json",
            "*behavior*pack*/trading/*.json",
            "*BP*/trading/*.json",
            "*.trade.json",
            "*.trade_table.tt.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/trading/trading.json"
        },
        {
          description = "Minecraft基岩版体积",
          fileMatch = {
            "behavior_packs/*/volumes/*.json",
            "*behavior*pack*/volumes/*.json",
            "*BP*/volumes/*.json",
            "*.volume.json"
          },
          url = "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/volumes/volumes.json"
        }
      }
    }
  }
})
```

### Neovim提示

1. **简化文件模式**：上述示例配置为可读性而简化了文件模式。这些模式处理`.json`文件。如果还需要匹配`.jsonc`或`.json5`文件，可以将这些扩展名添加到fileMatch数组中（例如`"manifest.jsonc"`、`"manifest.json5"`）。

2. **简化配置**：如果仅使用特定文件类型，可以将架构列表缩减为仅包含需要的架构。

3. **与lazy.nvim一起使用**：如果使用lazy.nvim，可以在LSP插件设置中添加此配置：

```lua
{
  'neovim/nvim-lspconfig',
  config = function()
    require('lspconfig').jsonls.setup({
      -- 此处放置架构配置
    })
  end
}
```

4. **文件模式匹配**：`fileMatch`模式支持glob模式。如果文件命名约定不同，相应调整模式。

---

## Visual Studio Code

Visual Studio Code是这些架构的主要支持编辑器。

### 设置

1. 从仓库根目录复制`vscode-settings.json`文件到项目的`.vscode`文件夹
2. 将其重命名为`settings.json`

也可以使用本指南文件夹中提供的[示例文件](vscode-settings.example.json)。

**或者**

1. 将`vscode-settings.json`的内容复制到`.code-workspace`文件的`settings`属性中：

```json
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "json.schemas": [
      
    ]
  }
}
```

**注意**：将上面的空`json.schemas`数组替换为`vscode-settings.json`文件中的完整数组。该数组应包含所有架构定义（每个都有`fileMatch`和`url`属性）。

架构将自动应用到工作区中的匹配文件。

---

## JetBrains IDE

JetBrains IDE（IntelliJ IDEA、WebStorm、PyCharm等）通过其内置JSON架构支持支持JSON架构。

### 设置

1. 打开**Settings/Preferences** → **Languages & Frameworks** → **Schemas and DTDs** → **JSON Schema Mappings**
2. 点击**+**按钮添加新的架构映射
3. 对于要使用的每个架构：
   - **名称**：提供描述性名称（例如"Minecraft基岩版清单"）
   - **架构文件或URL**：输入原始GitHub URL（例如`https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/manifest.json`）
   - **架构版本**：选择"JSON架构版本7"（或最新版本）
   - **文件路径模式**：添加应使用此架构的文件模式（例如`manifest.json`）

### 常见架构映射

以下是一些可能想添加的常见映射：

- **清单文件**：`https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/manifest.json`
  - 模式：`manifest.json`
  
- **实体文件（行为包）**：`https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/entities/entities.json`
  - 模式：`behavior_packs/*/entities/*.json`或`*.entity.bp.json`
  
- **实体文件（资源包）**：`https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/resource/entity/entity.json`
  - 模式：`resource_packs/*/entity/*.json`或`*.entity.rp.json`

---

## Sublime Text

Sublime Text通过LSP包支持JSON架构。

### 前置条件

- 安装[Package Control](https://packagecontrol.io/installation)
- 安装[LSP包](https://packagecontrol.io/packages/LSP)
- 安装[LSP-json](https://packagecontrol.io/packages/LSP-json)

### 设置

1. 打开**Preferences** → **Package Settings** → **LSP** → **Settings**
2. 添加以下内容到LSP设置中：

```json
{
  "clients": {
    "LSP-json": {
      "enabled": true,
      "settings": {
        "json": {
          "schemas": [
            {
              "fileMatch": ["manifest.json"],
              "url": "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/general/manifest.json"
            },
            {
              "fileMatch": ["behavior_packs/*/entities/*.json", "*.entity.bp.json"],
              "url": "https://raw.githubusercontent.com/Blockception/Minecraft-bedrock-json-schemas/main/behavior/entities/entities.json"
            }
          ]
        }
      }
    }
  }
}
```

注意：根据需要向`schemas`数组添加更多架构对象，遵循与上述示例相同的模式。

---

## 额外资源

- [主仓库](https://github.com/Blockception/Minecraft-bedrock-json-schemas)
- [贡献指南](https://github.com/Blockception/Minecraft-bedrock-json-schemas/blob/main/CONTRIBUTING.md)
- [VS Code设置示例](https://github.com/Blockception/Minecraft-bedrock-json-schemas/tree/main/docs/guide/vscode-settings.example.json)
- [VS Code设置（仓库根目录）](https://github.com/Blockception/Minecraft-bedrock-json-schemas/blob/main/vscode-settings.json)

有关所有可用架构及其URL的完整列表，请参阅仓库根目录中的[vscode-settings.json](https://github.com/Blockception/Minecraft-bedrock-json-schemas/blob/main/vscode-settings.json)文件或本文件夹中的[示例文件](https://github.com/Blockception/Minecraft-bedrock-json-schemas/tree/main/docs/guide/vscode-settings.example.json)。

---

## 故障排除

### 架构未加载

- 验证架构URL是否可访问（检查GitHub是否可到达）
- 确保文件模式与实际文件名匹配
- 检查编辑器的开发者控制台/日志中是否有错误

### 自动完成不工作

- 确保语言服务器正确运行
- 验证文件被识别为JSON（检查文件类型/语言模式）
- 尝试重新启动编辑器或语言服务器

### 架构验证错误

- 确保为文件类型使用了正确的架构
- 检查JSON是否有效（使用JSON验证器）
- 验证使用的是兼容的Minecraft基岩版格式版本
