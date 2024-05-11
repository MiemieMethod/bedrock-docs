# Trading

> 文档版本：1.21.0.24

UNDOCUMENTED.

## 架构

```mcschema
trading:
{
  format_version "format_version"
  array "tiers" : opt
  {
    object "<any array element>" : opt
    {
      array "trades" : opt
      {
        object "<any array element>" : opt
        {
          array "gives" : opt
          {
            string "<any array element>" : opt
            object "<any array element>" : opt
            {
              string "item" : opt
              integer "quantity" : opt
              object "quantity" : opt
              {
                integer "min" : opt
                integer "max" : opt
              }
              array "functions" : opt
              {
                Functions "<any array element>"
              }
              array "choice" : opt
              {
                string "<any array element>" : opt
                object "<any array element>" : opt
                {
                  string "item" : opt
                  number "price_multiplier" : opt
                  array "functions" : opt
                  array "biomes" : opt
                  {
                    item "<any array element>"
                  }
                  integer "quantity" : opt
                  object "quantity" : opt
                  {
                    integer "min" : opt
                    integer "max" : opt
                  }
                }
              }
            }
          }
          array "wants" : opt
          {
            string "<any array element>" : opt
            object "<any array element>" : opt
            {
              string "item" : opt
              integer "quantity" : opt
              object "quantity" : opt
              {
                integer "min" : opt
                integer "max" : opt
              }
              number "price_multiplier" : opt
              array "functions" : opt
              array "choice" : opt
              {
                 "<any array element>" : opt
              }
            }
          }
          integer "trader_exp" : opt
          integer "max_uses" : opt
          integer "weight" : opt
          boolean "reward_exp" : opt
        }
      }
      integer "total_exp_required" : opt
      array "groups" : opt
      {
        object "<any array element>" : opt
        {
          integer "num_to_select" : opt
          array "trades" : opt
        }
      }
    }
  }
}

```

