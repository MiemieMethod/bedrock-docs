---
标题: Minecraft Beta & Preview - 1.19.20.23
日期: 2022-07-20T13:37:29Z
更新: 2022-07-20T20:09:27Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/7814091998989-Minecraft-Beta-Preview-1-19-20-23
---

**发布于:** 2022年7月20日

## **关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![一张Minecraft截图，显示在远古城市中增加的幽匿斑块。](https://feedback.minecraft.net/hc/article_attachments/7814071288845/beta19U2_3_1600x900.jpg)

以下是本周Minecraft预览版和测试版的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，访问[bugs.mojang.com](http://bugs.mojang.com/)并向我们发送[您的反馈](https://aka.ms/MinecraftBetaFeedback)。

# **新特性和漏洞修复**

## **辅助功能特性**

- D-Pad左键现在可以再次按住以在菜单中向左移动光标（[MCPE-155976](https://bugs.mojang.com/browse/MCPE-155976)）

## **方块**

- 将幽匿催发体的经验掉落从20减少到5
- 红树原木、红树木和去皮红树木现在可以用来制作带木炭的营火（[MCPE-157271](https://bugs.mojang.com/browse/MCPE-157271)）

## **深暗之域**

- 远古城市中的幽匿斑块生成更加频繁（[MCPE-154229](https://bugs.mojang.com/browse/MCPE-154229)）
- 幽匿斑块地物现在可以放置在额外的方块类型上（[MCPE-156669](https://bugs.mojang.com/browse/MCPE-156669)）

## **游戏玩法**

- 玩家纹理和用户界面元素在高度拥挤的服务器上长时间游戏后不再变成粉色（[MCPE-105487](https://bugs.mojang.com/browse/MCPE-105487)）
- 瞬时效果（药水、药箭）不再可以施加于死亡的生物和玩家
- 玩家进入下界传送门时，如果传送门放置在Y=-21或更低的位置，将不再受到伤害（[MCPE-154888](https://bugs.mojang.com/browse/MCPE-154888)）

## **通用**

- 现在在玄武岩三角洲播放《So Below》音乐曲目（[MCPE-70890](https://bugs.mojang.com/browse/MCPE-70890)）
- 修复了记分板上的分数未正确排序的问题（[MCPE-141427](https://bugs.mojang.com/browse/MCPE-141427)）

## **物品**

- 修复了一个漏洞，导致使用/kill命令击杀时鱼钩掉落战利品（[MCPE-142329](https://bugs.mojang.com/browse/MCPE-142329)）

## **生物**

- 修复了一个导致拥有*minecraft:behavior.sleep*目标的幼年生物的击中箱缩小的漏洞（[MCPE-46040](https://bugs.mojang.com/browse/MCPE-46040)）
- 悦灵和蜜蜂现在不太可能卡在非完整方块中（[MCPE-155777](https://bugs.mojang.com/browse/MCPE-155777)）
- 监守者现在可以检测到在幽匿感测体上潜行的玩家（[MCPE-155804](https://bugs.mojang.com/browse/MCPE-155804)）
- 监守者现在可以让自己下落最多20个区块，而不仅仅是3个（[MCPE-158304](https://bugs.mojang.com/browse/MCPE-158304)）
- 悦灵现在可以拾取耐久度不同于其持有物品的盔甲（[MCPE-158339](https://bugs.mojang.com/browse/MCPE-158339)）

## **玩家**

- 玩家在灵魂沙上现在可以正确激活和取消灵魂疾行（[MCPE-157152](https://bugs.mojang.com/browse/MCPE-157152)）
- 修复了一个导致health_boost显示不正确生命值的漏洞，导致玩家死亡时变得隐形并无法与世界互动

## **稳定性和性能**

- 修复了一个可能导致生物无法加载到世界中的漏洞，如果它们的保存y位置大于或等于25

### **音频**

- 在交易时，村民根据输入槽中的物品播放正确的声音（[MCPE-152555](https://bugs.mojang.com/browse/MCPE-152555)）

## **原版趋同**

- 远古城市中的骷髅头现在更好地匹配Java版中的方向（[MCPE-153547](https://bugs.mojang.com/browse/MCPE-153547)）
- 山羊角的声音现在在设置中的唱片机/音符盒声音类别中（[MCPE-154885](https://bugs.mojang.com/browse/MCPE-154885)）

# **技术更新**

## **附加包**

- 在根定义中启用事件过滤器，以便在指定*format_version*为1.19.20或更高时独立于顺序或随机化进行评估

## **稳定性和性能**

- 修复了在Xbox和PlayStation的市场中浏览多个类别时可能导致崩溃的问题

# **实验性技术特性**

## **GameTest框架**

- 系统事件
  - 添加事件*beforeWatchdogTerminate* - 当发生关键脚本异常（例如脚本挂起）时关闭服务器。可以取消以防止关闭
  - 添加枚举*WatchdogTerminateReason* - 指定监视器终止的原因
  - 为基岩专用服务器的监视器配置添加新属性到*properties*
    - *script-watchdog-enable-exception-handling* - 通过*events.beforeWatchdogTerminate*事件启用监视器异常处理（默认值 = true）
    - *script-watchdog-enable-shutdown* - 在未处理的监视器异常情况下启用服务器关闭（默认值 = true）
    - *script-watchdog-hang-exception* - 当发生挂起时抛出关键异常（默认值 = true）

## **通用**

- 移除组件*minecraft:unwalkable*
- 将*'minecraft:explosion_resistance'*重命名为*'minecraft:destructible_by_explosion'*并重新结构化组件，使其可以定义为布尔值或对象
  - 将组件设置为true将使方块具有默认的*explosion_resistance*，将其设置为false将使方块无法被爆炸摧毁
  - 将组件设置为对象将允许用户定义方块对基础爆炸的抗性