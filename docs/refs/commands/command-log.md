# 基岩版命令更新记录

这份时间线适合用来判断命令语法何时加入、何时移除，以及何时解除实验性要求。做命令迁移、函数兼容性校验和教程版本标注时，都可以先从这里下手。

## 当前可核对的最新版本

- 正式版：`26.1.1`
- 预览版：`26.10.25`

这两个版本的命令表并不相同。`26.10.25`预览版已经出现`camera attach_to_entity`、`camera detach_from_entity`和`camera play_spline`，而`26.1.1`正式版命令表中尚未出现这三条语法。因此，阅读“当前命令”时，必须先分清自己面对的是正式版还是预览版。

## 当前命令表的观察口径

按当前可核对的两份命令表，`26.1.1`正式版与`26.10.25`预览版都能整理出78个命令标签。两者共同包含`packstack`、`controlscheme`、`inputpermission`和`schedule delay`等较新的语法，差异主要集中在`camera attach_to_entity`、`camera detach_from_entity`和`camera play_spline`这类仍处于预览版领先阶段的子命令。

这份记录反映的是对应游戏构建里可直接观察到的命令表，不适合直接当作BDS管理命令的完整清单使用。以`26.1.1`正式版命令表为例，可以看到`/stop`，但看不到`/allowlist`、`/reloadconfig`和`/sendshowstoreoffer`等更偏向专用服务端运维的语法。需要核对这类命令时，还应结合专门的服务端参考资料一起判断。

## 记录范围与局限

这份时间线主要按Android平台可取得的版本整理，因此不覆盖所有平台上的全部构建。对于`1.2`以下版本，部分命令又无法通过早期WebSocket服务器观察到，所以记录并不完整。

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

以`26.10.25`预览版的命令列表为例，当前测试构建除常见管理与世界编辑命令外，还包含以下较新的创作相关语法：

- `packstack`命令，可用于输出客户端或服务端包栈。
- `controlscheme`命令，用于控制相机控制方案。
- `inputpermission`命令，用于查询或设置输入权限。
- `script diagnostics startcapture`与`script diagnostics stopcapture`，用于脚本诊断捕获。
- `camera attach_to_entity`、`detach_from_entity`与`play_spline`等较新的相机子命令。

若目标是当前正式版，则应先以`26.1.1`命令表为准。该版本已经包含`packstack`、`controlscheme`、`inputpermission`和`schedule delay`等较新的语法，但尚未包含`camera attach_to_entity`、`camera detach_from_entity`和`camera play_spline`。

启用教育版选项后，还会额外提供`ability`、`immutableworld`、`wb`和`worldbuilder`等语法<!-- md:flag edu -->。

## 中国版版本对照

如果需要阅读旧教程或旧版中国版资料，可以先用这张对照表粗略换算到国际版时间线。不过这张表本身仍未补完，所以更适合当辅助线索，不适合单独下定论。

| 中国版版本 | 发布日期 | 对应国际版版本 |
| --- | --- | --- |
| `2.1.5.162567` | 2022-04-15 | `1.17.3.0.0` |
| `2.0.0.153450` | 2022-01-21 | `1.17.2.0.0` |
| `1.25.5.146956` | 2021-11-18 | `1.16.203.2.0` |
| `1.24.5.141220` | 2021-09-17 | `1.16.202.2.0` |
| `1.23.5.129766` | 2021-06-29 | `1.16.201.2.0` |

## 未记录版本

有些版本没有被纳入时间线，而且缺失原因已经明确列出。如果正好要排查这些构建，就不能只依赖这份时间线，还需要结合实机、旧导出资料或其他历史文档交叉核对。

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