# Random Ticking

> 文档版本：1.21.0.24

[Experimental] Triggers the specified event randomly based on the random tick speed gamerule. The random tick speed determines how often blocks are updated.

## 架构

```mcschema
random_ticking:
{
   "on_tick" : opt
  string "condition" : opt
  string "event" : opt
  string "target" : opt
}

```

/// html | div.result
//// define
`on_tick`

- the event that will be triggered on random ticks.


////


//// define
`condition`：<samp>string</samp>

- A condition using Molang queries that results to true/false. If true on the random tick, the event will be triggered. If false on the random tick, the event will not be triggered.


////


//// define
`event`：<samp>string</samp>

- The event that will be triggered.


////


//// define
`target`：<samp>string</samp>

- The target of the event executed by the block


////


///

