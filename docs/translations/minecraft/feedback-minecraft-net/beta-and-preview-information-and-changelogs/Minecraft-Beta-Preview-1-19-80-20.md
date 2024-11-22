---
title: Minecraft测试版与预览版 - 1.19.80.20
date: 2023-03-08T14:05:34Z
updated: 2023-03-09T11:47:03Z
categories: 测试版与预览版信息及更新日志
link: https://feedback.minecraft.net/hc/zh-cn/articles/13817573176461-Minecraft-Beta-Preview-1-19-80-20
hash:
  sneak: 15-sneak
---

**发布时间：** 2023年3月8日

**Minecraft预览版与测试版信息：**

- 这些进行中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上获取。要加入或退出测试版，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明
- **请注意：** 由于不可避免的情况，Android测试版将延期至下周初——对此带来的不便我们深表歉意，并将尽快向您发布更新！

![一张Minecraft的截图，显示一个村民站在一些樱花树和樱花附近。背景中有一个嗅探兽，樱花木板上有一个饰纹陶罐。](https://feedback.minecraft.net/hc/article_attachments/13817036172941)

现在，Minecraft 1.20正式命名为“足迹与故事”更新，我们将全速推进，带来一系列新的实验性地物和修复内容，本周将推出到基岩版！你准备好探索樱花树林（又名樱花生物群系）了吗？这个美丽的地方可能有两个名称在流传，如果这让你感到困惑，我们深感抱歉。就像这些地物一样，它们的名称也是正在进行中的**。**无论*你*选择叫什么，它都很美丽，所以建议你尽快去寻找。但这还不是全部！虽然我们还未准备好添加盔甲装饰，但我们对饰纹陶罐、可疑的沙子、刷子和骆驼进行了更改。我们甚至有一个新的“你死了！”屏幕。所以，出去把自己扔进熔岩或直视苦力怕吧。别忘了将所有反馈和想法发送给我们，访问 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback)，并将任何漏洞报告到 [bugs.mojang.com](http://bugs.mojang.com/)。

# **实验性功能**

## **樱花树林**

- 引入樱花树林生物群系，拥有漂亮的樱花树。你可以在山脉中找到它，像草甸一样
- 它有一种新的花卉，粉红色花簇，作为地面覆盖物，可以合成成粉红色染料
- 猪、兔子、绵羊和蜜蜂会在这里生成
- 配备了樱花树的新木材套装

## **饰纹陶罐**

- 根据反馈调整了饰纹陶罐的颈部设计 ([MCPE-167168](https://bugs.mojang.com/browse/MCPE-167168))
  - 对于原来的陶罐，我们决定让陶罐的颈部与方块重叠，以提高建造的灵活性。然而，我们遇到了一些Z-战斗问题，这意味着两个对象处于完全相同的位置，导致闪烁。通过这个新的方块模型，我们防止了这种情况，陶罐看起来更复杂了一些！
- 饰纹陶罐不再支持方块附加到其侧面 ([MCPE-167165](https://bugs.mojang.com/browse/MCPE-167165))
- 饰纹陶罐在物品栏中不可堆叠 ([MCPE-167223](https://bugs.mojang.com/browse/MCPE-167223))
- 饰纹陶罐的基本配方现在显示在生存模式的配方书中
- 饰纹陶罐粒子效果现在基于默认的饰纹陶罐侧面纹理
- 更新了射手陶器碎片纹理

## **刷子**

- 更改了刷子的配方，使用羽毛、铜锭和木棍 ([MCPE-167619](https://bugs.mojang.com/browse/MCPE-167619))
- 当第三人称视角下持有刷子时，破坏动画现在可以正常工作 ([MCPE-167183](https://bugs.mojang.com/browse/MCPE-167183))
- 使用刷子物品时，粒子和声音有了轻微的冷却时间

## **可疑的沙子**

- 可疑的沙子不再含水 ([MCPE-167222](https://bugs.mojang.com/browse/MCPE-167222))
- 可疑的沙子现在可以连接到栅栏方块
- 可疑的沙子在被刷子破坏后会变成普通沙子 ([MCPE-167166](https://bugs.mojang.com/browse/MCPE-167166))
- 可疑的沙子在被活塞破坏时会发出粒子效果
- 修复了在刷子刷动时，可疑的沙子内部物品闪烁的问题 ([MCPE-167180](https://bugs.mojang.com/browse/MCPE-167180))
- 此外，以前被活塞破坏时不会发出粒子的方块现在会发出粒子效果了！([MCPE-109293](https://bugs.mojang.com/browse/MCPE-109293)、[MCPE-126257](https://bugs.mojang.com/browse/MCPE-126257))

## **骆驼**

- 骆驼在进入可骑乘实体时现在会停止冲刺 ([MCPE-164065](https://bugs.mojang.com/browse/MCPE-164065))

## **1.5潜行**

- 在1.5方块间隙下潜行的能力现在在“短潜行”切换后启用。启用切换以继续测试此功能，同时我们继续进行优化

# **功能与修复**

**更新“你死了”体验**  
从今天开始，我们正在推出一些更改，修改当你在Minecraft中死亡时看到的屏幕。这个设计对所有在预览/测试版中的用户开放，除非你应用了附加包。我们希望听到你的反馈！请在 [这里](https://aka.ms/MinecraftPDScreen) 与我们分享你的意见。

![“你死了”屏幕的移动版本](https://feedback.minecraft.net/hc/article_attachments/13817265642253)

*图片：移动版本的“你死了”屏幕。*

要使用旧屏幕，请前往设置 -> 视频，并关闭“新‘你死了’屏幕（实验性）”。

## **辅助功能**

- 文字转语音不再在移动到新物品后朗读先前选择的物品
- 在用户在不同标签之间切换时，文字转语音不再卡在辅助功能标签的朗读上
- 在辅助功能设置中添加了一个闪光强度滑块，用于调整附魔物品上视觉闪光的透明度
- 在辅助功能设置中添加了一个闪光速度滑块，用于调整附魔物品上视觉闪光的闪动速度

## **方块**

- 红树、竹子和磨制黑石按钮在地图上不再可见
- 花卉再次在放置在花盆中时立即显示

## **游戏玩法**

- 修复了在使用手柄退出容器屏幕后玩家移动错误方向的问题 ([MCPE-121565](https://bugs.mojang.com/browse/MCPE-121565))
- 玩家在飞行时不能再潜行 ([MCPE-166834](https://bugs.mojang.com/browse/MCPE-166834))
- 修复了在部分方块周围时VR中出现不必要的黑色方块的问题
- 修复了游泳与行走之间的动画过渡 ([MCPE-166769](https://bugs.mojang.com/browse/MCPE-166769))
- 修复了命令方块可能导致区块内活动对象冻结的漏洞 ([MCPE-162011](https://bugs.mojang.com/browse/MCPE-162011))
- 生命提升效果在效果消失后将不再完全恢复玩家的生命值 ([MCPE-165434](https://bugs.mojang.com/browse/MCPE-165434))

## **通用**

- 修复了进入或加载末地时不再播放环境洞穴声音的问题 ([MCPE-141493](https://bugs.mojang.com/browse/MCPE-141493))
- 在熔炉中烹饪紫颂果现在会生成经验 ([MCPE-68127](https://bugs.mojang.com/browse/MCPE-68127))
- 下界传送门现在可以替换除空气之外的方块生成。这包括像草和雪层这样的方块 ([MCPE-162272](https://bugs.mojang.com/browse/MCPE-162272))
- 光源方块在生存或冒险模式中无法再更改其光照等级 ([MCPE-138868](https://bugs.mojang.com/browse/MCPE-138868))
- 营火的声音现在更大且更清晰 ([MCPE-122296](https://bugs.mojang.com/browse/MCPE-122296))

## **图形**

- 修复了在RTX中多个光源（如火把）错误地发出白光的问题 ([MCPE-166947](https://bugs.mojang.com/browse/MCPE-166947))
- 穿戴靴子时，靴子不再与玩家发生Z-战斗
- 穿戴护腿时，“腿部”和“腰带”部分不再与玩家发生Z-战斗
- 披风在受伤时不再闪烁红色 ([MCPE-105347](https://bugs.mojang.com/browse/MCPE-105347))
- 修复了漏斗模型中的可见间隙问题 ([MCPE-55122](https://bugs.mojang.com/browse/MCPE-55122))
- 修正了工作台输出槽的对齐问题 ([MCPE-143255](https://bugs.mojang.com/browse/MCPE-143255))
- 降低了附魔物品上闪光的默认可见度，现在可以在辅助功能设置中调整 ([MCPE-167814](https://bugs.mojang.com/browse/MCPE-167814))

## **稳定性与性能**

- 修复了无效的旗帜图案导致渲染距离内的玩家崩溃的漏洞 ([MCPE-164478](https://bugs.mojang.com/browse/MCPE-164478))

## **触控控制**

- 修复了使用触控输入时物品可能卡在工作台中的问题
- 如果玩家在水下且启用了自动跳跃，当他们接近比当前层高1级的方块时，会自动上升。这也允许玩家自动从水中跳到陆地上

## **用户界面**

- 在使用Pocket UI时，为物品栏屏幕中的物品栏标签添加了标题和标题
- 增加了设置屏幕中标题之间的间距以提高可读性
- 触控板滚动方向现在与操作系统的滚动方向一致

## **原版趋同**

- 重命名和附魔武器现在在重生和聊天窗口中以颜色显示，当玩家被使用它的实体杀死时 ([MCPE-162679](https://bugs.mojang.com/browse/MCPE-162679))
- 测重压力板现在发出的声音与Java版相同 ([MCPE-164912](https://bugs.mojang.com/browse/MCPE-164912))
- 移除了记分板记分项名称和记分项显示名称的字符限制 ([MCPE-165064](https://bugs.mojang.com/browse/MCPE-165064))
- 西瓜和南瓜现在可以在泥土、灰化土、缠根泥土和沾泥的红树根上生长
- 菌岩方块现在在创造模式的物品栏中与下界岩分组 ([MCPE-163587](https://bugs.mojang.com/browse/MCPE-163587))
- 盔甲架在使用/kill命令被杀死时现在会无声消失 ([MCPE-159136](https://bugs.mojang.com/browse/MCPE-159136))

## **生物**

- 生物现在只有在比船本身小的情况下才能进入船
- 村民在完成成功交易时现在会生成绿色粒子
- 生物在被喂食繁殖材料时不再播放玩家进食的声音
- 稍微减少了熊猫的碰撞箱以匹配Java版
- 稍微增加了北极熊的碰撞箱以匹配Java版
- 海龟现在可以进入带箱子的船和没有箱子的船 ([MCPE-65719](https://bugs.mojang.com/browse/MCPE-65719))
- 疣猪兽、北极熊和蜘蛛现在不能再进入带箱子的船和没有箱子的船 ([MCPE-161197](https://bugs.mojang.com/browse/MCPE-161197))

## **命令**

- 当第二个或后续子命令目标选择器出错时，/execute命令现在会显示适当的错误消息 ([MCPE-164304](https://bugs.mojang.com/browse/MCPE-164304))
- 为方块状态提供自动完成支持
- 为/summon命令添加了两个新的重载：
  - /summon \[spawnPos : x y z\] 面向 \<position: x y z\> \[spawnEvent: string\] \[nametag: string\]
  - /summon \[spawnPos : x y z\] 面向 \<lookAtEntity: target\> \[spawnEvent: string\] \[nametag: string\]
- 修复了命令方块UI中粘贴按钮在粘贴失败后会记忆额外按压的问题 ([MCPE-163705](https://bugs.mojang.com/browse/MCPE-163705))

# **技术更新**

## **基岩编辑器**

编辑器处于早期开发阶段，可在Windows PC基岩预览版本上通过键盘/鼠标使用。它是一个引擎内的、多方块编辑体验，旨在让所有技能水平的创作者都能轻松打造高质量的基岩体验！我们正在努力添加更多功能，并将根据像你这样的创作者的反馈进行重大更改。

- 学习 [如何使用](https://aka.ms/LearnEditor) 编辑器
- 加入我们的讨论论坛，发布漏洞，查看更详细的更新说明，并在 [GitHub](https://github.com/Mojang/minecraft-editor) 上分享你的创作
- 在社交渠道上使用 **#BedrockEditor** 标签

## **游戏事件**

- *item_interact_finish* 游戏事件现在的震动频率为2，而不是14
- *item_interact_start* 不再被视为可检测的震动
- 收杆钓鱼竿现在会发出 *projectile_shoot* 震动

## **数据驱动组件**

- 为投射物数据添加了“lose_target”字段，以指定实体在发射投射物后是否应取消选择其目标
- 为方块添加了一个新的变换组件，支持旋转、缩放和平移。该组件可以添加到整个方块和/或单个方块排列。例如：

```json
"minecraft:transformation": {  
    "translation": [0.0, 0.1, -0.1],  
    "scale": [0.5, 1, 1.5],  
    "rotation": [90, 180, 0]  
}
```

- 变换后的几何体仍然具有非变换几何体的相同限制，例如最大大小为30/16单位

## **附加包与脚本引擎**

- 某些树特征JSON中用于一些树干和树叶的机会信息类型现在允许机会为0（之前允许0.0001，但不允许0）

## **实体过滤器**

- 创建了新的实体过滤器“is_raider”以确定主体是否是袭击的一部分

## **方块**

- 废弃了 *minecraft:part_visibility* 方块组件
- 为 *minecraft:geometry* 方块组件添加了 *bone_visibility* 行为

## **市场**

- 在地图WDW Magic Kingdom中，大雷山、白雪公主与七个小矮人以及太空山上的矿车现在可以正确对齐它们附加的隐形矿车

## **服务器**

- 方块现在可以选择性地（通过StartGamePacket中的设置）使用其网络ID的哈希值。此哈希值独立于所有其他方块，并在未来的版本中保持稳定

## **用户界面**

- 暂停菜单中的反馈按钮现在会在重定向到浏览器之前提示用户一个模态窗口

# **实验性技术功能**

## **API**

- 更新版本以将新API添加到稳定版：
  - 添加了 @minecraft/server 的1.1.0版本
  - 添加了 @minecraft/server 的1.2.0-beta版本
  - 移除了 @minecraft/server 的1.1.0-beta版本
  - 将以下内容移动到 @minecraft/server 稳定版（1.1.0）
    - runTimeout
    - runInterval
    - clearRun
    - currentTick
    - Vector3
    - BlockPermutation（仅部分功能）
    - Block
    - getBlock
    - sendMessage
    - sendMessage

  - Minecraft运行时错误现在作为JavaScript Error对象而不是字符串触发
  - 修复了多个基类继承问题，并为某些类类型添加了几个新的基类
  - /reload 在脚本包引用客户端RP时有效
  - 修复了 *BeforeItemUseOnEvent* 函数 *getBlockLocation* 返回undefined的问题 ([MCPE-166945](https://bugs.mojang.com/browse/MCPE-166945))
  - *BeforeItemUseOnEvent* 类现在继承自 *ItemUseOnEvent*
  - 将以下内容移动到 @minecraft/server 稳定版（1.0）
  - 修复了当消息包含Unicode引号时 *sendMessage* 失败的漏洞
  - 标志
    - 添加了 *setText* 以使用常规字符串、*RawMessage* 或 *RawText* 设置标志上的文本
    - 添加了 *getText* 以获取标志上的字符串，如果使用 *RawMessage* 或 *RawText* 调用 *setText*，将返回undefined
    - 添加了 *getRawText* 以获取标志上的 *RawText*，如果使用字符串调用 *setText*，将返回undefined
    - 添加了 *getTextDyeColor* 和 *setTextDyeColor* 以读取/写入标志文本的染料颜色
  - 染料
    - 添加了 *DyeColor* 枚举
  - sendMessage
    - *rawtext* 现在是 *RawMessage[]* 而不是 *(string | RawMessage)[]*
  - RawMessage
    - *rawtext* 属性在 *RawMessage* 上不再是 *(string | RawMessage)* 而是 *RawMessage[]*
  - RawText
    - 添加了一个 *RawText* 类，用于读取标志上的 *RawMessage*
  - 骑乘
    - 添加了 *getRiders* 到 *EntityRideableComponent*，返回当前骑乘此实体的所有实体的数组
    - 添加了 *EntityRidingComponent* - 此组件仅存在于当前骑乘其他实体的实体上
      - 具有 *entityRidingOn* 属性，返回此实体当前骑乘的实体
    - 添加了函数 *getEntity(id: string): Entity | undefined* - 获取一个实体。对于不存在或未加载的实体，返回undefined
  - 维度
    - getEntities
      - 修改返回类型为 *Entity[]*
      - 修改参数名为 *options*
      - 新签名：*getEntities(options?: EntityQueryOptions): Entity[]*
    - getPlayers
      - 修改返回类型为 *Player[]*
      - 修改参数名为 *options*
      - 新签名：*getPlayers(options?: EntityQueryOptions): Player[];*
    - @minecraft/server-ui
      - 在构建表单时，所有只读的面向用户的字符串（例如文本标签、下拉选项等）现在接受 *RawMessage*。这影响以下类：
        - *ActionFormData*
        - *ModalFormData*
        - *MessageFormData*
      - 添加了函数 *getItemStack(amount?: number, withData?: boolean): ItemStack* - 获取方块的物品堆栈。对于没有对应物品的方块（例如空气），返回undefined
    - BlockPermutation
      - 添加了函数 *getItemStack(amount?: number): ItemStack* – 创建方块排列的物品堆栈。对于没有对应物品的方块（例如空气），返回undefined
      - 移除了数据 *property*
    - BlockComponent
      - 添加了只读属性 *block* - 获取附加此组件的方块
    - 将 *IEntityComponent* 重命名为 *EntityComponent*
    - 容器
      - 用 *Container* 替换了类 *BlockInventoryComponentContainer*、*InventoryComponentContainer* 和 *PlayerInventoryComponentContainer*
      - 函数 *addItem* 现在如果容器已满，则返回添加物品堆栈的剩余部分，否则返回 *undefined*
      - 函数 *transferItem* 不再接受目标槽位，现在将给定物品放置在第一个可用槽位。该函数现在如果容器已满，则返回物品堆栈的剩余部分，否则返回 *undefined*
      - 添加了函数 *moveItem(fromSlot: number, toSlot: number, toContainer: Container): void* - 将物品从一个容器移动到另一个容器，替换目标槽位中的任何物品
      - 函数 *swapItems* 现在可以交换空槽位
      - 移除了函数 *clearItem* - 请改用 *setItem(undefined)*