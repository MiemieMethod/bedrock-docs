# Projectile

> 文档版本：1.21.50.25

Allows the entity to be a thrown entity.

## 架构

```mcschema
projectile:
{
  integer "anchor" : opt
  number "angle_offset" : opt
  boolean "catch_fire" : opt
  boolean "crit_particle_on_hurt" : opt
  boolean "destroy_on_hurt" : opt
  string "filter" : opt
  boolean "fire_affected_by_griefing" : opt
  number "gravity" : opt
  boolean "hit_nearest_passenger" : opt
  array "ignored_entities" : opt
  {
    string "<any array element>" : opt
  }
  sound_event "hit_ground_sound"
  sound_event "hit_sound"
  boolean "homing" : opt
  number "inertia" : opt
  boolean "is_dangerous" : opt
  boolean "knockback" : opt
  boolean "lightning" : opt
  number "liquid_inertia" : opt
  boolean "multiple_targets" : opt
   "mob_effect" : opt
  vector_of_3_items "offset"
  number "on_fire_time" : opt
  object "on_hit" : opt
  {
    object "arrow_effect" : opt
    {
      boolean "apply_effect_to_blocking_targets" : opt
    }
    boolean "catch_fire" : opt
    object "definition_event" : opt
    {
      boolean "affect_projectile" : opt
      boolean "affect_shooter" : opt
      boolean "affect_splash_area" : opt
      boolean "affect_target" : opt
      event "event_trigger"
      number "splash_area" : opt
    }
    boolean "douse_fire" : opt
    object "freeze_on_hit" : opt
    {
      string "shape" : opt
      boolean "snap_to_block" : opt
      number "size" : opt
    }
    object "grant_xp" : opt
    {
      number "minXP" : opt
      number "maxXP" : opt
    }
    object "hurt_owner" : opt
    {
      number "owner_damage" : opt
      boolean "knockback" : opt
      boolean "ignite" : opt
    }
    boolean "ignite" : opt
    object "impact_damage" : opt
    {
      boolean "catch_fire" : opt
      boolean "channeling" : opt
      number "damage" : opt
      array "damage" : opt
      {
        number "0..0" : opt
        number "1..1" : opt
      }
      boolean "destroy_on_hit" : opt
      boolean "destroy_on_hit_requires_damage" : opt
      string "filter" : opt
      boolean "knockback" : opt
      integer "max_critical_damage" : opt
      integer "min_critical_damage" : opt
      number "power_multiplier" : opt
      boolean "semi_random_diff_damage" : opt
      boolean "set_last_hurt_requires_damage" : opt
      boolean "should_bounce" : opt
    }
    object "mob_effect" : opt
    {
      boolean "ambient" : opt
      integer "amplifier" : opt
      integer "duration" : opt
      integer "durationeasy" : opt
      integer "durationhard" : opt
      integer "durationnormal" : opt
      effect "effect"
      boolean "visible" : opt
    }
    number "on_fire_time" : opt
    object "particle_on_hit" : opt
    {
      number "num_particles" : opt
      boolean "on_entity_hit" : opt
      boolean "on_other_hit" : opt
      string "particle_type" : opt
    }
    integer "potion_effect" : opt
    object "remove_on_hit" : opt
    {
    }
    object "spawn_aoe_cloud" : opt
    {
      boolean "affect_owner" : opt
      vector_of_3_items "color"
      integer "duration" : opt
      string "particle" : opt
      integer "potion" : opt
      number "radius" : opt
      number "radius_on_use" : opt
      integer "reapplication_delay" : opt
    }
    object "spawn_chance" : opt
    {
      integer "first_spawn_count" : opt
      number "first_spawn_percent_chance" : opt
      number "first_spawn_chance" : opt
      number "second_spawn_chance" : opt
      integer "second_spawn_count" : opt
      boolean "spawn_baby" : opt
      string "spawn_definition" : opt
    }
    object "stick_in_ground" : opt
    {
    }
    boolean "teleport_owner" : opt
    object "thrown_potion_effect" : opt
    {
    }
  }
  string "particle" : opt
  integer "potion_effect" : opt
  number "power" : opt
  number "reflect_immunity" : opt
  boolean "reflect_on_hurt" : opt
  boolean "semi_random_diff_damage" : opt
  sound_event "shoot_sound"
  boolean "shoot_target" : opt
  boolean "should_bounce" : opt
  boolean "splash_potion" : opt
  number "splash_range" : opt
  boolean "stop_on_hurt" : opt
  number "uncertainty_base" : opt
  number "uncertainty_multiplier" : opt
}

```

