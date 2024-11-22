---
title: Minecraft Beta - 1.13.0.9（Xbox One/Windows 10/Android）
date: 2019-08-23T13:47:19Z
updated: 2019-08-27T23:21:42Z
categories: Beta 和预览信息及更新日志
link: https://feedback.minecraft.net/hc/zh-cn/articles/360032515012-Minecraft-Beta-1-13-0-9-Xbox-One-Windows-10-Android
---

**参与Minecraft Beta前请阅读：**

- 加入Beta将用Minecraft的开发中版本替换您的游戏
- 您将无法访问Realms，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间玩的任何世界无法在游戏的旧版本中打开，因此请复制世界以防止丢失
- Beta构建可能不稳定，不能代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明

## **新功能：**

- 添加了凋灵玫瑰
- 添加了谜之炖菜
- 物品展示框现在可以放置在地板和天花板上！
- 添加了棕色哞菇
  - 由闪电锤造！
- 添加了被遗弃的村庄
- 为地图制作者添加了光源方块
  - 支持0到15的光照等级辅助数据
  - 隐形末地烛（变种6）现在自动升级为新的光源方块
  - 通过/give、/fill和/setblock支持光源方块
- 添加了成功的村庄袭击庆祝
- 添加了游戏截图
  - 可在击败末影龙后查看，也可通过设置菜单中的新按钮查看
- 新的音符盒声音！
  - 为荧石、干草捆、绿宝石块、南瓜、灵魂沙、铁块、骨块、羊毛、浮冰、黏土和金块添加了音符盒功能

## **更改：**

