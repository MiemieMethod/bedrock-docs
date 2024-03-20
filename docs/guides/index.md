# 教程

这里提供了有关Minecraft基岩版技术开发的各种教程。如果你对想要开发的领域不知道该怎么开始以及怎么进行下去，你可以参考本页面中列出的教程，以下内容将引导你在不同技术领域进行开发学习。

<div class="grid cards" markdown>

-   :material-code-json:{ .lg .middle } __附加包__

    ---

    附加包可以通过数据驱动向游戏中加入新内容或修改原有内容，实现内容的基础定义。

    [:octicons-arrow-right-24: 制作第一个附加包](addons/index.md)

-   :material-script-text:{ .lg .middle } __社区模组__

    ---

    玩家社区开发出了许多模组格式，使得我们可以对原版游戏以另一种方式修改。

    [:octicons-arrow-right-24: 开始学习社区模组](community-mods/index.md)

-   :material-tools:{ .lg .middle } __软件工具__

    ---

    各种各样的软件工具可以使你在开发过程中更加轻松地创作丰富的内容。

    [:octicons-arrow-right-24: 尝试使用这些软件](tools/index.md)

-   :material-server:{ .lg .middle } __服务端__

    ---

    构建服务端内容，让来自各地的玩家一同体验Minecraft游戏世界。

    [:octicons-arrow-right-24: 了解服务端内容](servers/index.md)

-   :material-brush-variant:{ .lg .middle } __着色器__

    ---

    编写着色器可以使你的游戏世界更加色彩斑斓，体验不一样的游戏氛围。

    [:octicons-arrow-right-24: 试着接触着色器](shaders/index.md)

-   :material-shape-plus:{ .lg .middle } __杂项教程__

    ---

    Minecraft基岩版技术开发除了以上几个大板块外，还有一些分散独立的内容。

    [:octicons-arrow-right-24: 查看杂项教程](misc/index.md)

</div>

## 概述

### 附加包

