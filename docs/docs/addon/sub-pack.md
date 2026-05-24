# 子包

**子包（Sub-Pack）**是Minecraft基岩版附加包中用于提供不同资源变体选项的机制。子包允许一个附加包根据用户的选择或设备能力提供多套不同的资源，用户可以在应用附加包时选择所需的变体。

## 概述

子包的典型应用场景包括：

- 为不同性能等级的设备提供不同分辨率的纹理（如低清、高清、超高清）。
- 提供不同风格的资源变体供用户选择。
- 为不同的游戏内容配置提供选项。

子包在清单文件中声明，对应的资源文件放置在附加包的`subpacks/`目录下。

## 定义方式

子包在清单文件（{{file|manifest.json}}）的`subpacks`字段中定义。每个子包包含以下字段：

```json title="子包定义示例"
{
  "subpacks": [
    {
      "folder_name": "low",
      "name": "低分辨率",
      "memory_tier": 0
    },
    {
      "folder_name": "medium",
      "name": "中分辨率",
      "memory_tier": 1
    },
    {
      "folder_name": "high",
      "name": "高分辨率",
      "memory_tier": 2
    }
  ]
}
```

/// define
`folder_name`

- 子包的文件夹名称，对应`subpacks/`目录下的子目录名。

`name`

- 子包的显示名称，显示在选择界面上。

`memory_tier`

- 内存等级，用于按设备内存自动选择合适的子包。等级数值越高，表示资源越精细，对设备性能要求越高。

///

## 文件结构

子包的资源文件放置在`subpacks/<folder_name>/`目录中。该目录的内部结构与附加包根目录的结构一致。当某个子包被选择时，其目录中的文件会覆盖附加包根目录中的同路径文件。

/// html | div.treeview
- {{file|附加包根目录}}
    - {{file|manifest.json}}
    - {{file|textures}}
        - {{file|blocks}}
            - {{file|stone.png}}
    - {{file|subpacks}}
        - {{file|low}}
            - {{file|textures}}
                - {{file|blocks}}
                    - {{file|stone.png}}
        - {{file|high}}
            - {{file|textures}}
                - {{file|blocks}}
                    - {{file|stone.png}}
///

在上述结构中，若选择`high`子包，则`subpacks/high/textures/blocks/stone.png`会覆盖根目录的`textures/blocks/stone.png`。

## 用户选择

用户在世界设置或全局资源包设置中应用附加包时，如果该附加包定义了子包，界面上会显示一个滑块或选项，允许用户在各个子包之间选择。默认选择由`memory_tier`和设备的可用内存自动决定，但用户可以手动覆盖。

/// warning | 单子包情形
当附加包仅定义了一个子包时，选择界面依然会显示两个选项：一个子包选项和一个"无子包"选项。但选择"无子包"选项**不会**使附加包切换回其根目录中的资源，其效果与实际行为存在歧义，开发时应对此保持警惕。
///