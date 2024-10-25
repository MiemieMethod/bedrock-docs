# Break Blocks

> 文档版本：1.21.50.25

Specifies the blocks that this entity can break as it moves around.

## 架构

```mcschema
break_blocks:
{
  array "breakable_blocks" : opt
  {
    item "<any array element>"
  }
}

```

/// html | div.result
//// define
`breakable_blocks`：<samp>array</samp>

- A list of the blocks that can be broken as this entity moves around.


////

<div class="language-text highlight"><span class="filename"><code>breakable_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>item</samp> {#assets.schemas-blockception.general.blocks_item.json}


/////

```mcschema
item:
string

```

///// html | div.result

/////



////


///

