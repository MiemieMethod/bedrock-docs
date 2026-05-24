# 项目配置

/// details-info | 来源信息
- 原文仓库：[github.com/Bedrock-OSS/bedrock-wiki](https://github.com/Bedrock-OSS/bedrock-wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///


/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/guide/project-setup](https://wiki.bedrock.dev/guide/project-setup)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

## com.mojang文件夹

`com.mojang`文件夹是Minecraft存储数据（附加包、世界、玩家信息等）的特殊位置。Minecraft能够识别这个路径，所有我们访问或创建的文件都将存放在这个文件夹中！

建议您在桌面或移动设备上创建`com.mojang`文件夹的快捷方式以便快速访问。该文件夹的具体位置因设备操作系统而异。

### Windows

_提示：在搜索栏输入%appdata%可直接跳转至'C:\Users\用户名\AppData\'目录_

`C:\Users\USERNAME\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang`

### Android

Android 11及更早版本：`手机存储 > games > com.mojang`

Android 12及更新版本：`手机存储 > Android > data > com.mojang.minecraftpe > files > games > com.mojang`

### ChromeOS

在访问`com.mojang`文件夹前，需先在Minecraft设置中将`文件存储位置`更改为`外部`：

1. 进入`Minecraft设置`
2. 导航至`设置 > 通用 > 存储`
3. 将`文件存储位置`改为`外部`

设置完成后可通过以下路径访问：
`我的文件 > Play文件 > Android > data > com.mojang.minecraftpe > files > games > com.mojang`

### iOS

`我的设备 > Minecraft > games > com.mojang`

### 开发包

我们将在`development_behavior_packs`和`development_resource_packs`中开发附加包。在这些文件夹中修改内容后，只需_退出并重新进入已应用该包的世界_即可自动重载内容，无需重启Minecraft即可快速测试修改。

`resource_packs`和`behavior_packs`文件夹用于存放稳定版附加包（包括通过`.mcpack`导入的包），开发时可暂时忽略这些目录。

## 您的工作区

/// tip | 提示
Android平台的项目设置与其他平台有所不同，建议参考我们的Android专用指南。
///

[Android指南](./project-setup-android.md){ .md-button .md-button--primary }

/// tip | 提示
本指南中：
- BP指在`development_behavior_packs`中创建的文件夹（行为包）
- RP指在`development_resource_packs`中创建的文件夹（资源包）
///

首先需要在适当位置创建文件夹并建立工作区。_本指南后续步骤默认使用VSCode，您也可以使用其他编辑器。_

现在让我们在VSCode中创建第一个附加包工作区：

1. 打开VSCode（Visual Studio Code代码编辑器）
2. 在`development_resource_packs`中创建名为"`your_pack_name_RP`"的文件夹（以下简称`RP`）
3. 在`development_behavior_packs`中创建名为"`your_pack_name_BP`"的文件夹（以下简称`BP`）
4. 通过`文件 > 将文件夹添加到工作区...`依次添加`BP`和`RP`
5. 使用`文件 > 将工作区另存为...`将工作区文件保存到桌面。后续开发时只需双击打开该工作区文件，即可快速访问BP和RP文件夹

## BP清单文件

/// tip | 提示
本指南中会频繁要求您在特定路径创建指定文件。如果目标文件夹不存在，请先创建！
///

/// warning | 警告
文件名/文件夹名错误是常见问题来源，请仔细核对示例。
///

清单文件（manifest）是Minecraft识别附加包的核心文件。每个包都必须包含一个格式正确的清单文件，这是附加包能被识别的最低要求。

清单文件使用`JSON`格式编写。如需了解JSON格式，请参考[此文档](./understanding-json.md)。

在BP文件夹中右键新建文件，命名为`manifest.json`。初始内容可复制以下代码：

```json title="BP/manifest.json"
{
	"format_version": 2,
	"header": {
		"name": "pack.name",
		"description": "pack.description",
		"uuid": "...",
		"version": [1, 0, 0],
		"min_engine_version": [1, 16, 0]
	},
	"modules": [
		{
			"type": "data",
			"uuid": "...",
			"version": [1, 0, 0]
		}
	]
}
```

### 清单文件解析

- `format_version`指定清单语法版本，推荐使用最新稳定版2
- `name`定义行为包名称，`description`为游戏内显示的描述。使用"代码形式"定义以便后续本地化，详见[文本与翻译](https://wiki.bedrock.dev/concepts/text-and-translations)
- `UUID`字段至关重要，下文将详细说明
- `version`控制附加包版本号。当设备上已安装旧版本时，新版会自动覆盖旧版。若仅在`development_*_packs`中使用且用于私人世界，可不更新版本号
- `min_engine_version`指定兼容的最低Minecraft客户端版本
- `modules`中`type`设为`data`表明这是行为包

### UUID详解

UUID（通用唯一识别码）是Minecraft识别附加包的核心标识，格式示例：`5c830391-0937-44d6-9774-406de66b6984`

**禁止重复使用相同UUID**。您可以通过以下方式生成：
- [在线生成器](https://www.uuidgenerator.net/version4)
- VSCode用户可安装[此扩展](https://marketplace.visualstudio.com/items?itemName=netcorext.uuid-generator)
- 专业工具如_bridge._会自动生成

每个清单文件需要两个不同的UUID，分别填入`header.uuid`和`modules[0].uuid`。正确示例如下：

`"uuid": "5c830391-0937-44d6-9774-406de66b6984"`

## RP清单文件

资源包清单文件格式与行为包相似，主要区别在于`type`需设为`resources`：

```json title="RP/manifest.json"
{
	"format_version": 2,
	"header": {
		"name": "pack.name",
		"description": "pack.description",
		"uuid": "...",
		"version": [1, 0, 0],
		"min_engine_version": [1, 16, 0]
	},
	"modules": [
		{
			"type": "resources",
			"uuid": "...",
			"version": [1, 0, 0]
		}
	]
}
```

## 包图标

包图标是附加包在游戏内的展示图片。建议使用低分辨率正方形图片，或下载以下示例图标：

![包图标](/assets/images/guide/project-setup/pack_icon.png)

[下载图片](/assets/images/guide/project-setup/pack_icon.png){ .md-button }

将图片文件分别放入RP和BP文件夹，并命名为`pack_icon.png`

## 语言文件

最后需要为附加包设置语言支持。需为RP和BP分别创建语言文件，详见[本地化系统](https://wiki.bedrock.dev/concepts/text-and-translations)。

```json title="RP/texts/en_US.lang"
pack.name=Wiki资源包
pack.description=幽灵指南
```

```json title="BP/texts/en_US.lang"
pack.name=Wiki行为包
pack.description=幽灵指南
```

```json title="RP/texts/languages.json"
["en_US"]
```

```json title="BP/texts/languages.json"
["en_US"]
```

## 验证成果

完成上述步骤后，您的附加包应已出现在游戏中！如果未显示，请参考[问题排查指南](./troubleshooting.md)。

![](/assets/images/guide/project-setup/active_pack.png)

## 启用内容日志

/// warning | 警告
内容日志是调试附加包最重要的工具，请务必启用。
///

![](/assets/images/guide/content_log.png)

内容日志是至关重要的调试工具，建议始终保持开启：

1. 在`设置 > 创作者`中启用全部内容日志选项
2. 应用附加包进入世界后，任何错误都会显示在日志中
3. 游戏内按`ctrl+h`或通过创作者设置面板打开日志界面

了解更多内容日志信息请访问[问题排查指南](./troubleshooting.md)。

## 创建测试世界

现在让我们创建测试世界：

1. 点击"**创建新世界**"
2. 确保以下设置：
    ![](/assets/images/guide/project-setup/settings_1.png)
    ![](/assets/images/guide/project-setup/settings_2.png)
3. 激活行为包和资源包（选中后点击'应用'）
4. 点击"**创建**"！

---

## 当前进度

**完成本页面后的项目结构：**

后续指南中将使用简写：
- `com.mojang/development_behavior_packs/guide_RP/`简写为`RP`
- `com.mojang/development_behavior_packs/guide_BP/`简写为`BP`

/// html | div.treeview
- com.mojang/
    - development_resource_packs/
        - guide_RP/
            - {{file|manifest.json}}
            - {{file|pack_icon.png}}
            - texts/
                - {{file|en_US.lang}}
                - {{file|languages.json}}
    - development_behavior_packs/
        - guide_BP/
            - {{file|manifest.json}}
            - {{file|pack_icon.png}}
            - texts/
                - {{file|en_US.lang}}
                - {{file|languages.json}}
///

## 知识总结

/// tip | 已掌握内容：
- com.mojang文件夹的作用与位置
- 工作区设置方法
- manifest.json文件的作用
- UUID的使用规范
- 附加包图标创建
- .lang文件的作用
///

## 进度追踪

-   [x] 完成基础设置
-   [ ] 创建自定义物品
-   [ ] 创建自定义实体
-   [ ] 配置实体战利品、生成规则与合成配方