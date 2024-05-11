# minecraft:annotation.break_door

> 文档版本：1.21.0.24

Allows the actor to break doors assuming that that flags set up for the component to use in navigation.

## 架构

```mcschema
break_door:
{
  number "break_time" : opt
  string "min_difficulty" : opt
}

```

/// html | div.result
//// define
`break_time`：<samp>number</samp>

- The time in seconds required to break through doors.


////


//// define
`min_difficulty`：<samp>string</samp>

- The minimum difficulty that the world must be on for this entity to break doors.


////


///

