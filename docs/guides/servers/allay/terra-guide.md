---
comments: true
---

# Terra世界生成

你是否厌倦了单调的超平坦地形？玩家都转向BDS服务器而不是你的服务器？解决办法来了！

介绍[Terra](https://github.com/PolyhedralDev/Terra)，这是巩固你在MCBE服务器空间中地位的最佳解决方案。

Terra是一个现代的世界生成修改平台，主要面向Minecraft。Terra允许使用高级API进行世界生成的完全定制，与功能强大的配置系统紧密集成。

## 安装Terra

要在Allay中安装Terra，请到[CodeMC](https://ci.codemc.io/job/PolyhedralDev/job/Terra/)的CI网站，你会看到最新的构建。下载名称为`Terra-allay-<版本>-shaded.jar`的工件并将其移到插件文件夹。

## 编辑世界设置

接下来，我们需要指定世界的地形生成器为Terra而不是内置的平坦生成器。例如，如果我们想修改默认世界的生成器，只需打开`worlds/world-settings.yml`并修改以下内容：

```yml linenums="1" hl_lines="1-10 14-20"
built-in-dimensions:
  minecraft:overworld:
    min-height: -64
    max-height: 319
  minecraft:nether:
    min-height: 0
    max-height: 127
  minecraft:the_end:
    min-height: 0
    max-height: 255

worlds:
  world:
    storage-type: LEVELDB
    dimensions:
      minecraft:overworld:
        generator-type: TERRA
        generator-preset: meta-pack=DEFAULT;seed=114514
      minecraft:nether:
        generator-type: TERRA
        generator-preset: meta-pack=DEFAULT;seed=114514
      minecraft:the_end:
        generator-type: TERRA
        generator-preset: meta-pack=DEFAULT;seed=114514
# 默认世界是新加入玩家所在的世界
default-world: world
```

要设置Terra中使用的包，编辑`generator-preset`。`DEFAULT`元包被嵌入在插件中。

要改变内置维度的高度，编辑顶级`built-in-dimensions`部分。

如果你想禁用地狱或末路之地，只需从`dimensions`映射中省略这些维度条目。

你可能需要删除旧的世界文件（如果世界已经生成）。在本例中，你应该删除`worlds/world/db`。

**🎉 就这样！** 重启服务器并享受吧！