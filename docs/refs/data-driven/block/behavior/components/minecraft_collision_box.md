# 未命名

> 文档版本：1.21.0.24

Defines the area of the block that collides with entities. If set to true, default values are used. If set to false, the block's collision with entities is disabled. If this component is omitted, default values are used.

## 架构

```mcschema
minecraft:collision_box:
boolean

```

/// html | div.result

///


```mcschema
minecraft:collision_box:
{
  array "origin" : opt
  {
    number "<any array element>" : opt
  }
  array "size" : opt
  {
    number "<any array element>" : opt
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
`<any array element>`：<samp>number</samp>


/////


////


//// define
`size`：<samp>array</samp>

- Size of each side of the collision box. Size is specified as [x, y, z]. origin + size must be in the range (-8, 0, -8) to (8, 16, 8), inclusive.


////

<div class="language-text highlight"><span class="filename"><code>size</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


///

