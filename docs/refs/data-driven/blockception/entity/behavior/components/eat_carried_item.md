# Eat Carried Item

> 文档版本：1.21.50.25

If the mob is carrying a food item, the mob will eat it and the effects will be applied to the mob.

## 架构

```mcschema
eat_carried_item:
{
  priority "priority"
  number "delay_before_eating" : opt
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
`delay_before_eating`：<samp>number</samp>

- Time in seconds the mob should wait before eating the item.


////


///