附加包中最重要的部分就是 __数据驱动（Data-Driven）__ ，其指通过某些特定的数据格式来驱动游戏内容。在Minecraft基岩版中，最常用的数据格式是[JSON](https://zh.wikipedia.org/wiki/JSON)。将各种对游戏的修改数据以JSON等形式打包成附加包，并加载到游戏中，即可实现对游戏内容的定义和修改。

### 社区模组

除官方提供的模组接口外，玩家社区也在积极开发不同的模组格式，例如ICMod、ModPE、NMod等，这些模组格式一定程度上丰富了模组生态，创造出了更多新奇玩法。了解并学习社区模组，参与社区模组的编写，可以使你体验不一样的编写过程、实现更多独特的游戏玩法。

### 软件工具

合适的工具可以极大地提高工作效率，[Blockbench](https://www.blockbench.net/)、[Snowstorm](https://snowstorm.app/)和[Visual Studio Code](https://code.visualstudio.com/)等都是开发中高频使用的工具，提前准备并学习这些软件的使用方法能使后面的开发过程更轻松。

### 服务端

服务端是游戏运行的重要组成部分。学习相关内容，可以尝试搭建Minecraft服务器、编写服务端插件等。

### 着色器

着色器用于实现图像渲染，它在游戏中负责为我们提供绚丽的游戏画面。想要改变原有的游戏画面，获得不一样的视觉效果，你可以试着了解着色器基础知识并修改创作自己的着色器。

## 规范

/// note
“规则”是必须遵守的，“规范”可以遵守也可以不遵守，但规范是社区约定俗成的良好习惯，这意味着记住并保持规范更有利于社区交流和减少错误。
///

在开发过程中我们会经常与各种代码和文本标记打交道，也会创建许多文件和文件夹，为了使它们更整洁美观、便于维护，养成良好的开发习惯是至关重要的。

### 命名格式

对文件或标识符等命名时，最基本应使用英文、下划线和数字来命名，而避免使用中文等其他特殊字符，这些特殊字符可能会因为编码错误造成无法正常读取等异常情况，即使某些地方允许使用它们，也请保持良好的命名习惯。

好的命名即是注释，不管对什么东西命名，遵循“见名知义”的原则总是不会错的，也就是说命名要有实际意义。我们一般希望能够通过一个东西的名字来知道它是干什么的，所以名字应该是对命名对象的总结。如果你不知道命名对象的英文名是什么，可以通过翻译软件或查阅对应资料来获取正确命名。下面列举了一些命名案例：

| 正确命名            | 错误命名 |
| ------------------ | -------- |
| getAllVals         | abc      |
| EntityTypeIterator | 123      |
| test_for_block     | 测试     |
| RANGE_MAX          | x        |

命名一般情况下不宜过长，这不方便我们阅读，而且有些地方甚至会有长度限制，但如果遇到需要较多或较长的单词才能表达出含义时，你可以适当地进行缩写。缩写时一般取单词前三个字母或按照音节来分，有些专有名词也有对应的首字母缩写，下面列举了一些缩写案例：

| 全名              | 缩写 |
| ----------------- | ---- |
| argument          | arg  |
| boolean           | bool |
| Point of Interest | POI  |

值得注意的是，缩写不应过度，如果一味地追求缩短命名长度，只会适得其反——无法辨认出缩写的内容及含义是什么。

#### 命名法

我们通常约定一些命名法来保持命名风格的统一，这不仅能增加代码整洁性，还能提高交流和阅读效率。

/// tip
不同编程语言的命名风格可自行在网上查阅。
///

以下是一些常用的命名法：

- __帕斯卡命名法（Pascal Case）__：所有单词首字母大写，单词之间不添加任何字符，例如“BlockStateType”。
- __驼峰命名法（Camel Case）__：分为“小驼峰”和“大驼峰”。小驼峰命名法除第一个单词首字母不大写外，其他单词首字母均大写，单词之间不添加任何字符，例如：“getAllPlayers”；大驼峰命名法又叫帕斯卡命名法，命名规则参上。
- __匈牙利命名法（Hungarian Case）__：基本规则为，变量名=属性+类型+描述，即开头先用小写字母前缀作为标识，后面的所有单词首字母大写，单词之间不添加任何字符，例如“iEntityAge”（前缀“i”表示int类型）。匈牙利命名法在曾经使用较频繁，现在几乎不使用。
- __蛇形命名法（Snake Case）__：分为“小蛇形”和“大蛇形”。小蛇形命名法所有字母小写，单词之间使用下划线连接，例如“max_stack_size”；大蛇形命名法所有字母大写，单词之间使用下划线连接，例如“ENTITY_DAMAGE_TYPE”。
- __串式命名法（Kebab Case）__：所有字母小写，单词之间使用连字符连接，例如“system-debug-utils”。

不同的命名法使用场景和含义都不同，在后面的教程中你会经常见到这些命名法，并了解它们的含义。

#### 命名空间与标识符

命名空间与标识符是我们在开发过程中经常遇到的概念，当你向游戏中添加一个实体、方块或者物品时，你就需要为它拟定一个 __赋命名空间标识符（Namespaced Identifier）__。在保证命名合法的前提下，命名空间的命名需要其保证唯一性，我们一般使用项目名称，不宜使用过于简单和常见的单词或字母组合，因为这容易导致撞命名空间。对于标识符，一般为命名对象的名称，在有变种或不同状态的情况下使用形容词加以描述。

### 缩进
缩进指对文本与边界之间距离的调整，正确的缩进能够直观地展示出文本内容的层级关系。在开发时应为代码添加合适的缩进，并且单位缩进的宽度应保持一致。标准单位缩进宽度为四个空格或一个制表符，有些时候也使用两个空格宽度的单位缩进。

下面是一些正确缩进示范：

/// tab | JSON
```{.json}
{
    "format_version": 2,
    "header": {
        "description": "This is my pack.",
        "name": "My Pack",
        "uuid": "d803ad87-f59f-4c9c-b679-612fc5703732",
        "version": [1, 0, 0],
        "min_engine_version": [1, 20, 0]
    },
    "modules": [
        {
            "description": "test",
            "type": "resources",
            "uuid": "dd2dbed5-ce3d-47b7-b09b-6bd20174de09",
            "version": [1, 0, 0]
        }
    ]
}
```
///
/// tab | TypeScript
```{.typescript}
import { EntityQueryOptions, DimensionLocation } from '@minecraft/server';

function mobParty(targetLocation: DimensionLocation) {
    const mobs = ['creeper', 'skeleton', 'sheep'];

    // create some sample mob data
    for (let i = 0; i < 10; i++) {
        const mobTypeId = mobs[i % mobs.length];
        const entity = targetLocation.dimension.spawnEntity(mobTypeId, targetLocation);
        entity.addTag('mobparty.' + mobTypeId);
    }

    const eqo: EntityQueryOptions = {
        tags: ['mobparty.skeleton'],
    };

    for (const entity of targetLocation.dimension.getEntities(eqo)) {
        entity.kill();
    }
}
```
///

## 过时教程

<div class="grid cards" markdown>

-   :material-clock-time-nine:{ .lg .middle } __过时教程__

    ---

    随着时间推移某些教程已经不再适用，这里记录了各个板块曾经适用的教程。如果你需要在旧版本进行技术开发，可以在此参考对应版本的教程。

    [:octicons-arrow-right-24: 查看过时教程](outdated/index.md)

</div>
