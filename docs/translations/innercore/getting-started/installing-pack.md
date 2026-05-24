# 安装引擎

/// details-info | 署名信息
- 该页面内容翻译自[nernar.github.io](https://nernar.github.io/docs/getting-started/installing-pack)
- 原文档采用[GNU通用公共许可证第3版](https://www.gnu.org/licenses/gpl-3.0.html)（GPL-3.0）授权
///

InnerCore开发前需要先安装Horizon启动器并下载可用包。原文档强调，不同Android版本在存储访问权限上差异较大，目录访问方式也随之变化。

## 基本流程

1. 安装Horizon启动器。
2. 首次启动后下载Inner Core、Inner Core Test或Inner Core Legacy中的目标包。
3. 进入包目录，确认`packs`、`logs`、`innercore/mods`等关键路径可访问。

## 目录定位要点

- Android11及以下版本通常可直接通过`games/horizon`访问。
- 较新版本通常需通过`Android/data/com.zheka.horizon/files/horizon`访问。

## 实务建议

- 维护旧项目前先确认目标设备系统版本与目标包版本。
- 报错排查优先收集`logs`目录完整日志，而非只截取片段。
- 不要直接修改包内`assets`目录；资源应通过项目构建配置加载。