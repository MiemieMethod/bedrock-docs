# Repairable

> 文档版本：1.21.0.24

Repairable item component: how much damage can this item repair, what items can repair it.

## 架构

```mcschema
minecraft:repairable:
{
  array "repair_items" : opt
  {
    object "<any array element>" : opt
    {
      array "items" : opt
      {
        string "<any array element>" : opt
      }
      0 "repair_amount"
    }
  }
}

```

/// html | div.result
//// define
`repair_items`：<samp>array</samp>

- Repair item entries.


////

<div class="language-text highlight"><span class="filename"><code>repair_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- List of repair item entries.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`items`：<samp>array</samp>

- Items that can be used to repeair it


//////

<div class="language-text highlight"><span class="filename"><code>items</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- Item identifier


///////


//////


////// define
`repair_amount`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- Amount that can be repaired


//////

```mcschema
0:
string

```

////// html | div.result

//////


```mcschema
0:
number

```

////// html | div.result

//////




/////


////


///

