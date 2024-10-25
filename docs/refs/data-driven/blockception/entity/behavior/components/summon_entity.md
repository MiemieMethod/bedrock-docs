# Summon Entity

> 文档版本：1.21.50.25

Allows the mob to attack the player by summoning other entities.

## 架构

```mcschema
summon_entity:
{
  priority "priority"
  array "summon_choices" : opt
  {
    object "<any array element>" : opt
    {
      number "cast_duration" : opt
      number "cooldown_time" : opt
      boolean "do_casting" : opt
      filters "filters"
      number "max_activation_range" : opt
      number "min_activation_range" : opt
      integer "particle_color" : opt
      string "particle_color" : opt
      array "sequence" : opt
      {
        object "<any array element>" : opt
        {
          number "delay" : opt
          number "delay_per_summon" : opt
          number "entity_lifespan" : opt
          number "base_delay" : opt
          string "entity_type" : opt
          integer "num_entities_spawned" : opt
          string "shape" : opt
          number "size" : opt
          sound_event "sound_event"
          integer "summon_cap" : opt
          number "summon_cap_radius" : opt
          string "target" : opt
        }
      }
      sound_event "start_sound_event"
      number "weight" : opt
    }
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
`summon_choices`：<samp>array</samp>

- List of spells for the mob to use to summon entities.


////

<div class="language-text highlight"><span class="filename"><code>summon_choices</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`cast_duration`：<samp>number</samp>

- Time in seconds the spell casting will take.


//////


////// define
`cooldown_time`：<samp>number</samp>

- Time in seconds the mob has to wait before using the spell again.


//////


////// define
`do_casting`：<samp>boolean</samp>

- If true, the mob will do the casting animations and render spell particles.


//////


////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


////// define
`max_activation_range`：<samp>number</samp>

- Upper bound of the activation distance in blocks for this spell.


//////


////// define
`min_activation_range`：<samp>number</samp>

- Lower bound of the activation distance in blocks for this spell.


//////


////// define
`particle_color`：<samp>integer</samp>

- The color of the particles for this spell.


//////


////// define
`particle_color`：<samp>string</samp>

- The color of the particles for this spell.


//////



////// define
`sequence`：<samp>array</samp>

- List of steps for the spell.


//////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`delay`：<samp>number</samp>

- Amount of time in seconds to wait before this step starts.


////////


//////// define
`delay_per_summon`：<samp>number</samp>

- Amount of time in seconds before each entity is summoned in this step.


////////


//////// define
`entity_lifespan`：<samp>number</samp>

- Amount of time in seconds that the spawned entity will be alive for. A value of -1.0 means it will remain alive for as long as it can


////////


//////// define
`base_delay`：<samp>number</samp>

- Amount of time in seconds to wait before this step starts.


////////


//////// define
`entity_type`：<samp>string</samp>

- The entity type of the entities we will spawn in this step.


////////


//////// define
`num_entities_spawned`：<samp>integer</samp>

- Number of entities that will be spawned in this step.


////////


//////// define
`shape`：<samp>string</samp>

- The base shape of this step. Valid values are circle and line


////////


//////// define
`size`：<samp>number</samp>

- The base size of the entity.


////////


//////// define
`sound_event`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to play for this step.


////////

```mcschema
sound_event:
string

```

//////// html | div.result

////////



//////// define
`summon_cap`：<samp>integer</samp>

- Maximum number of summoned entities at any given time.


////////


//////// define
`summon_cap_radius`：<samp>number</samp>

- Maximum radius where the summon entities can spawn.


////////


//////// define
`target`：<samp>string</samp>

- The target of the spell. This is where the spell will start (line will start here, circle will be centered here)


////////


///////


//////


////// define
`start_sound_event`：<samp>[sound_event](#assets.schemas-blockception.general.sound_event.json)</samp>

- The sound event to play when using this spell.


//////


////// define
`weight`：<samp>number</samp>

- The weight of this spell. Controls how likely the mob is to choose this spell when casting one


//////


/////


////


///

