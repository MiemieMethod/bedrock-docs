# Music File

> 文档版本：1.21.0.24

The definition file of music of the resourcepack.

## 架构

```mcschema
json:
{
  object "<any object property>" : opt
  {
    string "event_name" : opt
    integer "min_delay" : opt
    integer "max_delay" : opt
  }
}

```

/// html | div.result
//// define
`<any object property>`：<samp>object</samp>

- A music definition.


////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`event_name`：<samp>string</samp>

- The name of the minecraft music event.


/////


///// define
`min_delay`：<samp>integer</samp>

- UNDOCUMENTED: Minimum delay.


/////


///// define
`max_delay`：<samp>integer</samp>

- UNDOCUMENTED: Maximum delay.


/////


////


///