/// html | div.result
//// define
`anchor`：<samp>integer</samp>

- Allows you to choose an anchor point for where the projectile is fired from. 0 = Original point, 1 = EyeHeight, and 2 = Middle or body height.


////


//// define
`angle_offset`：<samp>number</samp>

- Alters the angle at which a projectile is vertically shot. Many splash potions in the game use this to offset their angles by -20 degrees.


////


//// define
`catch_fire`：<samp>boolean</samp>

- If true, the entity hit will be set on fire.


////


//// define
`crit_particle_on_hurt`：<samp>boolean</samp>

- If true, when a projectile deals damage, whether or not to spawn in the critical damage particles.


////


//// define
`destroy_on_hurt`：<samp>boolean</samp>

- When this projectile deals damage, whether or not to immediately destroy this projectile.


////


//// define
`filter`：<samp>string</samp>

- Entity Definitions defined here can't be hurt by the projectile.


////


//// define
`fire_affected_by_griefing`：<samp>boolean</samp>

- If true, whether the projectile causes fire is affected by the mob griefing game rule.


////


//// define
`gravity`：<samp>number</samp>

- The gravity applied to this entity when thrown. When this actor is not on the ground, subtracts this amount from the actors change in vertical position every tick. The higher the value, the faster the entity falls.


////


//// define
`hit_nearest_passenger`：<samp>boolean</samp>

- If true, when hitting a vehicle, and there's at least one passenger in the vehicle, the damage will be dealt to the passenger closest to the projectile impact point. If there are no passengers, this setting does nothing.


////


//// define
`ignored_entities`：<samp>array</samp>

- [EXPERIMENTAL] An array of strings defining the types of entities that this entity does not collide with.


////

<div class="language-text highlight"><span class="filename"><code>ignored_entities</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`hit_ground_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound that plays when the projectile hits the ground.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`hit_sound`：<samp>[sound_event](#assets.schemas-blockception.general.sound_event.json)</samp>

- The sound that plays when the projectile hits something.


////


//// define
`homing`：<samp>boolean</samp>

- If true, the projectile homes in to the nearest entity.


////


//// define
`inertia`：<samp>number</samp>

- The fraction of the projectile's speed maintained every frame while traveling in air.


////


//// define
`is_dangerous`：<samp>boolean</samp>

- If true, the projectile will be treated as dangerous to the players.


////


//// define
`knockback`：<samp>boolean</samp>

- If true, the projectile will knock back the entity it hits.


////


//// define
`lightning`：<samp>boolean</samp>

- If true, the entity hit will be struck by lightning.


////


//// define
`liquid_inertia`：<samp>number</samp>

- The fraction of the projectile's speed maintained every frame while traveling in water.


////


//// define
`multiple_targets`：<samp>boolean</samp>

- If true, the projectile can hit multiple entities per flight.


////


//// define
`mob_effect`

- SEE on_hit/mob_effect.


////


//// define
`offset`：<samp>vector_of_3_items</samp> {#assets.schemas-blockception.general.vectors.number3.json}

- The offset from the entity's anchor where the projectile will spawn.


////

```mcschema
vector_of_3_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
  number "2..2" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The X component.


/////


///// define
`1..1`：<samp>number</samp>

- The Y component.


/////


///// define
`2..2`：<samp>number</samp>

- The Z component.


/////


////



//// define
`on_fire_time`：<samp>number</samp>

- Time in seconds that the entity hit will be on fire for.


////


//// define
`on_hit`：<samp>object</samp>

