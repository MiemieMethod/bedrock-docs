# MoLang

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/editor-docs/other/molang/](https://bridge-core.github.io/editor-docs/other/molang/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/editor-docs/other/molang.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/editor-docs/other/molang.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@9839a71bdc05d011b1ab4f79f88131b78b70e5db -->
- 该页面的作者有：
    - <!-- md:samp @solveddev -->
///

由bridge.团队使用和开发的快速MoLang解析器。该库全面支持Minecraft的所有MoLang功能。

## 关于

> MoLang是一种基于简单表达式的语言，旨在用于运行时快速计算数值。其重点仅在于在JavaScript于大规模情形下性能不佳的高性能系统中启用类似脚本的功能。我们需要在这些低级系统中具备脚本能力，以支持最终用户的模组功能、自定义实体、渲染和动画。
>
> \- 来自Minecraft文档

## 安装

- `npm i molang`
  
  **或者**
  
- 下载`dist/main.web.js`文件并将脚本添加到您的HTML页面中（通过全局`MoLang`对象访问库）。

## 基本用法

要执行一个基本的MoLang语句，首先构造一个新的`MoLang`类实例。第一个构造函数参数是您的MoLang脚本将可以访问的环境，第二个参数配置MoLang解释器。请查看[`IParserConfig`接口了解所有可用选项](https://github.com/bridge-core/MoLang/blob/master/lib/main.ts)。

`molang.execute(...)`简单地执行一个MoLang脚本并返回其计算的值。

```javascript
import { MoLang } from 'molang'

const molang = new MoLang(
  {
    query: {
      x: 0,
      get(val) {
        return val + 4
      },
    },
  },
  { useCache: true }
)
molang.execute('query.x + query.get(3) == 7')
```

### 设置嵌套环境

对于上下文切换操作符`->`，您可以这样设置嵌套环境：

```javascript
import { MoLang, Context } from 'molang'

const molang = new MoLang({
  query: {
    test: 1,
  },
  context: {
    other: new Context({
      query: { test: 2 },
    }),
  },
})

molang.execute('query.test') // 返回1
molang.execute('context.other->query.test') // 返回2
```

## 使用自定义MoLang函数

自定义MoLang函数旨在支持bridge内的`.molang`文件。

```javascript
import { CustomMoLang } from 'molang'

const customMoLang = new CustomMoLang({})

const moLangFunctions = ... // 以某种方式加载定义自定义函数的MoLang输入

// 使自定义函数在 MoLang 解析器中可用
customMoLang.parse(moLangFunctions)

const moLangSource = ... // 以某种方式从JSON文件加载MoLang源

const transformedSource = customMoLang.parse(moLangSource)
... // 将转换后的源字符串写回JSON文件或进行进一步处理
```

自定义MoLang函数定义如下：

```javascript
function('sq', 'base', {
  return math.pow(a.base, 2);
});

function('pow', 'base', 'exp', {
  return a.exp == 0 ? 1 : a.base * f.pow(a.base, a.exp - 1);
});
```

- 第一个参数总是定义函数名称
- 除最后一个参数外，所有后续参数定义输入参数
- 最后一个参数是函数体
- 临时变量会自动作用域到当前函数体
- 基础递归被支持，只要解释器能在编译时停止递归调用
- 要在MoLang脚本中调用函数，只需使用`f.sq(2)`或`f.pow(3, 2)`

## 使用AST脚本

您可以编写任意脚本来遍历该库构建的抽象语法树。

```javascript
import { MoLang, expressions } from 'molang'

const moLang = new MoLang()

let ast = moLang.parse(`context.other->query.something + 1`)
const { NumberExpression } = expressions

// 这将所有 MoLang 脚本中的数字递增
ast = ast.walk(expr => {
  if (expr instanceof NumberExpression)
    return new NumberExpression(expr.eval() + 1)
})

const output = ast.toString() // 'context.other->query.something+2'
```

## 性能

**免责声明：**bridge的MoLang库和Blockbench的库通常都足够快。然而，bridge的MoLang解释器在执行各种不同脚本（缓存无效）时表现出色，解释原版MoLang脚本的速度可快达10倍。

### 原版脚本

以下脚本在第一次测试中执行了100,000次：

`variable.hand_bob = query.life_time < 0.01 ? 0.0 : variable.hand_bob + ((query.is_on_ground && query.is_alive ? math.clamp(math.sqrt(math.pow(query.position_delta(0), 2.0) + math.pow(query.position_delta(2), 2.0)), 0.0, 0.1) : 0.0) - variable.hand_bob) * 0.02;`

### MoLang

由bridge.使用

| 测试                       | 平均时间    |
| -------------------------- | ----------- |
| 解析并执行（未缓存）       | 1253.332ms  |
| 解析并执行（已缓存）       | 90.036ms    |

### MoLangJS

由Blockbench和Snowstorm使用

| 测试                       | 平均时间    |
| -------------------------- | ----------- |
| 解析并执行（未缓存）       | 11872ms     |
| 解析并执行（已缓存）       | 185.299ms   |

### 早期返回

与上述相同的脚本，只是在其前面插入了一个`return 1;`。bridge的解释器足够智能，能够在解析`return 1;`后识别整个表达式为静态。这类优化在我们的库中随处可见。

### MoLang

由bridge.使用

| 测试                       | 平均时间    |
| -------------------------- | ----------- |
| 解析并执行（未缓存）       | 103.61ms    |
| 解析并执行（已缓存）       | 8.835ms     |

### MoLangJS

由Blockbench和Snowstorm使用

| 测试                       | 平均时间    |
| -------------------------- | ----------- |
| 解析并执行（未缓存）       | 13230.682ms |
| 解析并执行（已缓存）       | 147,786ms   |

## MoLang编程游乐场

我们使用此解释器构建了一个非常基础的MoLang编程游乐场。您可以在[bridge-core.github.io/molang-playground](https://bridge-core.github.io/molang-playground)使用它。