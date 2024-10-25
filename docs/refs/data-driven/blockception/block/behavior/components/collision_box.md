# Collision Box

> 文档版本：1.21.50.25

This component can be specified as a Boolean. If this component is omitted, the default value for this component is true, which will give your block the default values for its parameters (a collision box the size/shape of a regular block).

## 架构

```mcschema
collision_box:
boolean

```

/// html | div.result

///


```mcschema
collision_box:
{
  array "origin" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
  array "size" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
}

```

/// html | div.result
//// define
`origin`：<samp>array</samp>

- Minimal position of the bounds of the collision box. origin is specified as [x, y, z] and must be in the range (-8, 0, -8) to (8, 16, 8), inclusive.


////

<div class="language-text highlight"><span class="filename"><code>origin</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


///// define
`2..2`：<samp>number</samp>


/////


////


//// define
`size`：<samp>array</samp>

- Size of each side of the collision box. Size is specified as [x, y, z]. origin + size must be in the range (-8, 0, -8) to (8, 16, 8), inclusive.


////

<div class="language-text highlight"><span class="filename"><code>size</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


///// define
`2..2`：<samp>number</samp>


/////


////


///


