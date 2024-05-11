# Avoid Block

> 文档版本：1.21.0.24

Allows this entity to avoid certain blocks.

## 架构

```mcschema
avoid_block:
{
  priority "priority"
  integer "tick_interval" : opt
  integer "search_range" : opt
  integer "search_height" : opt
  number "sprint_speed_modifier" : opt
  string "target_selection_method" : opt
  array "target_blocks" : opt
  {
    descriptor "<any array element>"
  }
  sound_event "avoid_block_sound"
  number "walk_speed_modifier" : opt
  array "on_escape" : opt
  {
    event "<any array element>"
  }
  array "sound_interval" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "sound_interval" : opt
  object "sound_interval" : opt
  {
    number "range_min" : opt
    number "range_max" : opt
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
`tick_interval`：<samp>integer</samp>

- Should start tick interval.


////


//// define
`search_range`：<samp>integer</samp>

- Maximum distance to look for a block in xz.


////


//// define
`search_height`：<samp>integer</samp>

- Maximum distance to look for a block in y.


////


//// define
`sprint_speed_modifier`：<samp>number</samp>

- Modifier for sprint speed. 1.0 means keep the regular speed, while higher numbers make the sprint speed faster.


////


//// define
`target_selection_method`：<samp>string</samp>

- Block search method.


////


//// define
`target_blocks`：<samp>array</samp>

- List of block types this mob avoids.


////

<div class="language-text highlight"><span class="filename"><code>target_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



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

///// html | div.result
////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


//////


////// define
`item`：<samp>object</samp>

- An object that describes an item.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////



////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- [UNDOCUMENTED] A Molang expression ran against item or block to match.


//////

```mcschema
0:
string

```

////// html | div.result

//////



////// define
`item_tag`：<samp>string</samp>

- [UNDOCUMENTED] A tag to lookup item or block by.


//////


/////


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

///// html | div.result
////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


//////


////// define
`item`：<samp>object</samp>

- An object that describes an item.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////



/////




////


//// define
`avoid_block_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to play when the mob is avoiding a block.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`walk_speed_modifier`：<samp>number</samp>

- Modifier for walking speed. 1.0 means keep the regular speed, while higher numbers make the walking speed faster.


////


//// define
`on_escape`：<samp>array</samp>

- Escape trigger.


////

<div class="language-text highlight"><span class="filename"><code>on_escape</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}


/////

```mcschema
event:
string

```

///// html | div.result

/////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

///// html | div.result
////// define
`event`：<samp>string</samp>

- The event to fire.


//////


////// define
`target`：<samp>string</samp>

- The target of the event.


//////


/////




////


//// define
`sound_interval`：<samp>array</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`sound_interval`：<samp>number</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////


//// define
`sound_interval`：<samp>object</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`range_min`：<samp>number</samp>


/////


///// define
`range_max`：<samp>number</samp>


/////


////



///

