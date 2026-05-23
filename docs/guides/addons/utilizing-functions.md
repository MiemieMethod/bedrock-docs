# 使用函数

函数文件可以把多条命令放进一个`.mcfunction`文件，再用一条`/function`命令执行。它比命令方块更容易复制、版本管理和批量修改，非常适合地图机制、初始化流程和调试工具。

## 创建functions文件夹

函数属于行为包。创建如下结构：

/// html | div.treeview
- `demo_BP`
    - `manifest.json`
    - `functions`
        - `wiki`
            - `ouch.mcfunction`
///

`wiki/ouch.mcfunction`内容如下：

```mcfunction title="functions/wiki/ouch.mcfunction"
say Bye...
playsound random.explode @a
teleport @s ~10 ~10 ~10 true
say OUCH!
```

/// note | 注意
函数文件中的命令不写开头的`/`。
///

## 执行函数

进入启用了行为包和作弊的世界，运行：

```mcfunction
/function wiki/ouch
```

函数名即相对于`functions`文件夹的路径，不含扩展名。

## tick.json：每刻自动执行

函数文件夹里可以放一个`tick.json`文件，用来注册需要**每个游戏刻自动执行**的函数，效果类似于循环命令方块，但在服务端运行，且无需玩家在附近：

```json title="BP/functions/tick.json"
{
  "values": [
    "wiki/main"
  ]
}
```

`values`数组里的每个字符串都是一个函数路径。列出的所有函数会在每刻按顺序执行。

/// warning | 加载时机
`tick.json`中注册的函数会在**世界初始化时立即开始运行**，不等待玩家加载完成。这意味着在首刻执行的命令可能无法命中任何玩家。建议配合条件判断（如`execute if entity @a`）进行保护。
///

## 文件夹结构最佳实践

良好的命名规范可以让团队协作和长期维护更加轻松：

1. **使用命名空间根目录**：所有函数放在`functions/<命名空间>/`下，命名空间通常是你的名字缩写或项目名。
   - ✅ `BP/functions/wiki/random_number.mcfunction`
   - ❌ `BP/functions/random_number.mcfunction`

2. **全小写蛇形命名（snake_case）**：文件夹和文件名只使用小写字母、数字和下划线。
   - ✅ `add_all.mcfunction`
   - ❌ `Add-All.mcfunction`

3. **嵌套结构清晰**：路径层级反映功能归属，避免将多个概念压缩为单一文件名。
   - ✅ `wiki/event/players/on_death.mcfunction`
   - ❌ `wiki/player_death.mcfunction`

4. **动词在前（action_object格式）**：文件名动词放在主语之前。
   - ✅ `add_all`、`shuffle_position`
   - ❌ `all_add`、`position_shuffle`

5. **路径总长度不超过80个字符**（主机平台限制）。

6. **统一复数或单数**：同一层级内不要混用，保持一致。

## 注释风格指南

函数文件支持用`#`开头的行作为注释。建议按如下层级区分：

| 级别 | 格式 | 用途 |
|---|---|---|
| 一级标题 | `# 全大写` | 功能模块分区 |
| 二级标题 | `## 首字母大写` | 子功能说明 |
| 三级标题 | `### 普通行文` | 具体步骤注释 |

示例：

```mcfunction title="BP/functions/wiki/ability/fire_trail.mcfunction"
# ON PLAYER ITEM DROP

## Give Effects
### Fire resistance
execute at @e[type=item,name="Fire Trail Ability"] run effect @p[r=3] fire_resistance 10 255

## Add Particle Time
execute at @e[type=item,name="Fire Trail Ability"] run scoreboard players set @p[r=3] wiki:ability.fire_trail 200

## Delete Item
kill @e[type=item,name="Fire Trail Ability"]


# ENTITY TIMER

## Emit Particle Trail
execute at @a[scores={wiki:ability.fire_trail=1..}] run particle minecraft:basic_flame_particle ~~~

## Countdown Timer
scoreboard players remove @a[scores={wiki:ability.fire_trail=1..}] wiki:ability.fire_trail 1
```

一级标题前建议留两个空行，二级标题前留一个空行，以提升可读性。

## 初始化结构示例

推荐把初始化逻辑按功能拆分：

/// html | div.treeview
- `functions`
    - `wiki`
        - `init`
            - `scoreboard.mcfunction`
            - `give_items.mcfunction`
            - `all.mcfunction`
///

```mcfunction title="functions/wiki/init/all.mcfunction"
function wiki/init/scoreboard
function wiki/init/give_items
say 初始化完成
```

## 限制与注意

- **10000条命令上限**：单次`/function`调用（含所有子函数）最多执行10000条命令，超出将报错。
- **同一刻执行**：函数内所有命令在同一刻运行，大型函数可能导致帧率波动。
- **版本继承**：函数按`manifest.json`中的`min_engine_version`运行，例如`1.19.50`会采用新版`execute`语法。
- **调试方法**：启用内容日志（见"帮助"文章），可以看到函数中的命令错误、行号和语法提示。

## 专业工作流（可选）

### Visual Studio Code + 命令检查插件

VS Code是目前最适合编写函数包的编辑器。安装后在扩展市场搜索`MCBE Command Checker`，可获得命令语法高亮、自动补全和实时错误提示。

### GitHub版本管理

将函数包托管在GitHub，可以追踪修改历史、多人协作，并将特定版本作为`.mcpack`发布。推荐使用GitHub Desktop简化操作。

### 目录联接（Directory Junction）

通过Windows目录联接（`mklink /J`），可以将GitHub工作目录直接链接到Minecraft的`development_behavior_packs`目录，使VS Code中保存的修改立即在游戏中生效，无需手动复制文件：

```cmd
mklink /J "C:\Users\你的用户名\AppData\Roaming\Minecraft Bedrock\...\development_behavior_packs\我的项目" "C:\Github\我的项目"
```

链接完成后，在游戏里运行`/reload`即可实时应用改动。

## 常见错误

- 文件夹写成`function`：应为`functions`。
- 命令前写了`/`：函数文件中不需要斜杠。
- 世界没有开启作弊：`/function`无法执行。
- 修改后未刷新：先运行`/reload`，若仍不生效请退出世界重进。

## 继续阅读

- [命令](../../docs/general/command.md)
- [命令系统实践模板](../misc/command-systems.md)
- [记分板计时器](../misc/scoreboard-timers.md)
