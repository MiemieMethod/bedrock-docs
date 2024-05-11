# Random Ticking

> 文档版本：1.21.0.24

[Experimental] Describes the component that will trigger an even at a regular interval between two values.

## 架构

```mcschema
random_ticking:
{
  string "on_tick" : opt
  boolean "looping" : opt
  array "range" : opt
}

```

/// html | div.result
//// define
`on_tick`：<samp>string</samp>

- Describes the component that will trigger an even at a regular interval between two values.


////


//// define
`looping`：<samp>boolean</samp>

- Does the event loop.


////


//// define
`range`：<samp>array</samp>

- The Range between which the component will trigger his event.


////

<div class="language-text highlight"><span class="filename"><code>range</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////


///

