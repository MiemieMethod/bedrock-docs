# Explode

> 文档版本：1.21.50.25

Defines how the entity explodes.

## 架构

```mcschema
explode:
{
  boolean "allow_underwater" : opt
  boolean "breaks_blocks" : opt
  boolean "causes_fire" : opt
  number "damage_scaling" : opt
  boolean "destroy_affected_by_griefing" : opt
  boolean "fire_affected_by_griefing" : opt
  array "fuse_length" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "fuse_length" : opt
  boolean "fuse_lit" : opt
  number "knockback_scaling" : opt
  number "max_resistance" : opt
  boolean "negates_fall_damage" : opt
  string "particle_effect" : opt
  number "power" : opt
  string "sound_effect" : opt
  boolean "toggles_blocks" : opt
}

```

/// html | div.result
//// define
`allow_underwater`：<samp>boolean</samp>

- If true, the explosion will affect blocks and entities under water.


////


//// define
`breaks_blocks`：<samp>boolean</samp>

- If true, the explosion will destroy blocks in the explosion radius.


////


//// define
`causes_fire`：<samp>boolean</samp>

- If true, blocks in the explosion radius will be set on fire.


////


//// define
`damage_scaling`：<samp>number</samp>

- A scale factor applied to the explosion's damage to entities. A value of 0 prevents the explosion from dealing any damage. Negative values cause the explosion to heal entities instead.


////


//// define
`destroy_affected_by_griefing`：<samp>boolean</samp>

- If true, whether the explosion breaks blocks is affected by the mob griefing game rule.


////


//// define
`fire_affected_by_griefing`：<samp>boolean</samp>

- If true, whether the explosion causes fire is affected by the mob griefing game rule.


////


//// define
`fuse_length`：<samp>array</samp>

- The range for the random amount of time the fuse will be lit before exploding, a negative value means the explosion will be immediate.


////

<div class="language-text highlight"><span class="filename"><code>fuse_length</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`fuse_length`：<samp>number</samp>

- The range for the random amount of time the fuse will be lit before exploding, a negative value means the explosion will be immediate.


////



//// define
`fuse_lit`：<samp>boolean</samp>

- If true, the fuse is already lit when this component is added to the entity.


////


//// define
`knockback_scaling`：<samp>number</samp>

- A scale factor applied to the knockback force caused by the explosion.


////


//// define
`max_resistance`：<samp>number</samp>

- A blocks explosion resistance will be capped at this value when an explosion occurs.


////


//// define
`negates_fall_damage`：<samp>boolean</samp>

- Defines whether the explosion should apply fall damage negation to Players above the point of collision.


////


//// define
`particle_effect`：<samp>string</samp>

- The name of the particle effect to use.


////


//// define
`power`：<samp>number</samp>

- The radius of the explosion in blocks and the amount of damage the explosion deals.


////


//// define
`sound_effect`：<samp>string</samp>

- The name of the sound effect played when the explosion triggers.


////


//// define
`toggles_blocks`：<samp>boolean</samp>

- If true, the explosion will toggle blocks in the explosion radius.


////


///

