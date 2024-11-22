---
标题: Minecraft Beta & Preview - 1.21.0.26
日期: 2024-05-15T12:34:13Z
更新: 2024-05-15T16:21:56Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/26739672012045-Minecraft-Beta-Preview-1-21-0-26
哈希:
  h_01HXY3VHECZQYVVA5S748QCVVR: 特性与漏洞修复
  h_01HXY3VHECSVACXK98Q22J02GY: 试炼密室
  h_01HXY3VHECZNK4CNSW2M0B0XPB: 试炼刷怪笼
  h_01HXY3VHEC7CJPGAS6X4M7QRMT: 战利品
  h_01HXY3VHEC1282VKRX02W066D2: 趋同
  h_01HXY3VHEC62CYBJ1CXMGBAA6P: 重锤
  h_01HXY3VHEC5NYWZ4PC4BH94J3X: 物品
  h_01HXY3VHEC6HW25D5D1W3WZJ51: 魔咒
  h_01HXY3VHECFZZMHA474AVA3AMN: 领域
  h_01HXY3VHEC35E4HXED2CW05EGE: 角色创建
  h_01HXY3VHECH9TE41MW9CB8HYKS: 技术更新
  h_01HXY3VHEC4J4T6N6PYPGG4SMW: 附加包与脚本引擎
  h_01HXY3VHECJMKEVWGJ6SF1KE3B: 生物

**发布:** 2024年5月15日

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、PlayStation 4、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一个Minecraft试炼密室，里面有旗帜和试炼刷怪笼](https://feedback.minecraft.net/hc/article_attachments/26739672009229)

这里是最新的Minecraft基岩版Beta和预览更新中的新内容！请继续在 [feedback.minecraft.net](https://feedback.minecraft.net/) 提交您的建议，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告和投票您发现的任何漏洞！

# 特性与漏洞修复

## 试炼密室

- 生物不再自然生成在试炼密室内 ([MCPE-176986](https://bugs.mojang.com/browse/MCPE-176986 "https://bugs.mojang.com/browse/MCPE-176986"))

## 试炼刷怪笼

- 修复了一个漏洞，导致在切换“domobspawning”游戏规则开关后，试炼刷怪笼不再生成生物 ([MCPE-181209](https://bugs.mojang.com/browse/MCPE-181209 "https://bugs.mojang.com/browse/MCPE-181209"))
- 修复了一个漏洞，导致在不祥试炼中随机射出的箭矢效果为伤害 II 或缓降，而不是中毒或缓慢 IV

## 战利品

- 修复了一个漏洞，导致缓降箭矢可以在不祥宝库中找到，而不是缓慢 IV 箭矢
- 修复了一个漏洞，导致伤害 II 箭矢可以在宝库和补给箱中找到，而不是中毒箭矢 ([MCPE-180653](https://bugs.mojang.com/browse/MCPE-180653 "https://bugs.mojang.com/browse/MCPE-180653"))

## 趋同

- 生物装备掉落的几率已更接近Java版
  - 附魔生物装备不再有双倍掉落几率
  - 每级抢夺魔咒现在给予+1%的生物装备掉落几率，降低至+4%

## 重锤

- 在启动三叉戟激流攻击后切换到重锤时，重锤的猛击攻击不再自动触发 ([MCPE-181000](https://bugs.mojang.com/browse/MCPE-181000))

## 物品

- 旗帜再次可以通过配方书获得 ([MCPE-179650](https://bugs.mojang.com/browse/MCPE-179650))

## 魔咒

- 修复了一个漏洞，导致抢夺魔咒可能导致掉落几率为0%的生物装备仍然掉落，例如恼鬼的剑或不祥试炼的装备

## 领域

- 修复了打开领域故事时可能发生的错误

## 角色创建

- 修复了一个漏洞，导致角色创建器的皮肤去掉眼睛后破坏皮肤纹理加载 ([MCPE-181228](https://bugs.mojang.com/browse/MCPE-181228))

# 技术更新

## 附加包与脚本引擎

- 修复了粒子效果生命周期事件时间线未按预期触发事件的问题

## 生物

- 沼骸的纹理文件现在位于专用文件夹中，与其他实体一致 ([MCPE-179323](https://bugs.mojang.com/browse/MCPE-179323 "https://bugs.mojang.com/browse/MCPE-179323"))