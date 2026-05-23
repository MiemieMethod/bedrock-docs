# Ore UI

**Ore UI**是Mojang Studios公开源代码的**用户界面（User Interface）**构建块集合，用于使用网页技术构建电子游戏界面。其公开仓库说明该技术被Minecraft基岩版和Minecraft Legends等项目使用，并以React与TypeScript为主要基础。

## 概述

Ore UI不是Minecraft基岩版向附加包、资源包或脚本开放的界面接口。它更接近Mojang内部和相关项目使用的界面技术栈：界面可以借助嵌入式网页运行环境在游戏中显示，并使用React组织组件结构，同时通过专门的状态管理机制减少频繁界面更新造成的性能成本。

Ore UI当前公开文档的核心内容集中在React Facet。React Facet是面向高性能游戏界面的React状态管理库，设计目标是在保留React开发体验的同时，避免普通React状态更新引发过多重新协调。其主要思想是让叶级界面值，如样式、文本内容和HTML特性，在不触发完整React组件重新渲染的情况下更新。

## 组成

公开资料中列出的主要包包括：

- `@react-facet/core`：提供**方面（Facet）**核心结构、创建与操作函数、React钩子、相等性检查和辅助函数。
- `@react-facet/dom-fiber`：提供理解方面的自定义React渲染器，并提供`fast-*`组件。
- `@react-facet/shared-facet`：提供用于和游戏引擎一侧数据通信的共享方面机制。
- `@react-facet/dom-fiber-testing-library`：提供与自定义渲染器配套的测试工具。

公开仓库还提到`@mojang/react-gamepad`，其目标是声明式的手柄焦点导航，但公开文档中未提供可用细节。

## React Facet

React Facet使用可观察状态保存会随时间变化的界面数据。方面可以被组件订阅、映射、组合和传递。与普通React状态相比，方面的引用通常保持稳定，实际变化发生在其内部值上，因此适合频繁更新的游戏界面数据。

React Facet文档强调以下机制：

- `useFacetState`用于创建组件内部的方面状态。
- `useFacetMap`和`useFacetMemo`用于从一个或多个方面派生新的方面。
- `useFacetEffect`和`useFacetLayoutEffect`用于在方面值变化时执行副作用。
- `useFacetCallback`用于在回调中读取方面当前值。
- `useFacetUnwrap`会把方面值转为普通React状态，但会导致组件重新渲染，因此文档要求谨慎使用。
- `NO_VALUE`表示方面尚未持有可用值，读取方面值时需要显式处理这种状态。

为了减少无意义更新，React Facet还提供多种相等性检查。简单原始值可以使用严格相等，数组、对象和嵌套结构则可以使用浅比较、统一元素比较或自定义比较函数。

## 渲染模型

React Facet推荐通过`@react-facet/dom-fiber`提供的自定义渲染器进行渲染。该渲染器提供`fast-div`、`fast-text`、`fast-input`、`fast-textarea`、`fast-img`、`fast-a`、`fast-span`和`fast-p`等`fast-*`组件。此类组件可以直接接受方面作为属性值，从而让属性、文本和样式更新绕过常规React重新协调。

`fast-text`没有直接对应的HTML元素，它用于将方面中的文本渲染为文本节点。`fast-*`组件只支持面向目标游戏界面环境所需的一部分HTML属性和原生事件，并不追求与`react-dom`完全一致。

## 与Minecraft基岩版开发的关系

Ore UI与[JSON UI](json-ui.md)不同。JSON UI是资源包能够覆盖和修改的基岩版游戏内界面定义系统，而Ore UI是基于React、TypeScript和嵌入式网页技术的界面库。附加包开发者不能通过资源包把Ore UI组件直接加入游戏界面，也不能把React Facet当作`@minecraft/server-ui`或JSON UI的替代品使用。

Ore UI也不等同于[编辑器](editor.md)扩展接口。Minecraft编辑器扩展仍以`@minecraft/server-editor`等脚本模块为公开入口；公开Ore UI资料没有说明普通创作者可以在编辑器扩展中直接调用Ore UI内部组件。因而，在基岩文档中，Ore UI主要用于说明Minecraft相关官方工具和项目可能采用的界面技术背景，而不是作为附加包或脚本开发的直接教程对象。

## 限制

公开资料没有完整说明Ore UI在Minecraft基岩版内部的集成层、具体界面资源、编辑器界面实现细节或`@mojang/react-gamepad`的实际接口。公开文档主要面向React Facet库的使用者，而不是面向Minecraft基岩版普通创作者。因此，除非未来出现稳定且公开的Minecraft开发入口，Ore UI不应被视为基岩版附加包界面API。
