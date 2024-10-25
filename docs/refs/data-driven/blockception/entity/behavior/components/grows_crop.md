# Grows Crop

> 文档版本：1.21.50.25

Could increase crop growth when entity walks over crop.

## 架构

```mcschema
grows_crop:
{
  number "chance" : opt
  integer "charges" : opt
}

```

/// html | div.result
//// define
`chance`：<samp>number</samp>

- Value between 0-1. Chance of success per tick.


////


//// define
`charges`：<samp>integer</samp>

- Number of charges.


////


///

