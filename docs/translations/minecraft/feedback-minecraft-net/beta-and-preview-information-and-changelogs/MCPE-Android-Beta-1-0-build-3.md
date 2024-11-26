```markdown
---
title: MCPE 安卓测试版 - 1.0 构建 3
date: 2018-05-23T08:51:32Z
updated: 2018-05-23T22:17:07Z
categories: 测试版和预览信息及更新日志
tags:
  - 测试版
  - 安卓
  - mcpe
  - 1.0_build_3
link: https://feedback.minecraft.net/hc/en-us/articles/360004166371-MCPE-Android-Beta-1-0-build-3
---

请记住，此测试版仅适用于安卓。针对其他平台的错误修复和更改将在此更新的完整版发布后生效。此外，我们建议所有测试版玩家在运行新的测试版构建前备份他们的存档。

**调整内容：**

- 调整了渲染区块缓存，现在在后台按需构建。
- 潜影贝的传送更加平滑。
- Boss的生命条现在正确更新和显示。
- 调整了鞘翅的飞行时间，使其在附魔耐久下的表现符合预期，同时调整了其他鞘翅耐久性问题。
- 移动了聊天消息的位置，以免覆盖生命值、盔甲等。
- 调整了末地的照明，使其不再颠倒。
- 调整了使用钓鱼竿钓鱼的时间，使其不会比其他版本更长。
- 在使用控制器的LB/RB切换菜单标签时，现在行为符合预期。
- 恢复了/locate命令，但仅适用于寻找要塞。
- 从清单验证屏幕中移除了加粗标题。
- 修复了末影龙的影子过于巨大的问题。
- 南瓜和西瓜种子的纹理现在正确渲染。
- 修复了水的照明问题。
- 在世界模板屏幕上添加了消息，告诉玩家如何将世界上传到你的领地。

 

**错误修复：**

- 熔炉和附魔台不再融化雪屋。
- 你可以骑乘被拴绳牵引的驯服马。
- 修复了紫颂树被破坏后顶部部分仍然显示的问题（即使该部分实际上已经不存在）。
- 修复了选择种子采集器后发生的崩溃。
- 修复了在Rift和Gear VR上尝试获取皮肤包和纹理包时出现“无法连接到商店”的消息，而不是能够获取它们的问题。
- 使用控制器的LB/RB在选项中选择标签时，现在正确高亮显示具有行为或资源包的任何标签。
- 修复了在末地诗篇中登出后重新登录且世界中存在全局实体时可能发生的崩溃。
- 栅栏门、昼夜传感器和侦测器不再阻止红石线信号的进一步传输。
- 即使周围有方块，末地烛现在也可以放置在方块的底部。
- 在无限世界中，将末影珍珠放置在末地传送门框架上时，末影之眼不再被复制。
- 修复了移动实体传送时怪物受到坠落伤害的错误。
- 垂直放置的末地烛现在可以摧毁掉落到它们上的受重力影响的方块。
- 当玩家在末地时，末影龙的音效不再出现在主世界中。
- 滑翔鞘翅现在可以通过跳跃或撞墙、爬梯子取消。
- 在第三人称视角下，当你在滑翔鞘翅时上下看时，角色不再看起来像在旋转。
- 修复了领地邀请和邀请通知的某些问题。
- 村民在被击中后不再异常快速移动。
- 修复了当主机玩家的一个已连接朋友离开局域网游戏时主机设备上的崩溃。
- 修复了附加图形调试器时可能发生的崩溃。
- 当末影龙头颅在手中时，纹理颜色不再改变。
- 被投掷药水攻击的末影人再次传送。
- 末地折跃喷泉现在在击败末影龙时总是出现。
- 在末影龙战斗中现在有Boss音乐。
- 放置在构建极限高度下方的方块的光照级别现在在方块被破坏后正确更新。
- 修复了当玩家通过末地传送门时末地崩溃的问题。
- 末影珍珠的音效现在正确播放并可听见。
- 水现在可以保护黑曜石块不被凋零者的生成爆炸摧毁。
- 隐身效果不再受玩家个人游戏模式更改的影响。
- 末地城市天花板上悬挂的潜影贝不再因窒息而死亡。
- 修复了玩家以近战攻击凋零者时发生的崩溃。
- 取消按钮现在出现在音乐下载对话框上。
- 修复了游戏启动时控制器有任何输入时发生的崩溃（仅安卓和Fire）。
- Gear VR快捷栏不再卡在视图中央（仅Gear VR）。
- 黏液块再次在手中时显示（仅VR）。
- 你不再可以通过物品展示框复制物品。
- 具有自定义UI纹理的全局纹理包现在在启动屏幕上应用，无需重启游戏。
- 末影龙的死亡序列现在在你主机游戏或在他人游戏中游玩时看起来相同。
- 你现在需要停止骑乘猪或矿车才能使用末地传送门前往末地。
- 末地传送门现在总是立即传送玩家（即使你飞入其中）。
- 附魔瓶和喷溅药水在投掷时不再在空中抖动。
- 修复了如果玩家在领地中下雨时睡觉，玩家醒来后雨继续下但视觉上已消失的问题。这使得看起来太阳没有烧焦僵尸/骷髅，火迅速熄灭且无解释地炼药锅神秘充满。现在它实际上会停止下雨！
- 村庄现在自然生成不同类型的村民，而不仅仅是农民。
- 黑曜石水晶周围的铁条笼现在在末影龙重生时会重新生成。
- 滞留药水现在有投掷声音。
- 所有种类的箱子在卡通、城市和自然纹理包中不再有闪烁的侧面。陷阱箱的前面在纹理包中现在也是正确的。
- 箭矢在击中不透明方块后不再变黑。
- 箭矢现在在击中关闭的潜影贝时会反弹，而不是消失。
- 高功率不透明方块与红石比较器的交互现在像其他版本一样工作。
- 压力板不再卡在按下的位置。
- 农民村民现在收获完全长成的胡萝卜和马铃薯。
- 潜影贝现在通过开合来举起受重力影响的方块，导致方块掉落而不是传送离开方块。
- 驴/骡/马现在对不同的食物有适当的反应。
- 如果你使用命令尝试给予玩家超过最大堆叠数量的物品堆，现在你只会获得一个最大堆叠的物品，而不会出现错误。
- 当玩家被潜影贝击中并飘浮时，玩家现在看到正确的飘浮效果图标。
- 无论你放置什么方块在叶子旁边，叶子块的外观现在保持一致。
- 修复了鞘翅激活延迟的错误。
- 修复了塑料、幻想、城市、卡通和自然纹理包的各种错误。
- 末地传送门和末地折跃门现在实现了迷雾效果。
- 当你尝试加入预0.16版本服务器时，现在会显示“无法连接：服务器过时”的消息，而不是错误的“已断开服务器连接”消息。
- 鞘翅现在有翻滚动画。
- 怪物现在无论方块类型如何都能正常行为（不再在半方块上旋转！）
- 被驯服的动物现在会在进入末地或下界时与玩家一起传送（如果它们没有坐下）。
- 村民不再卡在梯子上。
- 旧世界类型中无法激活末地传送门。
- 附魔物品再次具有闪光效果（仅VR）。
- 修复了在末地传送门旁站立时传送你进入末地传送门的错误。
- 放置在其他非完整方块旁的雪层不再删除相邻方块。
- 在生存模式下使用刷怪蛋现在会消耗一个蛋并从你的物品栏中移除。
- 修复了在召唤过程中从末影龙传送出去时发生的崩溃。
- 你不再可以轻易穿过潜影贝。
- 从领地下载的世界现在正确显示世界名称。
- 修复了当你多次选择领地邀请消息然后接受或拒绝邀请时发生的崩溃。
- “你尚未将任何人添加到你的好友列表！”的领地消息现在正确显示（仅安卓Galaxy平板）。
- 当打开物品栏时，快捷栏上的头部图标现在可见。
- 怪物不再在移动到床上时跳跃和旋转。
- 在沉浸模式下潜行/蹲下时，你可以看到视角的变化（仅VR）。
- 聊天消息现在只显示一次！
- 在删除物品时，UI性能不再随着使用时间变长而变差。
- 在使用控制器时，安卓和iOS设备上的滑块现在行为正常。
- 如果你在没有后退按钮的设备上点击屏幕，末地诗篇现在会出现跳过按钮。
- 无论你离末影龙有多远，末影龙都会继续移动/更新。
- 龙息云现在颜色正确。
- 我们在安卓上支持的所有文件扩展类型现在应该在Gear VR上正常工作（仅Gear VR）。
- 当在领地中时，饥饿条不再异常快速减少。
- 修复了在多人游戏中放置受重力影响的方块时的延迟问题。
- 紫颂果和末影珍珠现在有1秒的冷却时间。
- 当发射器装满滞留药水时，现在能正确发射它们（而不是在发射时神奇地将它们转变为鸡蛋！）
- 工具再次在破坏时发出破坏噪音（仅领地）。
- 当你尝试在生存模式中开采龙蛋时，龙蛋现在会传送。
- 修复了击打物体时的复制漏洞。
- 保存领地到设备时游戏不再挂起（仅领地）。
- 当你吃紫颂果时，你现在会被传送。
- 手持的方块不再比应有的更大。
- 如果你没有箭矢，弓现在无法再被拉回。
- 鱿鱼不再在到达水面时立即消失（仅领地）。
- 钻石现在可以在生成的铁匠箱中随机找到。
- 滞留药水的腐朽现在有正确的纹理。
- 修复了各种僵尸的错误。
- 修复了各种兔子的错误。
- 修复了各种紫颂树的错误。
- 如果你在白天击中蜘蛛，附近的蜘蛛也不会尝试攻击你。
- 你死亡时不再保留盔甲（它会像其他物品一样掉落）。
- 修复了潜影贝的生命值。
- 当你在熔岩中时，雨、烟粒子和阴影不再可见。
- 箱子不再卡在看起来像是打开的状态。
- 怪物再次生成带有附魔物品并具有适当的生成/掉落率。
- 末影螨在重新加载世界后不再获得超速。
- 不死怪物在接近凋零者时夜间不再燃烧。
- 末地折跃门在创建/使用时现在发出适当的光束。
- 从种子生成的世界现在在PE和Win 10之间完全一致。
- 修复了告示牌和怪物头颅，使其基于玩家相对于方块的朝向来放置方向。
- 现在可以听到猪鞍的声音。
- 你现在可以听到召唤凋零者的声音。
- 当你一次拾取多个经验球时，经验球不再环绕你的头部。
- 你创建的铁傀儡将不再攻击你。
- 不死怪物不再在末地燃烧。
- 当末影龙坐下时被箭矢击中，末影龙不再看起来像是受到火焰伤害。
- 资源包图片不再出现在你设备的图片库中（仅安卓）。
- 云不再渲染在云高度或以上的玩家上方。
- 潜影弹现在在被攻击时被销毁。
- 潜影贝现在造成正确的伤害量。
- 陷阱箱在你的物品栏、快捷栏或在世界中被掉落时，不再与普通箱子相同。
- 修复了当玩家下矿车后销毁矿车时发生的崩溃。
- 被驯服的动物在你受到药水伤害时不再受到伤害。
- 末影人不再因药箭施加的状态效果而受到影响（因为它们在被击中前已经传送离开）。
- 附魔的火焰弓和力量弓再次工作，并正确应用效果/伤害给怪物。
- 你不再可以用水摧毁末地传送门。
- 你现在可以从台阶走到上面有地毯的方块。
- 从发射器发射的箭矢现在可以再次被捡回。
- 船和矿车现在在被破坏时发出声音（仅MCPE）。
- 修复了当玩家在Xbox Live登录屏幕上反复点击“免费注册”按钮时发生的崩溃。
- 重新进入世界后，第一个快捷栏槽位不再总是高亮显示。
- 当你手持一件盔甲并右键点击，如果该槽位为空，它会装备该盔甲。
- 修复了在访问领地设置时发生的崩溃（仅领地）。
- 玩家现在可以在部分覆盖的床上睡觉而不会窒息。
- 恶魂的火球再次点燃方块。
- 末影人再次在受到伤害后传送。
- 当你因溺水受到伤害时，你再次听到声音。
- 你现在可以听到新鲜、热熔岩的沸腾声！
- 修复了物品在物品展示框中无法正确放置的错误。
- 修复了熔炉、发射器和投掷器在世界中、在手中或在物品展示框中掉落时的纹理。
- 修复了敌对怪物死亡时发生的崩溃。
- 现在只有潜影贝的壳在隐身状态效果下变为不可见。
- 凋零者现在会被伤害箭治愈。
- 末影螨现在在2分钟后消失，除非你用命名牌命名它们。
- TTS现在会读取say、tell和whisper命令的输出。
- 洞穴蜘蛛在攻击你时现在会施加中毒效果。
- /toggledownfall命令现在在领地中切换关闭雨（仅领地）。
- 你不再可以通过手动添加IP地址加入已禁用多人游戏的世界。
- 你现在可以再次在Fire TV上连接到Xbox Live账户（仅Fire TV）。
- 光标键现在在安卓设备上正常工作（仅安卓）。
- 修复了物品传输，使其自动移动物品堆叠（仅MCPE）。
- 酿造台现在即使没有在酿造，也不会继续看起来在酿造。
- 在Win 10上使用MCPE UI时，滚动不再改变快捷栏选择（仅Win 10）。
- 修复了骑乘动物/矿车时的延迟。
- 当使用触控控制并控制相机时，将鼠标悬停在聊天上不再阻止相机旋转。
- 破坏冰块时不再破坏其下方的方块。
- 修复了加载旧世界时的生物群系图形问题。
```