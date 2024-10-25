# Entity Placer

> 文档版本：1.21.50.25

Entity placer item component. You can specifiy allowed blocks that the item is restricted to.

## 架构

```mcschema
minecraft:entity_placer:
{
  string "entity" : opt
  array "dispense_on" : opt
  {
     "<any array element>" : opt
  }
  array "use_on" : opt
  {
     "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`entity`：<samp>string</samp>

- The entity to be placed in the world.


////


//// define
`dispense_on`：<samp>array</samp>

- List of block descriptors that contain blocks that this item can be dispensed on. If left empty, all blocks will be allowed.


////

<div class="language-text highlight"><span class="filename"><code>dispense_on</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`

- Block that item can be dispensed on.


/////


////


//// define
`use_on`：<samp>array</samp>

- List of block descriptors that contain blocks that this item can be used on. If left empty, all blocks will be allowed.


////

<div class="language-text highlight"><span class="filename"><code>use_on</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`

- Block that item can be used on


/////


////


///

