# 附加包系列教程

欢迎来到附加包教程。这个系列会带你从一个空文件夹出发，逐步做出能导入、能调试、能发布的Minecraft基岩版附加包。你不需要一次读完所有页面；建议先完成“认识附加包”“制作纹理包”“数据驱动”三部分，再按自己要做的内容选择实体、方块、物品、世界生成等专题。

## 你会做出什么

在这个系列中，我们会反复使用一组简单的示例命名：命名空间使用`demo`，资源包文件夹使用`demo_RP`，行为包文件夹使用`demo_BP`。你可以换成自己的项目名，但请保持同一个附加包中所有标识符、文件路径和本地化键一致。

完整的附加包通常由这些部分组成：

/// html | div.treeview
- `demo_BP`
    - `manifest.json`
    - `blocks`
    - `entities`
    - `features`
    - `feature_rules`
    - `functions`
    - `items`
    - `loot_tables`
    - `recipes`
    - `structures`
    - `texts`
- `demo_RP`
    - `manifest.json`
    - `animations`
    - `animation_controllers`
    - `attachables`
    - `entity`
    - `fogs`
    - `models`
    - `particles`
    - `render_controllers`
    - `sounds`
    - `texts`
    - `textures`
    - `ui`
///

不是每个项目都需要所有文件夹。官方资料明确指出，资源包和行为包中唯一共同必需的文件是`manifest.json`；其他目录只在你使用对应功能时创建。

## 先准备环境

建议在Windows版Minecraft基岩版上学习本系列，因为桌面版更方便查看`com.mojang`目录、编辑文件和导入导出世界。各平台的路径如下：

/// tab | Windows
```text
%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang
```
在Windows资源管理器地址栏或运行框（++win+r++）中直接粘贴这段路径即可跳转。
///
/// tab | Android 11及更早版本
```text
手机存储/games/com.mojang
```
///
/// tab | Android 12及更新版本
```text
手机存储/Android/data/com.mojang.minecraftpe/files/games/com.mojang
```
Android 12以上系统对`Android/data`目录有访问限制，可能需要借助支持访问该目录的文件管理器（如X-Plore）。
///
/// tab | iOS
```text
我的设备/Minecraft/games/com.mojang
```
///

其中最常用的目录如下：

| 目录 | 用途 |
|---|---|
| `development_resource_packs` | 放正在开发的资源包。 |
| `development_behavior_packs` | 放正在开发的行为包。 |
| `minecraftWorlds` | 存放已创建的世界。 |
| `world_templates` | 存放已导入的世界模板。 |
| `skin_packs` | 存放已导入的皮肤包。 |

推荐准备这些工具：

- Visual Studio Code：编辑JSON、Molang、函数和语言文件。
- Blockbench：制作模型、纹理和动画。
- Snowstorm：制作粒子特效。
- Audacity或其他音频工具：导出OGG声音文件。
- 一个UUID生成器：给每个清单文件生成不会冲突的UUID。

/// warning | 不要共用UUID
`manifest.json`的`header.uuid`和每个`modules[].uuid`都应当不同。行为包依赖资源包时，行为包`dependencies`中填写的是资源包`header.uuid`，不是资源包模块UUID。
///

## 建议的学习顺序

1. 先读[认识附加包](understanding-addons.md)，弄清资源包、行为包、清单文件和导入目录。
2. 完成[制作纹理包](creating-texture-packs.md)，确认游戏能加载你的资源包。
3. 学习[本地化](localization.md)，把游戏内显示名称从硬编码改成语言键。
4. 进入[数据驱动](data-driven/index.md)，开始创建实体、方块、物品、配方和世界生成内容。
5. 学习[JSON UI进阶技巧](json-ui/index.md)，掌握HUD改造、绑定技巧和界面兼容实践。<!-- md:flag vanilla -->
6. 最后学习函数、世界模板、皮肤包和结构包，让附加包更适合发布或复用。

遇到问题时，参考[附加包故障排除](troubleshooting.md)。

## 调试习惯

每次修改后，都请按下面的顺序检查：

1. JSON能否被编辑器正确解析。
2. 文件夹名称是否与游戏约定完全一致，例如`functions`不能写成`function`。
3. 标识符是否都带命名空间，例如`demo:coin`。
4. 世界是否同时激活了资源包和行为包。
5. 内容日志中是否出现路径、格式版本或组件名称错误。

部分内容支持`/reload`重新加载，例如函数通常可以直接重载；脚本和数据驱动定义的热重载能力会随版本、模块和内容类型变化。纹理、模型和声音通常需要退出世界后重新进入才能可靠看到变化。

## 打包发布

开发时使用文件夹最方便；发布时可以把资源包或行为包根目录中的文件选中后压缩，再把扩展名改为`.mcpack`。如果同时发布资源包和行为包，可以把两个`.mcpack`再打包成`.mcaddon`。世界模板则使用`.mctemplate`。压缩时不要把外层文件夹本身压进去，否则Minecraft可能找不到根目录下的`manifest.json`。
