---
标题: Minecraft Beta - 1.16.0.53  (Xbox One/Windows 10/Android)
日期: 2020-03-25T15:39:07Z
更新: 2020-03-26T15:38:31Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360041459831-Minecraft-Beta-1-16-0-53-Xbox-One-Windows-10-Android
---

在参与Minecraft Beta之前，请阅读以下内容：

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。有关加入或退出测试版的详细说明，请参见[ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

** **

**注意：** 此测试版是完整下界更新的一个正在开发中的版本。在Java版快照中看到的一些功能可能尚未出现。

** **

## **崩溃与稳定性**

- 修复了游戏过程中可能发生的多个崩溃
- 修复了在分屏模式下，主机保存并退出游戏时可能发生的崩溃
- 修复了使用某些自定义角色创建皮肤时的稳定性问题
- 改进了与物品展示框中地图相关的性能（[REALMS-1532](https://bugs.mojang.com/browse/REALMS-1532)）

## **常规**

- 对基岩专用服务器文档进行了多项更新和修复（[BDS-1084](https://bugs.mojang.com/browse/BDS-1084)，[BDS-2341](https://bugs.mojang.com/browse/BDS-2341)，[BDS-3141](https://bugs.mojang.com/browse/BDS-3141)，[BDS-3051](https://bugs.mojang.com/browse/BDS-3051)，[BDS-1085](https://bugs.mojang.com/browse/BDS-1085)）
- 修复了在Gear VR上导入的世界模板（.mctemplate）不可见的问题
- 修复了与领域中区块未正确加载相关的问题（[REALMS-2037](https://bugs.mojang.com/browse/REALMS-2037)）
- 修复了“Alex”模型的皮肤纹理问题

## **游戏玩法**

- 修复了村民目标的问题，导致其无法正常工作
- 新创建的地图现在以正确的缩放级别开始（[MCPE-63416](https://bugs.mojang.com/browse/MCPE-63416)）
- 修复了来自转换“版本”世界的地图缩放不正确的问题（[MCPE-58796](https://bugs.mojang.com/browse/MCPE-58796)）
- 修复了剪羊毛时未更新为剪过的绵羊模型的纹理问题（[MCPE-63188](https://bugs.mojang.com/browse/MCPE-63188)）
- 修复了一些附魔未正确工作的相关问题（[MCPE-63124](https://bugs.mojang.com/browse/MCPE-63124)）
- 修复了音乐唱片名称未以正确语言显示的问题

## **图形**

- 修复了通过其他透明物体（如玻璃）渲染告示牌文本时出现的问题（[MCPE-55327](https://bugs.mojang.com/browse/MCPE-55327)）
- 修复了物品展示框中的地图在加载之前闪烁紫色和黑色图像的问题
- 动画缩放现在在关键帧之间使用线性插值

## **附加包和脚本**

- 使用渲染控制器切换到不同几何体时，现在会立即在游戏中更改几何体
- 修复了带有空标签作为参数的选择器 @e\[tag=\] 和 @e\[tag=!\] 的问题