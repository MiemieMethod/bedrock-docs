# `CompoundBlockVolume`

> 文档版本：1.21.0.20

`CompoundBlockVolume`类。

## 属性

/// define
capacity

- ```js
read-only capacity: uint64
```



///


/// define
volumeCount

- ```js
read-only volumeCount: uint64
```



///


## 方法

/// define
clear

- ```js
clear(): void
```



///


/// define
constructor

- ```js
new constructor(origin?: Vector3): CompoundBlockVolume
```



///


/// define
getBlockLocationIterator

- ```js
getBlockLocationIterator(): BlockLocationIterator
```



///


/// define
getBoundingBox

- ```js
getBoundingBox(): BoundingBox
```



///


/// define
getMax

- ```js
getMax(): Vector3
```



///


/// define
getMin

- ```js
getMin(): Vector3
```



///


/// define
getOrigin

- ```js
getOrigin(): Vector3
```



///


/// define
isEmpty

- ```js
isEmpty(): boolean
```



///


/// define
isInside

- ```js
isInside(worldLocation: Vector3): boolean
```



///


/// define
peekLastVolume

- ```js
peekLastVolume(forceRelativity?: CompoundBlockVolumePositionRelativity): CompoundBlockVolumeItem | undefined
```



///


/// define
popVolume

- ```js
popVolume(): boolean
```



///


/// define
pushVolume

- ```js
pushVolume(item: CompoundBlockVolumeItem): void
```



///


/// define
replaceOrAddLastVolume

- ```js
replaceOrAddLastVolume(item: CompoundBlockVolumeItem): boolean
```



///


/// define
setOrigin

- ```js
setOrigin(position: Vector3, preserveExistingVolumes?: boolean): void
```



///


/// define
translateOrigin

- ```js
translateOrigin(delta: Vector3, preserveExistingVolumes?: boolean): void
```



///

