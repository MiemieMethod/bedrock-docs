---
标题: Minecraft Beta - 1.16.210.58 (Xbox One/Windows 10/Android)
日期: 2021-02-03T16:33:40Z
更新: 2021-02-03T16:47:28Z
分类: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360056026212-Minecraft-Beta-1-16-210-58-Xbox-One-Windows-10-Android
---

**发布于:** 2021年2月3日

**请在参与Minecraft Beta之前阅读：**

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览Beta时无法加入非Beta玩家
- 在Beta期间游玩的任何世界无法在游戏的先前版本中打开，请务必备份世界以防丢失
- Beta构建可能不稳定，并不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

本周的Beta中有许多漏洞修复！感谢您迄今为止提供的所有反馈和漏洞报告！请将您的洞穴与悬崖的想法和反馈发送至[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索并报告您可能遇到的任何新漏洞。

 

![img_656.JPG](https://feedback.minecraft.net/hc/article_attachments/360084662732/img_656.JPG)

 

## **漏洞修复**

**辅助功能**

- 屏幕阅读器现在正确宣布个人资料屏幕上每个角色的编辑/创建角色按钮文本

**性能与稳定性**

- 修复了在游戏过程中可能发生的多个崩溃
- 修复了在反锯齿设置为1时打开成就屏幕可能发生的崩溃（[MCPE-110164](https://bugs.mojang.com/browse/MCPE-110164)）

**常规**

- 修复了刻未影响方块状态变化的问题——这意味着作物和树苗将再次正确生长（[MCPE-116221](https://bugs.mojang.com/browse/MCPE-116221)）
- 修复了玩家在生存模式下用工具破坏方块后无法与物品栏中的工具互动的问题（[MCPE-115341](https://bugs.mojang.com/browse/MCPE-115341)）
- 修复了干海带块底部和携带纹理，使绳子像素对齐（[MCPE-35476](https://bugs.mojang.com/browse/MCPE-35476)）
- 修复了雪在某些模拟距离下以线状积累的问题（[MCPE-73468](https://bugs.mojang.com/browse/MCPE-73468)）
- 被水淹没的TNT将再次在生存模式下将玩家发射出去
- 修复了成就名称和描述无法翻译的问题，与语言选择无关（[MCPE-85813](https://bugs.mojang.com/browse/MCPE-85813)）
- 邀请屏幕上跨平台好友的在线状态将在检测到变化时更新（[MCPE-70004](https://bugs.mojang.com/browse/MCPE-70004)）
- 修复了在更改语言设置后成就奖励未正确显示的问题
- 拥有和可购买的皮肤在离线时不再混入不同类别
- 表情标题在重新进入标签时不再显示之前预览的表情
- 更新了游戏内链接到反馈网站和漏洞追踪器

**图形**

- 山羊和其他染色刷怪蛋在手中持有时现在看起来正确（[MCPE-104145](https://bugs.mojang.com/browse/MCPE-104145)）
- 修复了可能在调整窗口大小时闪烁的屏幕分辨率问题（[MCPE-69721](https://bugs.mojang.com/browse/MCPE-69721)）
- 使用材质状态“混合”的实体现在在透明部分后面正确渲染

## **技术修复与更改**

**动画**

- 在“龙！”市场地图上，行为动画控制器在用有鞍的龙重新加载地图后将不再停止工作

**自定义生物群系和方块**

- 禁用自定义生物群系特征中实体的加载
- 修复数据驱动方块的UV未稍微缩小的问题，这导致纹理扭曲
- 修复活塞推动的数据驱动方块无法正常工作的情况

**渲染偏移组件**

- 简单物品，如剑或镐，可以应用可选偏移以修改其渲染方式。请注意，此组件不应添加到附着物上

**组件变量**

- main_hand - 一个可选对象，存储玩家右手的“第一人称”和“第三人称”的可选变换数据
- off_hand - 一个可选对象，存储玩家左手的“第一人称”和“第三人称”的可选变换数据
- first_person - 一个可选对象，存储用于构建第一人称矩阵的3个向量“位置”、“旋转”、“缩放”
- third_person - 一个可选对象，存储用于构建第三人称矩阵的3个向量“位置”、“旋转”、“缩放”