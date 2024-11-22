---
标题: Minecraft Beta & Preview - 1.21.10.23
日期: 2024-06-01T08:55:54Z
更新: 2024-06-11T23:05:19Z
类别: Beta 和预览信息及更改日志
链接: https://feedback.minecraft.net/hc/en-us/articles/27211163694861-Minecraft-Beta-Preview-1-21-10-23
哈希:
  h_01J04RJ2KRCJNNKPXM4YM2EN0F: 特性和漏洞修复
  h_01J04RJ2KRQERT77RSD0TWSG9Z: 方块
  h_01J04RJ2KRWG2M0M7X7B9DY7H6: 聊天
  h_01J04RJ2KR0EW07P85WHPSYZJD: 命令
  h_01J04RJ2KRT22SP56FEC8W7MWQ: 生物
  h_01J04RJ2KRC4094P7Q68J66S7E: 风弹
  h_01J04RJ2KRFBW8DH3YHF0RCXTA: 用户界面
  h_01J04RJ2KRRR3Z4Q9F9VFYCF3E: 技术更新
  h_01J04RJ2KRY718P62JEJ7SY3DJ: 附加包和脚本引擎
  h_01J04RJ2KRMBVP9DTJDZMTN4P2: API
  h_01J04RJ2KR5WR268EN1MWGF8R4: Molang
  h_01J04RJ2KRSK5C22S3KREEACYD: 实验性技术更新
  h_01J04RJ2KRD4JJEYH5TQCGVXDC: api-1
  h_01J04RJ2KSDZBHWCZ7EK0ATJFG: 方块-1
  h_01J04RJ2KSTQND7DJA12QWH2YB: 编辑器
---

**发布:** 2024年6月12日

**关于Minecraft预览和Beta的信息:**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、PlayStation 4、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

以下是最新的Minecraft: 基岩版Beta和预览更新中的新内容！请继续在[feedback.minecraft.net](https://feedback.minecraft.net/)提交您的建议，并在[bugs.mojang.com](https://bugs.mojang.com/)报告并投票您发现的任何漏洞！  

# **特性和漏洞修复:**

## **方块**

- 铜门现在遵循预期设计，仅在用石镐或更好的工具开采时掉落
- 在创造模式中，当顶部方块被开采时，门不再掉落
- 平滑石英台阶的纹理恢复正常（[MCPE-182104](https://bugs.mojang.com/browse/MCPE-182104)）
- 为生物生成器方块添加了破坏、掉落、击打、跳跃、着陆、放置和踩踏声音

## **聊天**

- 修复了使用“复制坐标”功能复制玩家坐标到剪贴板时出现的消息（[MCPE-182146](https://bugs.mojang.com/browse/MCPE-182146)）

## **命令**

- 修复了一个漏洞，/spreadplayers命令可能导致目标被传送到比预期位置低一格
- 为/spreadplayers命令添加了*最大高度*参数，允许您指定扩散发生的最大高度

## **生物**

- 狼、熊和熊猫在受到环境伤害（例如：火、熔岩、冰冻）时会惊慌并试图避免危险

## **风弹**

- 风弹在所有地形上的效果现在一致
- 蹲下不再影响风弹的击退/跳跃量
- 玩家直下方使用的风弹现在将玩家向上击退约6格，而不是约2.5格
- 使用风弹时与延迟相关的掉落伤害发生的频率降低
- 风弹的发射位置已调整，不再距离玩家过远

## **用户界面**

- 修复了暂停屏幕上Realms Stories按钮的未读徽章未更新的漏洞
- 安全区屏幕位置现在在关闭菜单时正确保存
- 当您悬停在安全区屏幕文本上时，文本不再被遮挡
- 安全区屏幕滑块即使值仅更改0.1也能正确保存
- 安全区屏幕位置滑块现在根据缩放滑块正确重置和缩放
- 在iOS上，当安全区屏幕设置为最小值时不再出现错误
- 修复了市场物品描述中标签垂直显示的问题
- 修复了市场“我的内容”部分缺失纹理的问题（[MCPE-181964](https://bugs.mojang.com/browse/MCPE-181964)）
- 游戏提示现在以“淡入”和“淡出”动画的形式出现在屏幕上并消失
- 将市场通行证渐变替换为实心灰色以提高可读性  

# **技术更新:**

## **附加包和脚本引擎**

- 修复了粒子效果生命周期事件时间线未按预期触发事件的问题

## **API**

- 修复了重新加载物品自定义组件时错误出现警告的问题
- EntityTameMountComponent
  - 将方法*tameToPlayer*和只读属性*tamedToPlayerId*、*tamedToPlayer*、*isTamed*、*isTamedToPlayer*从*beta*移至*1.12.0*
- 将*System*上的*runJob*方法从*beta*移至*1.12.0*
- 将*System*上的*clearJob*方法从*beta*移至*1.12.0*
- 将*System*上的*waitTicks*方法从*beta*移至*1.12.0*
- @minecraft/server-ui
  - 发布版本*1.2.0*
  - 添加新*beta*版本*1.3.0*
  - 将*ModalFormData*上的*submitButton*方法从*beta*移至*1.2.0*

## **Molang**

- 修复Molang内容错误以包含记录消息中的表达式  

# **实验性技术更新:**

## **API**

- *WorldInitializeBeforeEvent*
  - 将属性*blockTypeRegistry*重命名为*blockComponentRegistry*
- 将*BlockComponentRegistry*从*beta*移至*1.12.0*
- 将*BlockCustomComponentAlreadyRegisteredError*从*beta*移至*1.12.0*
- 将*BlockCustomComponentReloadVersionError*从*beta*移至*1.12.0*
- 将*BlockCustomComponentReloadNewEventError*从*beta*移至*1.12.0*
- 将*BlockCustomComponentReloadNewComponentError*从*beta*移至*1.12.0*
- 将*BlockCustomComponent*从*beta*移至*1.12.0*
- 将*BlockComponentStepOnEvent*从*beta*移至*1.12.0*
- 将*BlockComponentTickEvent*从*beta*移至*1.12.0*
- 将*BlockComponentRandomTickEvent*从*beta*移至*1.12.0*
- 将*BlockComponentEntityFallOnEvent*从*beta*移至*1.12.0*
- 将*BlockComponentStepOffEvent*从*beta*移至*1.12.0*
- 将*BlockComponentPlayerInteractEvent*从*beta*移至*1.12.0*
- 将*BlockComponentPlayerPlaceBeforeEvent*从*beta*移至*1.12.0*
- 将*BlockComponentPlayerDestroyEvent*从*beta*移至*1.12.0*
- 将*BlockComponentOnPlaceEvent*从*beta*移至*1.12.0*
- 添加四种用于自定义方块组件注册的新错误类类型
  - *ScriptBlockCustomComponentAlreadyRegisteredError* - 当注册自定义方块组件时，发现其已被注册
  - *ScriptBlockCustomComponentReloadVersionError* - 当注册自定义方块组件时，发现其在重新加载时脚本版本不同
  - *ScriptBlockCustomComponentReloadNewEventError* - 当注册自定义方块组件时，发现其在重新加载时实现了新事件
  - *ScriptBlockCustomComponentReloadNewComponentError* - 当注册自定义方块组件时，发现其在重新加载时存在新组件
- 将*Block::getMapColor*绑定到脚本方块API（Beta）

## **方块**

- *minecraft:custom_components*不再需要Beta APIs实验
- *minecraft:entity_fall_on*不再需要Beta APIs实验
- *minecraft:tick*不再需要Beta APIs实验

## **编辑器**

- 在内置UI主题中，光标颜色与字体默认颜色匹配