/// html | div.result
//// define
`format_version`：<samp>format_version</samp> {#assets.schemas-blockception.general.format_version.json}


////

```mcschema
format_version:
string

```

//// html | div.result

////



//// define
`tiers`：<samp>array</samp>

- A collection of tiers.


////

<div class="language-text highlight"><span class="filename"><code>tiers</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`trades`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>trades</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`gives`：<samp>array</samp>


////////

<div class="language-text highlight"><span class="filename"><code>gives</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>


/////////


///////// define
`<any array element>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`item`：<samp>string</samp>


//////////


////////// define
`quantity`：<samp>integer</samp>


//////////


////////// define
`quantity`：<samp>object</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>quantity</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`min`：<samp>integer</samp>


///////////


/////////// define
`max`：<samp>integer</samp>


///////////


//////////



////////// define
`functions`：<samp>array</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>functions</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>Functions</samp> {#assets.schemas-blockception.behavior.loot_tables.functions.json}


///////////

```mcschema
enchant_random_gear:
{
  string "function" : opt
  number "chance" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`chance`：<samp>number</samp>

- Takes a chance modifier to manipulate the algorithm. Note that a chance modifier of 1.0 doesn't mean a 100% chance that gear will become enchanted.


////////////


///////////




```mcschema
enchant_book_for_trading:
{
  string "function" : opt
  integer "base_cost" : opt
  integer "base_random_cost" : opt
  integer "per_level_random_cost" : opt
  integer "per_level_cost" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`base_cost`：<samp>integer</samp>

- UNDOCUMENTED.


////////////


//////////// define
`base_random_cost`：<samp>integer</samp>

- UNDOCUMENTED.


////////////


//////////// define
`per_level_random_cost`：<samp>integer</samp>

- UNDOCUMENTED.


////////////


//////////// define
`per_level_cost`：<samp>integer</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
enchant_randomly:
{
  string "function" : opt
  boolean "treasure" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`treasure`：<samp>boolean</samp>

- Supports the optional treasure boolean (true/false) to allow treasure enchantments to be toggled on and off.


////////////


///////////




```mcschema
enchant_with_levels:
{
  string "function" : opt
  integer "levels" : opt
  object "levels" : opt
  {
    integer "min" : opt
    integer "max" : opt
  }
  boolean "treasure" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`levels`：<samp>integer</samp>

- UNDOCUMENTED.


////////////


//////////// define
`levels`：<samp>object</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>levels</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`min`：<samp>integer</samp>


/////////////


///////////// define
`max`：<samp>integer</samp>


/////////////


////////////



//////////// define
`treasure`：<samp>boolean</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
exploration_map:
{
  string "function" : opt
  string "destination" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- Transforms a normal map into a treasure map that marks the location of hidden treasure.


////////////


//////////// define
`destination`：<samp>string</samp>

- The destination value defines what type of treasure map they receive.


////////////


///////////




```mcschema
fill_container:
{
  string "function" : opt
  string "loot_table" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`loot_table`：<samp>string</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
furnace_smelt:
{
  string "function" : opt
  array "conditions" : opt
  {
    conditions "<any array element>"
  }
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`conditions`：<samp>array</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>conditions</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`<any array element>`：<samp>conditions</samp> {#assets.schemas-blockception.behavior.loot_tables.conditions.json}


/////////////

```mcschema
entity_properties:
{
  string "condition" : opt
  string "entity" : opt
  object "properties" : opt
  {
    boolean "on_fire" : opt
    boolean "on_ground" : opt
  }
}

```

///////////// html | div.result
////////////// define
`condition`：<samp>string</samp>

- Returns true if the actor properties defined were executed.


//////////////


////////////// define
`entity`：<samp>string</samp>

- The entity to test. The value must be only `this`.


//////////////


////////////// define
`properties`：<samp>object</samp>

- The entity's properties. `on_fire`, `on_ground` is used for now.


//////////////

<div class="language-text highlight"><span class="filename"><code>properties</code></span><pre id="__code_1"><span></span></pre></div>

////////////// html | div.result
/////////////// define
`on_fire`：<samp>boolean</samp>

- Checks if the entity is on fire or not.


///////////////


/////////////// define
`on_ground`：<samp>boolean</samp>

- Checks if the entity is on the ground or not.


///////////////


//////////////


/////////////




```mcschema
has_mark_variant:
{
  string "condition" : opt
  integer "value" : opt
}

```

///////////// html | div.result
////////////// define
`condition`：<samp>string</samp>

- Returns the condition true if the actor's mark variant is matched to the value.


//////////////


////////////// define
`value`：<samp>integer</samp>

- Tests for the actor's mark variant (if it has one).


//////////////


/////////////




```mcschema
killed_by_player:
{
  string "condition" : opt
}

```

///////////// html | div.result
////////////// define
`condition`：<samp>string</samp>

- UNDOCUMENTED.


//////////////


/////////////




```mcschema
killed_by_player_or_pets:
{
  string "condition" : opt
}

```

///////////// html | div.result
////////////// define
`condition`：<samp>string</samp>

- UNDOCUMENTED.


//////////////


/////////////




```mcschema
random_chance:
{
  string "condition" : opt
  number "chance" : opt
  number "max_chance" : opt
}

```

///////////// html | div.result
////////////// define
`condition`：<samp>string</samp>

- UNDOCUMENTED.


//////////////


////////////// define
`chance`：<samp>number</samp>

- UNDOCUMENTED.


//////////////


////////////// define
`max_chance`：<samp>number</samp>

- The maximum random chance value allowed.


//////////////


/////////////




```mcschema
random_chance_with_looting:
{
  string "condition" : opt
  number "chance" : opt
  number "looting_multiplier" : opt
}

```

///////////// html | div.result
////////////// define
`condition`：<samp>string</samp>

- UNDOCUMENTED.


//////////////


////////////// define
`chance`：<samp>number</samp>

- The random chance of the value.


//////////////


////////////// define
`looting_multiplier`：<samp>number</samp>

- The multiplier for the chance if the target entity has the looting enchant that affects the actor.


//////////////


/////////////




```mcschema
random_difficulty_chance:
{
  string "condition" : opt
  number "default_chance" : opt
  number "easy" : opt
  number "hard" : opt
  number "normal" : opt
  number "peaceful" : opt
}

```

///////////// html | div.result
////////////// define
`condition`：<samp>string</samp>

- UNDOCUMENTED.


//////////////


////////////// define
`default_chance`：<samp>number</samp>

- The default random chance if the level difficulty is not assigned.


//////////////


////////////// define
`easy`：<samp>number</samp>

- The default random chance if the level difficulty is in easy. Omitting this field will set the value to `default_chance` field.


//////////////


////////////// define
`hard`：<samp>number</samp>

- The default random chance if the level difficulty is in hard. Omitting this field will set the value to `default_chance` field.


//////////////


////////////// define
`normal`：<samp>number</samp>

- The default random chance if the level difficulty is in normal. Omitting this field will set the value to `default_chance` field.


//////////////


////////////// define
`peaceful`：<samp>number</samp>

- The default random chance if the level difficulty is in peaceful. Omitting this field will set the value to `default_chance` field.


//////////////


/////////////




```mcschema
random_regional_difficulty_chance:
{
  string "condition" : opt
  number "default_chance" : opt
  number "max_chance" : opt
  number "easy" : opt
  number "hard" : opt
  number "normal" : opt
  number "peaceful" : opt
}

```

///////////// html | div.result
////////////// define
`condition`：<samp>string</samp>

- UNDOCUMENTED.


//////////////


////////////// define
`default_chance`：<samp>number</samp>

- The default random chance if the level difficulty is not assigned.


//////////////


////////////// define
`max_chance`：<samp>number</samp>

- UNDOCUMENTED.


//////////////


////////////// define
`easy`：<samp>number</samp>

- The default random chance if the level difficulty is in easy. Omitting this field will set the value to `default_chance` field.


//////////////


////////////// define
`hard`：<samp>number</samp>

- The default random chance if the level difficulty is in hard. Omitting this field will set the value to `default_chance` field.


//////////////


////////////// define
`normal`：<samp>number</samp>

- The default random chance if the level difficulty is in normal. Omitting this field will set the value to `default_chance` field.


//////////////


////////////// define
`peaceful`：<samp>number</samp>

- The default random chance if the level difficulty is in peaceful. Omitting this field will set the value to `default_chance` field.


//////////////


/////////////






////////////


///////////




```mcschema
looting_enchant:
{
  string "function" : opt
  object "count" : opt
  {
    integer "min" : opt
    integer "max" : opt
  }
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`count`：<samp>object</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>count</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`min`：<samp>integer</samp>


/////////////


///////////// define
`max`：<samp>integer</samp>


/////////////


////////////


///////////




```mcschema
random_aux_value:
{
  string "function" : opt
  object "values" : opt
  {
    integer "min" : opt
    integer "max" : opt
  }
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`values`：<samp>object</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>values</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`min`：<samp>integer</samp>

- UNDOCUMENTED.


/////////////


///////////// define
`max`：<samp>integer</samp>

- UNDOCUMENTED.


/////////////


////////////


///////////




```mcschema
random_block_state:
{
  string "function" : opt
  string "block_state" : opt
  object "values" : opt
  {
    integer "min" : opt
    integer "max" : opt
  }
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`block_state`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`values`：<samp>object</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>values</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`min`：<samp>integer</samp>


/////////////


///////////// define
`max`：<samp>integer</samp>


/////////////


////////////


///////////




```mcschema
set_actor_id:
{
  string "function" : opt
  string "id" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`id`：<samp>string</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
set_banner_details:
{
  string "function" : opt
  integer "type" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`type`：<samp>integer</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
set_book_contents:
{
  string "function" : opt
  string "author" : opt
  string "title" : opt
  array "pages" : opt
  {
    string "<any array element>" : opt
  }
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`author`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`title`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`pages`：<samp>array</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>pages</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`<any array element>`：<samp>string</samp>


/////////////


////////////


///////////




```mcschema
set_count:
{
  boolean "add" : opt
  string "function" : opt
  integer "count" : opt
  object "count" : opt
  {
    integer "min" : opt
    integer "max" : opt
  }
}

```

/////////// html | div.result
//////////// define
`add`：<samp>boolean</samp>

- UNDOCUMENTED.


////////////


//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`count`：<samp>integer</samp>

- UNDOCUMENTED.


////////////


//////////// define
`count`：<samp>object</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>count</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`min`：<samp>integer</samp>


/////////////


///////////// define
`max`：<samp>integer</samp>


/////////////


////////////



///////////




```mcschema
set_damage:
{
  boolean "add" : opt
  string "function" : opt
  number "damage" : opt
  object "damage" : opt
  {
    number "min" : opt
    number "max" : opt
  }
}

```

/////////// html | div.result
//////////// define
`add`：<samp>boolean</samp>

- UNDOCUMENTED.


////////////


//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`damage`：<samp>number</samp>

- UNDOCUMENTED.


////////////


//////////// define
`damage`：<samp>object</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>damage</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`min`：<samp>number</samp>

- UNDOCUMENTED.


/////////////


///////////// define
`max`：<samp>number</samp>

- UNDOCUMENTED.


/////////////


////////////



///////////




```mcschema
set_data:
{
  string "function" : opt
  integer "data" : opt
  object "data" : opt
  {
    integer "min" : opt
    integer "max" : opt
  }
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`data`：<samp>integer</samp>

- UNDOCUMENTED.


////////////


//////////// define
`data`：<samp>object</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>data</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`min`：<samp>integer</samp>

- UNDOCUMENTED.


/////////////


///////////// define
`max`：<samp>integer</samp>

- UNDOCUMENTED.


/////////////


////////////



///////////




```mcschema
set_data_from_color_index:
{
  string "function" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
trader_material_type:
{
  string "function" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
random_dye:
{
  string "function" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
set_lore:
{
  string "function" : opt
  array "lore" : opt
  {
    string "<any array element>" : opt
  }
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`lore`：<samp>array</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>lore</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`<any array element>`：<samp>string</samp>


/////////////


////////////


///////////




```mcschema
set_name:
{
  string "function" : opt
  string "name" : opt
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- UNDOCUMENTED.


////////////


//////////// define
`name`：<samp>string</samp>

- UNDOCUMENTED.


////////////


///////////




```mcschema
specific_enchants:
{
  string "function" : opt
  string "enchants" : opt
  object "enchants" : opt
  {
    string "id" : opt
    integer "level" : opt
    array "level" : opt
    {
      integer "0..0" : opt
      integer "1..1" : opt
    }
  }
  array "enchants" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
}

```

/////////// html | div.result
//////////// define
`function`：<samp>string</samp>

- Specific enchants.


////////////


//////////// define
`enchants`：<samp>string</samp>

- A enchanting specification.


////////////


//////////// define
`enchants`：<samp>object</samp>

- A enchanting specification.


////////////

<div class="language-text highlight"><span class="filename"><code>enchants</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`id`：<samp>string</samp>


/////////////


///////////// define
`level`：<samp>integer</samp>


/////////////


///////////// define
`level`：<samp>array</samp>


/////////////

<div class="language-text highlight"><span class="filename"><code>level</code></span><pre id="__code_1"><span></span></pre></div>

///////////// html | div.result
////////////// define
`0..0`：<samp>integer</samp>


//////////////


////////////// define
`1..1`：<samp>integer</samp>


//////////////


/////////////



////////////


//////////// define
`enchants`：<samp>array</samp>

- A enchanting specification.


////////////

<div class="language-text highlight"><span class="filename"><code>enchants</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`<any array element>`：<samp>object</samp>


/////////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////////// html | div.result

/////////////


////////////



///////////






//////////


////////// define
`choice`：<samp>array</samp>

- UNDOCUMENTED.


//////////

<div class="language-text highlight"><span class="filename"><code>choice</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>string</samp>


///////////


/////////// define
`<any array element>`：<samp>object</samp>


///////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result
//////////// define
`item`：<samp>string</samp>


////////////


//////////// define
`price_multiplier`：<samp>number</samp>


////////////


//////////// define
`functions`：<samp>array</samp>


////////////

<div class="language-text highlight"><span class="filename"><code>functions</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result

////////////


//////////// define
`biomes`：<samp>array</samp>

- UNDOCUMENTED.


////////////

<div class="language-text highlight"><span class="filename"><code>biomes</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`<any array element>`：<samp>item</samp> {#assets.schemas-blockception.general.biome_item.json}


/////////////

```mcschema
item:
string

```

///////////// html | div.result

/////////////



////////////


//////////// define
`quantity`：<samp>integer</samp>


////////////


//////////// define
`quantity`：<samp>object</samp>


////////////

<div class="language-text highlight"><span class="filename"><code>quantity</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`min`：<samp>integer</samp>


/////////////


///////////// define
`max`：<samp>integer</samp>


/////////////


////////////



///////////



//////////


/////////



////////


//////// define
`wants`：<samp>array</samp>


////////

<div class="language-text highlight"><span class="filename"><code>wants</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>


/////////


///////// define
`<any array element>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`item`：<samp>string</samp>


//////////


////////// define
`quantity`：<samp>integer</samp>


//////////


////////// define
`quantity`：<samp>object</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>quantity</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`min`：<samp>integer</samp>


///////////


/////////// define
`max`：<samp>integer</samp>


///////////


//////////



////////// define
`price_multiplier`：<samp>number</samp>

- UNDOCUMENTED.


//////////


////////// define
`functions`：<samp>array</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>functions</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


////////// define
`choice`：<samp>array</samp>

- UNDOCUMENTED.


//////////

<div class="language-text highlight"><span class="filename"><code>choice</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`


///////////


//////////


/////////



////////


//////// define
`trader_exp`：<samp>integer</samp>


////////


//////// define
`max_uses`：<samp>integer</samp>


////////


//////// define
`weight`：<samp>integer</samp>


////////


//////// define
`reward_exp`：<samp>boolean</samp>


////////


///////


//////


////// define
`total_exp_required`：<samp>integer</samp>


//////


////// define
`groups`：<samp>array</samp>

- A collection of groups.


//////

<div class="language-text highlight"><span class="filename"><code>groups</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`num_to_select`：<samp>integer</samp>


////////


//////// define
`trades`：<samp>array</samp>


////////

<div class="language-text highlight"><span class="filename"><code>trades</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////


//////


/////


////


///

