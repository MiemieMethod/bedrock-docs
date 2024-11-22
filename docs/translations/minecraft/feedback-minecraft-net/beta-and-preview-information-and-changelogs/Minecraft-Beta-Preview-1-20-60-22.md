---
标题：Minecraft Beta & Preview - 1.20.60.22
日期：2023-12-06T14:07:39Z
更新：2023-12-06T14:13:34Z
类别：Beta和预览信息及更新日志
链接：https://feedback.minecraft.net/hc/en-us/articles/21999492368781-Minecraft-Beta-Preview-1-20-60-22
哈希：
  h_01HBVR6KM8JCTEG8SDY8V3WBB3: 关于Minecraft预览和Beta的信息
  h_01HGZQAQEYS6RBN8QD678GE07M: 实验性特性
  h_01HGZQAQEYQ351H4T0YXXP0PH4: 铜门
  h_01HGZQAQEY0QZ1PH15RNAE47VD: 旋风人
  h_01HGZQAQEYPDCV3MHF4TETTVB0: 特性和漏洞修复
  h_01HGZQAQEYA6J8AJX77QSXGAA8: 方块
  h_01HGZQAQEZ2VNYNBBAVC86Y1NZ: 一般
  h_01HGZQAQEZH3SMSE36TV7GWM0M: 角色创建器
  h_01HGZQAQEZQ6TR6A2SNPFW7YZH: 用户界面
  h_01HGZQCQEW4QT21QYFVTHKRENJ: 技术更新
  h_01HGZQCQEWP7D0QMBWWCEP0NQ6: API
  h_01HGZQCQEWYHPCNTFT3X8PKHMQ: 方块-1
  h_01HGZQD8XBG0VZG0T6MWG80BT2: 组件
  h_01HGZQD8XB3M0HF6D27ATBN0RD: 编辑器
  h_01HGZQD8XBH6YDARPFWSXXBX0M: 图形
  h_01HGZQD8XB41CEP51S0WRN902T: 稳定性和性能
  h_01HGZQD8XBF8AST3Z7XGG9NP0C: 实验性技术更新
  h_01HGZQD8XB24D6J9SXH2EQ74RD: API-1
  h_01HGZQD8XBTBSF64VBA0BFZ513: 图形-1
  h_01HGZQD8XBX75PS9PJDCBAQ6N2: 脚本
---

**发布：** 2023年12月6日

## **关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一个旋风人靠近试炼刷怪笼，位于试炼室内](https://feedback.minecraft.net/hc/article_attachments/21999475600269)

我们又有了Minecraft Beta和预览更新，包含更多调整和修复！一如既往，我们希望听到您对这些特性的反馈，请将您的想法和建议发送给我们 [这里](https://aka.ms/Minecraft121Feedback)，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告任何漏洞！

# **实验性特性**

## **铜门**

- 更新了铜门的纹理，包括氧化变体
- 铜门和活板门现在具有正确的破坏时间和爆炸抗性

## **旋风人**

- 旋风人地面粒子在骑乘其他实体时不再播放
- 分离了旋风人的漫反射和自发光纹理

# **特性和漏洞修复**

## **方块**

- 被克隆的容器不再保持其容器界面打开，也不再导致崩溃

## **一般**

- 修复了可能在“七海”成就中发生的罕见崩溃

## **角色创建器**

- 修复了一个漏洞，该漏洞使得在使用侧边栏返回时预览的物品仍然保留在纸娃娃上
- 所有未拥有和已拥有的表情现在应该可以在更衣室的表情部分中发现

## **用户界面**

- 窗口重新获得焦点时，最后高亮的按钮将不再被按下 ([MCPE-170377](https://bugs.mojang.com/browse/MCPE-170377))
- 游戏界面的好友抽屉现在在打开和关闭时会发出声音

# **技术更新**

## **API**

- 在记分板 *addObjective* 中将显示名称参数设为可选

## **方块**

- 更改方块的 *brightness_gamma* 值现在可以正确地使方块变暗 ([MCPE-167836](https://bugs.mojang.com/browse/MCPE-167836))

## **组件**

- 在“交互”组件中添加了“drop_item_slot”字段，允许指定一个物品栏槽位以移除并丢弃物品

## **编辑器**

- 工具 测试世界 从工具栏移动，现在位于菜单 世界选项 下

## **图形**

- 修复了一个崩溃，该崩溃可能在玩家放置或破坏任何方块后，并在启用光线追踪时选择保存并退出时发生

## **稳定性和性能**

- 在StartGamePacket的blockProperties中发送“material”用于原版数据驱动方块。“block_id”也移动到“vanilla_block_data”对象中

# **实验性技术更新**

## **API**

- 添加方法 *eatItem(itemStack: ItemStack): void;*
- BlockSignComponent
  - 将函数 *setWaxed* 的签名更改为 *setWaxed(waxed: boolean)*
  - 移除事件/属性 *pistonActivate*
- 添加枚举 BlockPistonState export enum BlockPistonState { Expanded = "Expanded", Expanding = "Expanding", Retracted = "Retracted", Retracting = "Retracting" }
- 类 BlockPistonComponent
  - 移除属性 isExpanded
  - 移除属性 isExpanding
  - 移除属性 isRetracted
  - 移除属性 isRetracting
  - 添加属性 *readonly state: BlockPistonState*
  - 将函数 *getAttachedBlocks* 更改为 *return type Block\[\]*
  - 添加函数 *getAttachedBlocksLocations(): Vector3\[\]*
- 移除类 *PistonActivateBeforeEvent*
- 移除类 *PistonActivateBeforeEventSignal*
- 类型
  - 将 BlockType 从 *beta* 移动到 *1.8.0*
  - 将 FluidType 从 *beta* 移动到 *1.8.0*
- 将 *NavigationResult* 从 *@minecraft/server* 移动到 *@minecraft/server-gametest*

## **图形**

- 调整点光源（如火把、灯笼等）的衰减，以在延迟技术预览中使用平方的曼哈顿距离度量。
- 在延迟技术预览中，用点光源颜色调整环境光颜色，以在大距离上实现更好的多色照明

## **脚本**

- 修复了一个问题，即如果表单中有超过255个按钮，*ActionFormData* 按钮将无法被点击