- 鱿鱼现在可以在河流中生成！
- 添加了失活的珊瑚植物
- 更新并添加了新的音符盒声音
- 玩家现在高1.8区块（[MCPE-31710](https://bugs.mojang.com/browse/MCPE-31710)）
- 如果村民的物品栏中有面包，他们现在可以治疗
- 为结构方块添加了“如何玩”部分

## **针对地图制作者和附加包创建者：**

- **新的数据驱动物品：**
  - 海龟蛋与闪电互动现在是数据驱动的
  - 河豚膨胀状态现在是数据驱动的
  - 酿造台药水配方现在是数据驱动的
- 将可呼吸系统、骑乘刻和变换系统更改为使用ViewedEntityContext
- 为ScriptAPI添加了预编译头目标
- 显著增加了最大“生成半径”距离

## **修复：**

- **崩溃/性能**
  - 修复了游戏过程中可能发生的几个崩溃
  - 开始世界后游戏不再出现冻结
  - 改善了世界加载时间
  - 修复了由于遗留活动对象更新导致的组件/定义不匹配崩溃
  - 修复了尝试酿造某些药水时可能发生的崩溃
  - 优化了地形光照计算
  - 修复了在低端和中端Android设备上可能发生的崩溃
  - 修复了由于缺少组件定义导致的崩溃
  - 修复了客人通过邀请加入游戏时有时会发生的崩溃
  - 当分屏玩家拾取原木方块时，游戏不再崩溃
  - 修复了在接近生成点时影响某些世界的崩溃问题（[MCPE-46686](https://bugs.mojang.com/browse/MCPE-46686)）
  - 修复了更改文件存储位置后可能发生的崩溃
  - 用命令方块的矿车运行命令不再导致游戏崩溃
  - 修复了在信标UI中尝试双击物品时有时会发生的崩溃
  - 优化了Xbox One游戏中的FPS
  - 修复了将骨粉分发到一高花朵上时发生的崩溃问题（[MCPE-50760](https://bugs.mojang.com/browse/MCPE-50760)）
  - 优化了将怪物加载到世界中的时间
  - 修复了一些在内存较低的Android和iOS设备上有时发生的崩溃

<!-- -->

- **常规**
  - 现在可以解锁“We are being attacked!”和“I've got a bad feeling about this”成就（[MCPE-45060](https://bugs.mojang.com/browse/MCPE-45060)）
  - 使用/fill放置的动力铁轨在被红石供电时现在应该正常工作
  - 修复了购买某些内容包后出现的下载循环
  - 使用/setblock在活塞基座上不再留下隐形活塞臂
  - 删除全局资源包时，它现在会从活动堆栈中移除自身
  - 使用各种语言设置时，全局资源包屏幕顶部的信息现在会正确适配
  - 调整了“如何玩”指南中的“主机和玩家选项”部分（[MCPE-28976](https://bugs.mojang.com/browse/MCPE-28976)）
  - 克隆的活动怪物生成器现在有一个动画怪物
  - 修复了一些皮肤选择未保存并恢复到Steve或Alex的情况（[MCPE-32089](https://bugs.mojang.com/browse/MCPE-32089)）
  - 修复了尝试在皮肤加载前加入世界时弹出的“多人游戏限制皮肤！”错误消息（[MCPE-48494](https://bugs.mojang.com/browse/MCPE-48494)）
  - 修复了尝试扩展现有村庄时导致创建许多小且空的村庄的问题
  - 修复了打开皮肤选择器时的无限加载屏幕
  - 修复了“Tiny Footprints”市场包缺少盔甲层的问题
  - 更新了关于驯服猫的“如何玩”部分（[MCPE-43490](https://bugs.mojang.com/browse/MCPE-43490)）

<!-- -->

- **游戏玩法**
  - 火焰附加剑不再点燃创造模式玩家（[MCPE-14036](https://bugs.mojang.com/browse/MCPE-14036)）
  - 玩家现在可以在吃紫颂果时传送到非全或透明方块上方
  - 持有红沙的末影人在被击杀时不再掉落普通沙子（[MCPE-25926](https://bugs.mojang.com/browse/MCPE-25926)）
  - 修复了在潜行时站在潜影贝或船上阻止玩家移动的问题（[MCPE-44644](https://bugs.mojang.com/browse/MCPE-44644)）
  - 杀死鳕鱼、鲑鱼、热带鱼和河豚现在会掉落经验值
  - 船桨动画现在与Java版本匹配，并在停止划桨时重新同步
  - 闪电现在更少频繁地击中（[MCPE-38768](https://bugs.mojang.com/browse/MCPE-38768)）
  - LT控制器按钮现在可以快速装备或替换盔甲
  - 玩家现在可以在瞄准附近的怪物时使用钓鱼竿等物品
  - 通过引导三叉戟的闪电现在影响小范围内的不止一个怪物
  - 玩家在船上时打开物品栏UI，不再持续划桨（[MCPE-36522](https://bugs.mojang.com/browse/MCPE-36522)）
  - 箭现在能正确摧毁盔甲架（[MCPE-47785](https://bugs.mojang.com/browse/MCPE-47785)）
  - 花盆中的花现在不再变得隐形（[MCPE-40806](https://bugs.mojang.com/browse/MCPE-40806)）
  - 在灵魂沙中潜行不再触发发光
  - 在创造模式中破坏扩展的活塞不再掉落物品（[MCPE-37492](https://bugs.mojang.com/browse/MCPE-37492)）
  - 牛奶和药水的饮用声音现在正确播放（[MCPE-38340](https://bugs.mojang.com/browse/MCPE-38340)）
  - 怪物现在正确掉落盔甲和工具（[MCPE-48891](https://bugs.mojang.com/browse/MCPE-48891)）
  - 使用时运工具破坏下界疣现在有机会掉落更多物品（[MCPE-31107](https://bugs.mojang.com/browse/MCPE-31107)）
  - 动物繁殖冷却时间在重新加载世界后不再重置
  - 除TNT外的爆炸现在在水中造成伤害
  - 可以使用选取块在创造模式中拾取鹦鹉
  - 发射器现在正确放置船只
  - 铁砧在使用后现在正确承受损坏
  - 怪物现在可以正确进入船和矿车（[MCPE-48596](https://bugs.mojang.com/browse/MCPE-48596)）
  - 按钮现在可以通过配方书制作
  - 修复了退出水中时玩家的游泳状态
  - 诸如滞留药水之类的效果区域云现在在世界设置为“永远白天”时正常工作（[MCPE-39595](https://bugs.mojang.com/browse/MCPE-39595)）
  - 从发射器分发的水不再破坏末地传送门和折跃门
  - 信标块现在可以像其他不透明方块一样让玩家和怪物窒息（例如使用矿车时被剪切）
  - 玩家重生位置现在更倾向于浅水而不是深水
  - 如果玩家死亡或移动离开，末地中将不再生成多个末影龙（[MCPE-37590](https://bugs.mojang.com/browse/MCPE-37590)）
  - 漏斗现在正确从上方拾取物品（[MCPE-31393](https://bugs.mojang.com/browse/MCPE-31393)）
  - 可再生能源成就现在会正确解锁（[MCPE-39661](https://bugs.mojang.com/browse/MCPE-39661)）
  - 掠夺者现在更频繁地在掠夺者前哨站周围生成（[MCPE-43396](https://bugs.mojang.com/browse/MCPE-43396)）
  - 玩家在从某些方块走上潜影盒后移动速度不再减慢
  - “你去哪了？”成就现在在Android上正确解锁
  - 在船内放置和破坏方块现在正常工作
  - 怪物不再掉落完全修复的物品（[MCPE-45953](https://bugs.mojang.com/browse/MCPE-45953)）
  - 末地折跃传送门现在无法在末地的主黑曜石平台上生成
  - 定位地图标记现在在乘船时指向正确方向（[MCPE-50512](https://bugs.mojang.com/browse/MCPE-50512)）
  - 下降的雪层现在不再破坏红石装置中的方块（[MCPE-49773](https://bugs.mojang.com/browse/MCPE-49773)）
  - 玩家现在正确接收来自熔炉的存储经验值（[MCPE-47324](https://bugs.mojang.com/browse/MCPE-47324)）
  - 探索时地图现在绘制更快，这意味着“地图室”成就现在更一致地解锁（[MCPE-27720](https://bugs.mojang.com/browse/MCPE-27720)）

<!-- -->

- **怪物**
  - 在怪物死亡动画期间，实体击中和碰撞箱不再存在（[MCPE-9999](https://bugs.mojang.com/browse/MCPE-9999)）
  - 凋灵骷髅不再受凋灵效果影响（[MCPE-46317](https://bugs.mojang.com/browse/MCPE-46317)）
  - 狐狸现在在雷暴期间睡觉并寻找掩护
  - 怪物和实体在冰上方行走时不再减速
  - 幼年僵尸现在可以骑僵尸猪人（[MCPE-20163](https://bugs.mojang.com/browse/MCPE-20163)）
  - 凋灵不再在被生成后逃离玩家
  - 修复了恼鬼怪物的持剑位置
  - 幻翼的翅膀拍打动画现在更快（[MCPE-42935](https://bugs.mojang.com/browse/MCPE-42935)）
  - 末影人现在在应用隐身效果时正确受影响（[MCPE-44492](https://bugs.mojang.com/browse/MCPE-44492)）
  - 鹦鹉现在可以飞过栅栏和墙
  - 陸地上的溺尸现在根据亮度级别攻击，而不是根据时间
  - 站在台阶上的怪物在重新加载世界后不再免疫阳光伤害（[MCPE-32822](https://bugs.mojang.com/browse/MCPE-32822)）
  - 女巫现在不会在1.8高度的缝隙中生成（[MCPE-45935](https://bugs.mojang.com/browse/MCPE-45935)）
  - 被治愈的僵尸村民现在保持他们的贸易等级
  - 僵尸在路径寻找时不再卡在门上
  - 鹦鹉跳舞动画现在速度正确（[MCPE-48356](https://bugs.mojang.com/browse/MCPE-48356)）
  - 骑乘者现在不再在尝试移动到无法到达的坐骑时卡住

<!-- -->

- **方块**
  - 屏障块不再阻止草生长
  - 耕地方块现在防止下方草生长

<!-- -->

- **物品**
  - 海龟蛋物品现在与Java版本有相同的2D图标
  - 使用精准采集收集的树叶现在正确堆叠（[MCPE-32347](https://bugs.mojang.com/browse/MCPE-32347)）
  - 活板门物品现在具有正确的物品栏图标纹理（[MCPE-44214](https://bugs.mojang.com/browse/MCPE-44214)）
  - 六面的木块变种现在可以烧炼或用作熔炉燃料
  - 草径方块现在不在创造物品栏中缺失
  - 在水下破坏方块掉落的物品现在显示气泡
  - 受损的鞘翅现在有自己的纹理
  - 修复了阻止某些物品在配方书中正确建议的问题
  - 在营火上烹煮的物品现在正确堆叠（[MCPE-47684](https://bugs.mojang.com/browse/MCPE-47684)）

<!-- -->

- **图形**
  - 纸娃娃模型现在在应用挂起和恢复时正确重新加载动画
  - 玩家模型现在在睡在床上时再次可见
  - 改善了非精美图形的切石机纹理（[MCPE-42487](https://bugs.mojang.com/browse/MCPE-42487)）
  - 修复了第三人称视角中的盾牌格挡动画
  - 铁栏杆在被其他栏杆包围时不再丢失部分纹理（[MCPE-47324](https://bugs.mojang.com/browse/MCPE-47324)）
  - 修复了玩家潜行的流畅动画（[MCPE-49586](https://bugs.mojang.com/browse/MCPE-49586)）
  - 睡在床上时屏幕现在会渐变为黑色
  - 在结构方块UI中渲染的拴绳不再远距离拉伸
  - 为末影龙的死亡动画添加了正确的色调

<!-- -->

- **用户界面**
  - 修复了各种药水显示的错误提示文本
  - 当游戏在窗口焦点外加载时，键盘输入现在正常工作
  - 修复了在VR沉浸模式中睡觉后的HUD定位
  - 修复了触屏设备的“打开聊天”消息
  - 创造模式中在床上睡觉时飞行控制不再显示（[MCPE-44928](https://bugs.mojang.com/browse/MCPE-44928)）

<!-- -->

- **命令**
  - 现在不能通过斜杠命令放置数据值为6和7的活塞（[MCPE-21558](https://bugs.mojang.com/browse/MCPE-21558)）
  - 现在使用/clear @p item正确清除辅助值
  - 玩家现在无法在下界维度使用/spawnpoint命令
  - 现在使用/replaceitem命令与木桶配合正常工作（[MCPE-48184](https://bugs.mojang.com/browse/MCPE-48184)）
  - /clear命令现在与可损坏物品正常工作
  - 运行“/clear”命令消息现在显示正确移除的物品数量（[MCPE-34750](https://bugs.mojang.com/browse/MCPE-34750)）
  - 现在使用“/clear”命令正确移除地毯

<!-- -->

- **附加包和脚本引擎**
  - 修复了在离开世界死亡屏幕后死亡覆盖事件触发两次的问题
  - 修复了`minecraft:scale`组件未能缩放某些活动对象模型的问题
  - 现在运行“tick_world”组件时正确且一致地移除常加载区域
  - 修复了当怪物被非魔法伤害时发送双重伤害事件的问题
  - 设定行为包动画现在正确运行
  - 计时器组件现在在投射物上工作
  - “minecraft:spell_effects”不再错误地第二次触发
  - 修复了未添加的玩家实体组件
  - 为市场地图添加了石头台阶别名以允许向后兼容