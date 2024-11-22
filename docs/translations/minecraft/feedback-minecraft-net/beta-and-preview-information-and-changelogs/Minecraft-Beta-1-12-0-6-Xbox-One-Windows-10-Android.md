---
标题: Minecraft Beta - 1.12.0.6 (Xbox One/Windows 10/Android)
日期: 2019-05-14T09:37:11Z
更新: 2019-05-22T15:52:47Z
类别: Beta 和预览信息及更新日志
标签:
  - beta
  - 基岩
  - 1.12.0.5
链接: https://feedback.minecraft.net/hc/en-us/articles/360028058852-Minecraft-Beta-1-12-0-6-Xbox-One-Windows-10-Android
---

**请在参与Minecraft Beta之前阅读**：

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览Beta时无法加入非Beta玩家
- 在Beta中玩的任何世界无法在之前的游戏版本中打开，因此请备份世界以防丢失
- Beta版本可能不稳定，并不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

 

## 对于地图制作和附加包创建者：

- 如果存在，已移除函数文件开头的“字节顺序标记”
- 更新了ScriptHotbarContainerComponent的generateDocumentation函数，说明它检查玩家的第一个快捷栏物品槽，而不是第三个

## **修复：**

- **崩溃/性能**
  - 修复了在游戏检查先前下载内容时可能发生的崩溃
  - 对新村庄的性能进行了进一步改进
  - 修复了在Windows 10上退出游戏时有时发生的崩溃
  - 减少了加载纹理所需的内存量
  - 修复了加载游戏时可能发生的崩溃
  - 修复了投掷鸡蛋或雪球时可能发生的崩溃（[MCPE-40435](https://bugs.mojang.com/browse/MCPE-40435)）
  - 修复了加载火焰箭实体时可能发生的崩溃
  - 修复了Android上的全局资源崩溃
  - 修复了与村民交易时可能发生的崩溃
  - 修复了一个漏洞，该漏洞在生物进入水中时会导致性能下降
  - 改进了方块遮挡性能
  - 改进了与区块加载相关的性能

<!-- -->

- **常规**
  - 自定义皮肤现在可以正确应用，无需重启游戏即可查看（[MCPE-37926](https://bugs.mojang.com/browse/MCPE-37926)）
  - 通过移除某些物品名称开头的“tile”使物品名称更一致
  - “邀请加入游戏”按钮在第三方服务器上不再启用
  - 改进了漫游皮肤，重新加载或重新安装游戏并登录后应能正确应用
  - 自定义皮肤在重新加载游戏后不再恢复为早期的跨平台皮肤（[MCPE-45476](https://bugs.mojang.com/browse/MCPE-45476)）  
      

<!-- -->

- **游戏玩法**
  - “铁肚子”成就可以再次解锁（[MCPE-46260](https://bugs.mojang.com/browse/MCPE-46260)）
  - 金合欢木板可以再次正确合成（[MCPE-44398](https://bugs.mojang.com/browse/MCPE-44398)，[MCPE-44398](https://bugs.mojang.com/browse/MCPE-44398)）
  - 村庄工作地点方块在玩家使用时现在具有一致的音量水平
  - 玩家在与村民完成交易并使用控制器时现在能一致地收到物品
  - 玩家纸娃娃模型在玩家使用鞘翅滑翔时现在正确移动（[MCPE-44731](https://bugs.mojang.com/browse/MCPE-44731)）
  - 在甜浆果丛上使用Pickblock现在会给予玩家正确的物品（[MCPE-41877](https://bugs.mojang.com/browse/MCPE-41877)）
  - 烟花现在可以正确提升鞘翅飞行，如果通过/give或/setitem提供
  - 在草地上使用骨粉现在可以正确消耗
  - 画作现在可以用染色羊毛合成
  - 如果玩家替换与经验丰富的村民绑定的工作地点方块，玩家不再失去村民工作地点位置
  - 玩家在用满的物品栏在织布机中切换旗帜图案时不再丢失或重复旗帜图案
  - 不同生长阶段的仙人掌方块可以再次熔炼成绿色染料（[MCPE-42497](https://bugs.mojang.com/browse/MCPE-42497)）
  - 修复了在Switch的玩法说明部分缺少按钮图标的问题
  - 在制图输出槽按控制器Y键现在只会合成正确数量
  - 重新建立了修复，以保持遗留交易的正常工作方式
  - 如果流浪商人被杀，羊驼现在会掉落它们的拴绳（[MCPE-44704](https://bugs.mojang.com/browse/MCPE-44704)）

<!-- -->

- **生物**
  - 猫和村民坐着和睡觉时现在有正确的头部位置（[MCPE-44648](https://bugs.mojang.com/browse/MCPE-44648)）
    - 请注意，我们仍在努力修复旧世界中的驯服豹猫（[MCPE-41929](https://bugs.mojang.com/browse/MCPE-41929)）
  - 驯服的猫坐着时不再滑动（[MCPE-44491](https://bugs.mojang.com/browse/MCPE-44491)）
  - 盔甲架现在可以正确渲染副手物品
  - 没有职业的村民现在遵循常规日程
  - 鹦鹉的腿在飞行时现在对齐正确
  - 修复了某些市场地图中的苦力怕模型

<!-- -->

- **图形**
  - 更新了掠夺者队长的旗帜纹理
  - 火粒子不再显示在空的生物生成器方块上
  - 调整了箭的渲染时机以改善VR体验
  - 修复了钟纹理UV中的小错误

<!-- -->

- **命令**
  - 杀死可骑乘实体不再在同一刻重生其骑乘者
  - /testforblock命令现在可以可靠地与语言文件中重命名的物品一起使用
- **附加包和脚本引擎**
  - 自定义水下生物现在可以自然生成