---
标题: Minecraft Beta - 1.16.0.61 (Xbox One/Windows 10/Android)
日期: 2020-05-14T14:49:38Z
更新: 2020-05-15T09:07:53Z
分类: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360043160912-Minecraft-Beta-1-16-0-61-Xbox-One-Windows-10-Android
---

**在参与Minecraft Beta之前，请务必阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的先前版本中打开，因此请备份世界以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。有关加入或退出测试版的详细说明，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

# 修复

**崩溃与稳定性**

- 修复了游戏过程中可能发生的多个崩溃
- 修复了在Samsung Galaxy S Duos 2上启动时的崩溃
- 修复了在末地可能发生的崩溃
- 当使用/kill命令时，龙重生时游戏不再崩溃
- 修复了在更改维度时可能发生的一些崩溃，包括带驯服动物通过传送门
- 使用带灵魂火的/fill命令不再导致游戏崩溃（[MCPE-65672](https://bugs.mojang.com/browse/MCPE-65672)）

**一般**

- 修复了重新加载穿着经典皮肤角色时的问题
- 改进了加载角色的可靠性（[MCPE-55968](https://bugs.mojang.com/browse/MCPE-55968)）
- 改进了角色的离线支持
- 在多人服务器上，经典皮肤现在在角色创建者皮肤之前加载
- 当上传和下载的世界文件大小超过最大值时，现在会出现错误消息
- 修复了在Windows 10上尝试导入可用空间有限的大世界时可能导致失败的问题

**游戏玩法**

- 更改了生物群落数量上限，仅计算具有生成规则的生物（[MCPE-54378](https://bugs.mojang.com/browse/MCPE-54378)）
- 生物的消失范围现在与模拟范围相关联（[MCPE-65570](https://bugs.mojang.com/browse/MCPE-65570)）
- 修复了在多人世界中，有时村民无法正确链接到工作地点的问题（[MCPE-49580](https://bugs.mojang.com/browse/MCPE-49580)）
- 修复了可能导致重叠村庄被反复创建和摧毁的问题
- 趋同：水现在从边缘开始结冰，与Java版一致
- 从高处摔落的伤害保护现在按预期工作（[MCPE-74561](https://bugs.mojang.com/browse/MCPE-74561)）
- 使用鞘翅以过快速度飞入未加载的区块不再导致因动能死亡（[MCPE-55671](https://bugs.mojang.com/browse/MCPE-55671)）
- 修复了峡谷与旧版本相比未正确定位的问题
- 修复了玩家在重生菜单关闭标题时能够复制物品的问题
- 掉落附有消失魔咒的物品现在正常工作（[MCPE-65649](https://bugs.mojang.com/browse/MCPE-65649)）
- 玩家现在只能在生存模式下使用铁砧附魔一个指南针
- 修复了在重新加载世界时，有时导致红石火把卡住的问题（[MCPE-48054](https://bugs.mojang.com/browse/MCPE-48054)）
- 修复了可能导致海带过早停止生长的问题 - 海带现在在尝试添加自身时检查刻队列中的方块（[MCPE-57330](https://bugs.mojang.com/browse/MCPE-57330)）
- 摔落缓冲和保护魔咒现在提供正确的玩家伤害保护（[MCPE-74561](https://bugs.mojang.com/browse/MCPE-74561)）

**生物**

- 鹦鹉不再卡在飞行模式（[MCPE-64370](https://bugs.mojang.com/browse/MCPE-64370)）
- 恐慌的生物现在对所有伤害类型都表现出恐慌
- 能够捡起盔甲的生物现在优先选择铁盔甲而非链甲

**方块**

- 墙现在可以连接到大多数放置在其上方的方块（[MCPE-65404](https://bugs.mojang.com/browse/MCPE-65404)）
- 下落的方块现在会被放置在活塞臂上方的部分方块破坏
- 当用精准采集工具开采蘑菇柄时，现在掉落正确的方块（[MCPE-69012](https://bugs.mojang.com/browse/MCPE-69012)）
- 目标方块的红石信号持续时间基于投射物类型，三叉戟和箭的持续时间较长，其他投射物较短（[MCPE-65413](https://bugs.mojang.com/browse/MCPE-65413)）
- 在重新加载世界时，红石火把不再卡住（[MCPE-48054](https://bugs.mojang.com/browse/MCPE-48054)）
- 命令方块的条件设置在通过结构方块复制时现在会被保存
- 修复了允许南瓜灯放置在方块侧面的问题，破坏了一些市场内容
- 蘑菇柄在被精准采集时不再掉落棕色蘑菇方块（[MCPE-69012](https://bugs.mojang.com/browse/MCPE-69012)）

**图形**

- 修复了更改渲染距离值后区块闪烁的问题
- 修复了导致地图变为不可见的问题（[MCPE-76166](https://bugs.mojang.com/browse/MCPE-76166)）
- 画作现在正确渲染（[MCPE-69652](https://bugs.mojang.com/browse/MCPE-69652)）
- 信标光束现在正确渲染（[MCPE-76224](https://bugs.mojang.com/browse/MCPE-76224)）
- 火焰动画现在在燃烧的生物和火焰箭上正确显示（[MCPE-76224](https://bugs.mojang.com/browse/MCPE-76224)）
- 修复了导致动画纹理无法正常工作的一个问题（[MCPE-76180](https://bugs.mojang.com/browse/MCPE-76180)）
- 修复了导致烟花粒子无法正确出现的问题（[MCPE-76341](https://bugs.mojang.com/browse/MCPE-76341)）
- 提示框背景和控制器光标现在正确渲染（[MCPE-76154](https://bugs.mojang.com/browse/MCPE-76154), [MCPE-76168](https://bugs.mojang.com/browse/MCPE-76168)）

**用户界面**

- 修复了导致附魔物品在光标移动时闪烁的问题
- 修复了尝试在线游戏时出现的无用错误消息，缺乏适当的账户权限
- 修复了在“您的领域即将更新”屏幕上按“返回”后卡在加载资源的问题
- 修复了在使用韩文或中文虚拟键盘时阻止原生文本/字符输入的问题（[MCPE-62596](https://bugs.mojang.com/browse/MCPE-62596)）
- 修复了告示牌上的文本超出告示牌边缘的问题（[MCPE-64315](https://bugs.mojang.com/browse/MCPE-64315)）
- 修复了在登录账户但没有网络连接时启动游戏时显示的账户错误号-9
- 趋同：铁砧现在显示“附魔费用”而不是“经验费用”
- 修复了在使用经典用户界面的触控控制时偶尔无法选择物品栏物品的问题

**命令**

- 修复了在大距离传送'tick_world'实体时可能导致其消失的问题
- 现在在将盔甲架传送到玩家时，会将盔甲架旋转到玩家的朝向（[MCPE-35979](https://bugs.mojang.com/browse/MCPE-35979)）

**附加包**

- 鞘翅现在是数据驱动的
- 几何体中的自定义骨骼现在尊重其自定义父骨骼的变换
- 修复了粒子生成的生命周期小于当前帧时间2倍时，粒子通常不会绘制的问题。这影响了高级采矿内容的幽灵轨迹，以及任何其他生命周期非常短的粒子内容