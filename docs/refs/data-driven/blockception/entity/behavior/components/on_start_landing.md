# On Start Landing

> 文档版本：1.21.50.25

Only usable by the Ender Dragon. Adds a trigger to call when this entity lands.

## 架构

```mcschema
trigger:
string

```

/// html | div.result

///


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

/// html | div.result
//// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions for this trigger to execute.


////


//// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


////

```mcschema
subject:
string

```

//// html | div.result

////



///


```mcschema
trigger:
array
{
  object "<any array element>" : opt
  {
    string "event" : opt
    filters "filters"
    subject "target"
  }
}

```

/// html | div.result
//// define
`<any array element>`：<samp>object</samp>


////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////


///



