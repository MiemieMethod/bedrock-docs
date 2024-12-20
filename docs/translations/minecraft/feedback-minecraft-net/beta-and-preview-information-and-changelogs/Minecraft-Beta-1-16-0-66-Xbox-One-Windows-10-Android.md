---
标题: Minecraft Beta - 1.16.0.66 (Xbox One/Windows 10/Android)
日期: 2020-06-04T15:35:11Z
更新: 2020-07-24T19:18:33Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360044492151-Minecraft-Beta-1-16-0-66-Xbox-One-Windows-10-Android
---

**在参与Minecraft Beta之前，请阅读以下内容：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

# 修复

**性能和稳定性**

- 修复了在游戏过程中可能发生的多个崩溃
- 修复了尝试使用热带城市度假村混搭包创建世界时可能发生的崩溃
- 修复了在尝试打开某些世界时可能导致启动延迟的问题

**一般**

- 修复了如果投射物未造成伤害而被过早摧毁的问题。现在可以选择，新增了两个标志到投射物中

**游戏玩法**

- 修复了可能导致箱子生成时没有战利品的问题 [MCPE-69003](https://bugs.mojang.com/browse/MCPE-69003)

**图形**

- 修复了骑乘坐骑时的渲染问题

**附加包和脚本**

- 修复了当移动组件被移除时可能发生的问题，这意味着生物的速度需要从0重新加速
- 组件的更改：*set_last_hurt_requires_damage*和*destroy_on_hit_requires_damage*。每个默认值为true以尊重旧行为，但现在可以设置为false，如果希望投射物即使不造成伤害也被摧毁

**命令**

- 为/replaceitem添加了新的重载，选项为destroy（旧行为）或keep（如果该槽位被物品占用，命令将返回错误）
- 修复了一个漏洞，即如果所有目标都尝试被移除，生物不会删除其目标
- 修复了循环的、非零长度动画中粒子、声音和事件的重复问题
- 修复了在运行/xp命令时与等级相关的语法错误问题
- 修复了“糖果乐园中的噩梦”地图的问题，该地图不再正确传送玩家