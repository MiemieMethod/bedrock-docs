# 基岩版命令更新记录

本页整理ProjectXero维护的《Minecraft基岩版命令更新日志》可直接用于开发判断的部分，用于命令迁移、函数兼容性校验与教程版本标注。

- 原始项目：<https://github.com/XeroAlpha/Minecraft-Bedrock-Command-Log>
- 知识库来源：`.knowledge\基岩版命令更新记录\README.md`
- 最新版本命令列表核验：`.knowledge\基岩版命令更新记录\versions\vanilla\26.10.25.txt`与`.knowledge\基岩版命令更新记录\versions\vanilla\26.1.1.txt`

## 最新收录版本

按来源文档当前状态：

- 正式版：`26.1.1`
- 预览版：`26.10.25`

## 记录范围与局限

来源README明确说明，本日志主要依据Android平台可获取的版本整理，因此不收录未在Android平台发布的构建。对于`1.2`以下版本，还存在部分命令无法通过早期WebSocket服务器观察到的问题，因此记录并不完整。

这意味着本页适合用来判断命令语法的大致加入、移除和解除实验性时间点，但不适合作为“所有平台所有构建都完整覆盖”的绝对清单。

## 近期关键变更

| 游戏版本 | 变更摘要 |
| --- | --- |
| 26.10.25 | `camera attach_to_entity`、`camera detach_from_entity`和`camera play_spline`不再需要特定实验性玩法。 |
| 26.0.27 | `camera`新增`play_spline`子命令（实验性）。 |
| 26.0.23 | 新增`packstack`命令。 |
| 1.21.120.24 | `camera`新增`attach_to_entity`和`detach_from_entity`子命令（实验性）。 |
| 1.21.100.25 | `camera fov_clear`和`camera fov_set`不再需要特定实验性玩法。 |
| 1.21.90.23 | `controlscheme`命令不再需要特定实验性玩法。 |
| 1.21.80.25 | `camera entity_offset`与`view_offset`子命令可与`ease`组合使用。 |
| 1.21.60.25 | `camera remove_target`、`target_entity`和`target_center_offset`子命令不再需要特定实验性玩法。 |
| 1.21.60.24 | `script diagnostics startcapture`和`script diagnostics stopcapture`子命令加入。 |
| 1.21.60.23 | `loot mine`来源不再需要特定实验性玩法。 |
| 1.21.50.20 | `schedule delay`子命令加入。 |

## 当前命令清单特征

来源README给出的`26.10.25`命令列表显示，当前构建除常见管理与世界编辑命令外，还包含以下较新的创作相关语法：

- `packstack`命令，可用于输出客户端或服务端包栈。
- `controlscheme`命令，用于控制相机控制方案。
- `inputpermission`命令，用于查询或设置输入权限。
- `script diagnostics startcapture`与`script diagnostics stopcapture`，用于脚本诊断捕获。
- `camera attach_to_entity`、`detach_from_entity`与`play_spline`等较新的相机子命令。

启用教育版选项后，还会额外提供`ability`、`immutableworld`、`wb`和`worldbuilder`等语法<!-- md:flag edu -->。

## 中国版版本对照

来源README附带了中国版正式版与国际版正式版的部分对应关系，可用于在阅读旧教程或旧版中国版资料时粗略换算国际版时间线。该表目前仍标注为“待补充”，因此只宜作为辅助线索，不宜单独作为定论。

| 中国版版本 | 发布日期 | 对应国际版版本 |
| --- | --- | --- |
| `2.1.5.162567` | 2022-04-15 | `1.17.3.0.0` |
| `2.0.0.153450` | 2022-01-21 | `1.17.2.0.0` |
| `1.25.5.146956` | 2021-11-18 | `1.16.203.2.0` |
| `1.24.5.141220` | 2021-09-17 | `1.16.202.2.0` |
| `1.23.5.129766` | 2021-06-29 | `1.16.201.2.0` |

## 未记录版本

来源README还列出了部分未被纳入日志的版本及原因。这些缺口说明：如果正好要排查这些构建，就不能只依赖这份时间线，还需要结合实机、旧导出资料或其他历史文档交叉核对。

| 版本 | 未包含原因 |
| --- | --- |
| `1.0.5.0` | 启动后程序崩溃 |
| `1.0.5.3` | 启动后程序崩溃 |
| `1.8.0.8` | 打开聊天界面后程序崩溃 |
| `1.12.0.27` | 无法进入游戏主界面 |
| `1.12.0.28` | 无法进入游戏主界面 |
| `1.16.200.54` | 进入主界面后程序崩溃 |
| `1.21.50.22` | 测试版发成正式版了 |

## 使用建议

- 在撰写教程时，为命令语法标注最低可用版本。
- 在迁移旧工程时，先核对实验性要求是否已解除，再决定是否保留旧兼容写法。
- 对于命令方块、函数和脚本调用链，优先结合命令版本与目标构建进行实机验证。

## 相关页面

- [命令版本](version.md)
- [命令参考](index.md)
- [命令](../../docs/general/command.md)
- [版本](../../docs/general/version.md#命令版本)
- [如何判断命令能否在目标版本运行](../../topics/command-compatibility.md)
