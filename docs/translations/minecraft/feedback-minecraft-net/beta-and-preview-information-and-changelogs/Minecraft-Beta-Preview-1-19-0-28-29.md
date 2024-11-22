---
标题: Minecraft Beta & Preview - 1.19.0.28/29
日期: 2022-04-28T15:26:50Z
更新: 2022-04-28T19:49:03Z
分类: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/5862628722189-Minecraft-Beta-Preview-1-19-0-28-29
---

## 关于Minecraft预览版和测试版的信息：

- 测试版: 1.19.0.28 \| 预览版: 1.19.0.29 \| Xbox预览版: 1.19.0.64
- 虽然预览版和测试版的版本号不同，但游戏内容没有差异
- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Xbox、Windows 10/11和Android（Google Play）上使用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![一张展示新音乐唱片的Minecraft截图](https://feedback.minecraft.net/hc/article_attachments/5862625227277/Screenshot_2022-04-27_094221.jpg)

以下是本周测试版的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，访问[bugs.mojang.com](http://bugs.mojang.com/)并向我们发送[您的反馈](https://aka.ms/MinecraftBetaFeedback)。

# **旁观者模式（实验性）**

- 引入旁观者模式实验性开关。玩家现在可以通过启用实验性开关来尝试旁观者模式的早期开发版本
  - 提醒一下，我们在通知您之前不会接受与旁观者模式相关的漏洞报告，因为该功能在开发过程中可能会发生很大变化。
- 生物不再在旁观者模式下逃离玩家
- 旁观者模式将不再触发绊线陷阱

# **新特性和漏洞修复**

## **音乐唱片5**

- 添加了唱片残片5和音乐唱片5
  - 与其他唱片不同，它只能通过找到并合成9个唱片残片获得
  - 这些唱片残片在远古城市的箱子中稀有出现

## **监守者**

- 监守者的远程攻击进行了某些更改：
  - 使用远程攻击时，垂直击退现在会尊重方向性
  - 现在可以绕过盾牌和盔甲，并具有自定义死亡消息
  - 造成10点伤害而不是30点，冷却时间从5秒减少到2秒
- 监守者现在在死亡时掉落一个幽匿催发体
- 当被投射物分散注意力时，监守者现在增加愤怒（非频繁投射物为10，频繁投射物为35）
- 监守者现在对非箭类投射物作出反应
- 监守者现在可以被非箭类投射物正确分散注意力（[MCPE-153549](https://bugs.mojang.com/browse/MCPE-153549)）
- 监守者现在会对所有碰撞到它的生物感到愤怒（[MCPE-153839](https://bugs.mojang.com/browse/MCPE-153839)）

## **幽匿**

- 幽匿催发体和尖啸体的爆炸抗性与Java版相同（[MCPE-153208](https://bugs.mojang.com/browse/MCPE-153208)）
- 恢复了一些错误删除的幽匿相关声音（[MCPE-153296](https://bugs.mojang.com/browse/MCPE-153296)）
- 幽匿尖啸体的尖啸声音现在被正确分类为方块声音（[MCPE-154130](https://bugs.mojang.com/browse/MCPE-154130)）
- 幽匿感测体的激活和停用声音现在被正确分类为方块声音（[MCPE-115395](https://bugs.mojang.com/browse/MCPE-115395)）
- 幽匿感测体现在可以正确检测使用钓鱼竿的玩家
- 幽匿尖啸体在手持或放置在物品展示框中时不再出现z-fighting（[MCPE-145580](https://bugs.mojang.com/browse/MCPE-145580)）
- 活塞将无法推动幽匿尖啸体、幽匿感测体和幽匿催发体（[MCPE-154056](https://bugs.mojang.com/browse/MCPE-154056)）
- 在开采幽匿感测体时，周围的裂纹动画不再出现（[MCPE-121492](https://bugs.mojang.com/browse/MCPE-121492)）

## **红树**

- 红树胎生苗不再可以无限施肥（[MCPE-153707](https://bugs.mojang.com/browse/MCPE-153707)）
- 如果红树上方的区域被阻挡，红树将不再生长
- 将*mangrove_propagule_hanging*合并到*mangrove_propagule*方块中，并使用悬挂方块状态代替
- 红树木/原木类型现在可以正确防止树叶衰退（[MCPE-153948](https://bugs.mojang.com/browse/MCPE-153948)）
- 将红树树叶的外观与Java版保持一致
- 修复了红树在树枝中生成时没有原木的问题（[MCPE-153948](https://bugs.mojang.com/browse/MCPE-153948)）
- 修复了一个导致大多数红树木方块不受火焰影响的漏洞
- 非红树树苗现在可以在泥巴上施肥成长为完整的树木
- 红树树叶在被剪刀收获时现在掉落树叶方块（[MCPE-153787](https://bugs.mojang.com/browse/MCPE-153787)）
- 营火和烟熏炉现在可以用所有变种的红树木合成（[MCPE-153811](https://bugs.mojang.com/browse/MCPE-153811)）

## **悦灵**

- 现在可以从悦灵那里拿走可堆叠物品并添加到现有堆叠中（[MCPE-153540](https://bugs.mojang.com/browse/MCPE-153540)）
- 悦灵现在有了新的投掷声音

## **青蛙**

- 青蛙在泥巴方块上不再有路径寻找问题。为了解决这个问题，在实施适当的路径寻找修复之前，泥巴方块将不再轻微下沉实体（[MCPE-153961](https://bugs.mojang.com/browse/MCPE-153961)）
- 修复了青蛙在吃史莱姆或岩浆怪时嘴巴与头部发生z-fighting的漏洞（[MCPE-151539](https://bugs.mojang.com/browse/MCPE-151539)）

## **蛙明灯**

- 蛙明灯在被任何工具破坏时现在正确掉落
- 蛙明灯方块现在具有正确的地图颜色（[MCPE-154315](https://bugs.mojang.com/browse/MCPE-154315)）
- 蛙明灯方块现在具有正确的破坏时间

## **青蛙卵**

- 青蛙卵现在会被流动的水破坏

## **游戏玩法**

- 生物不再能够在按钮上生成（[MCPE-153897](https://bugs.mojang.com/browse/MCPE-153897)）
- 紫水晶簇不再可以放置在幽匿尖啸体和其他没有顶部支撑的方块上，现在可以放置在有底部支撑的方块上，符合预期（[MCPE-145676](https://bugs.mojang.com/browse/MCPE-145676)）
- 修复了一个未损坏的工具（如镐）在铁砧上更改名称后首次使用时无法正常工作的漏洞（[MCPE-152637](https://bugs.mojang.com/browse/MCPE-152637)）
- 带箱子的矿车/漏斗矿车/TNT的配方现在是无形状的
- 修复了在吸收效果下承受大量致命伤害可能导致软锁定的问题

## **原版趋同**

- 潜影贝现在免疫火焰（[MCPE-33236](https://bugs.mojang.com/browse/MCPE-33236)）
- 潜影贝现在在载具中保持直立位置（[MCPE-115269](https://bugs.mojang.com/browse/MCPE-115269)）
- 当相对负y轴和x轴有另一个潜影贝时，潜影贝不再无法生成

## **触控控制**

- 玩家现在可以从移动方向滑动以跳跃，并且在“经典”触控控制中跳跃和潜行被交换时不会被打断（[MCPE-151149](https://bugs.mojang.com/browse/MCPE-151149)）

## **图形**

- 修复了RTX世界中太阳方向未更新的问题（[MCPE-153958](https://bugs.mojang.com/browse/MCPE-153958)）

## **行商羊驼**

- 行商羊驼在被喂干草捆后可以繁殖
- 行商羊驼在从流浪商人释放后将不再保持持续状态（[MCPE-102302](https://bugs.mojang.com/browse/MCPE-102302)）

## **稳定性和性能**

- 修复了与最后与断开连接的玩家交易的村民交易时可能发生的崩溃
- 修复了在iOS的村庄中偶尔发生的崩溃

## **用户界面**

- 修复了在使用熔炉、高炉、烟熏炉、附魔台、砂轮、酿造台、铁砧、信标和锻造台时，点击玩家物品栏左侧深灰色区域可以掉落物品的漏洞
- 特征服务器消息文本不再居中

## **命令**

- 为'/loot'命令添加了'replace entity'重载

# **技术更新**

## **常规**

- 数据驱动方块的内容错误改进，记录资源包、文件和方块标识符
- 将BlockGeometryComponent的minecraft:geometry字段长度限制为256个字符

## **图形**

- Xbox上的设备恢复现在将使用初始创建时使用的相同值重新初始化

## **Molang**

- 在手动渲染期间避免清除临时Molang变量

## **GameTest框架（实验性）**

- 实体
  - 添加函数setRotation(degreesX: number, degreesY: number) - 设置实体的旋转
  - 添加只读属性rotation: XYRotation - 获取实体的旋转
  - 移除属性bodyRotation - 注意：请使用Entity.rotation.y代替

- 事件
  - 添加事件'buttonPushEvent' - 当按钮被按下时触发
- XYRotation
  - 将类PitchYawRotation重命名为XYRotation
  - 将属性pitch重命名为x
  - 将属性yaw重命名为y