# minecraft:spell_effects

> 文档版本：1.21.0.24

Defines what mob effects to add and remove to the entity when adding this component.

## 架构

```mcschema
minecraft:spell_effects:
{
  array "add_effects" : opt
  {
    object "<any array element>" : opt
    {
      string "effect" : opt
      integer "duration" : opt
      integer "amplifier" : opt
      boolean "ambient" : opt
      boolean "visible" : opt
      boolean "display_on_screen_animation" : opt
    }
  }
  string "remove_effects" : opt
}

```

/// html | div.result
//// define
`add_effects`：<samp>array</samp>

- List of effects to add to this entity after adding this component.


////

<div class="language-text highlight"><span class="filename"><code>add_effects</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`effect`：<samp>string</samp>


//////


////// define
`duration`：<samp>integer</samp>


//////


////// define
`amplifier`：<samp>integer</samp>


//////


////// define
`ambient`：<samp>boolean</samp>


//////


////// define
`visible`：<samp>boolean</samp>


//////


////// define
`display_on_screen_animation`：<samp>boolean</samp>


//////


/////


////


//// define
`remove_effects`：<samp>string</samp>

- List of identifiers of effects to be removed from this entity after adding this component.


////


///

