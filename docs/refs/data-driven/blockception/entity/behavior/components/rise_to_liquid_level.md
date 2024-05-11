# Rise To Liquid Level

> 文档版本：1.21.0.24

Allows the mob to stay at a certain level when in liquid.

## 架构

```mcschema
rise_to_liquid_level:
{
  priority "priority"
  number "liquid_y_offset" : opt
  number "rise_delta" : opt
  number "sink_delta" : opt
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
`liquid_y_offset`：<samp>number</samp>

- Vertical offset from the liquid.


////


//// define
`rise_delta`：<samp>number</samp>

- Displacement for how much the entity will move up in the vertical axis.


////


//// define
`sink_delta`：<samp>number</samp>

- Displacement for how much the entity will move down in the vertical axis.


////


///

