# 教育文件

<!-- md:flag edu -->

**教育文件（Education File）**是文件名均为{{file|education.json}}的特殊数据驱动文件，根据放置位置和用途，分为**教育元数据文件（Education Metadata File）**和**教育设置文件（Education Settings File）**两种类型。

## 教育元数据文件

教育元数据文件位于世界模板或附加包的根目录，当[清单文件](manifest.md)的`has_education_metadata`字段为`true`时被游戏读取，用于向教育版游戏展示该包的课程信息，包括预计时长、描述、目标、任务和指导等。

/// html | div.treeview
- {{file|wt}} 世界模板
    - {{file|education.json}}
///

### 结构

/// html | div.treeview
- {{json|object|}}：根对象（根对象在引擎内部的键名为`edu_metadata`，该键名仅在报错信息中出现，文件中不需要也不能填写该键名，应直接编写对象内容）。
    - {{json|string|type}}：课程类型，可选`"world"`（世界课程）或`"non_world"`（非世界课程）。
    - {{json|object|content|required=1}}：课程具体内容对象。
        - {{json|int|estimated_time|required=1}}：预计完成该课程所需时间，单位为分钟。
        - {{json|string|description|required=1}}：课程描述文本。
        - {{json|string|goals}}：课程目标文本。
        - {{json|array|tasks}}：课程任务列表，每个元素为一个字符串。
        - {{json|array|instructions}}：课程指导列表，每个元素为一个字符串。
        - {{json|string|link_to_more}}：指向更多相关资源的链接URL。
        - {{json|int|order|required=1}}：该课程在课程序列中的排列序数。
        - {{json|string|role}}：该课程适用的身份，可选`"student_and_teacher"`（学生与教师）或`"teacher"`（仅教师）。
///

## 教育设置文件

教育设置文件位于存档（游戏存档目录）的根目录，用于配置该存档内特定教育版功能的行为，包括代码构建器（Code Builder）的连接地址和显示标题、外部链接、摄像机（Camera）方块的视觉设置以及命令的可见性限制等。

### 结构

/// html | div.treeview
- {{json|object|}}：根对象。
    - {{json|object|codebuilder}}：代码构建器的设置。
        - {{json|string|defaulturi|required=1}}：代码构建器打开时默认加载的URI地址。
        - {{json|string|title|required=1}}：代码构建器界面标题文字。
        - {{json|bool|canResize}}：是否允许用户调整代码构建器窗口的大小，默认为`true`。
        - {{json|bool|disableLegacyTitleBar}}：是否禁用旧版标题栏。
        - {{json|object|capabilities}}：附加功能权限配置。
            - {{json|object|agent}}：代理（Agent）相关权限。
                - {{json|object|permissions}}：权限详情。
                    - {{json|bool|canModifyBlocks}}：是否允许代理修改方块。
    - {{json|object|externalLink}}：外部链接配置。
        - {{json|string|url}}：链接URL。
        - {{json|string|displayName}}：链接在界面中的显示名称。
    - {{json|object|camera}}：摄像机方块设置。
        - {{json|string|filter}}：摄像机拍照的视觉滤镜，目前可选值为`"grayscale"`（灰度）。
        - {{json|string|border}}：摄像机拍照的边框样式，目前可选值为`"borderpath"`。
    - {{json|object|commands}}：命令可见性配置。
        - {{json|array|hiddenFromPlayer}}：从玩家命令起点隐藏的命令名称列表。列表元素为命令名字符串，支持在命令名前加`!`表示排除该命令（取非），`*`代表全部命令。
        - {{json|array|hiddenFromAutomation}}：从自动化命令起点隐藏的命令名称列表，规则同上。
///