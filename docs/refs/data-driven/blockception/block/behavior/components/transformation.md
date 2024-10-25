# Transformation

> 文档版本：1.21.50.25

Supports rotation, scaling, and translation

## 架构

```mcschema
transformation:
{
  array "rotation" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
  array "scale" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
  array "translation" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
  array "scale_pivot" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
  array "rotation_pivot" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
}

```

/// html | div.result
//// define
`rotation`：<samp>array</samp>

- Amount in degrees the block should be rotated on each axis. "rotation" is specified as [x, y, z] using floating point values and must be axis aligned, otherwise the value will be rounded to the nearest axis-aligned value.


////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

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
`scale`：<samp>array</samp>

- Amount the block should be scaled along each axis. "scale" is specified as [x, y, z] using floating point values.


////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

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
`translation`：<samp>array</samp>

- Amount the block should be translated along each axis. "translation" is specified as [x, y, z] using floating point values.


////

<div class="language-text highlight"><span class="filename"><code>translation</code></span><pre id="__code_1"><span></span></pre></div>

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
`scale_pivot`：<samp>array</samp>

- Offset to the pivot point around which to apply the scale. "scale_pivot" is specified as [x, y, z] using floating point values.


////

<div class="language-text highlight"><span class="filename"><code>scale_pivot</code></span><pre id="__code_1"><span></span></pre></div>

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
`rotation_pivot`：<samp>array</samp>

- Offset to the pivot point around which to apply the rotation. "rotation_pivot" is specified as [x, y, z] using floating point values.


////

<div class="language-text highlight"><span class="filename"><code>rotation_pivot</code></span><pre id="__code_1"><span></span></pre></div>

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

