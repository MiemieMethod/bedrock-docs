# Teleport

> 文档版本：1.21.0.24

Defines an entity's teleporting behavior.

## 架构

```mcschema
teleport:
{
  number "dark_teleport_chance" : opt
  number "light_teleport_chance" : opt
  number "max_random_teleport_time" : opt
  number "min_random_teleport_time" : opt
  array "random_teleport_cube" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
  boolean "random_teleports" : opt
  number "target_distance" : opt
  number "target_teleport_chance" : opt
}

```

/// html | div.result
//// define
`dark_teleport_chance`：<samp>number</samp>

- Modifies the chance that the entity will teleport if the entity is in darkness.


////


//// define
`light_teleport_chance`：<samp>number</samp>

- Modifies the chance that the entity will teleport if the entity is in daylight.


////


//// define
`max_random_teleport_time`：<samp>number</samp>

- Maximum amount of time in seconds between random teleports.


////


//// define
`min_random_teleport_time`：<samp>number</samp>

- Minimum amount of time in seconds between random teleports.


////


//// define
`random_teleport_cube`：<samp>array</samp>

- Entity will teleport to a random position within the area defined by this cube.


////

<div class="language-text highlight"><span class="filename"><code>random_teleport_cube</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


///// define
`2..2`：<samp>number</samp>


/////


////


//// define
`random_teleports`：<samp>boolean</samp>

- If true, the entity will teleport randomly.


////


//// define
`target_distance`：<samp>number</samp>

- Maximum distance the entity will teleport when chasing a target.


////


//// define
`target_teleport_chance`：<samp>number</samp>

- The chance that the entity will teleport between 0.0 and 1.0. 1.0 means 100%


////


///

