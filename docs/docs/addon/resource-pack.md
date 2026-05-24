# 资源包

**资源包（Resource Pack）**是附加包的一种类型，负责定义Minecraft基岩版游戏的视觉和听觉表现。资源包属于客户端内容，在客户端加载和渲染，不影响游戏的逻辑行为。

## 概述

资源包可以修改或替换游戏中的纹理、模型、动画、音效、粒子特效、用户界面、字体等几乎所有客户端资源。通过资源包，开发者可以创建全新的视觉风格，也可以对原版素材进行局部调整。

资源包的清单文件中，模块类型应设置为`resources`。一个资源包可以独立使用，也可以与一个或多个行为包配合使用。

## 目录结构

一个典型的资源包的文件结构如下：

/// html | div.treeview
- {{file|manifest.json}}：清单文件。
- {{file|contents.json}}：内容文件，列出包内所有资源文件的校验信息。
- {{file|pack_icon.png}}：包图标。
- {{file|json}}**loading_messages.json**：加载消息。
- {{file|json}}**splashes.json**：闪烁标语。
- {{file|json}}**sounds.json**：音效事件映射。
- {{file|json}}**blocks.json**：方块渲染信息（旧版兼容）。
- {{file|folder}}**animation_controllers/**：动画控制器文件。
- {{file|folder}}**animations/**：动画文件。
- {{file|folder}}**atmospherics/**：大气设置文件。
- {{file|folder}}**attachables/**：附着物定义文件。
- {{file|folder}}**biomes/**：客户端生物群系定义文件（`minecraft:client_biome`格式）。
- {{file|folder}}**block_culling/**：自定义方块面剔除规则。
- {{file|folder}}**color_grading/**：色彩分级设置文件。
- {{file|folder}}**entity/**：客户端实体定义文件。
- {{file|folder}}**fogs/**：迷雾定义文件。
- {{file|folder}}**font/**：字体文件。
    - {{file|json}}**emoticons.json**：表情符号映射。
    - {{file|json}}**font_metadata.json**：字体元数据。
    - `*.png`：位图字体纹理。
    - `*.ttf`：TrueType字体文件。
- {{file|folder}}**lighting/**：全局照明设置文件。
- {{file|folder}}**materials/**：材质文件。
- {{file|folder}}**models/**：模型文件。
    - {{file|folder}}**entity/**：实体模型。
    - {{file|folder}}**blocks/**：方块模型。
- {{file|folder}}**particles/**：粒子特效定义文件。
- {{file|folder}}**pbr/**：PBR（基于物理的渲染）回退设置。
    - {{file|json}}**global.json**：全局PBR回退配置。
- {{file|folder}}**render_controllers/**：渲染控制器文件。
- {{file|folder}}**shadows/**：阴影设置。
    - {{file|json}}**global.json**：全局阴影配置。
- {{file|folder}}**sounds/**：音效文件（`.ogg`、`.wav`、`.fsb`）。
    - {{file|json}}**sound_definitions.json**：音效定义。
    - {{file|json}}**music_definitions.json**：音乐定义。
- {{file|folder}}**texts/**：本地化文件。
    - `*.lang`：各语言翻译文件。
    - {{file|json}}**languages.json**：支持的语言列表。
    - {{file|json}}**language_names.json**：语言显示名称映射。
    - {{file|folder}}**\*/**：各语言字体目录（含`font/*.png`）。
- {{file|folder}}**textures/**：纹理文件。
    - {{file|folder}}**blocks/**：方块纹理。
    - {{file|folder}}**entity/**：实体纹理。
    - {{file|folder}}**environment/**：环境纹理。
        - {{file|folder}}**overworld_cubemap/**：主世界天空盒立方体贴图（`cubemap_0`—`cubemap_5`）。
    - {{file|folder}}**items/**：物品纹理。
    - {{file|folder}}**particle/**：粒子纹理。
    - {{file|json}}**flipbook_textures.json**：翻书动画纹理列表。
    - {{file|json}}**item_texture.json**：物品纹理映射（物品图集）。
    - {{file|json}}**terrain_texture.json**：方块纹理映射（地形图集）。
    - {{file|json}}**textures_list.json**：纹理预加载列表，用于提前加载自定义纹理。
- {{file|folder}}**ui/**：JSON UI文件。
    - {{file|json}}**_ui_defs.json**：需要加载的UI屏幕文件列表。
    - {{file|json}}**_global_variables.json**：JSON UI全局变量。
    - `*.json`：具体屏幕与控件定义文件。
- {{file|folder}}**water/**：水体渲染设置文件。
///

## 资源覆盖

资源包通过**资源栈（Resource Stack）**机制实现叠加。排列在栈顶的资源包具有最高优先级。当多个资源包定义了同名的资源文件时，栈顶资源包的文件会覆盖下方资源包的文件。这种机制允许开发者只修改需要更改的文件，而无需重新创建完整的资源包。

## 全局与世界作用域

资源包可以作为**全局资源包**应用于所有世界，也可以作为**世界资源包**仅应用于特定世界。全局资源包在游戏主菜单的设置中管理，世界资源包在各个世界的设置中管理。

清单文件中的`pack_scope`字段可以限制资源包的可用作用域：

- `world`：仅可作为世界资源包使用。
- `global`：仅可作为全局资源包使用。
- `any`：两种作用域均可使用（默认）。
