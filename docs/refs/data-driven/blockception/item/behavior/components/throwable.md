# Throwable

> 文档版本：1.21.0.24

Throwable item component. Throwable items, such as a snowball.

## 架构

```mcschema
minecraft::
{
  boolean "do_swing_animation" : opt
  number "launch_power_scale" : opt
  number "max_draw_duration" : opt
  number "min_draw_duration" : opt
  number "max_launch_power" : opt
  boolean "scale_power_by_draw_duration" : opt
}

```

/// html | div.result
//// define
`do_swing_animation`：<samp>boolean</samp>

- Whether the item should use the swing animation when thrown. Default is set to false.


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
`min_draw_duration`：<samp>number</samp>

- The minimum duration to draw a throwable item. Default is set to 0.0.


////


//// define
`max_launch_power`：<samp>number</samp>

- The maximum power to launch the throwable item. Default is set to 1.0.


////


//// define
`scale_power_by_draw_duration`：<samp>boolean</samp>

- Whether or not the power of the throw increases with duration charged. Default is set to false.


////


///

