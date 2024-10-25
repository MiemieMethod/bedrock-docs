# Damage Sensor

> 文档版本：1.21.50.25

Defines what events to call when this entity is damaged by specific entities or items.

## 架构

```mcschema
damage_sensor:
{
  array "triggers" : opt
  {
    object "<any array element>" : opt
    {
      entity_damage_source "cause"
      number "damage_modifier" : opt
      number "damage_multiplier" : opt
      boolean "deals_damage" : opt
      trigger "on_damage"
      sound_event "on_damage_sound_event"
    }
  }
  object "triggers" : opt
  {
  }
}

```

/// html | div.result
//// define
`triggers`：<samp>array</samp>

- The list of triggers that fire when the environment conditions match the given filter criteria.


////

<div class="language-text highlight"><span class="filename"><code>triggers</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- List of triggers with the events to call when taking specific kinds of damage.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`cause`：<samp>entity_damage_source</samp> {#assets.schemas-blockception.general.entity.damage_source.json}

- Type of damage that triggers the events.


//////

```mcschema
entity_damage_source:
string

```

////// html | div.result

//////



////// define
`damage_modifier`：<samp>number</samp>

- A modifier that adds to/removes from the base damage from the damage cause. It does not reduce damage to less than 0.


//////


////// define
`damage_multiplier`：<samp>number</samp>

- A multiplier that modifies the base damage from the damage cause. If deals_damage is true the multiplier can only reduce the damage the entity will take to a minimum of 1.


//////


////// define
`deals_damage`：<samp>boolean</samp>

- If true, the damage dealt to the entity will take away health from it, set to false to make the entity ignore that damage.


//////


////// define
`on_damage`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Specifies filters for entity definitions and events.


//////

```mcschema
trigger:
string

```

////// html | div.result

//////


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

////// html | div.result
/////// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


///////


/////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions for this trigger to execute.


///////


/////// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


///////

```mcschema
subject:
string

```

/////// html | div.result

///////



//////


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

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////




////// define
`on_damage_sound_event`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Defines what sound to play, if any, when the on_damage filters are met.


//////

```mcschema
sound_event:
string

```

////// html | div.result

//////



/////


////


//// define
`triggers`：<samp>object</samp>

- List of triggers with the events to call when taking specific kinds of damage.


////

<div class="language-text highlight"><span class="filename"><code>triggers</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////



///

