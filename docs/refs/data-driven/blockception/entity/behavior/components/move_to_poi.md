# Move To Poi

> 文档版本：1.21.50.25

Allows the mob to move to a POI if able to.

## 架构

```mcschema
move_to_poi:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  string "poi_type" : opt
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
`poi_type`：<samp>string</samp>

- Tells the goal what POI type it should be looking for.


////


///

