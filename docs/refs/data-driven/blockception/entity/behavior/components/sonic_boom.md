# Sonic Boom

> 文档版本：1.21.0.24

[EXPERIMENTAL BEHAVIOR] Plays the provided sounds and activates the `SONIC BOOM` actor flag during the specified duration

## 架构

```mcschema
sonic_boom:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "attack_cooldown" : opt
  number "attack_damage" : opt
  number "attack_range_horizontal" : opt
  number "attack_range_vertical" : opt
  sound_event "attack_sound"
  sound_event "charge_sound"
  number "duration" : opt
  number "duration_until_attack_sound" : opt
  number "knockback_height_cap" : opt
  number "knockback_horizontal_strength" : opt
  number "knockback_vertical_strength" : opt
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
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

////



//// define
`attack_cooldown`：<samp>number</samp>

- Cooldown in seconds required after using this attack until the entity can use sonic boom again.


////


//// define
`attack_damage`：<samp>number</samp>

- Attack damage of the sonic boom.


////


//// define
`attack_range_horizontal`：<samp>number</samp>

- Horizontal range (in blocks) at which the sonic boom can damage the target.


////


//// define
`attack_range_vertical`：<samp>number</samp>

- Vertical range (in blocks) at which the sonic boom can damage the target.


////


//// define
`attack_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Sound event for the attack.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`charge_sound`：<samp>[sound_event](#assets.schemas-blockception.general.sound_event.json)</samp>

- Sound event for the charge up.


////


//// define
`duration`：<samp>number</samp>

- Goal duration in seconds.


////


//// define
`duration_until_attack_sound`：<samp>number</samp>

- Duration in seconds until the attack sound is played.


////


//// define
`knockback_height_cap`：<samp>number</samp>

- Height cap of the attack knockback's vertical delta.


////


//// define
`knockback_horizontal_strength`：<samp>number</samp>

- Horizontal strength of the attack's knockback applied to the attack target.


////


//// define
`knockback_vertical_strength`：<samp>number</samp>

- Vertical strength of the attack's knockback applied to the attack target.


////


///

