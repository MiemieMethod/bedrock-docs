---
标题: Minecraft Beta & Preview - 1.21.30.24
日期: 2024-08-21T15:11:47Z
更新: 2024-08-21T15:53:53Z
类别: Beta 和 Preview 信息与更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/29461929917069-Minecraft-Beta-Preview-1-21-30-24
哈希:
  user-content-experimental-features: experimental-features
  user-content-bundles: bundles
  user-content-features-and-bug-fixes: features-and-bug-fixes
  user-content-gameplay: gameplay
  user-content-realms: realms
  user-content-sounds: sounds
  user-content-stability-and-performance: stability-and-performance
  user-content-trial-chambers: trial-chambers
  user-content-user-interface: user-interface
  user-content-template-screen: template-screen
  user-content-vanilla-parity: vanilla-parity
  user-content-technical-updates: technical-updates
  user-content-add-ons-and-script-engine: add-ons-and-script-engine
  user-content-editor: editor
  user-content-items: items
  01J5TMY5ZP7M9XJEG4DSRARQWN: sounds-1
  user-content-experimental-technical-updates: experimental-technical-updates
  01J5TMY5ZPKJBY6S64RW6K71VF: gameplay-1
  user-content-graphical: graphical
---

**发布:** 2024年8月21日

**关于Minecraft Preview和Beta的信息:**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft Preview可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![Sunny正在持有一个收纳袋，站在一个有漏斗的合成器设置旁边，地上有一个收纳袋物品。](https://feedback.minecraft.net/hc/article_attachments/29461929905677)

是时候进行新的Minecraft Preview和Beta了！我们非常希望您能对收纳袋提供反馈，请通过 [aka.ms/mcbundlesfeedback](https://aka.ms/mcbundlesfeedback) 告诉我们您的想法，并在 [bugs.mojang.com](http://bugs.mojang.com/) 报告任何漏洞。

# 实验性功能

## 收纳袋

- 收纳袋配方现在通过获取皮革或线解锁
- 收纳袋在触摸屏设备上添加和移除物品时现在具有正确的动画
- 将多个物品的堆叠移动到收纳袋中时，任何现有的相同物品现在会正确移动到顶部
- 未染色的潜影盒不再可以放置在收纳袋内 ([MCPE-185477](https://bugs.mojang.com/browse/MCPE-185477))
- 游戏手柄右摇杆的“上”方向现在可以正确导航到收纳袋的子菜单
- 收纳袋的提示框现在可以显示3行，并且始终可以显示至少8种物品类型

> **开发者注:** *物品以四个一行的方式填充收纳袋，当一行满时，会被上方的行推下。这意味着顶部可能会有空位。  
>   
> 在之前的2020年收纳袋实验中，物品是从顶部填充的，没有留下任何空隙。我们改变了这种行为，因为这意味着在添加新物品时，物品会在收纳袋中左右移动。这使得一些玩家更难跟踪物品的顺序，有些甚至报告说物品在随机移动！  
>   
> 由于提示框只有两行，推送满行物品进一步下移收纳袋会移除一半的可见物品，这太多了。我们添加了第三行，以使设计更好，并允许玩家在填充收纳袋时看到更多物品。*

- **已知问题:** 放置在另一个收纳袋内的收纳袋在进出箱子时可能会丢失内容

# 功能和漏洞修复

## 游戏玩法

- 装备重锤的生物现在可以执行重击攻击

## 领域

- 领域备份列表现在显示备份创建的日期，而不是备份的年龄

## 声音

- 幽匿充能粒子现在有声音
- 凋灵骷髅现在有自己的“脚步”声音 ([MCPE-174857](https://bugs.mojang.com/browse/MCPE-174857))

## 稳定性和性能

- 修复了加载纹理数据时可能发生的崩溃 ([MCPE-184728](https://bugs.mojang.com/browse/MCPE-184728))

## 试炼密室

- 由于一些不可预见的问题，我们将撤回在([1.21.30.21](./Minecraft-Beta-Preview-1-21-30-21.md))基岩预览版本中引入的试炼密室修复
- 然而，漏斗和木桶的设置将保留
- 我们计划在未来的版本中重新引入这些修复，一旦核心问题得到解决

> **开发者注:** *我们撤回这些修复是为了处理一些在已生成的试炼密室中造成大量错误的潜在问题。虽然这不是一个容易的决定，但我们这样做是为了避免在您现有的世界中引入任何可能破坏它们的错误。*

## 用户界面

- 如果玩家在极限模式中死亡，极限世界现在将在新的游戏和编辑世界屏幕中显示灰色边框（仅限预览）
- 效果的图标现在会根据GUI缩放大小改变
- 修复了在创建新世界屏幕中，世界种子模板按钮可能缺失的问题

## 模板屏幕

我们引入了一个新的模板屏幕。以下是您可以期待在接下来的几个预览中看到的内容：

- 从模板创建世界
- 所有与模板相关的内容分为3个标签：
  - **市场通行证标签:** 包含在市场通行证订阅中的模板选择
  - **精选创作者标签:** 由Minecraft创作者设计的精选模板（可以选择在市场中发现更多）。
  - **我拥有的标签:** 您购买的所有模板。从这里您可以从模板创建世界并对模板进行评分。
- **搜索栏、过滤器和排序:** 通过搜索栏快速搜索您的模板，并使用过滤器和排序顺序细化结果。
- **订阅市场通行证:** 轻松发现通行证的所有内容并注册。
- 请通过 [aka.ms/startfromtemplatefeedback](https://aka.ms/startfromtemplatefeedback) 向我们反馈这些更改

## 原版趋同

- 玩家现在可以用一个瓶子草合成两个青色染料 ([MCPE-171061](https://bugs.mojang.com/browse/MCPE-171061))
- 狐狸现在有10点生命 ([MCPE-48233](https://bugs.mojang.com/browse/MCPE-48233))
- 村民在睡觉时不再发出闲聊声

# 技术更新

## 附加包和脚本引擎

- 修复了所有自定义方块在用户界面中旋转180度的漏洞
- “gui” “item_display_transforms” “rotation”字段的默认值现在是`[30, 45, 0]`而不是`[30, 225, 0]`
  - "item_display_transforms": {  
    "gui" : {  
    "translation": \[0, 0, 0\],  
    "rotation": \[30, 45, 0\],  
    "scale": \[0.625, 0.625, 0.625\],  
    "rotation_pivot" : \[0, 0, 0\],  
    "scale_pivot" : \[0, 0, 0\],  
    "fit_to_frame" : true  
    }  
    }

## 编辑器

- 从编辑器项目暂停菜单中移除了截图和个人资料按钮

## 物品

- minecraft:dyeable组件现在向创作者开放

## 声音

- 在sounds.json文件中指定无效的声音事件现在会触发内容错误

# 实验性技术更新

## 游戏玩法

- 聚焦目标相机: 在自由相机预设JSON中添加rotation_speed以控制目标实体的旋转速度。该值将是一个浮点数，表示每秒旋转的度数  
- 聚焦目标相机: 在自由相机预设JSON中添加snap_to_target布尔值，以在第一个刻触发对目标实体的快速对准  

## 图形

- 在启用延迟技术预览的Android设备上，SSR不再向错误方向泄漏