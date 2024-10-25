# Tick

> 文档版本：1.21.50.25

Mcfunction that are to be called per game tick (20 times per second).

## 架构

```mcschema
tick:
{
  array "values" : opt
  {
    string "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`values`：<samp>array</samp>

- The collection of function path to execute.


////

<div class="language-text highlight"><span class="filename"><code>values</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>

- The path to the function.


/////


////


///