- Defines the behaviors that may execute on a projectile's hit, including impact damage, impact effect, and stuck in ground. See more on these parameters below.


////

<div class="language-text highlight"><span class="filename"><code>on_hit</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`arrow_effect`：<samp>object</samp>

- The target receives a mob effect. See the table below for all arrow_effect parameters.


/////

<div class="language-text highlight"><span class="filename"><code>arrow_effect</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`apply_effect_to_blocking_targets`：<samp>boolean</samp>

- If true, the effect will be applied to blocking targets.


//////


/////


///// define
`catch_fire`：<samp>boolean</samp>

- Determines if the struck object is set on fire.


/////


///// define
`definition_event`：<samp>object</samp>

- The event that is triggered on a hit. See the table below for all definition event parameters.


/////

<div class="language-text highlight"><span class="filename"><code>definition_event</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`affect_projectile`：<samp>boolean</samp>

- The projectile that will be affected by this event.


//////


////// define
`affect_shooter`：<samp>boolean</samp>

- The shooter that will be affected by this event.


//////


////// define
`affect_splash_area`：<samp>boolean</samp>

- All entities in the splash area will be affected by this event.


//////


////// define
`affect_target`：<samp>boolean</samp>

- The target will be affected by this event.


//////


////// define
`event_trigger`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- The event triggered. Also has an option filters parameter to limit affected targets.


//////

```mcschema
event:
string

```

////// html | div.result

//////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

////// html | div.result
/////// define
`event`：<samp>string</samp>

- The event to fire.


///////


/////// define
`target`：<samp>string</samp>

- The target of the event.


///////


//////




////// define
`splash_area`：<samp>number</samp>

- The splash area that will be affected.


//////


/////


///// define
`douse_fire`：<samp>boolean</samp>

- If the target is on fire, then douse the fire.


/////


///// define
`freeze_on_hit`：<samp>object</samp>

- An area of entities that is frozen to block on hits. Has shape of either sphere or cube, snap_to_block boolean ,and size decimal properties.


/////

<div class="language-text highlight"><span class="filename"><code>freeze_on_hit</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`shape`：<samp>string</samp>

- The shape of the area that is frozen.


//////


////// define
`snap_to_block`：<samp>boolean</samp>

- If true, the area will snap to the nearest block.


//////


////// define
`size`：<samp>number</samp>

- The size of the area that is frozen.


//////


/////


///// define
`grant_xp`：<samp>object</samp>

- Grants XP on hit. Has minXP for minimum XP granted, maxXp for maximum, or simply flat xp properties.


/////

