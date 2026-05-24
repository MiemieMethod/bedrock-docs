---
comments: true
---

# Ore UI API参考

**Ore UI**（React Facet）是Mojang Studios开发的高性能游戏UI库。本页面提供Ore UI API的结构化参考。

## 概述

React Facet基于**方面**（Facet）的概念进行状态管理，旨在避免React传统状态管理的性能开销。完整的官方文档请参见[Ore UI官方仓库](https://github.com/Mojang/ore-ui)。

## 核心包

### `@react-facet/core`

提供方面的基础结构和React钩子。

#### 主要钩子

**状态与派生钩子：**

- `useFacetState(initialValue)` - 创建局部方面状态
- `useFacetMap(mapFn, dependencies, facetDependencies)` - 派生新方面（轻量级）
- `useFacetMemo(computeFn, dependencies, facetDependencies)` - 缓存派生方面
- `useFacetCallback(callbackFn, dependencies, facetDependencies)` - 记忆化回调
- `useFacetRef(initialValue)` - 方面引用追踪
- `useFacetWrap(value)` - 将值或方面转换为方面
- `useFacetWrapMemo(value, dependencies, equalityCheck)` - 稳定方面引用包装

**副作用钩子：**

- `useFacetEffect(effect, facetDependencies)` - 方面变化时执行副作用
- `useFacetLayoutEffect(effect, facetDependencies)` - 同步方面副作用

**值提取钩子：**

- `useFacetUnwrap(facet)` - 提取普通值（会触发重新渲染）

**转移钩子：**

- `useFacetTransition(startTransition)` - 标记低优先级更新

#### 相等性检查

控制方面更新时的比较策略：

- `defaultEqualityCheck` - 基元值用`===`，对象/数组始终不同（性能优化）
- `strictEqualityCheck` - 类型安全的严格相等
- `shallowObjectEqualityCheck` - 浅对象比较
- `shallowArrayEqualityCheck` - 浅数组比较
- `shallowObjectArrayEqualityCheck` - 对象数组浅比较
- `createUniformObjectEqualityCheck` - 自定义统一对象比较
- `createUniformArrayEqualityCheck` - 自定义统一数组比较
- `createObjectKeySpecificCheck` - 按键自定义比较
- `createOptionalValueEqualityCheck` - 可选值比较

#### 辅助函数

- `multiObserve(facets, callback)` - 同时观察多个方面
- `hasDefinedValue(facet)` - 检查方面是否有定义的值（非`NO_VALUE`）
- `areAllDefinedValues(...facets)` - 检查所有方面是否有定义的值
- `NO_VALUE` - 特殊符号，表示方面未持有可用值

### `@react-facet/dom-fiber`

提供自定义React渲染器和`fast-*`组件。

#### `fast-*`组件

直接接受方面作为属性的DOM元素：

| 组件 | 用途 | HTML等价物 |
|------|------|-----------|
| `fast-div` | 容器元素 | `<div>` |
| `fast-text` | 文本内容（文本节点） | 文本节点 |
| `fast-input` | 文本输入 | `<input type="text">` |
| `fast-textarea` | 多行文本输入 | `<textarea>` |
| `fast-img` | 图像 | `<img>` |
| `fast-a` | 链接/锚点 | `<a>` |
| `fast-span` | 内联元素 | `<span>` |
| `fast-p` | 段落 | `<p>` |

#### 渲染API

- `createRoot(container)` - 创建React根实例并渲染
- `render()` - 直接渲染到DOM

#### Gameface优化

`fast-*`组件支持特殊的数值属性以优化Coherent Labs Gameface的性能：

- 属性名以`PX`、`VH`或`VW`结尾的可以接收数值而非字符串
- 示例：`<fast-div widthPX={100} heightVH={50} />`

### `@react-facet/shared-facet`

提供与游戏引擎通信的共享方面机制。

#### 组件与钩子

- `SharedFacetDriverProvider` - 包装应用的共享方面驱动提供者
- `useSharedFacet(selector)` - 消费共享方面
- `sharedFacet(name, initialValue)` - 定义共享方面
- `sharedSelector(selectorFn, facetDependencies)` - 创建共享方面选择器

### `@react-facet/dom-fiber-testing-library`

提供与自定义渲染器配套的测试工具。

## 挂载组件

条件渲染组件，与方面无缝协作：

- `Mount` - 根据`Facet<boolean>`有条件地挂载子元素
- `Map` - 从`Facet<Array<T>>`渲染列表
- `With` - 使用方面值渲染（限制重新渲染范围）

## 常见模式

### 基本状态管理

```typescript
const [count, setCount] = useFacetState(0)
const doubledCount = useFacetMap(c => c * 2, [], [count])
```

### 副作用处理

```typescript
useFacetEffect(() => {
  console.log('Count changed')
}, [count])
```

### 条件渲染

```typescript
<Mount when={isVisible}>
  <fast-div>Visible content</fast-div>
</Mount>
```

### 列表渲染

```typescript
<Map items={itemsFacet}>
  {(item) => <fast-div key={item.id}>{item.name}</fast-div>}
</Map>
```

## 特殊值

### `NO_VALUE`

方面在初始化或未赋值时会持有`NO_VALUE`符号。访问方面值时必须显式检查：

```typescript
const [items, setItems] = useFacetState<string[]>([])

setItems((current) => {
  // 必须检查NO_VALUE
  return current !== NO_VALUE ? [...current, newItem] : [newItem]
})
```

## 性能考虑

- 使用`fast-*`组件绑定方面属性以绕过React协调
- 选择合适的相等性检查以避免不必要的派生计算
- 使用`useFacetTransition`标记低优先级更新
- 避免`useFacetUnwrap`除非必要（会触发完整重新渲染）

## 游戏UI开发

Ore UI特别针对游戏UI优化：

- 支持固定帧率预算（如60 fps）
- 最小化DOM操作开销
- 支持通过共享方面与游戏引擎（C++后端）通信

## 相关资源

- [Ore UI官方仓库](https://github.com/Mojang/ore-ui)
- [网站中的Ore UI概念文档](../../docs/general/ore-ui.md)
- 官方文档：[Goals](https://github.com/Mojang/ore-ui/blob/main/docs/docs/goals.md) | [Getting Started](https://github.com/Mojang/ore-ui/blob/main/docs/docs/getting-started.md)
