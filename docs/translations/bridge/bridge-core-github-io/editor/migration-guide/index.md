# bridge. v2迁移

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/editor-docs/migration-guide/](https://bridge-core.github.io/editor-docs/migration-guide/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/editor-docs/migration-guide/index.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/editor-docs/migration-guide/index.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@8bc861be15d2d236241d17841b38a97869768f1c -->
- 该页面的作者有：
    - <!-- md:samp @joelant05 -->
///

## bridge. v1项目与bridge. v2项目有何不同？

bridge. v1将其项目存储在`com.mojang`目录内的`development_behavior_packs`和`development_resource_packs`文件夹中。然而，bridge. v2采用不同的方法，将你的项目以更易于管理的格式存储在系统的其他位置，例如`Documents`文件夹，并且你可以选择将`com.mojang`文件夹链接到bridge. v2。

链接后，bridge. v2的编译器将在适当的`development_behavior_packs`、`development_resource_packs`、`minecraftWorlds`和`development_skin_packs`文件夹中写入其`dev`模式的输出。这意味着你的项目源文件将始终位于`com.mojang`目录之外，这具有多种好处，例如在卸载Minecraft时不会丢失所有项目，以及更容易进行git集成。

这也意味着你**不应**在`com.mojang`文件夹中编辑你的包，因为这些包将被bridge.的编译器输出覆盖。

## 一旦我迁移了项目，将会发生什么？

迁移过程绝不会删除你的原始项目。在迁移过程中，你的项目将被转移，并且自定义命令、自定义组件和自定义实体语法将继续按预期工作。你的BP中的`bridge`文件夹将被移除，bridge.会从中提取所需的数据并从已转移的项目副本中删除它，因为这些数据将不再需要。

## 转移项目

1. 要开始将你的项目转移到bridge. v2，启动bridge. v1并确保你使用的版本为`v1.8.0`或更高版本。你可以在右下角查看。如果你不是这个版本，请通过应用底部的更新提示更新bridge.。

2. 启动bridge. v1后，点击应用底部的更新到bridge. v2的通知。![更新到v2提示](./migration-guide-1.png)

3. 这会显示一个窗口，告诉你bridge. v2已可用，你可以现在更新。要继续，点击**`继续`**。

4. 然后会出现迁移窗口。首先，你需要选择一个目录来存储你的bridge. v2项目。要选择此目录，点击**`选择文件夹`**选项并选择一个目录。**确保不选择你的`com.mojang`文件夹。**

5. 选择文件夹后，向下滚动并从列表中选择你要转移的项目，你也可以点击**`全选`**按钮选择所有要转移的项目。选择项目后，点击**`确认`**按钮。

6. 当加载窗口关闭后，你将看到一些关于下一步要做什么的信息。要继续到bridge. v2，点击**`前往！`**。你也可以点击**`查看项目`**来打开转移后的项目目录。

## 使用已转移项目设置bridge. v2

当你打开bridge. v2时，设置过程的第一步将要求你选择一个项目文件夹来存储你的项目。如果你已经使用bridge. v1迁移了你的项目，你需要选择上面**第4步**中选择的同一目录。