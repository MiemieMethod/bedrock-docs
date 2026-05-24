---
title: 仓库README
---

# 仓库README

/// info | 来源信息
- 原文仓库：[`LiteLDev/LeviLamina`](https://github.com/LiteLDev/LeviLamina)
- 对应来源：`.knowledge\LeviLamina源码及文档\README.zh.md`、`.knowledge\LeviLamina源码及文档\README.md`
///

![LeviLamina](https://socialify.git.ci/LiteLDev/LeviLamina/image?description=1&font=Raleway&forks=1&issues=1&logo=https%3A%2F%2Fgithub.com%2FLiteLDev%2FLeviLamina%2Fraw%2Frefs%2Fheads%2Fmain%2Fdocs%2Fmain%2Fcontents%2Flogo.svg&name=1&owner=1&pattern=Circuit+Board&pulls=1&stargazers=1&theme=Auto)

[![Discord](https://img.shields.io/discord/849252980430864384?style=for-the-badge&logo=discord)](https://discord.gg/v5R5P4vRZk)
[![Telegram](https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=telegram)](https://t.me/LiteLoader)
[![656669024](https://img.shields.io/badge/656669024-red?style=for-the-badge&logo=qq)](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=ndxRXO1HARA8ing7OunMClOz3cQTogL0&authKey=D7QTcqnzhBzuh3zc%2F70FjgklsVvkCImTjSRqHMwYGCLwIFpxzp%2FflC97Y7AUG%2Fpy&noverify=0&group_code=656669024)
[![937236109](https://img.shields.io/badge/937236109-red?style=for-the-badge&logo=qq)](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=1u0nmmUIZOB716neFTlbyj_2aOQn_TV-&authKey=1lBqM20oOfdKjDnxkq09DjR729fqFfWVnaLQ7VjrDB%2FAg6qwvw6QCwdwYoRUrewU&noverify=0&group_code=937236109)
[![850517473](https://img.shields.io/badge/850517473-red?style=for-the-badge&logo=qq)](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=3Fxt0gwMYkoLPani_vQ9tsNfYrnVy4hK&authKey=2A%2BNk3jmRaK%2FO1FBQSjTIbStAU1kbZWkjEkyh2RTVA015eTg6c4CvVhfByc1BtGZ&noverify=0&group_code=850517473)

中文自述文件原文中的语言入口以“英语页可切换、简体中文为当前页”的状态显示；英文自述文件则相反。为避免在站内镜像中制造伪造的相对链接，本页仅保留这一镜像关系说明，而不直接复刻原始按钮跳转。

轻量级、模块化和多功能的基岩版模组加载器，LiteLoaderBDS的后继者。

LeviLamina是一个非官方的模组加载器，旨在为基岩版提供必不可少的API支持。它提供全面的API、实用接口、事件系统与封装后的开发基础设施，为扩展基岩版的附加游戏特征和功能提供基础。

开发者通常使用C++编写模组，并借助这一套接口以较统一的方式接入事件、命令和其他底层能力。

站内对应的资料入口见[LeviLamina文档归档](index.md)；如需访问官方站点原文，仍可参考[文档](https://lamina.levimc.org/zh/)。

与[官方文档首页](official-docs-home.md)相比，本页更接近仓库落地页：两者都重复出现项目简介与社区入口，但README额外承担安装入口、贡献入口与许可证声明的聚合作用。

如需对照官方文档站入口页中的社区入口与首页鸣谢信息，可再查看[官方文档首页](official-docs-home.md)。

## 中英文镜像关系

LeviLamina仓库同时提供`README.zh.md`和`README.md`两份首页说明。两者在项目定位、社区入口、安装入口、贡献入口和许可证声明上基本一致，但链接落点与个别表述存在差异：

- 中文版README直接链接中文EULA与中文使用指南。
- 英文版README链接英文EULA与英文使用指南镜像。
- 中文版README在贡献部分将行为准则表述为“行为准则”，英文版则直接链接Contributor Covenant行为准则页面。
- 中文版README中的语言切换按钮以中文页为当前页；英文版README中的按钮状态则与之相反。

因此，本站以中文README作为主要转述对象，同时用英文README复核镜像关系和链接差异，避免把中文页中的站内转述误当成唯一版本。

## 从README继续阅读

自述文件原文只给出安装入口标题，不展开兼容矩阵和具体步骤。若按站内链路继续阅读，建议直接分流到对应页面：

- 需要先确认版本匹配时，查看[支持的版本](versions.md)。
- 需要安装与升级时，查看[在服务器上安装](install-server.md)与[在客户端上安装](install-client.md)。
- 需要理解官方首页承担的门户与鸣谢职责时，查看[官方文档首页](official-docs-home.md)。
- 需要提交问题、拉取请求或核对协作约束时，查看[拉取请求模板](pull-request-template.md)与[行为准则](code-of-conduct.md)。
- 需要追溯许可证、最终用户许可协议和使用限制时，查看[法律与发布说明](legal-release-notes.md)、[许可证](license.md)与[最终用户许可协议](eula.md)。

/// warning | 最终用户许可协议和使用准则
你应该仔细阅读并遵守我们的[最终用户许可协议](eula.md)与[使用准则](usage-guidelines.md)。
///

## 安装和使用

请参考[在服务器上安装](install-server.md)和[在客户端上安装](install-client.md)。

## 星标蹭蹭涨

![星标历史图](https://api.star-history.com/svg?repos=LiteLDev/LeviLamina&type=Date)

## 致谢

我们衷心感谢[所有捐赠者](https://5g8svn.sharepoint.com/:x:/s/LiteLDev/EXx2ndbuC-9Bj5SR-FlJ-HUBZWy0wODjQCDb8OkzuKTFJg?e=QBF6nQ)和所有的开发者！

## 贡献

欢迎参与贡献！你可以[提出问题](https://github.com/LiteLDev/LeviLamina/issues/new/choose)或为我们提交拉取请求。

如果需要查看仓库在提交拉取请求时要求贡献者填写的自查条目，可继续参阅[拉取请求模板](pull-request-template.md)。

LeviLamina遵循[行为准则](code-of-conduct.md)。

### 贡献者

这个项目的存在要感谢所有的[贡献者](https://github.com/LiteLDev/LeviLamina/graphs/contributors)。

## 许可证

版权所有©2024 LeviMC，保留所有权利。

本项目的非闭源部分采用LGPL-3.0许可证发行。阅读[许可证](license.md)获取概要，并参阅[COPYING](https://github.com/LiteLDev/LeviLamina/blob/HEAD/COPYING)和[COPYING.LESSER](https://github.com/LiteLDev/LeviLamina/blob/HEAD/COPYING.LESSER)获取原文。
