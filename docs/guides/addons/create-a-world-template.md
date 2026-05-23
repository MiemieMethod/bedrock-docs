# 创建世界模板

世界模板适合发布“从同一个世界开局”的内容。玩家导入`.mctemplate`后，不会直接得到一个可玩的世界，而是在创建世界界面的“已导入模板”中选择它，再生成一份新的世界副本。

## 从导出世界开始

最稳妥的做法是先在游戏中创建并配置好一个普通世界：启用需要的资源包和行为包，设置游戏规则，放好出生点建筑，然后在世界设置中导出为`.mcworld`。`.mcworld`本质上是一个改了扩展名的压缩包，你可以把它改名为`.zip`并解压查看。

典型世界目录如下：

/// html | div.treeview
- `db`
- `level.dat`
- `level.dat_old`
- `levelname.txt`
- `world_icon.jpeg`
///

如果世界启用了附加包，导出包里还会包含`behavior_packs`、`resource_packs`以及用于记录启用包的世界资源文件。

## 添加模板清单

在解压后的世界根目录添加`manifest.json`：

```json title="manifest.json"
{
  "header": {
    "name": "pack.name",
    "description": "pack.description",
    "version": [1, 0, 0],
    "lock_template_options": true,
    "base_game_version": [1, 21, 80],
    "uuid": "填入第一个UUID"
  },
  "modules": [
    {
      "version": [1, 0, 0],
      "type": "world_template",
      "uuid": "填入第二个UUID"
    }
  ],
  "format_version": 2
}
```

再添加本地化文件：

/// html | div.treeview
- `texts`
    - `languages.json`
    - `en_US.lang`
///

```json title="texts/languages.json"
[
  "en_US"
]
```

```text title="texts/en_US.lang"
pack.name=Demo Template
pack.description=A reusable demo world.
```

`lock_template_options`用于锁定模板创建世界时的选项。`base_game_version`应填写这个世界模板创建和测试时使用的游戏版本。它只用于世界模板，用来决定世界按哪个原版基版本解释；不要把它填成高于目标玩家客户端的未来版本。如果不提供`texts`目录，模板在界面中可能直接显示`pack.name`。

## 重新打包

进入世界根目录，选中里面的所有文件和文件夹进行压缩，然后把压缩包扩展名改为`.mctemplate`。

/// danger | 不要压缩外层文件夹
压缩包打开后，根目录应当直接看到`manifest.json`、`level.dat`和`db`。如果打开后先看到一个同名文件夹，Minecraft通常无法按世界模板导入。
///

## 导入与排错

双击`.mctemplate`导入。导入完成后进入“创建新世界”，在已导入模板中找到它。如果导入失败，优先检查：

- 是否已经导入过相同UUID的模板。
- 压缩包根目录是否正确。
- `manifest.json`是否为世界模板模块类型。
- `header.lock_template_options`是否已经设置为`true`。
- `header.base_game_version`是否存在，并且不高于你用于测试的游戏版本。
- `texts/en_US.lang`是否包含`pack.name`和`pack.description`。
- `world_icon.jpeg`是否仍在根目录；官方资料建议世界图标使用800×450像素JPEG。
