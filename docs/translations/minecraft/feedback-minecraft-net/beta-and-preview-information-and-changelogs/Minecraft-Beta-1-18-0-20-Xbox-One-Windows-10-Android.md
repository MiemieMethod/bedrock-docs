---
标题: Minecraft Beta - 1.18.0.20 (Xbox One/Windows 10/Android)
日期: 2021-10-06T14:42:38Z
更新: 2021-10-06T16:24:34Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/4410756779405-Minecraft-Beta-1-18-0-20-Xbox-One-Windows-10-Android
哈希:
  caves-cliffs: caves--cliffs
---

**发布于:** 2021年10月6日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版期间无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的先前版本中打开，因此请务必备份世界以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参阅[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![Screen_Shot_10-06-21_at_10.47_AM_001.JPG](https://feedback.minecraft.net/hc/article_attachments/4410756729229/Screen_Shot_10-06-21_at_10.47_AM_001.JPG)

啊，测试版。它们成长得如此之快！曾经是一个小小的基岩测试版，现在在我们眼前绽放。您可能会问，为什么会有这种怀旧的转变？这可能是因为“洞穴与山崖”特性已经从实验性特性中搬出，成长为完全成熟的默认特性，略有空巢综合症。那不是我眼中的泪水，只是在搬家后非常尘土飞扬！也许暂时停止无端指控，享受本周的更新吧，像往常一样将您的反馈发送到[aka.ms/CavesCliffsFeedback](http://aka.ms/CavesCliffsFeedback)，并在[bugs.mojang.com](http://bugs.mojang.com/)报告漏洞。我的纸巾在哪里？！

**我们再次希望听到您对游戏性能的反馈 - 您可以通过这个简短的调查告诉我们游戏的运行情况：[aka.ms/MCPerfPoll](https://aka.ms/MCPerfPoll)**

**提醒：** 我们仍在调整世界生成，特性可能会发生变化，请记得**定期备份**您最喜欢的世界！

# **洞穴与山崖**

- 与“洞穴与山崖第二部分”相关的特性已从实验性切换中移出，现在默认启用
  - **注意：** 在将您的世界加载到此测试版时，将自动引入新的“洞穴与山崖第二部分”世界生成，而不会创建默认世界副本。您可以在我们的[常见问题解答](https://aka.ms/ccworldupgrade)中阅读有关如何在现有区块下添加新生成的更多信息！
- “洞穴与山崖第二部分”中的新世界生成目前与“自定义生物群系创建”实验不兼容。在此测试版中，预计具有自定义生物群系生成的世界可能不稳定，自定义生物群系仅存在于当前保存的世界区域中
- 更改矿物生成率以与Java版保持一致
- 修复了一个问题，该问题阻止大型树木在y=0以下生长（[MCPE-126254](https://bugs.mojang.com/browse/MCPE-126254)）
- 小型垂滴叶现在在繁茂洞穴生物群系中正确生成（[MCPE-125799](https://bugs.mojang.com/browse/MCPE-125799)）

## **洞穴生成**

- 旧洞穴现在可以延伸到地表
- 旧洞穴雕刻者的放置现在与Java版保持一致
- 洞穴中不再生成漂浮水源（[MCPE-141424](https://bugs.mojang.com/browse/MCPE-141424)）

## **地物放置**

- 草甸花不再替换村庄或其他结构中的方块（[MCPE-141378](https://bugs.mojang.com/browse/MCPE-141378)）
- 凝灰岩块地物现在在y=0以下生成（[MCPE-141452](https://bugs.mojang.com/browse/MCPE-141452)）
- 深板岩块不再在y=0以上生成（[MCPE-141330](https://bugs.mojang.com/browse/MCPE-141330)）
- 紫晶洞现在在世界生成期间放置在正确的y范围内（[MCPE-141326](https://bugs.mojang.com/browse/MCPE-141326)）

### **世界生成**

- 更新花岗岩、安山岩、闪长岩、泥土和沙砾的地物放置以匹配Java版
- 调整山峰，使小山看起来更像真正的锯齿状山峰，而不是平坦的丘陵
- 改进旧区块与新区块之间的融合
- 废弃矿井隧道不再能替换基岩（[MCPE-141123](https://bugs.mojang.com/browse/MCPE-141123)）

# **特性和漏洞修复**

## **稳定性和性能**

- 如果服务器和客户端具有不同的运行时方块ID，玩家不再会断开连接
- 优化了在主世界中放置藤蔓所需的时间

## **辅助功能**

- 在“控制器失去连接”提示中添加了缺失的屏幕阅读器

## **游戏玩法**

- 修正了当传送门被移动但位置未更新时的传送门位置（[MCPE-28765](https://bugs.mojang.com/browse/MCPE-28765)）
- 破坏火焰下方的方块不再在禁用'doFireTick'游戏规则时创建不可见的火焰方块（[MCPE-101371](https://bugs.mojang.com/browse/MCPE-101371)）

## **一般**

- 设置了高于推荐渲染距离的玩家现在会被提示更改为推荐值
- 渲染距离的默认和最大设置已更新以提高性能
- 现在有提示警告玩家，如果他们在游戏中登录，将被带回主菜单

## **图形**

- 雕刻南瓜的附魔光辉现在仅覆盖物品，而不是整个槽位（[MCPE-68219](https://bugs.mojang.com/browse/MCPE-68219)）
- 修复了在旧世界中可能发生的一个漏洞，在矿车中向上看时会显示矿车内部，阻挡玩家视线
- 更新物品渲染，使附魔物品在下界中不再不可见（[MCPE-116880](https://bugs.mojang.com/browse/MCPE-116880)）

## **市场**

- 在没有互联网连接或会话启动失败时不再出现商店更新提示

## **生物**

- 生物现在可以通过活板门路径
- 生物不再穿过营火（[MCPE-142054](https://bugs.mojang.com/browse/MCPE-142054)）
- 美西螈在空中时现在能正确动画（[MCPE-131322](https://bugs.mojang.com/browse/MCPE-131322)）
- 甜浆果丛现在会对生物造成伤害（[MCPE-56142](https://bugs.mojang.com/browse/MCPE-56142)）（[MCPE-140012](https://bugs.mojang.com/browse/MCPE-140012)）
- 生物不再尝试穿过甜浆果丛

## **用户界面**

- 结构方块现在可以在当前维度高度限制内保存和加载（[MCPE-122643](https://bugs.mojang.com/browse/MCPE-122643)）
- 修复了搜索不存在的内容时出现不正确的“1个结果”消息的问题
- 修复了在4:3分辨率屏幕上出现的重叠文本问题
- 修复了在多人游戏中躺在床上时的Java版趋同问题。消息将显示有多少玩家在床上等待所有玩家入睡
- 为不同的渲染距离设置提供更好的视觉反馈和提示

## **原版趋同**

- 袭击生物在袭击结束后，如果玩家移动得太远，则会消失
- 袭击boss条颜色从紫色更改为红色（[MCPE-46047](https://bugs.mojang.com/browse/MCPE-46047)）
- 卫道士不再自然生成在灾厄巡逻队中

## **村庄**

### **村庄英雄**

- 村庄英雄效果现在适用于所有帮助击杀袭击者的玩家，一旦袭击被击败，该效果将保留在玩家身上，即使他们离开村庄（[MCPE-53384](https://bugs.mojang.com/browse/MCPE-53384)）

# **技术更新**

## **命令**

- 通过'/execute'触发的函数调用顺序现在是一致的（[MCPE-111849](https://bugs.mojang.com/browse/MCPE-111849)）

## **一般**

- 为子区块请求添加了缓存支持，并修复了地形中的洞穴问题
- 修复了在尝试在基于JSON文件的游戏版本之前渲染原版生物时可能发生的渲染错误
- 大多数内容错误和警告现在每个世界仅显示一次（[MCPE-135153](https://bugs.mojang.com/browse/MCPE-135153)）

## **物品脚本**

实现了物品脚本组件的第一阶段

- ItemStack
  - 暴露接口以访问ItemStack上的脚本启用的ItemComponents
  - hasComponent(componentId: string) - 如果ItemStack附加了组件\[componentId\]，则返回true
  - getComponent(componentId: string) - 返回附加到此ItemStack的组件的句柄。如果组件不存在或尚未暴露给脚本，则返回未定义句柄
  - getComponents() - 返回此ItemStack上所有附加的脚本启用组件的数组
- NumberRange
  - 描述一个最小值和最大值之间随机值的类
  - 属性min - 范围内的最小值
  - 属性max - 范围内的最大值
  - next() - 返回min和max之间的随机数
- Items Registry
  - 添加Items注册类以按名称获取所有物品
  - get(itemId: string) - 如果给定名称存在类型，则返回ItemType的句柄
- 脚本启用的物品组件
  - minecraft:food
    - 只读属性nutrition - 描述此食物物品在被吃时给予玩家多少营养的数字
    - 只读属性saturationModifier - 在被吃时用于应用饱和度增益的饱和度修正值
    - 只读属性canAlwaysEat - 如果为true，玩家可以始终吃此物品（即使不饿）
    - 只读属性usingConvertsTo - 被吃时将转换为的物品的字符串名称。如果为空，则该物品不会转换为其他任何东西
  - minecraft:durability
    - 只读属性maxDurability - 此物品在破坏之前可以承受的最大伤害数量
    - 只读属性damageRange - 描述物品失去耐久度的机会的NumberRange
    - 属性damage - 获取或设置ItemStack上的当前伤害
  - getDamageChance(unbreaking: number = 0) - 获取在给定耐久等级的情况下，使用damageRange属性时此物品受损的最大机会。传入的耐久参数必须大于0