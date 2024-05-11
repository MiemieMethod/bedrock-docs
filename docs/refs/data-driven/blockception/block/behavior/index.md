# Block Behavior

> 文档版本：1.21.0.24

The minecraft block behavior specification.

## 架构

```mcschema
block:
{
  format_version "format_version"
  blocks "minecraft:block"
}

```

/// html | div.result
//// define
`format_version`：<samp>format_version</samp> {#assets.schemas-blockception.general.format_version.json}


////

```mcschema
format_version:
string

```

//// html | div.result

////



//// define
`minecraft:block`：<samp>blocks</samp> {#assets.schemas-blockception.behavior.blocks.format.minecraft.block.json}


////

```mcschema
blocks:
{
  object "description" : opt
  {
    identifier "identifier"
    object "menu_category" : opt
    {
      creative_category "category"
      item_group "group"
      boolean "is_hidden_in_commands" : opt
    }
    object "states" : opt
    {
      enum "^([a-zA-Z0-9_]+:[a-zA-Z0-9_\-]+)$"
      integer_range "^([a-zA-Z0-9_]+:[a-zA-Z0-9_\-]+)$"
    }
    object "traits" : opt
    {
      placement_direction "minecraft:placement_direction"
      placement_position "minecraft:placement_position"
    }
  }
  events "events"
  object "components" : opt
  {
    collision_box "minecraft:collision_box"
    crafting_table "minecraft:crafting_table"
    destructible_by_explosion "minecraft:destructible_by_explosion"
    destructible_by_mining "minecraft:destructible_by_mining"
    display_name "minecraft:display_name"
    flammable "minecraft:flammable"
    friction "minecraft:friction"
    geometry "minecraft:geometry"
    light_dampening "minecraft:light_dampening"
    light_emission "minecraft:light_emission"
    loot "minecraft:loot"
    map_color "minecraft:map_color"
    material_instances "minecraft:material_instances"
    placement_filter "minecraft:placement_filter"
    selection_box "minecraft:selection_box"
    transformation "minecraft:transformation"
    on_fall_on "minecraft:on_fall_on"
    on_interact "minecraft:on_interact"
    on_placed "minecraft:on_placed"
    on_player_destroyed "minecraft:on_player_destroyed"
    on_player_placing "minecraft:on_player_placing"
    on_step_off "minecraft:on_step_off"
    on_step_on "minecraft:on_step_on"
    random_ticking "minecraft:queued_ticking"
    random_ticking "minecraft:random_ticking"
    object "tag:.+" : opt
    {
    }
  }
  array "permutations" : opt
  {
    object "<any array element>" : opt
    {
      0 "condition"
      object "components" : opt
      {
      }
    }
  }
}

```

//// html | div.result
///// define
`description`：<samp>object</samp>

- The description for this block.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.block.identifier.json}

- The identifier for this block. The name must include a namespace and must not use the Minecraft namespace unless overriding a Vanilla block.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`menu_category`：<samp>object</samp>

- Specifies the menu category and group for the block, which determine where this block is placed in the inventory and crafting table container screens. If this field is omitted, the block will not appear in the inventory or crafting table container screens.


//////

<div class="language-text highlight"><span class="filename"><code>menu_category</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`category`：<samp>creative_category</samp> {#assets.schemas-blockception.general.vanilla.creative_category.json}


///////

```mcschema
creative_category:
string

```

/////// html | div.result

///////



/////// define
`group`：<samp>item_group</samp> {#assets.schemas-blockception.general.vanilla.item_group.json}


///////

```mcschema
item_group:
string

```

/////// html | div.result

///////



/////// define
`is_hidden_in_commands`：<samp>boolean</samp>

- Determines whether or not this item can be used with commands such as /give and /setblock. Commands can use blocks by default


///////


//////


////// define
`states`：<samp>object</samp>

- Block states are variables that can be set to different values in order to change how your block looks or behaves.


//////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`^([a-zA-Z0-9_]+:[a-zA-Z0-9_\-]+)$`：<samp>enum</samp> {#assets.schemas-blockception.behavior.blocks.format.states.enum.json}

- The key defines the name of a state, which must be properly namespaced. Each value is an array that contains all of the possible values of that state or an object defining a range of integers.


///////

```mcschema
enum:
array
{
  boolean "<any array element>" : opt
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>boolean</samp>


////////


///////


```mcschema
enum:
array
{
  integer "<any array element>" : opt
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>integer</samp>


////////


///////


```mcschema
enum:
array
{
  string "<any array element>" : opt
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>


////////


///////




/////// define
`^([a-zA-Z0-9_]+:[a-zA-Z0-9_\-]+)$`：<samp>integer_range</samp> {#assets.schemas-blockception.behavior.blocks.format.states.integer_range.json}

- The key defines the name of a state, which must be properly namespaced. Each value is an array that contains all of the possible values of that state or an object defining a range of integers.


///////

```mcschema
integer_range:
{
  object "values" : opt
  {
    integer "min" : opt
    integer "max" : opt
  }
}

```

/////// html | div.result
//////// define
`values`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>values</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`min`：<samp>integer</samp>

- The lowest integer this state supports. This is also used as the default state value.


/////////


///////// define
`max`：<samp>integer</samp>

- The highest integer this state supports. This cannot be more than 15 above the minimum.


/////////


////////


///////




//////


////// define
`traits`：<samp>object</samp>

- A shortcut for creators to use Vanilla block states without needing to define and manage a series of events or triggers on custom blocks


//////

<div class="language-text highlight"><span class="filename"><code>traits</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`minecraft:placement_direction`：<samp>placement_direction</samp> {#assets.schemas-blockception.behavior.blocks.format.traits.placement_direction.json}


///////

```mcschema
placement_direction:
{
  array "enabled_states" : opt
  {
    string "<any array element>" : opt
  }
  number "y_rotation_offset" : opt
}

```

/////// html | div.result
//////// define
`enabled_states`：<samp>array</samp>

- Block states you wish to enable


////////

<div class="language-text highlight"><span class="filename"><code>enabled_states</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>


/////////


////////


//////// define
`y_rotation_offset`：<samp>number</samp>

- This rotation offset only applies to the horizontal state values


////////


///////



/////// define
`minecraft:placement_position`：<samp>placement_position</samp> {#assets.schemas-blockception.behavior.blocks.format.traits.placement_position.json}


///////

```mcschema
placement_position:
{
  array "enabled_states" : opt
  {
    string "<any array element>" : opt
  }
}

```

/////// html | div.result
//////// define
`enabled_states`：<samp>array</samp>

- Block states you wish to enable


////////

<div class="language-text highlight"><span class="filename"><code>enabled_states</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>


/////////


////////


///////



//////


/////


///// define
`events`：<samp>events</samp> {#assets.schemas-blockception.behavior.blocks.format.events.json}


/////

```mcschema
events:
{
  object "minecraft:on_fall_on" : opt
  {
    string "condition" : opt
    string "event" : opt
    string "target" : opt
  }
  object "minecraft:on_interact" : opt
  {
  }
  object "minecraft:on_placed" : opt
  {
  }
  object "minecraft:on_player_destroyed" : opt
  {
  }
  object "minecraft:on_player_placing" : opt
  {
  }
  object "minecraft:on_step_off" : opt
  {
  }
  object "minecraft:on_step_on" : opt
  {
  }
}

```

///// html | div.result
////// define
`minecraft:on_fall_on`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_fall_on</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`condition`：<samp>string</samp>

- The condition of event to be executed on the block.


///////


/////// define
`event`：<samp>string</samp>

- The event executed on the block.


///////


/////// define
`target`：<samp>string</samp>

- The target of event executed on the block.


///////


//////


////// define
`minecraft:on_interact`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_interact</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`minecraft:on_placed`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_placed</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`minecraft:on_player_destroyed`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_player_destroyed</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`minecraft:on_player_placing`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_player_placing</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`minecraft:on_step_off`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_step_off</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`minecraft:on_step_on`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_step_on</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////



///// define
`components`：<samp>object</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minecraft:collision_box`：<samp>collision_box</samp>

- [`minecraft:collision_box`](./components/collision_box.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:crafting_table`：<samp>crafting_table</samp>

- [`minecraft:crafting_table`](./components/crafting_table.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:destructible_by_explosion`：<samp>destructible_by_explosion</samp>

- [`minecraft:destructible_by_explosion`](./components/destructible_by_explosion.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:destructible_by_mining`：<samp>destructible_by_mining</samp>

- [`minecraft:destructible_by_mining`](./components/destructible_by_mining.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:display_name`：<samp>display_name</samp>

- [`minecraft:display_name`](./components/display_name.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:flammable`：<samp>flammable</samp>

- [`minecraft:flammable`](./components/flammable.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:friction`：<samp>friction</samp>

- [`minecraft:friction`](./components/friction.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:geometry`：<samp>geometry</samp>

- [`minecraft:geometry`](./components/geometry.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:light_dampening`：<samp>light_dampening</samp>

- [`minecraft:light_dampening`](./components/light_dampening.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:light_emission`：<samp>light_emission</samp>

- [`minecraft:light_emission`](./components/light_emission.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:loot`：<samp>loot</samp>

- [`minecraft:loot`](./components/loot.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:map_color`：<samp>map_color</samp>

- [`minecraft:map_color`](./components/map_color.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:material_instances`：<samp>material_instances</samp>

- [`minecraft:material_instances`](./components/material_instances.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:placement_filter`：<samp>placement_filter</samp>

- [`minecraft:placement_filter`](./components/placement_filter.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:selection_box`：<samp>selection_box</samp>

- [`minecraft:selection_box`](./components/selection_box.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:transformation`：<samp>transformation</samp>

- [`minecraft:transformation`](./components/transformation.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:on_fall_on`：<samp>on_fall_on</samp>

- [`minecraft:on_fall_on`](./components/on_fall_on.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:on_interact`：<samp>on_interact</samp>

- [`minecraft:on_interact`](./components/on_interact.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:on_placed`：<samp>on_placed</samp>

- [`minecraft:on_placed`](./components/on_placed.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:on_player_destroyed`：<samp>on_player_destroyed</samp>

- [`minecraft:on_player_destroyed`](./components/on_player_destroyed.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:on_player_placing`：<samp>on_player_placing</samp>

- [`minecraft:on_player_placing`](./components/on_player_placing.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:on_step_off`：<samp>on_step_off</samp>

- [`minecraft:on_step_off`](./components/on_step_off.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:on_step_on`：<samp>on_step_on</samp>

- [`minecraft:on_step_on`](./components/on_step_on.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:queued_ticking`：<samp>random_ticking</samp>

- [`minecraft:queued_ticking`](./components/queued_ticking.md)组件。UNDOCUMENTED.


//////

////// define
`minecraft:random_ticking`：<samp>random_ticking</samp>

- [`minecraft:random_ticking`](./components/random_ticking.md)组件。UNDOCUMENTED.


//////

////// define
`tag:.+`：<samp>object</samp>

- Applies a tag to the block, using the key without the "tag:" prefix as the tag name.


//////

<div class="language-text highlight"><span class="filename"><code>tag:.+</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`permutations`：<samp>array</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>permutations</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`condition`：<samp>0</samp> {#assets.schemas-blockception.molang.boolean.json}

- A Molang expression that evaluates to true or false to determine if this permutation should be used. For permutation conditions you are limited to using one Molang query: "query.block_state()"


///////

```mcschema
0:
string

```

/////// html | div.result

///////


```mcschema
0:
boolean

```

/////// html | div.result

///////




/////// define
`components`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


/////


////



///

