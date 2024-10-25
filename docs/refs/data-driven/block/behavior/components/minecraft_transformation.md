# 未命名

> 文档版本：1.21.0.24

The block's translation around the center of the cube in degrees. The rotation order is [x, y, z]. Angles need to be in multiples of 90.

## 架构

```mcschema
minecraft:transformation:
{
  array "translation" : opt
  {
    number "<any array element>" : opt
  }
  array "scale" : opt
  {
    number "<any array element>" : opt
  }
  array "scale_pivot" : opt
  {
    number "<any array element>" : opt
  }
  array "rotation" : opt
  {
    number "<any array element>" : opt
  }
  array "rotation_pivot" : opt
  {
    number "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`translation`：<samp>array</samp>

- Amount the block should be translated along each axis. "Translation" is specified as [x, y, z] using floating point values.


////

<div class="language-text highlight"><span class="filename"><code>translation</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


//// define
`scale`：<samp>array</samp>

- Amount the block should be scaled along each axis. "Scale" is specified as [x, y, z] using floating point values.


////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


//// define
`scale_pivot`：<samp>array</samp>

- Offset to the pivot point around which to apply the scale. "scale_pivot" is specified as [x, y, z] using floating point values.


////

<div class="language-text highlight"><span class="filename"><code>scale_pivot</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


//// define
`rotation`：<samp>array</samp>

- Amount in degrees the block should be rotated on each axis. "rotation" is specified as [x, y, z] using floating point values and must be axis aligned, otherwise the value will be rounded to the nearest axis-aligned value.


////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


//// define
`rotation_pivot`：<samp>array</samp>

- Offset to the pivot point around which to apply the rotation. "rotation_pivot" is specified as [x, y, z] using floating point values.


////

<div class="language-text highlight"><span class="filename"><code>rotation_pivot</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


///

