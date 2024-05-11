# 未命名

> 文档版本：1.21.0.24

用于配置自定义方块可存在于哪些方块的上面。
会生效于玩家右键放置方块时；以及已存在的方块下方的方块发生改变时。

## 架构

```mcschema
netease:may_place_on:
{
  array "block" : opt
  {
    string "<any array element>" : opt
  }
  array "block_state" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  boolean "spawn_resources" : opt
}

```

/// html | div.result
//// define
`block`：<samp>array</samp>

- 方块identifier的列表。这些方块的所有方块状态都可放置。


////

<div class="language-text highlight"><span class="filename"><code>block</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`block_state`：<samp>array</samp>

- 方块状态的列表。
每个元素只对应一个特定的方块状态，如果方块有多个种类的状态，需要考虑排列组合的所有情况
最终可在上面放置的方块是block字段与block_state字段的并集


////

<div class="language-text highlight"><span class="filename"><code>block_state</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////


//// define
`spawn_resources`：<samp>boolean</samp>

- 已存在的方块因下方的方块发生改变而被破坏时，是否生成掉落物。


////


///