<div class="language-text highlight"><span class="filename"><code>grant_xp</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minXP`：<samp>number</samp>

- The minimum XP granted.


//////


////// define
`maxXP`：<samp>number</samp>

- The maximum XP granted.


//////


/////


///// define
`hurt_owner`：<samp>object</samp>

- Determines if the owner of the entity is hurt on hit. Contains decimal owner_damage, knockback boolean, and ignite boolean.


/////

<div class="language-text highlight"><span class="filename"><code>hurt_owner</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`owner_damage`：<samp>number</samp>

- The amount of damage the owner will take.


//////


////// define
`knockback`：<samp>boolean</samp>

- If true, the owner will be knocked back.


//////


////// define
`ignite`：<samp>boolean</samp>

- If true, the owner will be set on fire.


//////


/////


///// define
`ignite`：<samp>boolean</samp>

- Determines if a fire may be started on a flammable target.


/////


///// define
`impact_damage`：<samp>object</samp>

- Defines the damage that an entity may receive on being hit by this projectile. See the table below for all impact_damage parameters.


/////

<div class="language-text highlight"><span class="filename"><code>impact_damage</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`catch_fire`：<samp>boolean</samp>

- Determines if the struck object is set on fire.


//////


////// define
`channeling`：<samp>boolean</samp>

- Whether lightning can be channeled through hte weapon.


//////


////// define
`damage`：<samp>number</samp>

- The damage dealt on impact.


//////


////// define
`damage`：<samp>array</samp>

- The damage dealt on impact.


//////

<div class="language-text highlight"><span class="filename"><code>damage</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>number</samp>


///////


/////// define
`1..1`：<samp>number</samp>


///////


//////



////// define
`destroy_on_hit`：<samp>boolean</samp>

- Projectile is removed on hit.


//////


////// define
`destroy_on_hit_requires_damage`：<samp>boolean</samp>

- If true, then the hit must cause damage to destroy the projectile.


//////


////// define
`filter`：<samp>string</samp>

- The identifier of an entity that can be hit.


//////


////// define
`knockback`：<samp>boolean</samp>

- If true, the projectile will knock back the entity it hits.


//////


////// define
`max_critical_damage`：<samp>integer</samp>

- Maximum critical damage.


//////


////// define
`min_critical_damage`：<samp>integer</samp>

- Minimum critical damage.


//////


////// define
`power_multiplier`：<samp>number</samp>

- How much the base damage is multiplied.


//////


////// define
`semi_random_diff_damage`：<samp>boolean</samp>

- If true, damage will be randomized based on damage and speed.


//////


////// define
`set_last_hurt_requires_damage`：<samp>boolean</samp>

- If true, then the hit must cause damage to update the last hurt property.


//////


////// define
`should_bounce`：<samp>boolean</samp>

- If true, the projectile will bounce


//////


/////


///// define
`mob_effect`：<samp>object</samp>

- The target receives a mob effect. See the table below for all mob_effect parameters.


/////

<div class="language-text highlight"><span class="filename"><code>mob_effect</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`ambient`：<samp>boolean</samp>

- If true, a mob will spawn that is not hostile, like the bat entity in Minecraft.


//////


////// define
`amplifier`：<samp>integer</samp>

- The multiplier of the amplification of this effect.


//////


////// define
`duration`：<samp>integer</samp>

- The effect's duration.


//////


////// define
`durationeasy`：<samp>integer</samp>

- The effect's duration on easy mode.


//////


////// define
`durationhard`：<samp>integer</samp>

- The effect's duration on hard mode.


//////


////// define
`durationnormal`：<samp>integer</samp>

- The effect's duration on normal mode.


//////


////// define
`effect`：<samp>effect</samp> {#assets.schemas-blockception.general.vanilla.effect.json}

- The identifier of the mob entity to affect.


//////

```mcschema
effect:
string

