# Emitter Shape Box Component For 1.10.0

> 文档版本：1.21.0.24

UNDOCUMENTED.

## 架构

```mcschema
emitter_shape_box:
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
  array "half_dimensions" : opt
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
`half_dimensions`：<samp>array</samp>

- UNDOCUMENTED: half dimensions.


////

<div class="language-text highlight"><span class="filename"><code>half_dimensions</code></span><pre id="__code_1"><span></span></pre></div>

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

