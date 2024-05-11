# Item Controllable

> 文档版本：1.21.0.24

Efines what items can be used to control this entity while ridden.

## 架构

```mcschema
item_controllable:
{
  array "control_items" : opt
  {
    string "<any array element>" : opt
  }
  string "control_items" : opt
}

```

/// html | div.result
//// define
`control_items`：<samp>array</samp>

- List of items that can be used to control this entity.


////

<div class="language-text highlight"><span class="filename"><code>control_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>

- An item that can be used to control this entity.


/////


////


//// define
`control_items`：<samp>string</samp>

- List of items that can be used to control this entity.


////



///

