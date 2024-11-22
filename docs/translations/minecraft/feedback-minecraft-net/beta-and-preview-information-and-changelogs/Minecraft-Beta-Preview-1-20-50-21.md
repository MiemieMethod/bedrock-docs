---
标题: Minecraft Beta & Preview - 1.20.50.21
日期: 2023-10-18T11:36:55Z
更新: 2023-10-18T15:19:07Z
分类: Beta 和 Preview 信息与更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/20490119155981-Minecraft-Beta-Preview-1-20-50-21
哈希:
  h_01HBVR6KM8JCTEG8SDY8V3WBB3: 关于Minecraft预览版和测试版的信息
  h_01HD17VBQ35H2GA0AHH7G9GP4G: 实验性特性
  h_01HD195DNF84FCVMVN2C58C4SN: 合成器
  h_01HD17VBQ3KVH9FRQF428NR2DD: 特性和漏洞修复
  h_01HD17VBQ3J7ZQ896HNZ455F1K: 方块
  h_01HD17VBQ36ESYZW46RBQRY435: 饰纹陶罐
  h_01HD17VBQ3Z1GZZPGC01EBH28M: 生物
  h_01HD17VBQ3EQ88G16QDHK93GB1: 技术更新
  h_01HD17VBQ3S98TPC5WCBND66VK: API
  h_01HD17VBQ39JDZ496ZH9QJY54B: 一般
  h_01HD17VBQ303C7Q5GJKHRK7BNQ: 实验性技术特性
  h_01HD1957J6RQ59AGCD7V74ASQ5: 图形
  01HD1951020Z4NHSYG2R7XCY8C: api-1
---

**发布:** 2023年10月18日

## **关于Minecraft预览版和测试版的信息:**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见aka.ms/JoinMCBeta获取详细说明

![合成器在运作中的Minecraft截图。](https://feedback.minecraft.net/hc/article_attachments/20490157834381)

今天我特别有创意。是因为我早上在便利贴上潦草地写下了巧妙的红石计划吗？还是因为**合成器在今天的预览版中可供实验性测试？** 在10月15日的Minecraft Live上揭晓，合成器使用红石进行自动合成。选择一个配方，添加成分堆叠，提供红石脉冲，*哇！* 在短短几刻钟内，你的自动合成物品将*弹出*到Minecraft世界中。这是1.21版本中首批进入测试的特性之一，我们非常希望能听到你的反馈，以帮助我们将其*打磨*成最终版本。请将你的反馈发送到[这里](https://aka.ms/Minecraft121Feedback)，并在[bugs.mojang.com](https://bugs.mojang.com/)报告漏洞！

*(请注意：此预览版和测试版将于09:00 PDT开始向玩家推出)*

# 实验性特性

## **合成器**

- 向游戏中添加了合成器方块
- 合成器可以用红石粉、铁锭、工作台和投掷器合成
- 合成器在合成时使用独特的粒子效果
- 合成器在合成和失败时有独特的声音
- 合成器的抗爆炸值为3.5
- 连接到合成器的比较器现在输出的信号等于非空槽位加上禁用槽位的数量
- 从漏斗或投掷器移动物品到合成器时，物品将均匀分配，而不是先填满第一个堆叠
- 用红石信号为合成器供电会使其合成并输出物品

# 特性和漏洞修复

## 方块

- 水平末地烛的击中箱现在正确旋转 ([MCPE-171597](https://bugs.mojang.com/browse/MCPE-171597))

## 饰纹陶罐

- 当与饰纹陶罐交互失败时，陶罐摇晃的方向已反转

## 生物

- 长大为成年并且体型过大无法进入船的生物现在会跳出船 ([MCPE-171870)](https://bugs.mojang.com/browse/MCPE-171870)

# 技术更新

## API

- 事件
  - 将*PlayerInteractWithBlockAfterEvent*从*beta*移至*1.7.0*
  - 将*PlayerInteractWithBlockBeforeEvent*从*beta*移至*1.7.0*
  - 将*PlayerInteractWithEntityAfterEvent*从*beta*移至*1.7.0*
  - 将*PlayerInteractWithEntityBeforeEvent*从*beta*移至*1.7.0*

## 一般

- 修复了升级具有多个字符串名称的加载值时出现的问题

# 实验性技术特性

## **图形**

- 增强了辉光管线，以利用HDR场景信息更自然地强调延迟技术预览中的亮像素
- 修复了在延迟技术预览中渲染不存在生物的阴影的问题
- 修复了在延迟技术预览中切换维度时可能发生的崩溃

## API

- 将*PlayerLeaveBeforeEvent*从*beta*移至*1.7.0*
- 将*NumberRange*接口移至*minecraft/common*
  - 将*heightRange: NumberRange*从*beta*移至*1.7.0*
  - 将*matches*从*beta*移至*1.7.0*
  - 将函数*clearDynamicProperties*从*beta*移至*1.7.0*
  - 将函数*getDynamicProperties*从*beta*移至*1.7.0*
  - 将函数*getDynamicPropertyIds*从*beta*移至*1.7.0*
  - 将函数*getDynamicPropertyTotalByteCount*从*beta*移至*1.7.0*
  - 将函数*setDynamicProperty*从*beta*移至*1.7.0*
  - 将函数*clearDynamicProperties*从*beta*移至*1.7.0*
  - 将函数*getDynamicProperties*从*beta*移至*1.7.0*
  - 将函数*getDynamicPropertyIds*从*beta*移至*1.7.0*
  - 将函数*getDynamicPropertyTotalByteCount*从*beta*移至*1.7.0*
  - 将函数*setDynamicProperty*从*beta*移至*1.7.0*
- 每秒刻数
  - 从beta移至*1.7.0*
  - 将*offset*从*beta*移至*1.7.0*
  - 将*above*从*beta*移至*1.7.0*
  - 将*below*从*beta*移至*1.7.0*
  - 将*north*从*beta*移至*1.7.0*
  - 将*east*从*beta*移至*1.7.0*
  - 将*south*从*beta*移至*1.7.0*
  - 将*west*从*beta*移至*1.7.0*
  - 将*center*从*beta*移至*1.7.0*
  - 将*bottomCenter*从*beta*移至*1.7.0*