# Go And Give Items To Owner

> 文档版本：1.21.0.24

[EXPERIMENTAL BEHAVIOR] The entity will attempt to toss the items from its inventory to its owner.

## 架构

```mcschema
go_and_give_items_to_owner:
{
  priority "priority"
  trigger "on_item_throw"
  number "reach_mob_distance" : opt
  number "run_speed" : opt
  number "throw_force" : opt
  sound_event "throw_sound"
  number "vertical_throw_mul" : opt
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
`on_item_throw`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event(s) to run when this mob throws items.


////

```mcschema
trigger:
string

```

//// html | div.result

////


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


/////


///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions for this trigger to execute.


/////


///// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


/////

```mcschema
subject:
string

```

///// html | div.result

/////



////


```mcschema
trigger:
array
{
  object "<any array element>" : opt
  {
    string "event" : opt
    filters "filters"
    subject "target"
  }
}

```

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////




//// define
`reach_mob_distance`：<samp>number</samp>

- Sets the desired distance to be reached before giving items to owner.


////


//// define
`run_speed`：<samp>number</samp>

- Sets the entity's speed when running toward the owner.


////


//// define
`throw_force`：<samp>number</samp>

- Sets the throw force.


////


//// define
`throw_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Sound to play when this mob throws an item.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`vertical_throw_mul`：<samp>number</samp>

- Sets the vertical throw multiplier that is applied on top of the throw force in the vertical direction.


////


///

