# Skeleton Horse Trap

> 文档版本：1.21.0.24

Allows Equine mobs to be Horse Traps and be triggered like them, spawning a lightning bolt and a bunch of horses when a player is nearby. Can only be used by Horses, Mules, Donkeys and Skeleton Horses.

## 架构

```mcschema
skeleton_horse_trap:
{
  priority "priority"
  number "duration" : opt
  number "within_radius" : opt
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
`duration`：<samp>number</samp>

- Amount of time in seconds the trap exists. After this amount of time is elapsed, the trap is removed from the world if it hasn't been activated


////


//// define
`within_radius`：<samp>number</samp>

- Distance in blocks that the player has to be within to trigger the horse trap.


////


///

