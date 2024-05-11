# Digger

> 文档版本：1.21.0.24

Digger item. Component put on items that dig.

## 架构

```mcschema
minecraft:digger:
{
  boolean "use_efficiency" : opt
  array "destroy_speeds" : opt
  {
    object "<any array element>" : opt
    {
      number "speed" : opt
      string "block" : opt
      object "block" : opt
      {
        string "tags" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`use_efficiency`：<samp>boolean</samp>

- Toggles if the item will be used efficiently.


////


//// define
`destroy_speeds`：<samp>array</samp>

- Destroy speed per block.


////

<div class="language-text highlight"><span class="filename"><code>destroy_speeds</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- Destroy speed per block.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`speed`：<samp>number</samp>


//////


////// define
`block`：<samp>string</samp>

- The block identifier.


//////


////// define
`block`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>block</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`tags`：<samp>string</samp>

- The block tags.


///////


//////



/////


////


///

