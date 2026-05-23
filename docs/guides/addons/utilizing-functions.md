# 使用函数

函数文件可以把多条命令放进一个`.mcfunction`文件，再用一条`/function`命令执行。它比命令方块更容易复制、版本管理和批量修改，非常适合地图机制、初始化流程和调试工具。

## 创建functions文件夹

函数属于行为包。创建如下结构：

/// html | div.treeview
- `demo_BP`
    - `manifest.json`
    - `functions`
        - `ouch.mcfunction`
///

`ouch.mcfunction`内容如下：

```mcfunction title="functions/ouch.mcfunction"
say Bye...
playsound random.explode
teleport @s ~10 ~10 ~10 true
say OUCH!
```

注意，函数文件中的命令不写开头的`/`。

## 执行函数

进入启用了行为包和作弊的世界，运行：

```mcfunction
/function ouch
```

如果函数放在子文件夹中，例如`functions/init/ouch.mcfunction`，执行名就是：

```mcfunction
/function init/ouch
```

## 使用函数做初始化

建议把初始化逻辑放进单独目录：

/// html | div.treeview
- `functions`
    - `init`
        - `scoreboard.mcfunction`
        - `give_items.mcfunction`
        - `all.mcfunction`
///

```mcfunction title="functions/init/all.mcfunction"
function init/scoreboard
function init/give_items
say 初始化完成
```

函数最多不能在一次调用中运行超过10000条命令。大型项目应拆成多个函数，必要时用命令方块、计划刻或脚本分批执行。

## 常见错误

- 文件夹写成`function`：应为`functions`。
- 命令前写了`/`：函数文件中不需要斜杠。
- 世界没有开启作弊：`/function`无法执行。
- 包改了但没生效：先运行`/reload`，如果仍然失败，再退出世界重进。

函数不会替代所有命令系统，但它能让命令逻辑从世界里的命令方块迁移到行为包中。后续制作世界模板时，把函数随世界一起分发会非常方便。
