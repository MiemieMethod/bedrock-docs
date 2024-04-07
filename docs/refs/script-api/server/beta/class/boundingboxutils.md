# `BoundingBoxUtils`

> 文档版本：1.21.0.20

`BoundingBoxUtils`类。

## 属性

## 方法

/// define
createValid

- ```js
static createValid(min: Vector3, max: Vector3): BoundingBox
```



///


/// define
dilate

- ```js
static dilate(box: BoundingBox, size: Vector3): BoundingBox
```



///


/// define
equals

- ```js
static equals(box: BoundingBox, other: BoundingBox): boolean
```



///


/// define
expand

- ```js
static expand(box: BoundingBox, other: BoundingBox): BoundingBox
```



///


/// define
getCenter

- ```js
static getCenter(box: BoundingBox): Vector3
```



///


/// define
getIntersection

- ```js
static getIntersection(box: BoundingBox, other: BoundingBox): BoundingBox | undefined
```



///


/// define
getSpan

- ```js
static getSpan(box: BoundingBox): Vector3
```



///


/// define
intersects

- ```js
static intersects(box: BoundingBox, other: BoundingBox): boolean
```



///


/// define
isInside

- ```js
static isInside(box: BoundingBox, pos: Vector3): boolean
```



///


/// define
isValid

- ```js
static isValid(box: BoundingBox): boolean
```



///


/// define
translate

- ```js
static translate(box: BoundingBox, delta: Vector3): BoundingBox
```



///

