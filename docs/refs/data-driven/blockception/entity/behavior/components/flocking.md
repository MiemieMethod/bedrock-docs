# Flocking

> 文档版本：1.21.0.24

Allows entities to flock in groups in water or not.

## 架构

```mcschema
flocking:
{
  number "block_distance" : opt
  number "block_weight" : opt
  number "breach_influence" : opt
  number "cohesion_threshold" : opt
  number "cohesion_weight" : opt
  number "goal_weight" : opt
  integer "high_flock_limit" : opt
  boolean "in_water" : opt
  number "influence_radius" : opt
  number "innner_cohesion_threshold" : opt
  number "loner_chance" : opt
  integer "low_flock_limit" : opt
  boolean "match_variants" : opt
  number "max_height" : opt
  number "min_height" : opt
  number "separation_threshold" : opt
  number "separation_weight" : opt
  boolean "use_center_of_mass" : opt
}

```

/// html | div.result
//// define
`block_distance`：<samp>number</samp>

- The amount of blocks away the entity will look at to push away from.


////


//// define
`block_weight`：<samp>number</samp>

- The weight of the push back away from blocks.


////


//// define
`breach_influence`：<samp>number</samp>

- The amount of push back given to a flocker that breaches out of the water.


////


//// define
`cohesion_threshold`：<samp>number</samp>

- The threshold in which to start applying cohesion.


////


//// define
`cohesion_weight`：<samp>number</samp>

- The weight applied for the cohesion steering of the flock.


////


//// define
`goal_weight`：<samp>number</samp>

- The weight on which to apply on the goal output.


////


//// define
`high_flock_limit`：<samp>integer</samp>

- Determines the high bound amount of entities that can be allowed in the flock.


////


//// define
`in_water`：<samp>boolean</samp>

- Tells the Flocking Component if the entity exists in water.


////


//// define
`influence_radius`：<samp>number</samp>

- The area around the entity that allows others to be added to the flock.


////


//// define
`innner_cohesion_threshold`：<samp>number</samp>

- The distance in which the flocker will stop applying cohesion.


////


//// define
`loner_chance`：<samp>number</samp>

- The percentage chance between 0-1 that a fish will spawn and not want to join flocks. Invalid values will be capped at the end points.


////


//// define
`low_flock_limit`：<samp>integer</samp>

- Determines the low bound amount of entities that can be allowed in the flock.


////


//// define
`match_variants`：<samp>boolean</samp>

- Tells the flockers that they can only match similar entities that also match the variant, mark variants, and color data of the other potential flockers.


////


//// define
`max_height`：<samp>number</samp>

- The Maximum height allowable in the air or water.


////


//// define
`min_height`：<samp>number</samp>

- The Minimum height allowable in the air or water.


////


//// define
`separation_threshold`：<samp>number</samp>

- The distance that is determined to be to close to another flocking and to start applying separation.


////


//// define
`separation_weight`：<samp>number</samp>

- The weight applied to the separation of the flock.


////


//// define
`use_center_of_mass`：<samp>boolean</samp>

- Tells the flockers that they will follow flocks based on the center of mass.


////


///

