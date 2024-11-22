---
标题: Minecraft Beta & Preview - 1.19.50.20
日期: 2022-10-13T14:44:31Z
更新: 2022-10-17T10:43:47Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/9857822954765-Minecraft-Beta-Preview-1-19-50-20
---

**发布于:** 2022年10月13日

## **关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一张Minecraft截图，展示了在旁观者游戏模式下飞行穿越地形时世界的样子](https://feedback.minecraft.net/hc/article_attachments/9857667786893)

以下是本周Minecraft预览和Beta中的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，欢迎随时向我们发送 [您的反馈](https://aka.ms/MinecraftBetaFeedback)。

**Minecraft Live生物投票：** 要参与Minecraft Live生物投票，您需要使用基岩版1.19.31。

您可以在Google Play商店中选择退出Android Beta，并卸载/重新安装Minecraft以恢复到1.19.31版本 - 如果您这样做，请记得备份您的世界！

您还可以通过Minecraft启动器或在网页浏览器中访问 [minecraft.net/live](https://www.minecraft.net/en-us/live) 进行投票。投票将在10月14日东部时间中午12点开始，持续24小时！

# **功能和漏洞修复**

## **原版趋同**

### **旁观者模式**

- 旁观者模式已从实验性切换移入基础游戏
  - 请记住，使用过实验性切换的世界将始终标记为实验性。我们建议将这些实验性世界与您的主存档分开。更多信息请参见 [这篇文章](./Experimental-Features-Toggle-in-Minecraft-Bedrock-Edition.md)。
- 玩家可以通过设置菜单中的个人游戏模式或启用作弊的情况下使用'/gamemode spectator'命令进出旁观者模式 ([MCPE-156688](https://bugs.mojang.com/browse/MCPE-156688))
- 旁观者的HUD减少，不显示十字准星、快捷栏、经验、生命、饥饿或盔甲UI元素
- 切换到旁观者模式时，玩家的物品栏、生命、持有物品等保持不变，离开旁观者模式时也是如此
- 旁观者始终处于飞行状态，无法接触地面
- 旁观者可以穿过固体方块和实体而不发生碰撞
- 旁观者在方块内部时可以看到固体物体
- 旁观者无法受到伤害，不受任何方块、生物、物品、传送门或效果的影响
- 旁观者无法使用物品或与方块或生物互动
- 旁观者无法打开物品栏或与箱子等方块UI互动
- 除了其他旁观者模式的玩家外，旁观者无法被生物或其他玩家看到
- 旁观者不需要睡觉来度过夜晚
- 在旁观者模式下，其他玩家看到的旁观者呈透明漂浮的头颅
- 在第一人称视角下，旁观者无法看到自己的手臂或持有的物品
- 旁观者在飞往新区块时会生成区块
- 旁观者不会生成任何生物
- 在旁观者周围的非持久生物在决定是否应毁除时会检查与任何非旁观者的距离
- 命令可以选择并作用于旁观者
- 玩家进入旁观者模式时，打开的容器、命令方块或结构方块界面现在会关闭
- 旁观者模式现在出现在设置中的个人游戏模式列表中 ([MCPE-156688](https://bugs.mojang.com/browse/MCPE-156688))

### **方块**

- 泥土径和耕地的碰撞现在降低了一个像素 ([MCPE-12109](https://bugs.mojang.com/browse/MCPE-12109))
- 玩家在泥巴上游泳时，屏幕不会被遮挡 ([MCPE-153737](https://bugs.mojang.com/browse/MCPE-153737))
- 投射物落在泥巴上时不会反复震动 ([MCPE-153744](https://bugs.mojang.com/browse/MCPE-153744))
- 两栖生物不再在泥巴块周围遇到路径寻找问题 ([MCPE-153961](https://bugs.mojang.com/browse/MCPE-153961))
- 泥巴和灵魂沙块的边界框现在与玩家放置方块时的视觉边界框相匹配 ([MCPE-162252](https://bugs.mojang.com/browse/MCPE-162252))
- 当水源被移除时，甘蔗将在下一个随机刻破坏 ([MCPE-162351](https://bugs.mojang.com/browse/MCPE-162351))
- 修复了一个漏洞，放置的光源方块即使在选择光源方块时也会不可见

## **游戏玩法**

- 修复了活塞移动方块时闪烁的问题
- 修复了繁殖带有效果的生物时，后代会永久获得效果加成的问题 ([MCPE-81890](https://bugs.mojang.com/browse/MCPE-81890))
- 活塞的臂现在更平滑地伸展 ([MCPE-155987](https://bugs.mojang.com/browse/MCPE-155987))
- 附着在活塞上的方块现在移动得更平滑 ([MCPE-146597](https://bugs.mojang.com/browse/MCPE-146597))
- 修复了一个可能导致玩家在退出传送门后被传送回传送门的问题 ([MCPE-157494](https://bugs.mojang.com/browse/MCPE-157494))
- 修复了一个问题，放置告示牌时不会播放放置声音 ([MCPE-65423](https://bugs.mojang.com/browse/MCPE-65423))
- 被黑色像素损坏的地图现在可以通过重新访问损坏区域进行修复。之前受影响的地图现在可以通过主手或副手持有进行修复 ([MCPE-162421](https://bugs.mojang.com/browse/MCPE-162421))
- 巨型菌类方块在从菌岩生长时不再替换部分方块 ([MCPE-65661](https://bugs.mojang.com/browse/MCPE-65661))

## **一般**

- 修复了蝙蝠休息位置在负世界高度时偏移的问题
- 修复了一个漏洞，当通过传送门时完全充能的物品会丢失 ([MCPE-55279](https://bugs.mojang.com/browse/MCPE-55279))
- 气泡柱现在在水下岩浆块上方正确生成

## **图形**

- 对活塞移动的方块应用了环境光 ([MCPE-136928](https://bugs.mojang.com/browse/MCPE-136928))
- 修复了启用RTX时夜空的亮度问题 ([MCPE-162445](https://bugs.mojang.com/browse/MCPE-162445))

## **物品**

- 新合成的工具和盔甲现在在首次使用时有效 ([MCPE-161151](https://bugs.mojang.com/browse/MCPE-161151))
- 武器、工具和盔甲在重命名后首次可以从玩家的物品栏中掉落 ([MCPE-162132](https://bugs.mojang.com/browse/MCPE-162132))
- 修复了一个问题，坐标0,0,0处的实体阻止了压力板的放置 ([MCPE-161377](https://bugs.mojang.com/browse/MCPE-161377))

## **生物效果**

- 跳跃提升现在始终影响被玩家骑乘的生物 ([MCPE-45823](https://bugs.mojang.com/browse/MCPE-45823))
- 缓降现在始终影响被玩家骑乘的生物 ([MCPE-126604](https://bugs.mojang.com/browse/MCPE-126604))

## **移动数据**

- 在Android/iOS上，当移动数据可用但在游戏中禁用且未连接Wi-Fi时，添加了新的移动数据被阻止的屏幕

## **生物**

- 末影人的跟随范围从32增加到64 ([MCPE-35306](https://bugs.mojang.com/browse/MCPE-35306))

## **触控控制**

- 在预览中，我们重新启用了触控设备的新堆叠分割功能
- "分割控制"选项仅在经典控制模式下出现，仅影响经典控制方案
- 修复了在某些情况下，十字准星和触控控制方案中无法触摸快捷栏槽位的问题
- 滚动物品栏屏幕变得更容易，因为停留时间已增加到180毫秒（之前为120毫秒）。停留时间是指物品必须被按住的时间长度，才能开始拖动操作
- 解开了“锁定摇杆”、“摇杆始终可见”和“摇杆在未使用时可见”之间的连接
- 在触控设置中添加了“延迟破坏方块（仅限创造模式）”的切换，以控制此功能
- 修复了在高刷新率屏幕上双击触控控制按钮可能会很困难的问题 ([MCPE-156351](https://bugs.mojang.com/browse/MCPE-156351))
- 改进了新触控控制中按钮按压和摄像机移动的协同工作方式
- 在使用十字准星模式时，坐船时操作按钮现在会出现 ([MCPE-159376](https://bugs.mojang.com/browse/MCPE-159376))

## **用户界面**

- 修复了一个漏洞，boss条名称在boss名称更改时不会更新，直到玩家重新加载该条
- 当玩家即将失去更改并离开创建新世界屏幕时，现在会出现警告
- 更改了复制世界时的错误处理，以显示模态弹出窗口，而不是吐司通知
- 修复了一个漏洞，导致HUD在VR中乘船时不会随玩家方向旋转
- 更改了“允许移动数据进行在线游戏”选项的描述文本颜色，以提高可读性 ([MCPE-162459](https://bugs.mojang.com/browse/MCPE-162459))
- 快捷栏物品文本背景现在受文本背景不透明度滑块的影响 ([MCPE-79331](https://bugs.mojang.com/browse/MCPE-79331))

## **命令**

- 使用'/enchant'命令应用相同等级的附魔不再导致应用更高等级 ([MCPE-153204](https://bugs.mojang.com/browse/MCPE-153204))
- 修复了一个问题，如果未提供数据值，*hasItem*无法正确检测具有数据值的物品 ([MCPE-162460](https://bugs.mojang.com/browse/MCPE-162460))

# **技术更新**

## **一般**

- 声音事件中的最小/最大距离值现在仅影响该声音事件，而不影响使用相同声音的所有事件 ([MCPE-154376](https://bugs.mojang.com/browse/MCPE-154376))
- 在server.properties中添加了客户端区块生成启用切换

## **网络**

- 添加了服务器属性'enable-lan-visibility'以禁用客户端的显式局域网发现。这将防止在单个主机上运行多个专用服务器时出现意外的端口冲突。明确了服务器日志中的端口使用，并使错误消息更加清晰 ([BDS-1094](https://bugs.mojang.com/browse/BDS-1094))

## **稳定性和性能**

- 修复了一个崩溃问题，如果刷怪蛋的*texture_index*超出范围。现在将显示内容日志错误
- 在CameraAPI中检索活动对象引用时添加了空指针检查，以防止崩溃
- 修复了一个问题，当末影龙的吐息攻击未击中方块或掉入虚空时，游戏会崩溃 ([MCPE-161204](https://bugs.mojang.com/browse/MCPE-161204))
- 修复了一个问题，当在村民界面中使用键盘向下导航时可能会导致崩溃

# **实验性功能**

## **一般**

- 当方块更改为具有不同*minecraft:crafting_table*组件的排列时，工作台UI会更新

## **脚本、API和游戏测试框架**

- 修复了在使用/gametest clearall命令清除远程游戏测试结构后，线框仍在渲染的问题
- 实体
  - 移除了*runCommand*函数。考虑使用*runCommandAsync*作为替代
- 维度
  - 移除了*runCommand*函数。考虑使用*runCommandAsync*作为替代
- 将BlockRaycastOptions转换为接口
- 将EntityEventOptions转换为接口
- 将ScoreboardObjectiveDisplayOptions转换为接口
  - 位置类型更新为IVec3
- 向量
  - add - 更新*a*和*b*参数以接受IVec3接口类型
  - cross - 更新*a*和*b*参数以接受IVec3接口类型
  - distance - 更新*a*和*b*参数以接受IVec3接口类型
  - divide - 更新*a*参数以接受IVec3接口类型
  - lerp - 更新*a*和*b*参数以接受IVec3接口类型
  - max - 更新*a*和*b*参数以接受IVec3接口类型
  - min - 更新*a*和*b*参数以接受IVec3接口类型
  - multiply - 更新*a*参数以接受IVec3接口类型
  - slerp - 更新*a*和*b*参数以接受IVec3接口类型
  - subtract - 更新*a*和*b*参数以接受IVec3接口类型