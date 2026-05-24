# 使用子包

子包让一个资源包提供多套资源变体，玩家可以在包设置中选择。例如，你可以提供低清纹理、标准纹理和高清纹理，而不必发布三个独立资源包。

## 创建子包目录

在资源包根目录创建`subpacks`文件夹，再为每个子包创建一个子文件夹：

/// html | div.treeview
- `demo_RP`
    - `manifest.json`
    - `textures`
        - `blocks`
            - `lamp.png`
    - `subpacks`
        - `low`
            - `textures`
                - `blocks`
                    - `lamp.png`
        - `high`
            - `textures`
                - `blocks`
                    - `lamp.png`
///

子包中的文件会覆盖主资源包中的同路径文件。因此，主资源包里应当保留一个默认版本，子包只放需要变化的文件。

## 修改manifest.json

在资源包`manifest.json`中加入`subpacks`数组：

```json hl_lines="17-30" title="demo_RP/manifest.json"
{
  "format_version": 2,
  "header": {
    "name": "Demo Resource Pack",
    "description": "A pack with selectable subpacks.",
    "uuid": "填入资源包UUID",
    "version": [1, 0, 0],
    "min_engine_version": [1, 20, 30]
  },
  "modules": [
    {
      "type": "resources",
      "uuid": "填入模块UUID",
      "version": [1, 0, 0]
    }
  ],
  "subpacks": [
    {
      "folder_name": "low",
      "name": "低清资源",
      "memory_tier": 6
    },
    {
      "folder_name": "high",
      "name": "高清资源",
      "memory_tier": 32
    }
  ]
}
```

稳定清单中使用`memory_tier`表示最低内存层级，每一级大约对应250MB内存。官方资料还记录了`memory_performance_tier`，取值为1到5，但该字段与清单版本3相关；如果目标版本要求使用它，请按对应版本的清单参考同步调整`format_version`和版本字段写法。

## 测试子包

1. 激活资源包。
2. 在已激活资源包列表中打开包设置。
3. 切换子包选项。
4. 退出世界并重新进入，观察资源是否变化。

子包特别适合资源包，不适合用来隐藏复杂逻辑差异。逻辑差异如果放在行为包中，通常应该拆成不同包或用数据驱动条件、函数、脚本等方式处理。