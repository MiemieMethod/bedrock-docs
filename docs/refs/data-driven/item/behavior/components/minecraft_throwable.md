# minecraft:throwable

> 文档版本：1.21.0.24

Throwable items can be thrown by the player, such as a snowball.

## 架构

```mcschema
minecraft:throwable:
{
  number "default_offset_scale" : opt
  boolean "do_swing_animation" : opt
  number "inside_block_offset_scale" : opt
  number "launch_power_scale" : opt
  number "max_draw_duration" : opt
  number "max_launch_power" : opt
  number "min_draw_duration" : opt
  boolean "scale_power_by_draw_duration" : opt
}

```

/// html | div.result
//// define
`default_offset_scale`：<samp>number</samp>

- The scale at which the throw position is adjusted by the aim direction.


////


//// define
`do_swing_animation`：<samp>boolean</samp>

- Determines whether the item should use the swing animation when thrown. Default is set to false.


////


//// define
`inside_block_offset_scale`：<samp>number</samp>

- The scale at which the throw position is adjusted by the aim direction if the default throw position is inside a solid block.


////


//// define
`launch_power_scale`：<samp>number</samp>

- The scale at which the power of the throw increases. Default is set to 1.0.


////


//// define
`max_draw_duration`：<samp>number</samp>

- The maximum duration to draw a throwable item. Default is set to 0.0.


////


//// define
`max_launch_power`：<samp>number</samp>

- The maximum power to launch the throwable item. Default is set to 1.0.


////


//// define
`min_draw_duration`：<samp>number</samp>

- The minimum duration to draw a throwable item. Default is set to 0.0.


////


//// define
`scale_power_by_draw_duration`：<samp>boolean</samp>

- Whether or not the power of the throw increases with duration charged. Default is set to false.


////


///

