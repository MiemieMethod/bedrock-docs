# Mingle

> 文档版本：1.21.50.25

Allows an entity to go to the village bell and mingle with other entities.

## 架构

```mcschema
mingle:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "cooldown_time" : opt
  number "duration" : opt
  number "mingle_distance" : opt
  array "mingle_partner_type" : opt
  {
    string "<any array element>" : opt
  }
  string "mingle_partner_type" : opt
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
`cooldown_time`：<samp>number</samp>

- Time in seconds the mob has to wait before using the goal again.


////


//// define
`duration`：<samp>number</samp>

- Amount of time in seconds that the entity will chat with another entity.


////


//// define
`mingle_distance`：<samp>number</samp>

- The distance from its partner that this entity will mingle. If the entity type is not the same as the entity, this value needs to be identical on both entities.


////


//// define
`mingle_partner_type`：<samp>array</samp>

- The entity type that this entity is allowed to mingle with.


////

<div class="language-text highlight"><span class="filename"><code>mingle_partner_type</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>

- The entity type that this entity is allowed to mingle with.


/////


////


//// define
`mingle_partner_type`：<samp>string</samp>

- The entity type that this entity is allowed to mingle with.


////



///

