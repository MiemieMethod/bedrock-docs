---
comments: true
---

# 绘图形状

绘图形状是Allay在较新版本中提供的调试与可视化能力。它允许服务端直接让客户端渲染一些简单几何体，非常适合做区域标记、方向指示、调试文本和路径可视化。

## 先知道它的边界

资料明确说明，这项能力是在较新的1.21.90相关文档中引入的。使用前应先确认你的目标Allay版本是否已经包含对应接口。

## 往维度里添加一个形状

绘图形状是按维度管理的。最基础的做法是构造一个形状对象，然后调用`dimension.addPrimitiveShape(...)`。

```java linenums="1"
PrimitiveBox box = new PrimitiveBox(
    new Vector3f(100, 64, 100),
    Color.RED,
    1.0f,
    new Vector3f(2, 2, 2)
);

dimension.addPrimitiveShape(box);
```

一旦把形状添加到维度里，进入该维度的玩家就能看到它；玩家离开维度后，它也会从该玩家视图中自动移除。

## 删除形状

```java linenums="1"
dimension.removePrimitiveShape(box);
dimension.removeAllPrimitiveShapes();
```

如果你把这些形状当作临时调试标记，用完后记得主动清掉。

## Allay资料里列出的形状类型

### 盒体

```java linenums="1"
PrimitiveBox box = new PrimitiveBox(
    new Vector3f(100, 64, 100),
    Color.BLUE,
    1.5f,
    new Vector3f(3, 3, 3)
);
```

### 线段

```java linenums="1"
PrimitiveLine line = new PrimitiveLine(
    new Vector3f(100, 64, 100),
    Color.GREEN,
    new Vector3f(110, 64, 110)
);
```

### 箭头

```java linenums="1"
PrimitiveArrow arrow = new PrimitiveArrow(
    new Vector3f(100, 64, 100),
    Color.YELLOW,
    new Vector3f(110, 64, 110),
    1.0f,
    0.5f,
    4,
    1.0f
);
```

### 圆

```java linenums="1"
PrimitiveCircle circle = new PrimitiveCircle(
    new Vector3f(100, 64, 100),
    Color.MAGENTA,
    2.0f,
    30
);
```

### 球

```java linenums="1"
PrimitiveSphere sphere = new PrimitiveSphere(
    new Vector3f(100, 64, 100),
    Color.CYAN,
    1.0f,
    20
);
```

### 文本

```java linenums="1"
PrimitiveText text = new PrimitiveText(
    new Vector3f(100, 64, 100),
    Color.WHITE,
    "Hello, Primitive!",
    1.0f
);
```

## 也可以单独控制查看者

虽然最常见的用法是把形状挂到维度里，但资料也给出了按查看者控制的接口：

```java linenums="1"
box.addViewer(player);
box.removeViewer(player);
```

这适合做“只有管理员能看到的调试线框”“只给某支队伍显示路线”之类的逻辑。

## 适合拿来做什么

- 标出副本边界、传送门范围或安全区。
- 给开发中的机器、路径寻找或生成器画辅助线。
- 临时把坐标点、方向和文本说明渲染到玩家眼前。

## 使用提醒

- 它更像调试和可视化工具，不是完整的客户端自定义渲染框架。
- 形状留得太多会增加画面噪声，所以调试结束后及时移除。
- 如果你想做真正可交互的界面，而不是世界里的几何提示，请改看[表单开发](form-guide.md)或[容器API](container-guide.md)。
