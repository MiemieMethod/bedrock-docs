# 未命名

> 文档版本：1.21.0.24

Makes your block into a custom crafting table which enables the crafting table UI and the ability to craft recipes.

## 架构

```mcschema
minecraft:crafting_table:
{
  array "crafting_tags" : opt
  string "table_name" : opt
}

```

/// html | div.result
//// define
`crafting_tags`：<samp>array</samp>

- Defines the tags recipes should define to be crafted on this table. Limited to 64 tags. Each tag is limited to 64 characters.


////

<div class="language-text highlight"><span class="filename"><code>crafting_tags</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////


//// define
`table_name`：<samp>string</samp>

- Specifies the language file key that maps to what text will be displayed in the UI of this table. If the string given can not be resolved as a loc string, the raw string given will be displayed. If this field is omitted, the name displayed will default to the name specified in the "display_name" component. If this block has no "display_name" component, the name displayed will default to the name of the block.


////


///

