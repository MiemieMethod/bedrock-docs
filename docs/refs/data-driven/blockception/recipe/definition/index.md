# Recipe

> 文档版本：1.21.50.25

Minecraft recipe

## 架构

```mcschema
recipe:
{
  string "format_version" : opt
  furnace "minecraft:recipe_furnace"
  container "minecraft:recipe_brewing_container"
  mix "minecraft:recipe_brewing_mix"
  shaped "minecraft:recipe_shaped"
  shapeless "minecraft:recipe_shapeless"
  recipe_smithing_transform "minecraft:recipe_smithing_transform"
}

```

/// html | div.result
//// define
`format_version`：<samp>string</samp>

- A version that tells minecraft what type of data format can be expected when reading this file.


////


//// define
`minecraft:recipe_furnace`：<samp>furnace</samp> {#assets.schemas-blockception.behavior.recipes.types.furnace.json}


////

```mcschema
furnace:
{
  definition "description"
  tags "tags"
  string "input" : opt
  string "output" : opt
  unlock "unlock"
}

```

//// html | div.result
///// define
`description`：<samp>definition</samp> {#assets.schemas-blockception.behavior.recipes.types.base types.definition.json}


/////

```mcschema
definition:
{
  string "identifier" : opt
}

```

///// html | div.result
////// define
`identifier`：<samp>string</samp>

- UNDOCUMENTED.


//////


/////



///// define
`tags`：<samp>tags</samp> {#assets.schemas-blockception.behavior.recipes.types.base types.tags.json}


/////

```mcschema
tags:
array
{
  string "<any array element>" : opt
}

```

///// html | div.result
////// define
`<any array element>`：<samp>string</samp>


//////


/////



///// define
`input`：<samp>string</samp>

- Items used as input for the furnace recipe.


/////


///// define
`output`：<samp>string</samp>

- Items used as output for the furnace recipe.


/////


///// define
`unlock`：<samp>unlock</samp> {#assets.schemas-blockception.behavior.recipes.types.base types.unlock.json}


/////

```mcschema
unlock:
{
  string "context" : opt
}

```

///// html | div.result
////// define
`context`：<samp>string</samp>

- The context of the achievement to unlock


//////


/////


```mcschema
unlock:
array
{
  object "<any array element>" : opt
  {
    string "item" : opt
    integer "data" : opt
  }
  object "<any array element>" : opt
  {
    string "tag" : opt
  }
}

```

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`item`：<samp>string</samp>

- The item to unlock


///////


/////// define
`data`：<samp>integer</samp>

- The data of the item to unlock


///////


//////


////// define
`<any array element>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`tag`：<samp>string</samp>

- The item to unlock


///////


//////



/////




////



//// define
`minecraft:recipe_brewing_container`：<samp>container</samp> {#assets.schemas-blockception.behavior.recipes.types.recipe_brewing_container.json}


////

```mcschema
container:
{
  definition "description"
  tags "tags"
  unlock "unlock"
  string "input" : opt
  string "output" : opt
  string "reagent" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[definition](#assets.schemas-blockception.behavior.recipes.types.base types.definition.json)</samp>


/////


///// define
`tags`：<samp>[tags](#assets.schemas-blockception.behavior.recipes.types.base types.tags.json)</samp>


/////


///// define
`unlock`：<samp>[unlock](#assets.schemas-blockception.behavior.recipes.types.base types.unlock.json)</samp>


/////


///// define
`input`：<samp>string</samp>

- Input potion used on the brewing stand.


/////


///// define
`output`：<samp>string</samp>

- Output potion from mixing the input potion with the reagent on the brewing stand.


/////


///// define
`reagent`：<samp>string</samp>

- Item used to mix with the input potion.


/////


////



//// define
`minecraft:recipe_brewing_mix`：<samp>mix</samp> {#assets.schemas-blockception.behavior.recipes.types.recipe_brewing_mix.json}


////

```mcschema
mix:
{
  definition "description"
  tags "tags"
  unlock "unlock"
  string "input" : opt
  string "output" : opt
  string "reagent" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[definition](#assets.schemas-blockception.behavior.recipes.types.base types.definition.json)</samp>


/////


///// define
`tags`：<samp>[tags](#assets.schemas-blockception.behavior.recipes.types.base types.tags.json)</samp>


/////


///// define
`unlock`：<samp>[unlock](#assets.schemas-blockception.behavior.recipes.types.base types.unlock.json)</samp>


/////


///// define
`input`：<samp>string</samp>

- Input potion used on the brewing stand.


/////


///// define
`output`：<samp>string</samp>

- Output potion from mixing the input potion with the reagent on the brewing stand.


/////


///// define
`reagent`：<samp>string</samp>

- Item used to mix with the input potion.


/////


////



//// define
`minecraft:recipe_shaped`：<samp>shaped</samp> {#assets.schemas-blockception.behavior.recipes.types.recipe_shaped.json}


////

```mcschema
shaped:
{
  definition "description"
  tags "tags"
  unlock "unlock"
  object "key" : opt
  {
    item "<any object property>"
  }
  string "group" : opt
  array "pattern" : opt
  {
    string "<any array element>" : opt
  }
  integer "priority" : opt
  item "result"
  array "result" : opt
  {
    item "<any array element>"
  }
  boolean "assume_symmetry" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[definition](#assets.schemas-blockception.behavior.recipes.types.base types.definition.json)</samp>


/////


///// define
`tags`：<samp>[tags](#assets.schemas-blockception.behavior.recipes.types.base types.tags.json)</samp>


/////


///// define
`unlock`：<samp>[unlock](#assets.schemas-blockception.behavior.recipes.types.base types.unlock.json)</samp>


/////


///// define
`key`：<samp>object</samp>

- Patten key character mapped to item names.


/////

<div class="language-text highlight"><span class="filename"><code>key</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any object property>`：<samp>item</samp> {#assets.schemas-blockception.behavior.recipes.types.base types.item.json}


//////

```mcschema
item:
string

```

////// html | div.result

//////


```mcschema
item:
{
  string "item" : opt
  integer "data" : opt
  integer "count" : opt
}

```

////// html | div.result
/////// define
`item`：<samp>string</samp>


///////


/////// define
`data`：<samp>integer</samp>


///////


/////// define
`count`：<samp>integer</samp>


///////


//////


```mcschema
item:
{
  string "tag" : opt
}

```

////// html | div.result
/////// define
`tag`：<samp>string</samp>

- The item to unlock


///////


//////




/////


///// define
`group`：<samp>string</samp>

- UNDOCUMENTED.


/////


///// define
`pattern`：<samp>array</samp>

- Characters that represent a pattern to be defined by keys.


/////

<div class="language-text highlight"><span class="filename"><code>pattern</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>string</samp>


//////


/////


///// define
`priority`：<samp>integer</samp>

- Item used as output for the furnace recipe.


/////


///// define
`result`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>

- When input items match the pattern then these items are the result.


/////


///// define
`result`：<samp>array</samp>

- When input items match the pattern then these items are the result.


/////

<div class="language-text highlight"><span class="filename"><code>result</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>


//////


/////



///// define
`assume_symmetry`：<samp>boolean</samp>

- Used to automatically assume a symmetrical recipe should return the same resultUsed to automatically assume a symmetrical recipe should return the same result


/////


////



//// define
`minecraft:recipe_shapeless`：<samp>shapeless</samp> {#assets.schemas-blockception.behavior.recipes.types.recipe_shapeless.json}


////

```mcschema
shapeless:
{
  definition "description"
  tags "tags"
  unlock "unlock"
  array "ingredients" : opt
  {
    item "<any array element>"
  }
  string "group" : opt
  integer "priority" : opt
  item "result"
  array "result" : opt
  {
    item "<any array element>"
  }
}

```

//// html | div.result
///// define
`description`：<samp>[definition](#assets.schemas-blockception.behavior.recipes.types.base types.definition.json)</samp>


/////


///// define
`tags`：<samp>[tags](#assets.schemas-blockception.behavior.recipes.types.base types.tags.json)</samp>


/////


///// define
`unlock`：<samp>[unlock](#assets.schemas-blockception.behavior.recipes.types.base types.unlock.json)</samp>


/////


///// define
`ingredients`：<samp>array</samp>

- Items used as input (without a shape) for the recipe.


/////

<div class="language-text highlight"><span class="filename"><code>ingredients</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>


//////


/////


///// define
`group`：<samp>string</samp>

- UNDOCUMENTED.


/////


///// define
`priority`：<samp>integer</samp>

- Item used as output for the furnace recipe.


/////


///// define
`result`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>

- When input items match the pattern then these items are the result.


/////


///// define
`result`：<samp>array</samp>

- When input items match the pattern then these items are the result.


/////

<div class="language-text highlight"><span class="filename"><code>result</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>


//////


/////



////



//// define
`minecraft:recipe_smithing_transform`：<samp>recipe_smithing_transform</samp> {#assets.schemas-blockception.behavior.recipes.types.recipe_smithing_transform.json}


////

```mcschema
recipe_smithing_transform:
{
  definition "description"
  tags "tags"
  unlock "unlock"
  item "base"
  array "base" : opt
  {
    item "<any array element>"
  }
  item "addition"
  array "addition" : opt
  {
    item "<any array element>"
  }
  item "result"
  array "result" : opt
  {
    item "<any array element>"
  }
}

```

//// html | div.result
///// define
`description`：<samp>[definition](#assets.schemas-blockception.behavior.recipes.types.base types.definition.json)</samp>


/////


///// define
`tags`：<samp>[tags](#assets.schemas-blockception.behavior.recipes.types.base types.tags.json)</samp>


/////


///// define
`unlock`：<samp>[unlock](#assets.schemas-blockception.behavior.recipes.types.base types.unlock.json)</samp>


/////


///// define
`base`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>

- Item used as base for the smithing recipe.


/////


///// define
`base`：<samp>array</samp>

- Item used as base for the smithing recipe.


/////

<div class="language-text highlight"><span class="filename"><code>base</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>


//////


/////



///// define
`addition`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>

- Item used as addition for the smithing recipe.


/////


///// define
`addition`：<samp>array</samp>

- Item used as addition for the smithing recipe.


/////

<div class="language-text highlight"><span class="filename"><code>addition</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>


//////


/////



///// define
`result`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>

- When input items match the pattern then these items are the result.


/////


///// define
`result`：<samp>array</samp>

- When input items match the pattern then these items are the result.


/////

<div class="language-text highlight"><span class="filename"><code>result</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[item](#assets.schemas-blockception.behavior.recipes.types.base types.item.json)</samp>


//////


/////



////



///

