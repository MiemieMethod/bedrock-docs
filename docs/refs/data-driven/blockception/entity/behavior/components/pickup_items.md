# Pickup Items

> 文档版本：1.21.50.25

Allows the mob to pick up items on the ground.

## 架构

```mcschema
pickup_items:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "can_pickup_any_item" : opt
  boolean "can_pickup_to_hand_or_equipment" : opt
  number "cooldown_after_being_attacked" : opt
  array "excluded_items" : opt
  {
    descriptor "<any array element>"
  }
  number "goal_radius" : opt
  number "max_dist" : opt
  number "search_height" : opt
  boolean "pickup_based_on_chance" : opt
  boolean "pickup_same_items_as_in_hand" : opt
  boolean "track_target" : opt
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
`can_pickup_any_item`：<samp>boolean</samp>

- If true, the mob can pickup any item.


////


//// define
`can_pickup_to_hand_or_equipment`：<samp>boolean</samp>

- If true, the mob can pickup items to its hand or armor slots.


////


//// define
`cooldown_after_being_attacked`：<samp>number</samp>

- Amount of time an offended entity needs before being willing to pick up items.


////


//// define
`excluded_items`：<samp>array</samp>

- List of items this mob will not pick up.


////

<div class="language-text highlight"><span class="filename"><code>excluded_items</code></span><pre id="__code_1"><span></span></pre></div>

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
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the `wiggle room` to stop the AI from bouncing back and forth trying to reach a specific spot.


////


//// define
`max_dist`：<samp>number</samp>

- Maximum distance this mob will look for items to pick up.


////


//// define
`search_height`：<samp>number</samp>

- Height in blocks the mob will look for items to pick up.


////


//// define
`pickup_based_on_chance`：<samp>boolean</samp>

- If true, depending on the difficulty, there is a random chance that the mob may not be able to pickup items.


////


//// define
`pickup_same_items_as_in_hand`：<samp>boolean</samp>

- If true, the mob will pickup the same item as the item in its hand.


////


//// define
`track_target`：<samp>boolean</samp>

- If true, this mob will chase after the target as long as it's a valid target.


////


///

