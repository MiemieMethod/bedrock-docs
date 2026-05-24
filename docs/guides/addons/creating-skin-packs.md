# 制作皮肤包

皮肤包用来分发一组经典皮肤。它不需要行为包或资源包，只需要清单、皮肤清单、语言文件和PNG皮肤图片。

## 文件结构

/// html | div.treeview
- `DemoSkinPack`
    - `manifest.json`
    - `skins.json`
    - `skin_alex.png`
    - `skin_steve.png`
    - `texts`
        - `languages.json`
        - `en_US.lang`
///

皮肤PNG放在皮肤包根目录，文件名要和`skins.json`中的`texture`一致。

## 编写manifest.json

```json title="manifest.json"
{
  "header": {
    "name": "pack.name",
    "version": [1, 0, 0],
    "uuid": "填入第一个UUID"
  },
  "modules": [
    {
      "version": [1, 0, 0],
      "type": "skin_pack",
      "uuid": "填入第二个UUID"
    }
  ],
  "format_version": 1
}
```

皮肤包模块类型是`skin_pack`。官方打包指南中还强调，皮肤包JSON能力目前不能添加自定义模型，只能在`geometry.humanoid.custom`和`geometry.humanoid.customSlim`等内置几何体之间选择。

## 编写skins.json

```json title="skins.json"
{
  "serialize_name": "DemoSkinPack",
  "localization_name": "DemoSkinPack",
  "skins": [
    {
      "localization_name": "AlexDemo",
      "geometry": "geometry.humanoid.customSlim",
      "texture": "skin_alex.png",
      "type": "free"
    },
    {
      "localization_name": "SteveDemo",
      "geometry": "geometry.humanoid.custom",
      "texture": "skin_steve.png",
      "type": "free"
    }
  ]
}
```

`localization_name`会参与语言键拼接。皮肤包名使用`skinpack.<localization_name>`，单个皮肤名使用`skin.<pack_localization_name>.<skin_localization_name>`。

## 添加语言文件

```json title="texts/languages.json"
[
  "en_US"
]
```

```text title="texts/en_US.lang"
skinpack.DemoSkinPack=Demo Skin Pack
skin.DemoSkinPack.AlexDemo=Alex Demo
skin.DemoSkinPack.SteveDemo=Steve Demo
```

## 打包和测试

选中皮肤包根目录中的全部文件，压缩后把扩展名改成`.mcpack`，双击导入。进入更衣室，选择经典皮肤，再查看导入的皮肤包。

如果皮肤无法使用，请检查游戏设置中的“仅允许受信任的皮肤”是否关闭，并确认PNG文件确实在皮肤包根目录。