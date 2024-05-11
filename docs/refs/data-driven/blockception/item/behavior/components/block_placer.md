# Block Placer

> 文档版本：1.21.0.24

Planter item component. planter items are items that can be planted.

## 架构

```mcschema
minecraft:block_placer:
{
  string "block" : opt
  array "use_on" : opt
  {
    object "<any array element>" : opt
    {
      0 "tags"
    }
  }
}

```

/// html | div.result
//// define
`block`：<samp>string</samp>

- Set the placement block name for the planter item.


////


//// define
`use_on`：<samp>array</samp>

- List of block descriptors that contain blocks that this item can be used on. If left empty, all blocks will be allowed.


////

<div class="language-text highlight"><span class="filename"><code>use_on</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A block descriptor that allows to be placed.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- Tags.


//////

```mcschema
0:
string

```

////// html | div.result

//////



/////


////


///

