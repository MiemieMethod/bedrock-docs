# Map Color

> 文档版本：1.21.0.24

Sets the color of the block when rendered to a map. The color is represented as a hex value in the format "#RRGGBB". May also be expressed as an array of [R, G, B] from 0 to 255. If this component is omitted, the block will not show up on the map.

## 架构

```mcschema
map_color:
string

```

/// html | div.result

///


```mcschema
map_color:
array
{
  integer "0..0" : opt
  integer "1..1" : opt
  integer "2..2" : opt
}

```

/// html | div.result
//// define
`0..0`：<samp>integer</samp>


////


//// define
`1..1`：<samp>integer</samp>


////


//// define
`2..2`：<samp>integer</samp>


////


///


