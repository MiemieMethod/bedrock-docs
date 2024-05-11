# Equipment

> 文档版本：1.21.0.24

Sets the equipment table to use for the entity.

## 架构

```mcschema
equipment:
{
  array "slot_drop_chance" : opt
  {
    object "<any array element>" : opt
    {
      number "drop_chance" : opt
      string "slot" : opt
    }
  }
  identifier "table"
}

```

/// html | div.result
//// define
`slot_drop_chance`：<samp>array</samp>

- A list of slots with the chance to drop an equipped item from that slot.


////

<div class="language-text highlight"><span class="filename"><code>slot_drop_chance</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A slots with the chance to drop an equipped item from that slot.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`drop_chance`：<samp>number</samp>

- The chance that the item in this slot will drop.


//////


////// define
`slot`：<samp>string</samp>

- The slot in which the item will drop from.


//////


/////


////


//// define
`table`：<samp>identifier</samp> {#assets.schemas-blockception.general.loot_table.identifier.json}

- The file path to the equipment table, relative to the behavior pack's root.


////

```mcschema
identifier:
string

```

//// html | div.result

////



///

