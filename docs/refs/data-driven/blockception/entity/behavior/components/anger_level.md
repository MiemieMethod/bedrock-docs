# Anger Level

> 文档版本：1.21.50.25

Allows this entity to track anger towards a set of nuisances

## 架构

```mcschema
anger_level:
{
  number "anger_decrement_interval" : opt
  integer "angry_boost" : opt
  integer "angry_threshold" : opt
  number "default_annoyingness" : opt
  number "default_projectile_annoyingness" : opt
  integer "max_anger" : opt
  filters "nuisance_filter"
  array "on_increase_sounds" : opt
  {
    object "<any array element>" : opt
    {
      string "condition" : opt
      string "sound" : opt
    }
  }
  boolean "remove_targets_below_angry_threshold" : opt
}

```

/// html | div.result
//// define
`anger_decrement_interval`：<samp>number</samp>

- Anger level will decay over time. Defines how often anger towards all nuisances will be decreased by one


////


//// define
`angry_boost`：<samp>integer</samp>

- Anger boost applied to angry threshold when mob gets angry.


////


//// define
`angry_threshold`：<samp>integer</samp>

- Threshold that define when the mob is considered angry at a nuisance.


////


//// define
`default_annoyingness`：<samp>number</samp>

- The default amount of annoyingness for any given nuisance. Specifies how much to raise anger level on each provocation


////


//// define
`default_projectile_annoyingness`：<samp>number</samp>

- The default amount of annoyingness for projectile nuisance. Specifies how much to raise anger level on each provocation


////


//// define
`max_anger`：<samp>integer</samp>

- The maximum anger level that can be reached. Applies to any nuisance


////


//// define
`nuisance_filter`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Filter that is applied to determine if a mob can be a nuisance.


////


//// define
`on_increase_sounds`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>on_increase_sounds</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`condition`：<samp>string</samp>

- The event that will trigger the sound


//////


////// define
`sound`：<samp>string</samp>

- The sound to play


//////


/////


////


//// define
`remove_targets_below_angry_threshold`：<samp>boolean</samp>

- Defines if the mob should remove target if it falls below 'angry' threshold.


////


///

