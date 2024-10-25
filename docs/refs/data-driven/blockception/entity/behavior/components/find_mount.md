# Find Mount

> 文档版本：1.21.50.25

Allows the mob to look around for another mob to ride atop it.

## 架构

```mcschema
find_mount:
{
  priority "priority"
  boolean "avoid_water" : opt
  number "mount_distance" : opt
  integer "start_delay" : opt
  boolean "target_needed" : opt
  number "within_radius" : opt
  integer "max_failed_attempts" : opt
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
`avoid_water`：<samp>boolean</samp>

- If true, the mob will not go into water blocks when going towards a mount.


////


//// define
`mount_distance`：<samp>number</samp>

- This is the distance the mob needs to be, in blocks, from the desired mount to mount it. If the value is below 0, the mob will use its default attack distance


////


//// define
`start_delay`：<samp>integer</samp>

- Time the mob will wait before starting to move towards the mount.


////


//// define
`target_needed`：<samp>boolean</samp>

- If true, the mob will only look for a mount if it has a target.


////


//// define
`within_radius`：<samp>number</samp>

- Distance in blocks within which the mob will look for a mount.


////


//// define
`max_failed_attempts`：<samp>integer</samp>

- The number of failed attempts to make before this goal is no longer used.


////


///

