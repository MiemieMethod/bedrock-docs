# 未命名

> 文档版本：1.21.50.25



## 架构

```mcschema
items:
{
  string "format_version" : opt
  object "minecraft:item" : opt
  {
    object "description" : opt
    {
      identifier "identifier"
      string "category" : opt
    }
    object "components" : opt
    {
      string "minecraft:icon" : opt
      string "minecraft:render_offsets" : opt
    }
  }
}

```

/// html | div.result
//// define
`format_version`：<samp>string</samp>

- A version that tells minecraft what type of data format can be expected when reading this file.


////


//// define
`minecraft:item`：<samp>object</samp>

- A resource pack definition of an item.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:item</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- The description of an item.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.item.identifier.json}

- The item identifier.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`category`：<samp>string</samp>

- The category this item belongs in.


//////


/////


///// define
`components`：<samp>object</samp>

- The components that describe this item.


/////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minecraft:icon`：<samp>string</samp>

- The texture defined in `textures/item_texture.json`


//////


////// define
`minecraft:render_offsets`：<samp>string</samp>

- The render offset used for the item.


//////


/////


////


///







```mcschema
items:
{
  format_version "format_version"
}

```

/// html | div.result
//// define
`format_version`：<samp>format_version</samp> {#assets.schemas-blockception.general.format_version.json}


////

```mcschema
format_version:
string

```

//// html | div.result

////



///


