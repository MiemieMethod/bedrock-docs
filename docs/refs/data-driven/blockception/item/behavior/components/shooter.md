# Shooter

> 文档版本：1.21.0.24

Shooter Item Component.

## 架构

```mcschema
minecraft:shooter:
{
  array "ammunition" : opt
  {
    object "<any array element>" : opt
    {
      string "item" : opt
      boolean "use_offhand" : opt
      boolean "search_inventory" : opt
      boolean "use_in_creative" : opt
    }
  }
  boolean "charge_on_draw" : opt
  number "max_draw_duration" : opt
  boolean "scale_power_by_draw_duration" : opt
}

```

/// html | div.result
//// define
`ammunition`：<samp>array</samp>

- Ammunition.


////

<div class="language-text highlight"><span class="filename"><code>ammunition</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- Ammunition definition


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`item`：<samp>string</samp>

- Item identifier


//////


////// define
`use_offhand`：<samp>boolean</samp>

- If ammo can be in offhand


//////


////// define
`search_inventory`：<samp>boolean</samp>

- If ammo can be stored in the inventory


//////


////// define
`use_in_creative`：<samp>boolean</samp>

- If it needs ammo to be used in creative


//////


/////


////


//// define
`charge_on_draw`：<samp>boolean</samp>

- Charge on draw? Default is set to false.


////


//// define
`max_draw_duration`：<samp>number</samp>

- Draw Duration. Default is set to 0.


////


//// define
`scale_power_by_draw_duration`：<samp>boolean</samp>

- Scale power by draw duration? Default is set to false.


////


///

