---
标题: Minecraft Beta - 1.9.0.0 (Xbox One/Windows 10/Android)
日期: 2018-11-14T00:25:39Z
更新: 2018-11-15T17:21:41Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360019773811-Minecraft-Beta-1-9-0-0-Xbox-One-Windows-10-Android
---

2018年11月15日

## 请在参与Minecraft Beta之前阅读：

- 您将无法访问Realms，并且在预览Beta时无法加入非Beta玩家。特色服务器可能也不可用。
- Beta仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出Beta，请参见<u>[ms/JoinMCBeta](http://aka.ms/JoinMCBeta)</u>以获取详细说明。
- Beta版本可能不稳定，并且不代表最终版本的质量。请在加入Beta之前备份您的世界。
- 完成的版本可能不包括所有Beta中的新功能、变化和修复，以保持稳定性，并可能推迟到后续版本。

注意：此特定Beta版本可能在某些Android设备上不可用。

## **实验性游戏玩法：**

（仅在世界设置中启用实验性游戏玩法时可用）

- 掠夺者
- 竹子现在在丛林生物群系中生成

## **新功能：**

- 新增花卉：铃兰和矢车菊
- 新增云杉、白桦、丛林、金合欢和深色橡木告示牌
- 新增楼梯、台阶和墙体变种：
  - 石头楼梯和台阶
  - 花岗岩楼梯、台阶和墙
  - 磨制花岗岩楼梯和台阶
  - 闪长岩楼梯、台阶和墙
  - 磨制闪长岩楼梯和台阶
  - 安山岩楼梯、台阶和墙
  - 磨制安山岩楼梯和台阶
  - 砂岩墙
  - 平滑红砂岩楼梯和台阶
  - 平滑石英楼梯和台阶
  - 红砖墙
  - 石砖墙
  - 苔石砖楼梯、台阶和墙
  - 下界砖墙
  - 末地石砖楼梯、台阶和墙
  - 海晶石墙
  - 红砂岩墙
  - 红色下界砖楼梯、台阶和墙
  - 平滑砂岩楼梯和台阶
  - 苔石楼梯和台阶
- 新增/gamerule命令中的新选项showDeathMessages，允许玩家选择在玩家或驯服生物死亡时是否在聊天中显示消息
- 新增“即时重生”选项及相关/gamerule
- 新增/tellraw命令，启用使用原始文本格式化以通过JSON将可翻译文本输出发送到聊天

## **更改：**

- 新增多个由社区建议的新加载屏幕提示和小知识！
- 当驯服动物死亡时，现在会向聊天发送通知（[MCPE-35138](https://bugs.mojang.com/browse/MCPE-35138)）
- 绊线在被破坏时现在会被激活，除非使用剪刀破坏
- 使用函数命令时性能有所改善；它们现在在世界重新加载时被预编译

## **修复：**

- 修复了游戏过程中发生的崩溃
- 修复了在用铁门替换木门时可能发生的崩溃（[MCPE-37941](https://bugs.mojang.com/browse/MCPE-37941)）
- 修复了在对装满成书的箱子使用取块时可能发生的崩溃
- 更新了低磁盘空间错误消息
- 持有的物品在更改资源包时现在显示正确的纹理（[MCPE-38302](https://bugs.mojang.com/browse/MCPE-38302)）
- 修复了触控控制，使玩家在水下不再卡在潜行位置（[MCPE-38212](https://bugs.mojang.com/browse/MCPE-38212)）
- 修复了熊猫喂食动画
- 在触摸屏设备上与方块或生物互动时，弩不再意外发射（[MCPE-38321](https://bugs.mojang.com/browse/MCPE-38321)）
- 现在可以使用弩击打生物（[MCPE-38314](https://bugs.mojang.com/browse/MCPE-38314)）
- 投掷三叉戟的动画不再与新的弩动画混淆（[MCPE-38358](https://bugs.mojang.com/browse/MCPE-38358)）
- 修复了在触摸屏设备上尝试发射弩时破坏方块的问题（[MCPE-38465](https://bugs.mojang.com/browse/MCPE-38465)）
- 新增缺少模板的世界通知，并在必要时提示重新从商店下载相关模板
- 改进了在各种字段中的文本输入 - 文本框可以使用键盘高亮和选择
- 皮肤选择菜单现在仅在在线时显示进度/加载动画
- 修复了在手持模式下在任天堂Switch上保存购买时缺少“保存到Microsoft账户”消息
- 玩家在多人游戏中不再能更改自定义玩家权限
- 修复了使用相对坐标的剩余命令，y坐标低于3的情况（[MCPE-35130](https://bugs.mojang.com/browse/MCPE-35130)）
- 潜影盒在打开时现在会推动生物（[MCPE-22480](https://bugs.mojang.com/browse/MCPE-22480)）
- 在尝试加入不可用世界时，错误消息现在更具信息性
- 修复了可能导致在触摸屏设备上突然改变方向的剩余问题（[MCPE-35910](https://bugs.mojang.com/browse/MCPE-35910)）
- 下落方块实体现在可以使用命令被杀死（[MCPE-38300](https://bugs.mojang.com/browse/MCPE-38300)）
- 击败末影龙现在掉落正确数量的经验，并在转换的世界中生成龙蛋（[MCPE-28864](https://bugs.mojang.com/browse/MCPE-28864)）
- 使用精准采集工具收集的藤蔓可以在旗帜设计中正确使用（[MCPE-35134](https://bugs.mojang.com/browse/MCPE-35134)）
- 末地折跃门现在即使目标区域已经生成也能正常工作（[MCPE-19699](https://bugs.mojang.com/browse/MCPE-19699)）
- 丢弃的物品现在被台阶和玻璃正确位移（[MCPE-12025](https://bugs.mojang.com/browse/MCPE-12025)）
- 使用控制器或键盘时改进市场导航
- 修复了加勒比海盗混搭包中“Syrena”皮肤的游泳动画
- 循环型命令方块在克隆时现在保持“始终激活”状态（[MCPE-36340](https://bugs.mojang.com/browse/MCPE-36340)）
- 时钟和指南针物品在加入世界时现在正确加载（[MCPE-36952](https://bugs.mojang.com/browse/MCPE-36952)）