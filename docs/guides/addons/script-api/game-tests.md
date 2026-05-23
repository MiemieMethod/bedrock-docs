# GameTest框架<!-- md:flag vanilla --><!-- md:flag experimental -->

**GameTest框架（GameTest Framework）**是基岩版脚本API的一部分，允许开发者使用JavaScript编写自动化测试用例，以验证游戏机制和附加包行为是否按预期工作。GameTest需要启用Beta APIs实验性功能。

## 概述

GameTest通过`@minecraft/server-gametest`模块提供，同时依赖`@minecraft/server`模块。测试用例由结构文件和注册的测试函数组成，可以通过`/gametest`命令运行。

自1.19.40版本起，原版GameTest不再包含在游戏内置文件中，需要自行在行为包中添加测试用例。

## 可用命令

- `/gametest runthis` —— 运行范围内最近的GameTest。
- `/gametest runthese` —— 运行范围内所有GameTest。
- `/gametest pos` —— 显示最近GameTest的相对坐标。
- `/gametest clearall [radius: int]` —— 清除指定半径内的所有GameTest。
- `/gametest run <testName: GameTestName> [rotationSteps: int]` —— 创建并运行指定的GameTest。
- `/gametest runset [tag: GameTestTag] [rotationSteps: int]` —— 运行所有带有指定标签的GameTest。
- `/gametest create <testName: string> [width: int] [height: int] [depth: int]` —— 创建指定尺寸的空白GameTest区域。
- `/reload` —— 重新加载所有行为包中的函数和脚本文件（1.19+）。

## 配置清单文件

在行为包的`manifest.json`中声明两个模块依赖：

```json title="BP/manifest.json（依赖部分）"
{
    "dependencies": [
        {
            "module_name": "@minecraft/server",
            "version": "1.7.0-beta"
        },
        {
            "module_name": "@minecraft/server-gametest",
            "version": "1.0.0-beta"
        }
    ]
}
```

## 编写测试用例

每个测试用例需要通过`GameTest.register()`注册。注册时需要指定：

1. 测试类名（字符串，用于命名空间分组）
2. 测试名称（字符串，唯一标识该测试）
3. 测试函数（接收`test`对象的回调）

同时需要通过`.structureName()`指定关联的MCStructure结构文件，结构文件路径规则为`BP/structures/<命名空间>/<名称>.mcstructure`。

```javascript title="BP/scripts/Main.js"
import * as GameTest from "@minecraft/server-gametest";

GameTest.register(
    "wiki",           // 测试类名
    "simpleTest",     // 测试名称
    (test) => {
        const location = { x: 0, y: 0, z: 0 };
        const cow = test.spawn("minecraft:cow", location);

        test.succeedWhen(() => {
            test.assertEntityPresentInArea("minecraft:cow", true);
        });
    }
)
    .maxTicks(410)
    .structureName("wiki:test");  // 对应 BP/structures/wiki/test.mcstructure
```

运行上述注册后，使用`/gametest run wiki:simpleTest`即可在游戏中执行该测试。

/// note | 测试函数的作用域隔离
测试函数在注册时会被锁定，注册后无法从测试函数外部访问测试函数内部的变量，也无法在注册后修改测试函数的逻辑。
///

## 主要测试API

测试函数接收一个`test`对象，其常用方法如下：

/// define
`test.spawn(entityTypeId, location)`

- 在指定位置生成实体，返回`Entity`实例。

`test.assertEntityPresentInArea(entityTypeId, isPresent)`

- 断言指定类型的实体是否在测试区域内存在。

`test.succeedWhen(callback)`

- 注册一个条件回调：当回调不抛出异常时，测试判定为成功。

`test.fail(errorMessage)`

- 立即使测试以指定消息失败。

`test.succeed()`

- 立即标记测试为成功。

`.maxTicks(ticks)`

- 设置测试的最大运行刻数，超时则判定失败（默认100刻）。

`.structureName(name)`

- 指定测试使用的结构文件，格式为`命名空间:名称`。

///
