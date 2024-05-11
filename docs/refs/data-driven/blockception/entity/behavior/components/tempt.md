# Tempt

> 文档版本：1.21.0.24

Allows an entity to be tempted by a set item.

## 架构

```mcschema
tempt:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "can_get_scared" : opt
  boolean "can_tempt_while_ridden" : opt
  boolean "can_tempt_vertically" : opt
  array "items" : opt
  {
    descriptor "<any array element>"
  }
  number "sound_interval" : opt
  array "sound_interval" : opt
  {
    integer "0..0" : opt
    integer "1..1" : opt
  }
  sound_event "tempt_sound"
  number "within_radius" : opt
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
`can_get_scared`：<samp>boolean</samp>

- If true, the mob can stop being tempted if the player moves too fast while close to this mob.


////


//// define
`can_tempt_while_ridden`：<samp>boolean</samp>

- If true, the mob can be tempted even if it has a passenger (i.e. if being ridden).


////


//// define
`can_tempt_vertically`：<samp>boolean</samp>

- If true, vertical distance to the player will be considered when tempting.


////


//// define
`items`：<samp>array</samp>

- List of items this mob is tempted by.


////

<div class="language-text highlight"><span class="filename"><code>items</code></span><pre id="__code_1"><span></span></pre></div>

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
`sound_interval`：<samp>number</samp>

- Range of random ticks to wait between tempt sounds.


////


//// define
`sound_interval`：<samp>array</samp>

- Range of random ticks to wait between tempt sounds.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>integer</samp>


/////


///// define
`1..1`：<samp>integer</samp>


/////


////



//// define
`tempt_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Sound to play while the mob is being tempted.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`within_radius`：<samp>number</samp>

- Distance in blocks this mob can get tempted by a player holding an item they like.


////


///

