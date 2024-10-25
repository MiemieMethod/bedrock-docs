# Cooldown

> 文档版本：1.21.50.25

Cool down time for a component. After you use an item it becomes unusable for the duration specified by the `cool down time` setting in this component.

## 架构

```mcschema
minecraft:cooldown:
{
  string "category" : opt
  number "duration" : opt
}

```

/// html | div.result
//// define
`category`：<samp>string</samp>

- The type of cool down for this item.


////


//// define
`duration`：<samp>number</samp>

- The duration of time this item will spend cooling down before becoming usable again.


////


///

