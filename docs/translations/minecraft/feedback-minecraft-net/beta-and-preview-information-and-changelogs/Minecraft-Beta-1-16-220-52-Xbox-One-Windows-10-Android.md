---
标题: Minecraft Beta - 1.16.220.52 (Xbox One/Windows 10/Android)
日期: 2021-03-17T10:00:19Z
更新: 2021-03-31T08:41:26Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360058166892-Minecraft-Beta-1-16-220-52-Xbox-One-Windows-10-Android
---

**发布于:** 2021年3月18日

**请在参与Minecraft Beta之前阅读：**

- 加入Beta将用一个正在开发中的Minecraft版本替换你的游戏
- 你将无法访问领域，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的备份以防丢失
- Beta版本可能不稳定，并不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![lush2_1170_500.jpg](https://feedback.minecraft.net/hc/article_attachments/360089909011/lush2_1170_500.jpg)

# 新的实验性特性！

在本周的Beta中，我们有一些令人兴奋的新洞穴和悬崖特性，可以通过在你的世界中启用“实验性特性”开关来访问！(你可以在[aka.ms/MCExperimentalToggle](https://aka.ms/MCExperimentalToggle)了解更多关于使用开关的信息。)

你可以在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)的讨论中给我们反馈这些特性，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索和报告你可能遇到的任何新漏洞。

## **世界生成变化**

- 生成范围和构建限制已扩展64个区块向上和64个区块向下，总范围为384个区块
- 地下特性、结构和洞穴生成到y -64

## **新的繁茂洞穴方块！**

请注意：我们添加了几种将在繁茂洞穴中生成的新方块——但洞穴本身尚未在世界中生成！

- 添加了孢子花方块
- 引入了苔藓块和苔藓地毯
  - 当苔藓块被施肥时，随机植物可以在苔藓块上生长
  - 苔藓地毯是一种看起来像羊毛地毯的繁茂洞穴植物
  - 锄是挖掘苔藓块和苔藓地毯的最有效工具
- 添加了杜鹃树和盛开的杜鹃花丛方块
- 添加洞穴藤蔓：
  - 使用发光浆果在其他方块的底面放置洞穴藤蔓
  - 洞穴藤蔓有随机生长的机会
  - 当洞穴藤蔓生长时，有机会包含发光浆果
  - 与带有发光浆果的洞穴藤蔓互动会导致发光浆果弹出
  - 当没有发光浆果的洞穴藤蔓被施肥时，会获得发光浆果
  - 带有发光浆果的洞穴藤蔓方块会发出光
  - 洞穴藤蔓可以攀爬
- 引入发光浆果：
  - 用于引诱和繁殖狐狸
  - 可以食用，营养价值与甜浆果相当
  - 发光浆果也可以种植在大多数坚固的立方体形状方块的底部，以在其下方放置洞穴藤蔓
- 添加以下方块：
  - 杜鹃树叶
  - 盛开的杜鹃树叶
  - 缠根泥土
  - 苔藓
  - 垂根
  - 孢子花
  - 发光浆果
  - 洞穴藤蔓
  - 大型垂滴叶
- 苔藓地毯是一种由苔藓制成的地毯状方块
- 用骨粉施肥的缠根泥土会在其下方生成垂根
- 用锄耕作缠根泥土会将方块变为泥土，并掉落一个根系物品
- 杜鹃树和盛开的杜鹃花丛现在可以用作熔炉燃料
- 添加了垂滴叶方块
- 大型垂滴叶方块是繁茂洞穴中的一个平台方块。站在方块上的实体会导致方块倾斜，并掉落该实体
- 小型垂滴叶方块是繁茂洞穴中的一个装饰性方块。用骨粉施肥会生成一个大型垂滴叶方块

# 漏洞修复和调整

## **铜和避雷针**

- 铜矿石方块纹理已正确定向 ([MCPE-116068](https://bugs.mojang.com/browse/MCPE-116068))
- 铜锭现在只能在工作台上由未氧化的铜块合成 ([MCPE-116091](https://bugs.mojang.com/browse/MCPE-116091))
- 关于状态“dripstone_thickness”和“copper_oxidation”的方块状态模糊性已解决 ([MCPE-116756](https://bugs.mojang.com/browse/MCPE-116756))
- 铜块、台阶和楼梯使用不同的方块ID注册 ([MCPE-116754](https://bugs.mojang.com/browse/MCPE-116754))
- 在铜块上行走/奔跑的声音现在分配给“玩家”音频类别
- 蜡制铜块现在可以在切石机中切割
- 无法在切石机中将锈蚀的切制铜块切割成台阶的问题已解决
- 在切石机中从铜块合成台阶现在将产生两个台阶
- 铜块、楼梯和台阶现在具有正确的地图颜色
- 雷电击中目标实体和方块的优先级顺序与Java版相同
- 铜氧化现在使用随机刻来改变状态，与Java版趋同
- 切石机可用于获取切制、台阶和楼梯变种，使用铜块或切制铜块
- 持斧右键点击铜块将去蜡铜块，逐步刮去铜绿
- 蜡制铜块变种无法通过熔炉或高炉去蜡
- 当以下情况发生时，铜块周围会发出粒子：
  - 玩家蜡制
  - 发射器蜡制
  - 玩家去蜡
  - 刮去铜绿层
  - 被雷电击中
- 被雷电击中的避雷针将减少附近铜块的氧化年龄
- 被方块包围的树叶在顶部放置避雷针时不再变得不透明 ([MCPE-116256](https://bugs.mojang.com/browse/MCPE-116256))
- 避雷针不再与栅栏或墙体连接 ([MCPE-116150](https://bugs.mojang.com/browse/MCPE-116150))
- 避雷针现在可以含水，这解决了水的剔除问题 ([MCPE-116541](https://bugs.mojang.com/browse/MCPE-116541))
- 避雷针在雷暴期间如果上方没有任何东西，会发出粒子
- 玩家在手持避雷针时可以与其他方块互动 ([MCPE-116074](https://bugs.mojang.com/browse/MCPE-116074))

## **一般**

- 在旧世界中，告示牌文本不再不可见 ([MCPE-119628](https://bugs.mojang.com/browse/MCPE-119628))
- 墨囊和染料在使用于告示牌时现在会发出声音 ([MCPE-117944](https://bugs.mojang.com/browse/MCPE-117944))
- 在个人资料屏幕上选择特色优惠将正确重定向用户到完整的特色优惠列表
- 修复了Xbox上非客人分屏玩家丢失数据的问题 ([MCPE-55815](https://bugs.mojang.com/browse/MCPE-55815))
- 使登录按钮文本适合葡萄牙-BR的按钮
- 在设置屏幕的存储菜单中使用较浅的文本颜色
- 修复了应用资源包时按钮纹理缩放错误的问题
- 在某些无法使用的屏幕中启用仅使用键盘导航到返回按钮
- 修复了在切换个人资料时，所有其他预览的个人资料被初始个人资料覆盖的漏洞
- /clear命令将为树苗物品应用正确的“data”参数 ([MCPE-117889](https://bugs.mojang.com/browse/MCPE-117889))
- /clear命令将不再从玩家的副手槽位移除额外物品 ([MCPE-116857](https://bugs.mojang.com/browse/MCPE-116857))
- 修复了如果视角摇晃设置被禁用，玩家的手仍然会摇晃的问题 ([MCPE-79380](https://bugs.mojang.com/browse/MCPE-79380))
- 修复了HudCursor未渲染反转颜色的问题 ([MCPE-58826](https://bugs.mojang.com/browse/MCPE-58826))
- 活塞和黏性活塞在禁用轮廓选择时不再显示为黑色 ([MCPE-53858](https://bugs.mojang.com/browse/MCPE-53858))
- 修复了下界生物群系中的迷雾在某些资源包中未正确渲染的问题 ([MCPE-111680](https://bugs.mojang.com/browse/MCPE-111680))
- 带有文本的告示牌上不再可见闪烁的线条 ([MCPE-110321](https://bugs.mojang.com/browse/MCPE-110321))
- 修复了屏障漏洞，导致非完整方块因屏障未写入深度而闪烁 ([MCPE-116767](https://bugs.mojang.com/browse/MCPE-116767))
- 非持久性生物在进入下界后不再立即消失
- 溺尸在投掷三叉戟时将挥动手臂
- 修复了进入下界传送门并同时投掷附魔之瓶时崩溃的问题 ([MCPE-114793](https://bugs.mojang.com/browse/MCPE-114793))

## **角色创建器**

- 当未装备鞋子时，史蒂夫的裤子不再给外观的脚底上色
- 多人游戏中的用户不再看到其他玩家使用他们不拥有的外观部件作为史蒂夫
- 在分屏中更换皮肤现在应正确保存所有本地用户，并正确更新远程用户
- 亚历克斯的衬衫在搭配不同裤子时不再看起来损坏
- “万岁！”表情现在将在表情部分显示，如果已拥有 ([MCPE-111165](https://bugs.mojang.com/browse/MCPE-111165))

## **虚拟现实**

- 在虚拟现实中，当处于全屏效果（着火、站在传送门中等）后，死亡屏幕现在可见
- 修复了被遮挡的用户界面元素的半透明渲染，包括在靠近方块时查看菜单时
- 物品别名在重复物品的自动完成中不显示，但如果用户使用别名运行命令，命令仍然可以成功