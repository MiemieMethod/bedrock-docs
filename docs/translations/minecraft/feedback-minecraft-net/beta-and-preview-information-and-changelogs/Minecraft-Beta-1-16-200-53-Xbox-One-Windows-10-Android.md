---
标题: Minecraft Beta - 1.16.200.53 (Xbox One/Windows 10/Android)
日期: 2020-11-05T15:19:27Z
更新: 2020-11-06T16:27:50Z
类别: 测试版和预览信息及更新日志
标签:
  - 测试版
  - 测试版更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360051721352-Minecraft-Beta-1-16-200-53-Xbox-One-Windows-10-Android
---

请在参与Minecraft测试版之前阅读：

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realms，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请参见[ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

# **新特性：**

**新的音量选项**

- 为各种声音类别（例如：敌对、生物、天气等）添加了多种音量滑块
  - 这些滑块将在主设置菜单中播放相关声音的预览，并在游戏中播放默认的点击声音

![img_557.JPG](https://feedback.minecraft.net/hc/article_attachments/360075430292/img_557.JPG)

 

**光线追踪**

- 在支持光线追踪硬件的Windows 10 GPU上启用光线追踪
  - 在视频选项中添加了上采样选项
  - 在视频设置中添加了光线追踪切换和光线追踪渲染距离滑块

# **漏洞修复**

## 性能和稳定性

- 修复了在游戏过程中可能发生的多个崩溃
- 修复了在加载本地世界时Minecraft偶尔崩溃的漏洞

## 一般

- “草莓金发”颜色在角色创建器中现在有了正确的名称（[MCPE-102674](https://bugs.mojang.com/browse/MCPE-102674)）
- 修复了如果禁用视角摇晃设置，玩家的手仍然会摇晃的漏洞（[MCPE-79380](https://bugs.mojang.com/browse/MCPE-79380)）
- 修复了使用“set_data”函数的战利品表生成不正确战利品的情况

## 辅助功能

- 修复了在未登录Microsoft账户时，服务器标签无法正确读取文本转语音提示的问题
- 修复了启动屏幕上文本转语音索引不正确的各种问题
- 修复了用户界面控件在弹出模态框中文本转语音索引不当的问题
- 减少了触控用户界面顶部按钮行的透明度，以提高可读性

## 游戏玩法

- 下界合金盔甲现在提供90%的击退减免（[MCPE-77430](https://bugs.mojang.com/browse/MCPE-77430)）

## 生物

- 蜜蜂将不再离家蜂箱超过22个区块（[MCPE-60252](https://bugs.mojang.com/browse/MCPE-60252)）

## 图形、纹理和用户界面

- 合成网格中的幽灵物品现在根据物品在物品栏中的可用性具有不同颜色的背景
- 玩家权限菜单现在可以使用控制器进行导航，无论玩家的权限级别如何

## 市场

- 在市场中添加了各种用户界面元素以传达光线追踪功能（仅限Windows 10）
  - 市场中的资源包现在能够识别光线追踪功能，并在用户界面中显示支持标签
  - 尝试购买和/或下载需要光线追踪的资源包时，如果用户没有所需的最低规格硬件，将通知用户购买错误。在这种情况下，我们将向玩家传达所需的最低规格硬件信息
- 拥有的包在重启游戏后现在能够正确刷新