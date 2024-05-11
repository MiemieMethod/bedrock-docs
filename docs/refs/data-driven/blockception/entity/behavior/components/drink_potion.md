# Drink Potion

> 文档版本：1.21.0.24

Allows the mob to drink potions based on specified environment conditions.

## 架构

```mcschema
drink_potion:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
   "speed_modifier" : opt
  array "potions" : opt
  {
    object "<any array element>" : opt
    {
      integer "id" : opt
      number "chance" : opt
      filters "filters"
    }
  }
}

```

/// html | div.result
//// define
`priority`：<samp>priority</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.priority.json}


////

```mcschema
priority:
integer

```

//// html | div.result

////



//// define
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

////



//// define
`speed_modifier`

- Movement speed modifier of the mob when using this AI Goal.


////


//// define
`potions`：<samp>array</samp>

- A list of potions that this entity can drink.


////

<div class="language-text highlight"><span class="filename"><code>potions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A potions that this entity can drink.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`id`：<samp>integer</samp>

- The registry ID of the potion to use.


//////


////// define
`chance`：<samp>number</samp>

- The percent chance (from 0.0 to 1.0) of this potion being selected when searching for a potion to use.


//////


////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The filters to use when determining if this potion can be selected.


//////


/////


////


///

