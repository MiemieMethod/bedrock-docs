# `StructureManager`

> 文档版本：1.21.0.20

`StructureManager`类。

## 属性

## 方法

/// define
createEmpty

- ```js
createEmpty(identifier: string, size: Vector3, saveMode: StructureSaveMode): Structure
```



///


/// define
createFromWorld

- ```js
createFromWorld(identifier: string, dimension: Dimension, blockVolume: BlockVolume, options?: StructureCreateOptions): Structure
```



///


/// define
delete

- ```js
delete(structure: string | Structure): boolean
```



///


/// define
get

- ```js
get(identifier: string): Structure | undefined
```



///


/// define
getIds

- ```js
getIds(): string[]
```



///


/// define
place

- ```js
place(structure: string | Structure, dimension: Dimension, location: Vector3, options?: StructurePlaceOptions): void
```



///

