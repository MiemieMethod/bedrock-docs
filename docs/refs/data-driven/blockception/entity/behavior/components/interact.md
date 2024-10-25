# Interact

> 文档版本：1.21.50.25

Defines interactions with this entity.

## 架构

```mcschema
interact:
{
  object "interactions" : opt
  {
    object "add_items" : opt
    {
      identifier "table"
    }
    number "cooldown" : opt
    boolean "admire" : opt
    boolean "barter" : opt
    number "cooldown_after_being_attacked" : opt
    integer "health_amount" : opt
    integer "hurt_item" : opt
    string "interact_text" : opt
    trigger "on_interact"
    object "particle_on_start" : opt
    {
      boolean "particle_offset_towards_interactor" : opt
      string "particle_type" : opt
      number "particle_y_offset" : opt
    }
    sound_event "play_sounds"
    string "spawn_entities" : opt
    object "spawn_items" : opt
    {
      identifier "table"
    }
    boolean "swing" : opt
    string "transform_to_item" : opt
    boolean "use_item" : opt
    string "vibration" : opt
    boolean "give_item" : opt
    boolean "take_item" : opt
    string "drop_item_slot" : opt
    string "equip_item_slot" : opt
    object "repair_entity_item" : opt
    {
      integer "amount" : opt
      string "slot" : opt
    }
  }
  array "interactions" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
}

```

/// html | div.result
//// define
`interactions`：<samp>object</samp>

- The interactions.


////

<div class="language-text highlight"><span class="filename"><code>interactions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`add_items`：<samp>object</samp>

- Loot table with items to add to the player's inventory upon successful interaction.


/////

<div class="language-text highlight"><span class="filename"><code>add_items</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`table`：<samp>identifier</samp> {#assets.schemas-blockception.general.loot_table.identifier.json}

- File path, relative to the Behavior Pack's path, to the loot table file.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



/////


///// define
`cooldown`：<samp>number</samp>

- Time in seconds before this entity can be interacted with again.


/////


///// define
`admire`：<samp>boolean</samp>

- Allows entity to admire the item. Requires "minecraft:admire_item" and "minecraft:behavior.admire_item" to work.


/////


///// define
`barter`：<samp>boolean</samp>

- Allows entity to barter with the item. Requires "minecraft:barter" to work.


/////


///// define
`cooldown_after_being_attacked`：<samp>number</samp>

- Time in seconds before this entity can be interacted with after being attacked.


/////


///// define
`health_amount`：<samp>integer</samp>

- The amount of health this entity will recover or hurt when interacting with this item. Negative values will harm the entity.


/////


///// define
`hurt_item`：<samp>integer</samp>

- The amount of damage the item will take when used to interact with this entity. A value of 0 means the item won't lose durability.


/////


///// define
`interact_text`：<samp>string</samp>

- Text to show when the player is able to interact in this way with this entity when playing with Touch-screen controls.


/////


///// define
`on_interact`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event to fire when the interaction occurs.


/////

```mcschema
trigger:
string

```

///// html | div.result

/////


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

///// html | div.result
////// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


//////


////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions for this trigger to execute.


//////


////// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


//////

```mcschema
subject:
string

```

////// html | div.result

//////



/////


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

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////




///// define
`particle_on_start`：<samp>object</samp>

- Particle effect that will be triggered at the start of the interaction.


/////

<div class="language-text highlight"><span class="filename"><code>particle_on_start</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`particle_offset_towards_interactor`：<samp>boolean</samp>

- Whether or not the particle will appear closer to who performed the interaction.


//////


////// define
`particle_type`：<samp>string</samp>

- The type of particle that will be spawned.


//////


////// define
`particle_y_offset`：<samp>number</samp>

- Will offset the particle this amount in the y direction.


//////


/////


///// define
`play_sounds`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- List of sounds to play when the interaction occurs.


/////

```mcschema
sound_event:
string

```

///// html | div.result

/////



///// define
`spawn_entities`：<samp>string</samp>

- List of entities to spawn when the interaction occurs.


/////


///// define
`spawn_items`：<samp>object</samp>

- Loot table with items to drop on the ground upon successful interaction.


/////

<div class="language-text highlight"><span class="filename"><code>spawn_items</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`table`：<samp>[identifier](#assets.schemas-blockception.general.loot_table.identifier.json)</samp>

- File path, relative to the Behavior Pack's path, to the loot table file.


//////


/////


///// define
`swing`：<samp>boolean</samp>

- If true, the player will do the "swing" animation when interacting with this entity.


/////


///// define
`transform_to_item`：<samp>string</samp>

- The feed item used will transform to this item upon successful interaction. Format: itemName:auxValue


/////


///// define
`use_item`：<samp>boolean</samp>

- If true, the interaction will use an item.


/////


///// define
`vibration`：<samp>string</samp>

- Vibration to emit when the interaction occurs. Admitted values are entity_interact (used by default), shear, and none (no vibration emitted).


/////


///// define
`give_item`：<samp>boolean</samp>

- UNDOCUMENTED Item to give to the player upon successful interaction.


/////


///// define
`take_item`：<samp>boolean</samp>

- UNDOCUMENTED Takes an item from the player.


/////


///// define
`drop_item_slot`：<samp>string</samp>

- The entity's equipment slot to remove and drop the item from, if any, upon successful interaction.


/////


///// define
`equip_item_slot`：<samp>string</samp>

- The entity's equipment slot to equip the item to, if any, upon successful interaction.


/////


///// define
`repair_entity_item`：<samp>object</samp>

- Allows to repair one of the entity's items.


/////

<div class="language-text highlight"><span class="filename"><code>repair_entity_item</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`amount`：<samp>integer</samp>

- How much of the item durability should be restored upon interaction.


//////


////// define
`slot`：<samp>string</samp>

- The entity's slot containing the item to be repaired.


//////


/////


////


//// define
`interactions`：<samp>array</samp>

- The interactions.


////

<div class="language-text highlight"><span class="filename"><code>interactions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////



///

