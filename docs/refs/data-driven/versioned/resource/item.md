# 物品客户端定义

> 文档版本：1.21.60.21



## 结构

/// tab | 1.10.0
//// html | div.treeview
- {{json|object||required=1}}：根对象。
    - {{json|array|format_version|required=1}}：
        - {{json|int|}}：
    - {{json|string|format_version|required=1}}：
    - {{json|object|minecraft:item|required=1}}：
        - {{json|object|description|required=1}}：
            - {{json|string|identifier}}：
            - {{json|string|category}}：
        - {{json|object|components|required=1}}：
            - {{json|string|minecraft:hover_text_color}}：
            - {{json|string|minecraft:icon}}：<!-- md:flag china -->
            - {{json|string|minecraft:icon_atlas}}：
            - {{json|string|minecraft:icon_variant}}：<!-- md:flag china -->
            - {{json|object|minecraft:use_animation}}：
                - {{json|string|value}}：
            - {{json|object|netease:frame_animation}}：<!-- md:flag china -->
                - {{json|int|frame_count}}：<!-- md:flag china -->
                - {{json|string|texture_name}}：<!-- md:flag china -->
                - {{json|boolean|animate_in_toolbar}}：<!-- md:flag china -->
            - {{json|object|netease:frame_anim_in_scene}}：<!-- md:flag china -->
                - {{json|int|ticks_per_frame}}：<!-- md:flag china -->
                - {{json|string|texture_path}}：<!-- md:flag china -->
            - {{json|object|netease:render_offsets}}：<!-- md:flag china -->
                - {{json|array|controller_position_adjust}}：<!-- md:flag china -->
                    - {{json|float|}}：<!-- md:flag china -->
                - {{json|array|controller_rotation_adjust}}：<!-- md:flag china -->
                    - {{json|float|}}：<!-- md:flag china -->
                - {{json|float|controller_scale}}：<!-- md:flag china -->

////

///

/// tab | 1.16.100
//// info | 未实现
当前对象未在此版本中实现，无法正常解析。
////

///

/// tab | 1.16.200
//// html | div.treeview
- {{json|object||required=1}}：根对象。
    - {{json|array|format_version|required=1}}：
        - {{json|int|}}：
    - {{json|string|format_version|required=1}}：
    - {{json|object|minecraft:item|required=1}}：
        - {{json|object|description|required=1}}：
            - {{json|string|identifier}}：
            - {{json|string|category}}：
        - {{json|object|components|required=1}}：
            - {{json|string|minecraft:hover_text_color}}：
            - {{json|string|minecraft:icon}}：<!-- md:flag china -->
            - {{json|string|minecraft:icon_atlas}}：
            - {{json|string|minecraft:icon_variant}}：<!-- md:flag china -->
            - {{json|object|minecraft:use_animation}}：
                - {{json|string|value}}：
            - {{json|object|netease:frame_animation}}：<!-- md:flag china -->
                - {{json|int|frame_count}}：<!-- md:flag china -->
                - {{json|string|texture_name}}：<!-- md:flag china -->
                - {{json|boolean|animate_in_toolbar}}：<!-- md:flag china -->
            - {{json|object|netease:frame_anim_in_scene}}：<!-- md:flag china -->
                - {{json|int|ticks_per_frame}}：<!-- md:flag china -->
                - {{json|string|texture_path}}：<!-- md:flag china -->
            - {{json|object|netease:render_offsets}}：<!-- md:flag china -->
                - {{json|array|controller_position_adjust}}：<!-- md:flag china -->
                    - {{json|float|}}：<!-- md:flag china -->
                - {{json|array|controller_rotation_adjust}}：<!-- md:flag china -->
                    - {{json|float|}}：<!-- md:flag china -->
                - {{json|float|controller_scale}}：<!-- md:flag china -->

////

///

/// tab | 1.17.0
//// info | 未实现
当前对象未在此版本中实现，无法正常解析。
////

///

