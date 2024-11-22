---
标题: Minecraft Beta & Preview - 1.20.30.24
日期: 2023-08-23T14:12:15Z
更新: 2023-08-23T14:13:55Z
分类: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/18794896918157-Minecraft-Beta-Preview-1-20-30-24
---

**发布于:** 2023年8月23日

**关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明。

![一张Minecraft的截图，展示了有树木和洞穴的山脉。](https://feedback.minecraft.net/hc/article_attachments/18794941329549)

是时候进行新的Minecraft预览版和测试版更新了。以下是本周的新内容。请继续向我们发送您的 [反馈](https://aka.ms/MC120Feedback) 和 [漏洞报告](https://bugs.mojang.com/)，祝您玩得愉快！

**实验性交易变更**  
感谢所有提交建议和反馈的玩家！我们正在尝试这些变更，以重新平衡村民交易系统，使其对每个人都更加公平和有趣。然而，这些变更尚未最终确定，它们将在我们继续改进的过程中保持为实验性地物。我们仍然需要您的反馈来帮助我们改进和决策，因此请继续告诉我们您对新交易的看法，您喜欢和不喜欢的地方，以及您的建议，访问 [aka.ms/VillagerTradingFeedback](http://aka.ms/VillagerTradingFeedback)。

# **地物和漏洞修复**

## **用户界面**

- 修复了新游戏界面中反馈按钮行为未链接到反馈页面的问题
- 新的死亡界面现在部分支持“格式化代码”（颜色、静态混淆）

## **音频**

- 玩家实体在进入/退出水时现在会播放适当的声音（[MCPE-132511](https://bugs.mojang.com/browse/MCPE-132511)）

## **方块**

- 修复了方块渲染未更新的问题，除非玩家跳跃（[MCPE-173706](https://bugs.mojang.com/browse/MCPE-173706)）
- 绊线钩不再在南方和西方有延迟失效（[MCPE-174011](https://bugs.mojang.com/browse/MCPE-174011)）
- 混凝土粉末方块现在在从旧版本导入的世界中显示正确的颜色

## **游戏玩法**

- 同一刻发送的相机命令不再被忽略（[MCPE-173524](https://bugs.mojang.com/browse/MCPE-173524)）
- 玩家潜行时，姓名标签不再完全不可见，玩家仍然可见（[MCPE-168789](https://bugs.mojang.com/browse/MCPE-168789)）

## **生物**

- 以下生物在攻击时如果自身着火，将会点燃目标：溺尸、尸壳、僵尸和僵尸村民（[MCPE-77746](https://bugs.mojang.com/browse/MCPE-77746)）

## **教育功能**

- 海豚现在在附加气球时会正确上升
- 骆驼和嗅探兽现在可以附加气球

## **用户界面**

- 修复了HUD屏幕上的各种像素缩放问题
- 新的死亡界面上的游戏菜单手柄快捷键现在正常工作
- 新增三条用户友好的断开连接错误消息，并改进了另外两条

# **技术更新**

## **API**

- 更改 *scoreboardIdentity* 使其在实体被击杀后仍然有效

## **物品**

- 修复了在最新格式版本中，物品内容错误会影响其他物品的问题

## **生物**

- 暴露新的数据参数“can_spread_on_fire”用于“minecraft:behavior.melee_attack”组件，以指定当攻击生物着火时，是否应点燃其目标（[MCPE-77746](https://bugs.mojang.com/browse/MCPE-77746)）

# **实验性技术功能**

## **API**

- 世界事件
  - 将 *BlockBreakAfterEvent* 重命名为 *PlayerBreakBlockAfterEvent*
    - 新增 *readonly itemStackAfterBreak?: ItemStack*（如果空手则为未定义）
    - 新增 *readonly itemStackBeforeBreak?: ItemStack*（如果空手则为未定义）
  - 将 *BlockBreakAfterEventSignal* 重命名为 *PlayerBreakBlockAfterEventSignal*
    - *subscribe* 函数现在接受 *options?: BlockEventOptions*
  - 新增 *PlayerBreakBlockBeforeEvent*，包含以下成员
    - *cancel: boolean*，取消事件的发生
    - *itemStack?: ItemStack*，玩家正在使用的物品堆叠（如果空手则为未定义）
    - *readonly player: Player*，破坏方块的玩家
  - 新增 *PlayerBreakBlockBeforeEventSignal*
  - 将 *BlockPlaceAfterEvent* 重命名为 *PlayerPlaceBlockAfterEvent*
  - 将 *BlockPlaceAfterEventSignal* 重命名为 *PlayerPlaceBlockAfterEventSignal*
    - *subscribe* 函数现在接受 *options?: BlockEventOptions*
  - 新增 *PlayerPlaceBlockBeforeEvent*，包含以下成员
    - *cancel: boolean*，取消事件的发生
    - *readonly face: Direction*，方块放置的面
    - *readonly faceLocation: Vector3*，方块放置在面的具体位置
    - *itemStack: ItemStack*，用于放置方块的物品堆叠
    - *readonly player: Player*，放置方块的玩家
  - 新增 *PlayerPlaceBlockBeforeEventSignal*
  - 修改 *WorldAfterEvents*
    - 将 *blockBreak* 重命名为 *playerBreakBlock*
    - 将 *blockPlace* 重命名为 *playerPlaceBlock*
  - 修改 *WorldBeforeEvents*
    - 新增 *playerBreakBlock*
    - 新增 *playerPlaceBlock*
  - 新增 *BlockEventOptions*，包含以下成员
    - *blockTypes?: string\[\]*，要过滤的方块名称
    - *permutations?: BlockPermutation\[\]*，要过滤的特定方块排列
  - 新增类 *EntityLoadAfterEvent*
    - 新增字段 *entity: Entity*
    - 新增类 *EntityLoadAfterEventSignal*
  - 类 *EntitySpawnAfterEvent*
    - 新增属性 *readonly cause: EntityInitializationCause*_
  - 类 *WorldAfterEvents*
    - 新增属性 *readonly entityLoad: EntityLoadAfterEventSignal*
  - 新增枚举 *EntityInitializationCause*

## **图形**

- 禁用美丽天空或平滑光照不再影响在延迟技术预览中使用的视觉效果
- 将平滑光照和美丽天空按钮移动到仅在延迟技术预览的简单和精美图形菜单中显示
- 在延迟技术预览中，从简单、精美和光线追踪菜单中移除辉光选项