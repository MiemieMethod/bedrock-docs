# Group Size

> 文档版本：1.21.50.25

Keeps track of entity group size in the given radius.

## 架构

```mcschema
group_size:
{
  filters "filters"
  number "radius" : opt
}

```

/// html | div.result
//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions that must be satisfied for other entities to be counted towards group size.


////


//// define
`radius`：<samp>number</samp>

- Radius from center of entity.


////


///

