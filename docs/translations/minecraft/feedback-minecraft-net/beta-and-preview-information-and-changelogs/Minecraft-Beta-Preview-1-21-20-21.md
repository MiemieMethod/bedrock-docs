---
title: Minecraft Beta & Preview - 1.21.20.21
date: 2024-06-27T09:55:37Z
updated: 2024-06-27T16:15:11Z
categories: Beta和Preview信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/27935763028237-Minecraft-Beta-Preview-1-21-20-21
hash:
  h_01J1D6N39S0VSPTCF8M0KPDW0C: notethis-weeks-update-may-may-be-delayed-on-windows-1011-we-apologize-for-the-inconvenience-and-are-working-to-resolve-the-issue
  h_01J1CNFD7YA1FG1FTC8K6AADRB: features-and-bug-fixes
  h_01J1CNFD7Y8P6Z07QAHHGME0M1: banners
  h_01J1CNFD7YM8W3XKZSEW2NFCWD: blocks
  h_01J1CNFD7YXEEXQKGTHCMKADDQ: gameplay
  h_01J1CNFD7YF43766WMZBY50DF6: realms
  h_01J1CNFD7Y59M3KER2XSBS5DP3: updated-realms-tab
  h_01J1CNFD7Y0D9G9XY9WXPFR8DR: sound
  h_01J1CNFD7Y4HJ0JARAXH1VTN6P: music
  h_01J1CNFD7YGK9ZTCRX2PRZBTWZ: structure-block
  h_01J1CNFD7YEERKTD1GV131A6T6: user-interface
  h_01J1CNFD7YDS90J4YH1XMBH5XV: vanilla-parity
  h_01J1CNFD7Y0HDMDFKNSMZ8ZSV3: technical-updates
  h_01J1CNFD7YFEZCJVEBCJG0N7F6: add-ons-and-script-engine
  h_01J1CNFD7Y3XEM3B3NXGHZBZ9H: ai-goals
  h_01J1CNFD7YFFYKG6ZN17FZAH1D: api
  h_01J1CNFD7Y96CC3YAA2YC7ANKE: blocks-1
  h_01J1CNFD7YDX21WY2NQ87R3930: editor
  h_01J1CNFD7Z8T7VVP03QSXH073D: general
  h_01J1CNFD7Z1WE2A3SEV1Y3TK2A: graphical
  h_01J1CNFD7ZXKVQYGJTK7JHMMXS: technical-experimental-features
  h_01J1CNFD7ZCGXD49VMKQF7YMVG: api-1
  h_01J1CNFD7ZEW50GJDPNMW5QWQ0: graphical-1
  h_01J1CNFD7ZJEYE733F21B1PQK0: blocks-2
---

**发布于：**2024年6月27日

### **注意：**本周的更新可能会在Windows 10/11上延迟。对于由此带来的不便，我们深表歉意，并正在努力解决该问题。

**Minecraft Preview和Beta的信息：**

- 这些正在开发中的版本可能不稳定，且可能不代表最终版本的质量
- Minecraft Preview可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版可在Android（Google Play）上获取。要加入或退出Beta，请参阅[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)了解详细说明

