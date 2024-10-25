# Emitter Shape Disc Component For 1.10.0

> 文档版本：1.21.50.25

UNDOCUMENTED.

## 架构

```mcschema
emitter_shape_disc:
{
  string "direction" : opt
  array "direction" : opt
  {
    0 "0..0"
    0 "1..1"
    0 "2..2"
  }
  0 "radius"
  array "offset" : opt
  {
    0 "0..0"
    0 "1..1"
    0 "2..2"
  }
  string "plane_normal" : opt
  array "plane_normal" : opt
  {
    0 "0..0"
    0 "1..1"
    0 "2..2"
  }
  boolean "surface_only" : opt
}

```

/// html | div.result
//// define
`direction`：<samp>string</samp>

- UNDOCUMENTED: direction.


////


//// define
`direction`：<samp>array</samp>

- UNDOCUMENTED: direction.


////

<div class="language-text highlight"><span class="filename"><code>direction</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}


/////

```mcschema
0:
string

```

///// html | div.result

/////


```mcschema
0:
number

```

///// html | div.result

/////




///// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


/////


///// define
`2..2`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


/////


////



//// define
`radius`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: radius.


////


//// define
`offset`：<samp>array</samp>

- UNDOCUMENTED.


////

<div class="language-text highlight"><span class="filename"><code>offset</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED.


/////


///// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED.


/////


///// define
`2..2`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED.


/////


////


//// define
`plane_normal`：<samp>string</samp>

- Specifies the normal of the disc plane, the disc will be perpendicular to this direction.


////


//// define
`plane_normal`：<samp>array</samp>

- Specifies the normal of the disc plane, the disc will be perpendicular to this direction.


////

<div class="language-text highlight"><span class="filename"><code>plane_normal</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED.


/////


///// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED.


/////


///// define
`2..2`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED.


/////


////



//// define
`surface_only`：<samp>boolean</samp>

- UNDOCUMENTED: surface only.


////


///

