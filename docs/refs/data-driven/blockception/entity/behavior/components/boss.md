# Boss

> 文档版本：1.21.0.24

The current state of the boss for updating the boss HUD.

## 架构

```mcschema
boss:
{
  integer "hud_range" : opt
  string "name" : opt
  boolean "should_darken_sky" : opt
}

```

/// html | div.result
//// define
`hud_range`：<samp>integer</samp>

- The Maximum distance from the boss at which the boss's health bar is present on the players screen.


////


//// define
`name`：<samp>string</samp>

- The name that will be displayed above the boss's health bar.


////


//// define
`should_darken_sky`：<samp>boolean</samp>

- Whether the sky should darken in the presence of the boss.


////


///

