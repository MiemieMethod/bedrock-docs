# Lay Egg

> 文档版本：1.21.50.25

Allows the mob to lay an egg block on a sand block if the mob is pregnant.

## 架构

```mcschema
lay_egg:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "allow_laying_from_below" : opt
  descriptor "egg_type"
  number "goal_radius" : opt
  sound_event "lay_egg_sound"
  number "lay_seconds" : opt
  trigger "on_lay"
  integer "search_height" : opt
  integer "search_range" : opt
  array "target_blocks" : opt
  {
    descriptor "<any array element>"
  }
  array "target_materials_above_block" : opt
  boolean "use_default_animation" : opt
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
`allow_laying_from_below`：<samp>boolean</samp>

- [EXPERIMENTAL] Allows the mob to lay its eggs from below the target if it can't get there. This is useful if the target block is water with air above, since mobs may not be able to get to the air block above water.


////


//// define
`egg_type`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- [EXPERIMENTAL] Block type for the egg to lay. If this is a turtle egg, the number of eggs in the block is randomly set.


////

```mcschema
identifier:
string

```

//// html | div.result

////



```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
  }
  0 "tags"
  string "item_tag" : opt
}

```

//// html | div.result
///// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


/////


///// define
`item`：<samp>object</samp>

- An object that describes an item.


/////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////



///// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- [UNDOCUMENTED] A Molang expression ran against item or block to match.


/////

```mcschema
0:
string

```

///// html | div.result

/////



///// define
`item_tag`：<samp>string</samp>

- [UNDOCUMENTED] A tag to lookup item or block by.


/////


////


```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
    identifier "item"
    object "item" : opt
    {
    }
    0 "tags"
    string "item_tag" : opt
  }
}

```

//// html | div.result
///// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


/////


///// define
`item`：<samp>object</samp>

- An object that describes an item.


/////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////



////




//// define
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the "wiggle room" to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`lay_egg_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Sound event name for laying egg. Defaulted to lay_egg which is used for Turtles.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`lay_seconds`：<samp>number</samp>

- Duration of the laying egg process in seconds.


////


//// define
`on_lay`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event to run when this mob lays the egg.


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
`search_height`：<samp>integer</samp>

- Height in blocks the mob will look for a target block to move towards.


////


//// define
`search_range`：<samp>integer</samp>

- The distance in blocks it will look for a target block to move towards.


////


//// define
`target_blocks`：<samp>array</samp>

- Blocks that the mob can lay its eggs on top of.


////

<div class="language-text highlight"><span class="filename"><code>target_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>


/////


////


//// define
`target_materials_above_block`：<samp>array</samp>

- Types of materials that can exist above the target block. Valid types are Air, Water, and Lava.


////

<div class="language-text highlight"><span class="filename"><code>target_materials_above_block</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////


//// define
`use_default_animation`：<samp>boolean</samp>

- Specifies if the default lay-egg animation should be played when the egg is placed or not.


////


///

