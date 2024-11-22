---
标题: Minecraft Beta & Preview - 1.19.30.20
日期: 2022-08-04T12:29:51Z
更新: 2022-08-04T15:46:03Z
类别: Beta 和预览信息及变更日志
链接: https://feedback.minecraft.net/hc/en-us/articles/8175535399181-Minecraft-Beta-Preview-1-19-30-20
---

**发布时间:** 2022年8月4日

## **Minecraft 预览和 Beta 信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft 预览可在 Xbox、Windows 10/11 和 iOS 设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta 版本可在 Android（Google Play）上使用。要加入或退出 Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![beta19U3_1_16x9.png](https://feedback.minecraft.net/hc/article_attachments/8175529065357/beta19U3_1_16x9.png)

以下是本周 Minecraft 预览和 Beta 的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，访问 [bugs.mojang.com](https://bugs.mojang.com/) 并向我们发送 [您的反馈](https://aka.ms/MinecraftBetaFeedback)。

# **原版趋同**

**一般**

- 末影人不再对创造模式玩家生气 ([MCPE-42977](https://bugs.mojang.com/browse/MCPE-42977))
- 修改了火球实体的碰撞箱以匹配 Java 版
- 附魔台在附魔物品时现在会发出声音
- 紫水晶块在跳下时不再发出声音

### **深暗之域**

- 增加了深暗之域和古代城市中幽匿尖啸体和幽匿感测体的生成率，以更好地匹配 Java 版 ([MCPE-153525](https://bugs.mojang.com/browse/MCPE-153525))

### **西瓜块**

- 修复了西瓜块底部纹理以匹配顶部纹理 ([MCPE-31035](https://bugs.mojang.com/browse/MCPE-31035))

### **生物**

- 修改了猫坐着时头部的位置以匹配 Java 版 ([MCPE-46668](https://bugs.mojang.com/browse/MCPE-46668))

### **用户界面**

- 物品堆叠弹出动画现在仅在新物品添加到堆叠时播放 ([MCPE-23995](https://bugs.mojang.com/browse/MCPE-23995))
- 如果村民有名牌，它现在会与他们的交易品质一起显示 ([MCPE-152644](https://bugs.mojang.com/browse/MCPE-152644))

### **旁观模式（实验性）**

- 末影人不再对旁观模式中的玩家生气 ([MCPE-156742](https://bugs.mojang.com/browse/MCPE-156742))
- 旁观模式中的玩家不再通过在水或熔岩中游泳与幽匿感测体互动 ([MCPE-153879](https://bugs.mojang.com/browse/MCPE-153879))
- 切换到旁观模式的玩家将解除与他们相关的鱼钩
- 旁观模式中的玩家不再会被爆炸推开 ([MCPE-156687](https://bugs.mojang.com/browse/MCPE-156687))
- 粉雪在旁观者穿过时不再发出粒子 ([MCPE-153876](https://bugs.mojang.com/browse/MCPE-153876))
- 大型垂滴叶在旁观模式中被玩家触碰时不再倾斜 ([MCPE-156686](https://bugs.mojang.com/browse/MCPE-156686))
- 旁观模式中的玩家在死亡时现在保留他们的物品栏和装备物品 ([MCPE-156681](https://bugs.mojang.com/browse/MCPE-156681))
- 旁观者不再能在持有他们喜欢的食物时吸引生物的注意 ([MCPE-153882](https://bugs.mojang.com/browse/MCPE-153882))
- /testfor 命令现在可以针对旁观者 ([MCPE-158042](https://bugs.mojang.com/browse/MCPE-158042))
- 旁观模式不再可以通过 /gamemode 6 命令进入，仅可通过 /gamemode spectator 进入
- 使用触控控制的旁观者不再能破坏船和矿车 ([MCPE-158307](https://bugs.mojang.com/browse/MCPE-158307))
- 河豚不再对附近的旁观者做出反应

# **功能和漏洞修复**

## **方块**

- 泥砖台阶现在可以通过命令作为顶层台阶放置 ([MCPE-157852](https://bugs.mojang.com/browse/MCPE-157852))

## **游戏玩法**

- 活塞在伸展和收缩时的动画现在更加流畅 ([MCPE-155987](https://bugs.mojang.com/browse/MCPE-155987))

### **边界方块**

- 边界方块现在应在所有高度上阻止通过

## **物品**

- 红树、猩红木和诡异木板现在可以用来修复盾牌 ([MCPE-158940](https://bugs.mojang.com/browse/MCPE-158940))

## **市场**

- “无法连接到市场”错误将不再被文本转语音阅读器错误地读取

## **生物**

- 修复了一个导致在拥有者玩家更换维度后，拴绳与悦灵断开的漏洞 ([MCPE-158955](https://bugs.mojang.com/browse/MCPE-158955))

### **山羊**

- 山羊的冲撞动画被修改为在准备冲撞时缓慢低下头 ([MCPE-129477](https://bugs.mojang.com/browse/MCPE-129477))

### **村民**

- 修复了一个偶尔导致村民的边界框与服务器不同步的漏洞

## **专用服务器**

- 添加了服务器属性 ‘disable-custom-skins’ 以在服务器范围内阻止不受信任的皮肤

## **稳定性和性能**

- 修复了一个在加载床上的玩家时偶尔崩溃的漏洞

## **用户界面**

- 修复了一个 UI 漏洞，其中附魔皮革物品的部分纹理未显示闪光动画 ([MCPE-98929](https://bugs.mojang.com/browse/MCPE-98929))
- 添加了新的断开连接错误消息，以更好地突出断开连接发生的区域

## **村庄**

- 袭击条在破坏床以取消袭击后不再卡住 ([MCPE-152851](https://bugs.mojang.com/browse/MCPE-152851))

# **技术更新**

## **活动对象属性**

- 数值活动对象属性（浮点数和整数）现在将始终将其值限制在指定的值范围内

## **附加包和脚本引擎**

- *minecraft:instant_despawn* 不再影响玩家

## **命令**

- 命令选择器现在获取与命令来源玩家位置相同的位置

## **市场**

- 修复了一个漏洞，文本转语音功能会读取整个“我的内容”页面，包括高亮和非高亮的物品

# **实验性功能**

## **命令**

- “/execute if block” 命令现在显示方块位置的整数值 ([MCPE-156285](https://bugs.mojang.com/browse/MCPE-156285))

## **GameTest 框架**

- 向量
  - 修复了一个漏洞，其中 *function* 长度返回未定义
  - 添加了 *lengthSquared* 函数 - 返回向量的平方长度
  - 添加了 *stackOverflow* 作为 *beforeWatchdogTerminate* 事件的可能 *WatchdogTerminateReason*
- IRawMessage - 表示消息的接口对象
  - rawtext : (字符串 \| IRawMessage)\[\] - （可选）用于构建消息的文本对象列表
  - text : 字符串 - （可选）包含直接显示的纯文本的字符串。仅在用作父 *rawtext* 或 *with* 成员的子成员时有效
  - translate : 字符串 - （可选）表示翻译标识符的字符串，用于翻译玩家选择语言中的文本
  - with : (字符串 \| IRawMessage)\[\] - （可选）用于填充 *translate* 文本中值的文本对象参数列表。当 *translate* 不存在时被忽略
  - say(字符串 \| IRawMessage) - 用于向所有玩家广播消息
  - tell(字符串 \| IRawMessage) - 向玩家发送消息
- 修复了一个漏洞，当使用在基岩专用服务器或领域上托管的世界时，动态属性不会持久化
- 对原生模块的包依赖可以使用模块名称声明，而无需指定 UUID，使用 “module_name” 属性。模块名称与导入语句匹配（例如，“mojang-minecraft”）
- 移除了 mojang-gametest 模块版本 0.1.0；使用 "mojang-gametest" 特定 API 的包必须更新为使用 GameTest 版本 1.0.0-beta
- "mojang-gametest" 模块 1.0.0-beta 需要 "mojang-minecraft" 模块 1.0.0-beta

## **一般**

- 移除了 *minecraft:unwalkable* 方块组件的使用，并向方块描述中添加了方块创造组和类别
