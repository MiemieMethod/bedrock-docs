# Tick

> 文档版本：1.21.50.25

Describes the component that will trigger an even at a regular interval between two values.

## 架构

```mcschema
tick:
{
  boolean "looping" : opt
  array "interval_range" : opt
}

```

/// html | div.result
//// define
`looping`：<samp>boolean</samp>

- Does the event loop.


////


//// define
`interval_range`：<samp>array</samp>

- The Range between which the component will trigger his event.


////

<div class="language-text highlight"><span class="filename"><code>interval_range</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////


///

