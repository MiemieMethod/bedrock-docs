# Move Towards Restriction

> 文档版本：1.21.0.24

Allows Guardians, Iron Golems and Villagers to move within their pre-defined area that the mob should be restricted to. Other mobs don't have a restriction defined.

## 架构

```mcschema
move_towards_restriction:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  array "control_flags" : opt
  {
    string "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`priority`：<samp>priority</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.priority.json}


////

```mcschema
priority:
integer

```

//// html | div.result

////



//// define
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

////



//// define
`control_flags`：<samp>array</samp>

- UNDOCUMENTED: control flags.


////

<div class="language-text highlight"><span class="filename"><code>control_flags</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED: control flags.


/////


////


///

