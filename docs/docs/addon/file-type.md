# 文件类型

**文件类型（File Type）**是Minecraft基岩版用于打包和分发各类内容的一组专有文件格式扩展名。所有基岩版专有文件本质上均为ZIP压缩包，通过重命名使用以`mc`为前缀的专有扩展名来标识其内容类别。

## 概述

基岩版文件类型按所含内容的性质可划分为三类：

- **世界文件**：包含单个世界或编辑器项目的存档数据及相关资源。
- **资源文件**：包含单个行为包、资源包、皮肤包或世界模板等独立内容实例。
- **复合文件**：可同时包含最多一个世界文件及任意数量的资源文件。

无论是哪种类型，均可通过操作系统常规的文件打开方式触发游戏导入流程。资源文件被导入后，游戏会将其内容解压并写入对应的目录结构中。若游戏尚未运行，多数文件类型会以普通模式启动游戏；`mcproject`和`mceditoraddon`则会直接进入编辑器模式。

## 世界文件

世界文件包含普通世界或编辑器项目的存档数据及所关联的资源。无论何种模式，所有世界文件导入后均存放在`com.mojang/minecraftWorlds`目录中。

若导入的世界文件与已有存档完全一致，会生成同名的重复存档。复合文件中若嵌套了多个世界文件，游戏仅会导入其中一个。

### mcworld

{{file|example.mcworld|mcworld}}代表单个普通游戏世界的压缩存档包。

创建`.mcworld`文件的方式包括：

- 将世界目录的**全部内容**打包为ZIP文件后，将扩展名改为`.mcworld`；
- 在游戏设置界面点击"导出世界"；
- 在编辑器模式中选择"文件 → 导出为 → 可游玩世界"，或执行`/project export world`命令；导出结果将保存至`com.mojang/projectbackups`目录。

在编辑器模式下导入`.mcworld`文件时，该世界会作为项目导入，导入后的世界无法在编辑器模式之外直接游玩，需要重新导出为可游玩世界才能正常访问。

### mcproject

{{file|example.mcproject|mcproject}}代表单个编辑器项目的压缩存档包。

创建`.mcproject`文件的方式包括：

- 将项目目录的**全部内容**打包为ZIP文件后，将扩展名改为`.mcproject`；
- 在编辑器模式中执行`/project export project`命令；导出结果将保存至`com.mojang/projectbackups`目录。

若游戏尚未运行，打开`.mcproject`文件会直接进入编辑器模式。若游戏已在运行但并非处于编辑器模式，则导入会失败。

## 资源文件

资源文件代表各类非世界内容的独立实例，涵盖行为包、资源包、皮肤包和世界模板。

所有资源文件均包含用于描述其内容的[清单文件](manifest.md)。若导入的资源文件的UUID和版本号与同类型的已有资源完全相同，则导入会失败。需要注意，行为包和资源包共享同一UUID命名空间，即同一UUID不能同时存在于两种包中。内置于世界、项目或世界模板中的行为包和资源包不受此重复校验限制。

尽管`.mcpack`和`.mctemplate`在技术层面功能相同，惯例上建议区分使用：

- 使用`.mcpack`发布行为包、资源包和皮肤包；
- 使用`.mctemplate`发布世界模板。

### mcpack

{{file|example.mcpack|mcpack}}代表单个行为包、资源包、皮肤包或世界模板的压缩包，建议仅将`.mctemplate`用于世界模板。

手动创建`.mcpack`的方式：将行为包、资源包或皮肤包目录的全部内容打包为ZIP文件后，将扩展名改为`.mcpack`。全局安装的行为包与资源包不会与世界或项目中内置的同名资源产生冲突。

/// define
**行为包**

- 用于修改或扩展游戏逻辑，安装至`com.mojang/behavior_packs`目录。开发中的行为包应放置于`com.mojang/development_behavior_packs`目录。

**资源包**

- 用于修改客户端音效、视觉效果等，安装至`com.mojang/resource_packs`目录。开发中的资源包应放置于`com.mojang/development_resource_packs`目录。

**皮肤包**

- 仅限客户端的自定义皮肤资源，安装至`com.mojang/skin_packs`目录。

///

### mctemplate

{{file|example.mctemplate|mctemplate}}代表单个世界模板的压缩包，安装至`com.mojang/world_templates`目录。

创建`.mctemplate`文件的方式包括：

- 将世界目录的全部内容打包为ZIP文件，加入世界模板清单文件后，将扩展名改为`.mctemplate`；
- 在编辑器模式中选择"导出模板"，或执行`/project export template`命令；导出结果将保存至`com.mojang/projectbackups`目录。

## 复合文件

复合文件用于在单次导入操作中同时导入最多一个世界文件及任意数量的资源文件。复合文件的顶层目录中可以直接放置已打包的`.mcworld`、`.mcproject`、`.mcpack`、`.mctemplate`等文件，也可以直接放置行为包、资源包、皮肤包或世界模板的原始目录结构（但不能将其放入子目录中）。

复合文件内的内容按常规方式处理。例如，在编辑器模式下导入包含`.mcworld`的`.mcaddon`时，世界文件会作为项目导入。

复合文件可以包含任意数量或层级的其他复合文件，但嵌套复合文件不能突破单世界导入的限制。复合文件只能通过手动打包现有文件或目录的方式创建。

### mcaddon

{{file|example.mcaddon|mcaddon}}是通用的复合内容存档，可用于一次性分发整套附加包（行为包与资源包的组合）。在编辑器模式下导入`.mcaddon`时，其中包含的世界文件会作为项目导入，其余资源类型则按常规方式导入。

### mceditoraddon

{{file|example.mceditoraddon|mceditoraddon}}是专用于编辑器模式的复合内容存档。若游戏尚未运行，打开`.mceditoraddon`文件会直接进入编辑器模式；若游戏已在运行但并非处于编辑器模式，则导入会失败。

## 相关页面

- [附加包](addon.md)
- [清单文件](manifest.md)
- [行为包](behavior-pack.md)
- [资源包](resource-pack.md)
- [世界模板](world-template.md)
- [皮肤包](skin-pack.md)