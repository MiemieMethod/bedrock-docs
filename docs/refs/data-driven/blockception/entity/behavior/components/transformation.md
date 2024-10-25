# Transformation

> 文档版本：1.21.50.25

Defines an entity's transformation from the current definition into another

## 架构

```mcschema
transformation:
{
  object "add" : opt
  {
    array "component_groups" : opt
    {
      string "<any array element>" : opt
    }
  }
  sound_event "begin_transform_sound"
  number "delay" : opt
  object "delay" : opt
  {
    number "block_assist_chance" : opt
    number "block_chance" : opt
    integer "block_max" : opt
    integer "block_radius" : opt
    array "block_types" : opt
    {
      identifier "<any array element>"
    }
    number "value" : opt
  }
  boolean "drop_equipment" : opt
  boolean "drop_inventory" : opt
  string "into" : opt
  boolean "keep_level" : opt
  boolean "keep_owner" : opt
  boolean "preserve_equipment" : opt
  sound_event "transformation_sound"
}

```

/// html | div.result
//// define
`add`：<samp>object</samp>

- List of components to add to the entity after the transformation.


////

<div class="language-text highlight"><span class="filename"><code>add</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`component_groups`：<samp>array</samp>

- Names of component groups to add.


/////

<div class="language-text highlight"><span class="filename"><code>component_groups</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>string</samp>


//////


/////


////


//// define
`begin_transform_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Sound to play when the transformation starts.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`delay`：<samp>number</samp>

- Defines the properties of the delay for the transformation.


////


//// define
`delay`：<samp>object</samp>

- Defines the properties of the delay for the transformation.


////

<div class="language-text highlight"><span class="filename"><code>delay</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`block_assist_chance`：<samp>number</samp>

- Chance that the entity will look for nearby blocks that can speed up the transformation. Value must be between 0.0 and 1.0


/////


///// define
`block_chance`：<samp>number</samp>

- Chance that, once a block is found, will help speed up the transformation.


/////


///// define
`block_max`：<samp>integer</samp>

- Maximum number of blocks the entity will look for to aid in the transformation. If not defined or set to 0, it will be set to the block radius


/////


///// define
`block_radius`：<samp>integer</samp>

- Distance in Blocks that the entity will search for blocks that can help the transformation.


/////


///// define
`block_types`：<samp>array</samp>

- List of blocks that can help the transformation of this entity.


/////

<div class="language-text highlight"><span class="filename"><code>block_types</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>identifier</samp> {#assets.schemas-blockception.general.block.identifier.json}


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



/////


///// define
`value`：<samp>number</samp>

- Time in seconds before the entity transforms.


/////


////



//// define
`drop_equipment`：<samp>boolean</samp>

- Cause the entity to drop all equipment upon transformation.


////


//// define
`drop_inventory`：<samp>boolean</samp>

- Cause the entity to drop all items in inventory upon transformation.


////


//// define
`into`：<samp>string</samp>

- Entity Definition that this entity will transform into.


////


//// define
`keep_level`：<samp>boolean</samp>

- If this entity has trades and has leveled up, it should maintain that level after transformation.


////


//// define
`keep_owner`：<samp>boolean</samp>

- If this entity is owned by another entity, it should remain owned after transformation.


////


//// define
`preserve_equipment`：<samp>boolean</samp>

- Cause the entity to keep equipment after going through transformation.


////


//// define
`transformation_sound`：<samp>[sound_event](#assets.schemas-blockception.general.sound_event.json)</samp>

- Sound to play when the entity is done transforming.


////


///

