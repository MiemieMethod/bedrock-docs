---
title: 法律与发布说明
---

# 法律与发布说明

/// details-info | 来源信息
- 原文仓库：[github.com/LiteLDev/LeviLamina](https://github.com/LiteLDev/LeviLamina)
- 许可说明：以原仓库或原站点公开许可声明为准。
///



本页不是单一源文件的逐段翻译，而是根据LeviLamina仓库中的法律、许可、行为规范、版本与发布资料所做的站内整理，用于说明这些资料对阅读、安装、分发和升级LeviLamina意味着什么。

## 法律文件的分工

LeviLamina相关法律边界并不集中在同一个文件中，而是分散在仓库自述文件、最终用户许可协议、使用指南、许可证文本和更新日志里。

- [许可证](license.md)说明，LeviLamina的非闭源部分按LGPL-3.0发行。
- [最终用户许可协议](eula.md)说明，LeviMC的闭源软件适用单独的最终用户许可协议；文中明确举出的例子包括PreLoader和PeEditor。
- [使用指南](usage-guidelines.md)说明，LeviLamina名称、品牌、资产及其衍生物的使用边界、免责声明要求和再分发限制。
- [行为准则](code-of-conduct.md)约束社区空间、贡献和公开互动中的行为。
- 英文最终用户许可协议镜像还额外明确，其文本只是中文原文的译本；若两者不一致，应以中文版本为准。

因此，在站内介绍LeviLamina时，不应将“LeviLamina开源部分的LGPL-3.0许可”与“LeviMC闭源软件的最终用户许可协议”混为一谈，也不应把使用指南误解为开源许可证正文。

## 对使用与分发的影响

从官方文件组合来看，至少有以下几项边界需要同时注意：

- 只要流程涉及LeviMC的闭源软件，就不能只看LGPL-3.0，还应同时阅读最终用户许可协议。
- 即使讨论的是LeviLamina项目本身，名称、品牌和资产的使用也还要遵守使用指南。
- 使用指南明确要求，在相关产品、服务、页面或材料中显著声明其并非LeviMC官方产品，且未获LeviMC批准、与LeviMC无关联。
- 使用指南还明确反对重新分发其产品、修改后的产品或产品文档，因此在整理、转述和翻译官方资料时，应保留来源说明，并避免把站内摘要误写成原始法律文本替代品。

## 对升级与运维的影响

LeviLamina的版本兼容性和风险信息同样分散在多个文件中：

- [支持的版本](versions.md)给出LeviLamina版本、BDS版本和客户端版本的对应关系。
- [更新日志](changelog.md)给出每个版本的新增、变更和修复。
- GitHub发布页则提供具体发行包、标签和发布时间。

这意味着部署或升级时不应只看“有没有新版本”，而应同时核对：

1. 目标BDS或客户端是否在支持矩阵中。
2. 该版本是否包含运行时数据升级、头文件同步或生命周期调整。
3. 该版本是否修复了崩溃、漏洞或兼容性问题。

`CHANGELOG.md`中的典型高风险条目包括：

- `1.9.6`：在到达脆弱代码路径前丢弃异常短的数据包，以绕过Mojang修改版RakNet导致的`MCPE-228407`相关崩溃风险。
- `1.9.4`：修复`SubChunkRequestPacket`漏洞。
- `1.9.3`：修复`Certificate::validate`崩溃。

这类信息直接影响服主是否应尽快升级，也影响文档站在介绍LeviLamina时是否需要提醒读者关注更新日志。

## 站内阅读建议

如果目标是研究LeviLamina的法律边界和运维风险，建议按以下顺序阅读：

1. [许可证](license.md)
2. [最终用户许可协议](eula.md)
3. [使用指南](usage-guidelines.md)
4. [支持的版本](versions.md)
5. [更新日志](changelog.md)

如需了解这些内容在概念和入门页面中的落位，可继续参阅[LeviLamina](../../docs/server/levilamina.md)与[LeviLamina入门](../../guides/servers/levilamina.md)。