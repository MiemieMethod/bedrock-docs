# Spell Effects

> 文档版本：1.21.0.24

Defines what mob effects to add and remove to the entity when adding this component.

## 架构

```mcschema
spell_effects:
{
  array "add_effects" : opt
  {
    string "<any array element>" : opt
    object "<any array element>" : opt
    {
      integer "amplifier" : opt
      boolean "ambient" : opt
      number "duration" : opt
      boolean "display_on_screen_animation" : opt
      string "effect" : opt
      boolean "visible" : opt
    }
  }
  array "remove_effects" : opt
  {
    ['string'] "<any array element>" : opt
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
`<any array element>`：<samp>string</samp>


/////


///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`amplifier`：<samp>integer</samp>

- The level of the effect, same as used in the /effect command (0 for level I, 1 for level II, etc). Defaults to 0. NOTE: Values can be negative but its not an intentional feature


//////


////// define
`ambient`：<samp>boolean</samp>

- Boolean value that should cause the particles emitted by the entity to be partially transparent. This does not work properly, resulting in this property having no effect. Defaults to false.


//////


////// define
`duration`：<samp>number</samp>

- The amount of time in seconds the effect should last. This allows for fractional numbers. For example, instant effects should be set to 0.05 seconds (one tick).


//////


////// define
`display_on_screen_animation`：<samp>boolean</samp>

- Boolean value. When set to true, applying this effect displays an animated graphic on-screen similar to the totem of undying effect. Obviously, this only works for players. Defaults to false.


//////


////// define
`effect`：<samp>string</samp>

- The string identifier of the status effect to add. These are the same as used in the /effect command.


//////


////// define
`visible`：<samp>boolean</samp>

- Boolean value. When set to true, the effect will be visible to the player. Defaults to true.


//////


/////



////


//// define
`remove_effects`：<samp>array</samp>

- List of identifiers of effects to be removed from this entity after adding this component.


////

<div class="language-text highlight"><span class="filename"><code>remove_effects</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>['string']</samp>

- identifier of the effect to be removed from this entity after adding this component.


/////


////


//// define
`remove_effects`：<samp>string</samp>

- List of identifiers of effects to be removed from this entity after adding this component.


////



///

