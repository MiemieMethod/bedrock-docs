# Hurt On Condition

> 文档版本：1.21.0.24

Defines a set of conditions under which an entity should take damage.

## 架构

```mcschema
hurt_on_condition:
{
  array "damage_conditions" : opt
  {
    object "<any array element>" : opt
    {
      filters "filters"
      entity_damage_source "cause"
      integer "damage_per_tick" : opt
    }
  }
}

```

/// html | div.result
//// define
`damage_conditions`：<samp>array</samp>

- An array of conditions used to compare the event to.


////

<div class="language-text highlight"><span class="filename"><code>damage_conditions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A condition used to compare the event to.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


////// define
`cause`：<samp>entity_damage_source</samp> {#assets.schemas-blockception.general.entity.damage_source.json}

- Damage cause.


//////

```mcschema
entity_damage_source:
string

```

////// html | div.result

//////



////// define
`damage_per_tick`：<samp>integer</samp>

- Amount of damage done each tick that the conditions are met.


//////


/////


////


///