```

////// html | div.result

//////



////// define
`visible`：<samp>boolean</samp>

- Does the entity's look change.


//////


/////


///// define
`on_fire_time`：<samp>number</samp>

- The amount of time a target will remain on fire.


/////


///// define
`particle_on_hit`：<samp>object</samp>

- The particles that spawn on hit. See the table below for all particle_on_hit parameters.


/////

<div class="language-text highlight"><span class="filename"><code>particle_on_hit</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`num_particles`：<samp>number</samp>

- The number of particles to spawn.


//////


////// define
`on_entity_hit`：<samp>boolean</samp>

- If true, spawns particles on an entity hit.


//////


////// define
`on_other_hit`：<samp>boolean</samp>

- If true, spawns particles on any other hit.


//////


////// define
`particle_type`：<samp>string</samp>

- The id of the particle to spawn on hit.


//////


/////


///// define
`potion_effect`：<samp>integer</samp>

- Defines the effect the arrow will apply to the entity it hits.


/////


///// define
`remove_on_hit`：<samp>object</samp>

- Removes the projectile.


/////

<div class="language-text highlight"><span class="filename"><code>remove_on_hit</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`spawn_aoe_cloud`：<samp>object</samp>

- Potion spawns an area of effect cloud. See the table below for all spawn_aoe_cloud parameters.


/////

<div class="language-text highlight"><span class="filename"><code>spawn_aoe_cloud</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`affect_owner`：<samp>boolean</samp>

- Determines if the projectile shooter is affected.


//////


////// define
`color`：<samp>[vector_of_3_items](#assets.schemas-blockception.general.vectors.number3.json)</samp>

- Particle color defined by three rgb values.


//////


////// define
`duration`：<samp>integer</samp>

- How long the particle emits.


//////


////// define
`particle`：<samp>string</samp>

- The particle emitter.


//////


////// define
`potion`：<samp>integer</samp>

- The id of the potion.


//////


////// define
`radius`：<samp>number</samp>

- Defines the affected area.


//////


////// define
`radius_on_use`：<samp>number</samp>

- Defines the affected area when potion is used.


//////


////// define
`reapplication_delay`：<samp>integer</samp>

- Delay before the potion can affect the area again.


//////


/////


///// define
`spawn_chance`：<samp>object</samp>

- Contains information on the chance of spawning an entity on hit. See parameters below.


/////

<div class="language-text highlight"><span class="filename"><code>spawn_chance</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`first_spawn_count`：<samp>integer</samp>

- The amount of new entities spawned.


//////


////// define
`first_spawn_percent_chance`：<samp>number</samp>

- The chance that a spawn occurs when a projectile hits the entity.


//////


////// define
`first_spawn_chance`：<samp>number</samp>

- The chance that a first spawn occurs when a projectile hits the entity.


//////


////// define
`second_spawn_chance`：<samp>number</samp>

- The chance that a second spawn occurs when a projectile hits the entity.


//////


////// define
`second_spawn_count`：<samp>integer</samp>

- The amount of new entities spawned in teh second spawn.


//////


////// define
`spawn_baby`：<samp>boolean</samp>

- Determines if a baby spawns.


//////


////// define
`spawn_definition`：<samp>string</samp>

- The entity that will spawn.


//////


/////


///// define
`stick_in_ground`：<samp>object</samp>

- Decides if the object sticks in ground and contains shake_time integer parameter to determine how long it will shake.


/////

<div class="language-text highlight"><span class="filename"><code>stick_in_ground</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`teleport_owner`：<samp>boolean</samp>

- Determines if the owner is transported on hit.


/////


///// define
`thrown_potion_effect`：<samp>object</samp>

- Creates a splash area for effects caused by a thrown potion.


/////

<div class="language-text highlight"><span class="filename"><code>thrown_potion_effect</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////


//// define
`particle`：<samp>string</samp>

- Particle to use upon collision.


////


//// define
`potion_effect`：<samp>integer</samp>

- Defines the effect the arrow will apply to the entity it hits.


////


//// define
`power`：<samp>number</samp>

- Determines the velocity of the projectile.


////


//// define
`reflect_immunity`：<samp>number</samp>

- During the specified time, in seconds, the projectile cannot be reflected by hitting it


////


//// define
`reflect_on_hurt`：<samp>boolean</samp>

- If true, this entity will be reflected back when hit.


////


//// define
`semi_random_diff_damage`：<samp>boolean</samp>

- If true, damage will be randomized based on damage and speed.


////


//// define
`shoot_sound`：<samp>[sound_event](#assets.schemas-blockception.general.sound_event.json)</samp>

- The sound that plays when the projectile is shot.


////


//// define
`shoot_target`：<samp>boolean</samp>

- If true, the projectile will be shot towards the target of the entity firing it.


////


//// define
`should_bounce`：<samp>boolean</samp>

- If true, the projectile will bounce upon hit.


////


//// define
`splash_potion`：<samp>boolean</samp>

- If true, the projectile will be treated like a splash potion.


////


//// define
`splash_range`：<samp>number</samp>

- Radius in blocks of the 'splash' effect.


////


//// define
`stop_on_hurt`：<samp>boolean</samp>

- Determines if the projectile stops when the target is hurt.


////


//// define
`uncertainty_base`：<samp>number</samp>

- The base accuracy. Accuracy is determined by the formula uncertaintyBase - difficultyLevel * uncertaintyMultiplier.


////


//// define
`uncertainty_multiplier`：<samp>number</samp>

- Determines how much difficulty affects accuracy. Accuracy is determined by the formula uncertaintyBase - difficultyLevel * uncertaintyMultiplier.


////


///

