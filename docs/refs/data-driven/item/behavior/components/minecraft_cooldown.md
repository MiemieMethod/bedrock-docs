# minecraft:cooldown

> 文档版本：1.21.0.24

After you use an item, all items specified with the same `cool down category` setting becomes unusable for the duration specified by the 'cool down time' setting in this component.

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

- The type of cool down for this item. All items with a cool down component with the same category are put on cool down when one is used.


////


//// define
`duration`：<samp>number</samp>

- The duration of time (in seconds) items with a matching category will spend cooling down before becoming usable again.


////


///

