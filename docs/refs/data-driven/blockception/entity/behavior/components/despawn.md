# Despawn

> 文档版本：1.21.50.25

Despawns the Actor when the despawn rules or optional filters evaluate to true.

## 架构

```mcschema
despawn:
{
  boolean "despawn_from_chance" : opt
  object "despawn_from_distance" : opt
  {
    integer "max_distance" : opt
    integer "min_distance" : opt
  }
  boolean "despawn_from_inactivity" : opt
  boolean "despawn_from_simulation_edge" : opt
  filters "filters"
  integer "min_range_inactivity_timer" : opt
  integer "min_range_random_chance" : opt
  boolean "remove_child_entities" : opt
}

```

/// html | div.result
//// define
`despawn_from_chance`：<samp>boolean</samp>

- Determines if `min_range_random_chance` is used in the standard despawn rules.


////


//// define
`despawn_from_distance`：<samp>object</samp>

- Defines the minimum and maximum distance for despawn to occur.


////

<div class="language-text highlight"><span class="filename"><code>despawn_from_distance</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`max_distance`：<samp>integer</samp>

- Maximum distance for standard despawn rules to instantly despawn the mob.


/////


///// define
`min_distance`：<samp>integer</samp>

- Minimum distance for standard despawn rules to try to despawn the mob.


/////


////


//// define
`despawn_from_inactivity`：<samp>boolean</samp>

- Determines if the `min_range_inactivity_timer` is used in the standard despawn rules.


////


//// define
`despawn_from_simulation_edge`：<samp>boolean</samp>

- Determines if the mob is instantly despawned at the edge of simulation distance in the standard despawn rules.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions that must be satisfied before the Actor is despawned. If a filter is defined then standard despawn rules are ignored.


////


//// define
`min_range_inactivity_timer`：<samp>integer</samp>

- The amount of time in seconds that the mob must be inactive.


////


//// define
`min_range_random_chance`：<samp>integer</samp>

- A random chance between 1 and the given value.


////


//// define
`remove_child_entities`：<samp>boolean</samp>

- If true, all entities linked to this entity in a child relationship (eg. leashed) will also be despawned.


////


///

