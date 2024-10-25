# Dyeable

> 文档版本：1.21.50.25

Enables custom items to be dyed in cauldrons.

## 架构

```mcschema
minecraft:dyeable:
{
  string "default_color" : opt
  array "default_color" : opt
  {
    integer "0..0" : opt
    integer "1..1" : opt
    integer "2..2" : opt
  }
}

```

/// html | div.result
//// define
`default_color`：<samp>string</samp>

- Color to use by default. If you do not want a default color you can leave the "default_color" off and the texture will be the same as if you did not have the component until it is dyed.


////


//// define
`default_color`：<samp>array</samp>

- Color to use by default. If you do not want a default color you can leave the "default_color" off and the texture will be the same as if you did not have the component until it is dyed.


////

<div class="language-text highlight"><span class="filename"><code>default_color</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>integer</samp>


/////


///// define
`1..1`：<samp>integer</samp>


/////


///// define
`2..2`：<samp>integer</samp>


/////


////



///