![背景中有冰原的Minecraft村庄](https://feedback.minecraft.net/hc/article_attachments/27935763024781)

亲爱的读者，大家好！本周，我们开始了1.21.20.21的Beta和Preview版本，我们知道许多紧密关注更新版本的玩家将期待零售更新的到来。然而，经过慎重考虑，我们决定跳过1.21.10更新。相反，我们将专注于1.21.20，以优先提升质量和稳定性。但请不要担心——最近Beta和Preview中的所有调整不会丢失！它们也将包含在1.21.20中，我们将像处理1.21.1一样，在热修复中评估和解决关键漏洞。感谢您的耐心和理解，并请继续向我们发送您的反馈和漏洞报告。我们非常感谢您的意见！

以下是本周的新内容列表：

# 功能和漏洞修复

## 旗帜

- 镜像了骷髅、Vex和流动旗帜纹理的背面 ([MCPE-179894](https://bugs.mojang.com/browse/MCPE-179894))

## 方块

- 修复了石英台阶纹理的问题 ([MCPE-182604](https://bugs.mojang.com/browse/MCPE-182604))
- 旨在针对所有方块变体的纹理覆盖现在不再仅覆盖默认变体
- "light_block"方块现分为独特的实例："light_block_0"，"light_block_1"，"light_block_2"，"light_block_3"，"light_block_4"，"light_block_5"，"light_block_6"，"light_block_7"，"light_block_8"，"light_block_9"，"light_block_10"，"light_block_11"，"light_block_12"，"light_block_13"，"light_block_14"和"light_block_15"
- "minecraft:yellow_flower"方块已重命名为"minecraft:dandelion"，旧名称在命令和数据中仍然可识别
- "sandstone"方块现分为独特的实例"sandstone"，"chiseled_sandstone"，"cut_sandstone"和"smooth_sandstone"
  - "smooth_sandstone"的破坏时间从0.8变为2.0，爆炸抗性从0.8变为6.0

## 游戏玩法

- 修复了试炼刷怪笼在旧世界中不掉落战利品的问题 ([MCPE-182758](https://bugs.mojang.com/browse/MCPE-182758))
- 由不祥试炼刷怪笼生成的生物现在会掉落它们捡起的物品 ([MCPE-182630](https://bugs.mojang.com/browse/MCPE-182630))
- 区域效果云在被对效果免疫的实体进入时不再缩小
- 修复了一个配方漏洞，其中"chiseled_sandstone"和"cut_sandstone"砂岩变体可以在熔炉中用于制作"smooth_sandstone"。现在只能接受普通的"sandstone"，不能使用其他类型的砂岩
- 修复了涉及"red_sandstone_slab"作为成分或结果物品的原版配方，它们会错误地使用"red_sandstone"
  - 现在可以使用3个水平"red_sandstone:0"再次制作"red_sandstone_slab"
  - 现在可以使用3个水平"red_sandstone:1"再次制作"red_sandstone_slab"
  - 现在可以使用2个垂直"red_sandstone_slab"再次制作"red_sandstone:1"
- 修复了当Breeze在攻击时位于屋顶下的方块中时可能卡在一个地方的错误
- 玩家投掷的风弹不再有机会每击中造成超过1点伤害
- 跳跃不再覆盖之前较大的向上速度，因此不会在风爆爆炸和跳跃同时发生时取消动量
- 使用带有激流附魔的三叉戟现在正确取消了来自风弹的坠落伤害减少
- 修复了风弹的坠落伤害保护错误地在第二次着陆时防止坠落伤害的错误

## Realms

- 如果拥有者在应用多个附加包的情况下进入并退出Realms设置屏幕后，玩家将不再被从Realm中踢出
- 阅读完故事的第一页后，从Realms Stories故事反馈标签中导航离开将移除未读故事徽章，因为用户已查看了最近的帖子
- 修复了新Realm事件在第一次打开故事反馈时无法正确显示的错误
- 修复了在取消加入最近认领的Preview Realm的过程中将玩家锁定在无限循环中的错误

## 更新的Realms标签

我们引入了全新的Realms标签。它位于新游戏屏幕中，但不幸的是，通过这种方式实际加入Realm存在问题！（抱歉！）您将不得不切换到旧的用户界面以在Preview中加入Realms——我们希望尽快解决此问题。

以下是您在接下来的几个Preview中可以期待的内容：

- Realms列表：轻松查看您拥有或已加入的所有Realms
- 开始游戏：直接从此屏幕启动您的Realm
- 在线玩家计数：查看每个Realm当前在线的玩家数量
- Realm管理：通过编辑世界和管理订阅来控制您拥有的Realms
- 添加或加入Realms：通过添加或加入来探索新的Realms
- Realm故事：查看Realm故事

我们将在未来的版本中继续改进Realms标签。请通过[aka.ms/realmstabfeedback](https://aka.ms/realmstabfeedback)向我们发送您的反馈

## 声音

- 合成器的制作和失败声音现在具有随机音调偏移
- 合成器失败声音的最大距离现在为3个方块，而不是5个
- 铜灯的破坏、放置和击打声音现在音调不同
- 铜格栅的破坏、放置和击打声音现在音调不同
- 铜格栅的踏步声音音量较低
- 铜门的“开启”声音现在音调不同
- 不祥试炼刷怪笼的破坏和放置声音现在音调不同
- 宝库的破坏和放置声音现在音调不同
- 凝灰岩、凝灰岩砖和磨制凝灰岩方块的破坏、放置和击打声音现在音调不同

## 音乐

- "Echo in the Wind"现在在繁茂洞穴生物群系中播放 ([MCPE-182278](https://bugs.mojang.com/browse/MCPE-182278))
- "5"，"Otherside"，"Relic"，"Creator"，"Creator (Music Box)"和"Precipice"现在分配给唱片机/记音块滑块 ([MCPE-169933](https://bugs.mojang.com/browse/MCPE-169933))

## 结构方块

- 修复了在保存并退出存档时玩家ID未保存到结构方块的问题 ([MCPE-149183](https://bugs.mojang.com/browse/MCPE-149183))
- 从1.21.20版本开始，通过结构方块加载的驯服生物将始终使用原始拥有者的玩家ID

## 用户界面

- 在穿戴海龟头盔时，水下呼吸效果图标和计时器不再闪烁 ([MCPE-142173](https://bugs.mojang.com/browse/MCPE-142173))
- 启用了新的床屏幕版本。用户可以通过设置-视频标签下的功能切换选择加入或退出。（仅限Preview）

## 原版趋同

- 自然生成的蘑菇柄在被采矿时不再掉落蘑菇 ([MCPE-71123](https://bugs.mojang.com/browse/MCPE-71123))
- 棕色和红色蘑菇方块的蘑菇掉落几率（最多2个）已增加至与Java版匹配，从每个蘑菇10%提高到11.11%
- 河豚现在在食用时给予反胃I效果，而不是反胃II ([MCPE-98458](https://bugs.mojang.com/browse/MCPE-98458))
- 僵尸疣猪兽在追逐玩家或生物时现在会发出愤怒的声音 ([MCPE-95523](https://bugs.mojang.com/browse/MCPE-95523))
- 蜜蜂在水下后1秒开始受到窒息伤害 ([MCPE-114688](https://bugs.mojang.com/browse/MCPE-114688))
- 在切石机中使用氧化切制铜块进行合成现在产出两个台阶而不是一个 ([MCPE-136077](https://bugs.mojang.com/browse/MCPE-136077))
- 从石英方块合成石英砖现在产出4个石英砖而不是1个 ([MCPE-69281](https://bugs.mojang.com/browse/MCPE-69281))

# 技术更新

## 附加包和脚本引擎

- 修复了一个错误，该错误使得在专用服务器上应用附加包时，强制玩家下载所有应用于该服务器的资源包才能加入。注意：如果由于此问题下载了不需要的包，您可能需要从设备上本地删除它们，以避免在加入世界时应用这些包 ([MCPE-180344](https://bugs.mojang.com/browse/MCPE-180344))
- 更新了"minecraft:geometry"方块组件以验证几何体是否适合30/16单位的边界，并且在每个轴上至少有1/16的长度位于单位立方体内。此验证适用于使用1.21.0或更高版本json的所有方块上的所有几何组件 ([MCPE-178607](https://bugs.mojang.com/browse/MCPE-178607))

## AI意向

- 公开了"minecraft:behavior.swim_up_for_breath" AI意向组件，该组件允许生物在即将耗尽可呼吸气体时尝试移动到可以呼吸空气的位置。在原版中，这由海豚使用。任何在1.21.20或更高版本基于原版海豚构建的自定义内容将需要手动添加此组件以启用此AI行为。

## API

- EntityLeashableComponent
  - 将类*EntityLeashableComponent*从beta移至*1.13.0*

## 方块

- "infested_stone"及其衍生方块现在定义了它们的方块声音 ([MCPE-182290](https://bugs.mojang.com/browse/MCPE-182290))

## 编辑器

编辑器及其相应的API处于早期开发阶段，并可在Windows PC Bedrock Preview版本上通过键盘/鼠标使用。在社交平台上使用**#BedrockEditor**标签与我们互动。

了解[如何使用](https://aka.ms/LearnEditor)编辑器，加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)论坛与团队交流，并通过[starter kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit)和[samples](https://github.com/Mojang/minecraft-editor-extension-samples)开始构建扩展。

本周更新：

- 添加了设置面板以修改延迟光照的环境、全局光照和色彩分级设置（需要延迟光照资源包并启用设置）
  - 已知问题：UI元素会产生阴影。可以通过CTRL+TAB切换十字准星模式作为解决方法
  - 已知问题：启用延迟光照时，粘贴预览（CTRL+SHIFT+V）无法正常渲染

  ![editorPicture1.png](https://feedback.minecraft.net/hc/article_attachments/27938232806029)

- 添加了*Input Mappings*动作栏项，该项打开一个模态窗口，显示所有可用的键绑定和输入上下文。
  - 可以使用快捷字段重新配置键绑定，该字段检测按键输入以设置绑定。待定更改将在保存或清除前高亮显示文本。关闭模态窗口将恢复任何待定更改。
  - 右键点击选定的快捷字段将清除绑定，或者可以使用字段旁边的清除按钮。
  - 添加了一个用于独占（API中的*None*）键动作的切换，以支持高级输入场景。
  - 通过点击绑定、活动上下文和所有修改绑定的恢复按钮，可以恢复已修改的绑定。
  - 保存的绑定可跨不同编辑器项目访问。

  ![editorPicture2.png](https://feedback.minecraft.net/hc/article_attachments/27938262668685)

- 扩展了游戏选项，包括更多的导出选项以及应用选项以导出存档数据
- 为键绑定注册API函数添加了可选的*KeyBindingInfo*参数，以分配附加信息给快捷方式
- 为Property Pane API添加了新的*BlockList* UI元素
- 为*ModalToolCreationParameters* API添加了*inputContextId*和*inputContextLabel*可选属性，以代表用户定义的模态工具标识符
- 添加了接口*KeyBinding*并修改了键绑定注册API方法以使用该对象
- 当下拉菜单超出窗口边界时，将尝试向相反方向打开
- 为*IPropertyItemOptionsColorPicker* API添加了*variant: ColorPickerVariant*可选属性，以支持不同类型的色彩选择器属性项。将默认变种更改为符合面板布局。将*Default*和*Inline*变种的渐变选择器移动到弹出窗口，可通过点击选定的颜色框访问
- 更新了编辑器选择器中出现的实体集合
- 更新了编辑器选择器中出现的方块集合
- 引入了新的过滤器"is_navigating"，用于检查实体当前是否在路径查找中。这需要一个"minecraft:navigation"组件

## 通用

- 更新了滤镜组的架构文档

## 图形

- 资源包中的2通道纹理现在得到适当支持。加载时，它们将始终使用第一个通道表示所有三个颜色通道，第二个通道用于透明度（例如，正常纹理为*(R, G, B, A)*，而2通道纹理将始终被视为*(R, R, R, A)*）
- 修复了数据驱动方块的剔除规则未随变换组件旋转的错误

# 技术实验性功能

## API

- EntityBreathableComponent
  - 在beta中将函数*setAirSupply(value: number): void*更改为属性*airSupply: number*
  - 在beta中添加了只读属性*canBreathe: boolean*
- 在*1.14.0 beta*中添加了*isHardcore*

## 图形

- 延迟技术预览中现在支持自定义天盒 ([MCPE-174200](https://bugs.mojang.com/browse/MCPE-174200))
- 修复了启用延迟技术预览时，生成的世界缩略图为空白白色的错误 ([MCPE-178373](https://bugs.mojang.com/browse/MCPE-178373))
- 修复了延迟技术预览中，世界中的某些对象会透过伽玛校准菜单可见的错误
- 扩展EXT_texture_cube_map_array现在是运行支持GLES 3.1的Android设备上延迟技术预览的必需项。然而，大多数设备不受影响，但一些设备将失去支持

## 方块

- 在方块几何文件中添加了"item_display_transforms"控制。这控制方块在用户界面、玩家身上和地面上漂浮时的视觉表现方式。它存在于minecraft:geometry内，并要求使用格式版本1.21.20
  - 默认值示例：
    - "item_display_transforms": {  
      "gui" : {  
               "translation": [0, 0, 0],  
               "rotation": [30, 225, 0],  
               "scale": [0.625, 0.625, 0.625]  
      },  
      "firstperson_righthand": {  
               "translation": [0, 0, 0],  
               "rotation": [0, 45, 0],  
               "scale": [0.4, 0.4, 0.4]  
      },  
      "firstperson_lefthand": {  
          "translation": [0, 0, 0],  
          "rotation": [0, -135, 0],  
          "scale": [0.4, 0.4, 0.4]  
      },  
      "thirdperson_righthand": {  
          "translation": [0, 2.5, 0],  
          "rotation": [75, 45, 0],  
          "scale": [0.375, 0.375, 0.375]  
      },  
      "thirdperson_lefthand": {  
          "translation": [0, 2.5, 0],  
          "rotation": [75, 45, 0],  
          "scale": [0.375, 0.375, 0.375]  
      },  
      "ground": {  
          "translation": [0, 3.0, 0],  
          "rotation": [0, 0, 0],  
          "scale": [0.25, 0.25, 0.25]  
      },  
      "fixed": {  
          "translation": [0, 0, 0],  
          "rotation": [0, 0, 0],  
          "scale": [0.5, 0.5, 0.5]  
      },  
      "head": {  
          "translation": [0, 0, 0],  
          "rotation": [0, 0, 0],  
          "scale": [1, 1, 1]  
      }  
    }