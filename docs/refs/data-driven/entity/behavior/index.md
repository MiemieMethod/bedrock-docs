# Entity Server Definition

> 文档版本：1.21.0.24

The minecraft entity server definition file, defining a entity's behavior.

## 架构

```mcschema
entity:
{
  format_version "format_version"
  entity "minecraft:entity"
}

```

/// html | div.result
//// define
`format_version`：<samp>format_version</samp> {#assets.schemas.common.semver.format_version_no_number.json}


////

```mcschema
format_version:
array
{
  integer "<any array element>" : opt
}

```

//// html | div.result
///// define
`<any array element>`：<samp>integer</samp>


/////


////


```mcschema
format_version:
string

```

//// html | div.result

////




//// define
`minecraft:entity`：<samp>entity</samp> {#assets.schemas.behavior.entities.subschemas.minecraft_entity.json}


////

```mcschema
entity:
{
  object "description" : opt
  {
    string "identifier" : opt
    boolean "is_spawnable" : opt
    boolean "is_summonable" : opt
    boolean "is_experimental" : opt
  }
  object "components" : opt
  {
    minecraft:attack "minecraft:attack"
    minecraft:spell_effects "minecraft:spell_effects"
    minecraft:strength "minecraft:strength"
    minecraft:addrider "minecraft:addrider"
    minecraft:admire_item "minecraft:admire_item"
    minecraft:ageable "minecraft:ageable"
    minecraft:anger_level "minecraft:anger_level"
    minecraft:angry "minecraft:angry"
    break_door "minecraft:annotation.break_door"
    open_door "minecraft:annotation.open_door"
    minecraft:area_attack "minecraft:area_attack"
    minecraft:attack_cooldown "minecraft:attack_cooldown"
    minecraft:barter "minecraft:barter"
    minecraft:block_climber "minecraft:block_climber"
    minecraft:block_sensor "minecraft:block_sensor"
    minecraft:boostable "minecraft:boostable"
    minecraft:boss "minecraft:boss"
    minecraft:break_blocks "minecraft:break_blocks"
    minecraft:breathable "minecraft:breathable"
    minecraft:breedable "minecraft:breedable"
    minecraft:bribeable "minecraft:bribeable"
    minecraft:buoyant "minecraft:buoyant"
    minecraft:burns_in_daylight "minecraft:burns_in_daylight"
    minecraft:can_join_raid "minecraft:can_join_raid"
     "minecraft:behavior.python_custom:" : opt
    minecraft:behavior_python_custom "^minecraft:behavior\.python_custom:[a-zA-Z0-9_]*$"
  }
  object "events" : opt
  {
    definition_event "minecraft:entity_born"
    definition_event "minecraft:entity_spawned"
    definition_event "minecraft:entity_transformed"
    definition_event "minecraft:on_prime"
    definition_event "<any object property>"
  }
}

```

//// html | div.result
///// define
`description`：<samp>object</samp>

- The entity description.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>string</samp>

- The entity identifier.


//////


////// define
`is_spawnable`：<samp>boolean</samp>

- Specifies whether the entity can be spawned using the spawn egg.


//////


////// define
`is_summonable`：<samp>boolean</samp>

- Specifies whether the entity can be spawned using the summon command.


//////


////// define
`is_experimental`：<samp>boolean</samp>

- Specifies whether the experimental gameplay needs to be turned on in order to spawn the entity.


//////


/////


///// define
`components`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minecraft:attack`：<samp>minecraft:attack</samp>

- [`minecraft:attack`](./components/minecraft_attack.md)组件。


//////

////// define
`minecraft:spell_effects`：<samp>minecraft:spell_effects</samp>

- [`minecraft:spell_effects`](./components/minecraft_spell_effects.md)组件。


//////

////// define
`minecraft:strength`：<samp>minecraft:strength</samp>

- [`minecraft:strength`](./components/minecraft_strength.md)组件。


//////

////// define
`minecraft:addrider`：<samp>minecraft:addrider</samp>

- [`minecraft:addrider`](./components/minecraft_addrider.md)组件。


//////

////// define
`minecraft:admire_item`：<samp>minecraft:admire_item</samp>

- [`minecraft:admire_item`](./components/minecraft_admire_item.md)组件。


//////

////// define
`minecraft:ageable`：<samp>minecraft:ageable</samp>

- [`minecraft:ageable`](./components/minecraft_ageable.md)组件。


//////

////// define
`minecraft:anger_level`：<samp>minecraft:anger_level</samp>

- [`minecraft:anger_level`](./components/minecraft_anger_level.md)组件。


//////

////// define
`minecraft:angry`：<samp>minecraft:angry</samp>

- [`minecraft:angry`](./components/minecraft_angry.md)组件。


//////

////// define
`minecraft:annotation.break_door`：<samp>break_door</samp>

- [`minecraft:annotation.break_door`](./components/minecraft_annotation_break_door.md)组件。


//////

////// define
`minecraft:annotation.open_door`：<samp>open_door</samp>

- [`minecraft:annotation.open_door`](./components/minecraft_annotation_open_door.md)组件。


//////

////// define
`minecraft:area_attack`：<samp>minecraft:area_attack</samp>

- [`minecraft:area_attack`](./components/minecraft_area_attack.md)组件。


//////

////// define
`minecraft:attack_cooldown`：<samp>minecraft:attack_cooldown</samp>

- [`minecraft:attack_cooldown`](./components/minecraft_attack_cooldown.md)组件。


//////

////// define
`minecraft:barter`：<samp>minecraft:barter</samp>

- [`minecraft:barter`](./components/minecraft_barter.md)组件。


//////

////// define
`minecraft:block_climber`：<samp>minecraft:block_climber</samp>

- [`minecraft:block_climber`](./components/minecraft_block_climber.md)组件。


//////

////// define
`minecraft:block_sensor`：<samp>minecraft:block_sensor</samp>

- [`minecraft:block_sensor`](./components/minecraft_block_sensor.md)组件。


//////

////// define
`minecraft:boostable`：<samp>minecraft:boostable</samp>

- [`minecraft:boostable`](./components/minecraft_boostable.md)组件。


//////

////// define
`minecraft:boss`：<samp>minecraft:boss</samp>

- [`minecraft:boss`](./components/minecraft_boss.md)组件。


//////

////// define
`minecraft:break_blocks`：<samp>minecraft:break_blocks</samp>

- [`minecraft:break_blocks`](./components/minecraft_break_blocks.md)组件。


//////

////// define
`minecraft:breathable`：<samp>minecraft:breathable</samp>

- [`minecraft:breathable`](./components/minecraft_breathable.md)组件。


//////

////// define
`minecraft:breedable`：<samp>minecraft:breedable</samp>

- [`minecraft:breedable`](./components/minecraft_breedable.md)组件。


//////

////// define
`minecraft:bribeable`：<samp>minecraft:bribeable</samp>

- [`minecraft:bribeable`](./components/minecraft_bribeable.md)组件。


//////

////// define
`minecraft:buoyant`：<samp>minecraft:buoyant</samp>

- [`minecraft:buoyant`](./components/minecraft_buoyant.md)组件。


//////

////// define
`minecraft:burns_in_daylight`：<samp>minecraft:burns_in_daylight</samp>

- [`minecraft:burns_in_daylight`](./components/minecraft_burns_in_daylight.md)组件。


//////

////// define
`minecraft:can_join_raid`：<samp>minecraft:can_join_raid</samp>

- [`minecraft:can_join_raid`](./components/minecraft_can_join_raid.md)组件。


//////

////// define
`minecraft:behavior.python_custom:`


//////


////// define
`^minecraft:behavior\.python_custom:[a-zA-Z0-9_]*$`：<samp>minecraft:behavior_python_custom</samp>

- [`^minecraft:behavior\.python_custom:[a-zA-Z0-9_]*$`](./components/minecraft_behavior_python_custom.md)组件。


//////

/////


///// define
`events`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>events</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minecraft:entity_born`：<samp>definition_event</samp> {#assets.schemas.common.definition.definition_event.json}


//////

```mcschema
definition_event:
{
  number "weight" : opt
  expression_node_no_version "condition"
  array "randomize" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "sequence" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  definition_trigger_no_condition "trigger"
}

```

////// html | div.result
/////// define
`weight`：<samp>number</samp>


///////


/////// define
`condition`：<samp>expression_node_no_version</samp> {#assets.schemas.common.molang.expression_node_no_version.json}


///////

```mcschema
expression_node_no_version:
string

```

/////// html | div.result

///////


```mcschema
expression_node_no_version:
boolean

```

/////// html | div.result

///////


```mcschema
expression_node_no_version:
number

```

/////// html | div.result

///////




/////// define
`randomize`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>randomize</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////


/////// define
`sequence`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////


/////// define
`trigger`：<samp>definition_trigger_no_condition</samp> {#assets.schemas.common.definition.definition_trigger_no_condition.json}


///////

```mcschema
definition_trigger_no_condition:
string

```

/////// html | div.result

///////


```mcschema
definition_trigger_no_condition:
{
  string "event" : opt
  string "target" : opt
}

```

/////// html | div.result
//////// define
`event`：<samp>string</samp>


////////


//////// define
`target`：<samp>string</samp>


////////


///////




//////



////// define
`minecraft:entity_spawned`：<samp>[definition_event](#assets.schemas.common.definition.definition_event.json)</samp>


//////


////// define
`minecraft:entity_transformed`：<samp>[definition_event](#assets.schemas.common.definition.definition_event.json)</samp>


//////


////// define
`minecraft:on_prime`：<samp>[definition_event](#assets.schemas.common.definition.definition_event.json)</samp>


//////


////// define
`<any object property>`：<samp>[definition_event](#assets.schemas.common.definition.definition_event.json)</samp>


//////


/////


////



///

