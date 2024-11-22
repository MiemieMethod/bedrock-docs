---
标题: Minecraft Beta - 1.17.40.21 (Xbox One/Windows 10/Android)
日期: 2021-09-22T13:38:49Z
更新: 2021-09-22T15:50:37Z
分类: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/4409802760717-Minecraft-Beta-1-17-40-21-Xbox-One-Windows-10-Android
---

**发布于:** 2021年9月22日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![bedrock-beta17U4-2-header.jpg](https://feedback.minecraft.net/hc/article_attachments/4409786741005/bedrock-beta17U4-2-header.jpg)

您好？您好？有人能听到我吗？我在一个新生成的洞穴里，我不是说我迷路了，但我确实不知道怎么找到出去的路。我知道我跟着一条比平常更深的铜矿石矿脉，突然间，我在我保存的一个区块下面，我们就这样了。在我尝试挖出来的时候，请享受本周的基岩测试版更新，并在[aka.ms/CavesCliffsFeedback](http://aka.ms/CavesCliffsFeedback)上给我们反馈，报告任何漏洞请访问[bugs.mojang.com](http://bugs.mojang.com/)。如果基岩团队的其他人问我在哪里，请告诉他们我被困在交通中。他们永远不会让我忘记这件事……

# **实验性功能**

- 在使用洞穴与山崖实验性开关升级Y=0以下的保存区块时，新增世界/洞穴生成
  - 之前在基岩下方升级的区块将不会看到此更改
  - 有关更多信息，请参见我们的[常见问题解答](https://aka.ms/ccworldupgrade)！我们期待您在[aka.ms/CavesCliffsFeedback](http://aka.ms/CavesCliffsFeedback)上的反馈

#### **平坦世界生成**

- 将旧的平坦世界升级到使用洞穴与山崖实验性开关可用的新扩展高度
- 使用洞穴与山崖实验性开关的新平坦世界将从“y=-64”开始生成

## **游戏玩法**

- 修复了测试版构建中飞行超过世界限制（非洞穴与山崖实验性为255，洞穴与山崖实验性为319）被禁止的问题 ([MCPE-141360](https://bugs.mojang.com/browse/MCPE-141360))

### **铜矿石**

- 铜矿石现在在y=96处生成，而不是y=64 ([MCPE-125233](https://bugs.mojang.com/browse/MCPE-125233))

# **非实验性功能和漏洞修复**

## **常规**

- 手持顶部雪时，悬停在草方块上不再导致不正确的行为 ([MCPE-140659](https://bugs.mojang.com/browse/MCPE-140659)) ([MCPE-140660](https://bugs.mojang.com/browse/MCPE-140660))
- 蜂巢现在在世界中正确生成 ([MCPE-141324](https://bugs.mojang.com/browse/MCPE-141324)) ([MCPE-132195](https://bugs.mojang.com/browse/MCPE-132195))
- 非防火生物现在会避免穿越火焰 ([MCPE-23835](https://bugs.mojang.com/browse/MCPE-23835))

## **游戏玩法**

- 原版趋同：玩家现在可以在向上移动时激活鞘翅滑翔 ([MCPE-59580](https://bugs.mojang.com/browse/MCPE-59580))
- 在包含格式化颜色文本的告示牌上使用染料将覆盖格式化颜色文本

## **世界生成**

- 化石现在生成在结构中的几率大大降低
- 地牢在非洞穴与山崖实验性开关下不再错误放置或缺失 ([MCPE-121708](https://bugs.mojang.com/browse/MCPE-121708))

## **生物**

- 铁傀儡现在仅在实心方块上生成 ([MCPE-140145](https://bugs.mojang.com/browse/MCPE-140145))
- 现在持有的武器在掠夺者和卫道士上正确渲染 ([MCPE-141321](https://bugs.mojang.com/browse/MCPE-141321))

## **用户界面**

- 骑乘动物时，在使用非触控控制时将显示正确的按钮提示

## **角色创建器**

- 背部外观部件将不再遮挡个人资料界面中的左右箭头
- 修复了个人资料界面中的特色物品未打开特色目录的问题
- 修复了如果之前编辑了其他物品的颜色，默认衣物会改变颜色的问题
- 在使用控制器时，导航回之前选择的侧边栏选项后，侧边栏选项现在可以在扩展视图中选择
- 在更衣室中扩展任何经典皮肤包时，侧边栏不再打开
- 改进了角色创建器的导航流程，以便始终切换到所选的角色创建器个人资料 ([MCPE-139022](https://bugs.mojang.com/browse/MCPE-139022))
- 在游戏中从市场购买的皮肤现在会应用于角色

# **技术更新**

## **动画**

- 修复了在更改渲染控制器时导致动画重新启动的漏洞

## **图形**

- 修复了告示牌上的文本在遇到新行或换行时丢失格式的问题。格式现在将持续到找到重置代码或覆盖代码。这不具有追溯性，之前创建的告示牌不会更改

## **图形**

- 作为持续测试的一部分，移除了Android设备上的RenderDragon引擎（ARMv7）

## **Molang**

- 包含大写字母的Molang表达式现在可以正确评估
- 'query.get_equipped_item_name'现在将识别海晶灯 ([MCPE-67893](https://bugs.mojang.com/browse/MCPE-67893))
- 为像1 + (9 10)这样的表达式添加新的编译错误，这些表达式之前被忽略（这是引擎版本1.17.40的版本更改）

## **GameTest框架（实验性）**

- 更新了GameTest框架接口，并添加了新的模拟玩家功能：
  - 向GameTest添加了'SimulatedPlayer'类。该类使GameTest能够模拟各种玩家行为，例如移动、使用物品以及与方块和实体的交互。有关更多详细信息，请参见[GameTest API](https://docs.microsoft.com/en-us/minecraft/creator/scriptapi/mojang-gametest/mojang-gametest)参考文档。
    - 添加函数 spawnSimulatedPlayer(blockLocation: BlockLocation, name: string): SimulatedPlayer
    - 添加函数 removeSimulatedPlayer(simulatedPlayer: SimulatedPlayer): void
  - mojang-gametest.Test类型
    - 更改函数 assertEntityInstancePresent(entity: Entity, blockLocation: BlockLocation, isPresent: boolean = true) 的签名
  - mojang-minecraft组件
    - 组件inventory现在与玩家物品栏一起工作