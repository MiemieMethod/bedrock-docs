# minecraft:breedable

> 文档版本：1.21.0.24

Defines the way an entity can get into the 'love' state.

## 架构

```mcschema
minecraft:breedable:
{
  boolean "allow_sitting" : opt
  boolean "blend_attributes" : opt
  number "blend_cooldown" : opt
  array "breeds_with" : opt
  {
    object "<any array element>" : opt
    {
      string "baby_type" : opt
      definition_trigger_no_condition "breed_event"
      string "mate_type" : opt
    }
  }
  boolean "causes_pregnancy" : opt
  object "deny_parents_variant" : opt
  {
    number "chance" : opt
    integer "max_variant" : opt
    integer "min_variant" : opt
  }
  array "environment_requirements" : opt
  {
    object "<any array element>" : opt
    {
      block_descriptor "blocks"
      integer "count" : opt
      integer "radius" : opt
    }
  }
  number "extra_baby_chance" : opt
  boolean "inherit_tamed" : opt
  entity_filters "love_filters"
  object "mutation_factor" : opt
  {
    number "color" : opt
    number "extra_variant" : opt
    number "variant" : opt
  }
  string "mutation_strategy" : opt
  array "parent_centric_attribute_blending" : opt
  {
    string "<any array element>" : opt
  }
  array "random_extra_variant_mutation_interval" : opt
  {
    integer "<any array element>" : opt
  }
  array "random_variant_mutation_interval" : opt
  {
    integer "<any array element>" : opt
  }
  boolean "require_full_health" : opt
  boolean "require_tame" : opt
  item_descriptor "transform_to_item"
}

```

/// html | div.result
//// define
`allow_sitting`：<samp>boolean</samp>

- If true, entities can breed while sitting.


////


//// define
`blend_attributes`：<samp>boolean</samp>

- If true, the entities will blend their attributes in the offspring after they breed.


////


//// define
`blend_cooldown`：<samp>number</samp>

- Time in seconds before the Entity can breed again.


////


//// define
`breeds_with`：<samp>array</samp>

- The list of entity definitions that this entity can breed with.


////

<div class="language-text highlight"><span class="filename"><code>breeds_with</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`baby_type`：<samp>string</samp>

- The entity definition of this entity's babies.


//////


////// define
`breed_event`：<samp>definition_trigger_no_condition</samp> {#assets.schemas.common.definition.definition_trigger_no_condition.json}

- Event to run when this entity breeds.


//////

```mcschema
definition_trigger_no_condition:
string

```

////// html | div.result

//////


```mcschema
definition_trigger_no_condition:
{
  string "event" : opt
  string "target" : opt
}

```

////// html | div.result
/////// define
`event`：<samp>string</samp>


///////


/////// define
`target`：<samp>string</samp>


///////


//////




////// define
`mate_type`：<samp>string</samp>

- The entity definition of this entity's mate.


//////


/////


////


//// define
`causes_pregnancy`：<samp>boolean</samp>

- If true, the entity will become pregnant instead of spawning a baby.


////


//// define
`deny_parents_variant`：<samp>object</samp>

- Determines how likely the baby of parents with the same variant will deny that variant and take a random variant within the given range instead.


////

<div class="language-text highlight"><span class="filename"><code>deny_parents_variant</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`chance`：<samp>number</samp>

- The percentage chance of denying the parents' variant.


/////


///// define
`max_variant`：<samp>integer</samp>

- The inclusive maximum of the variant range.


/////


///// define
`min_variant`：<samp>integer</samp>

- The inclusive minimum of the variant range.


/////


////


//// define
`environment_requirements`：<samp>array</samp>

- The list of nearby block requirements to get the entity into the 'love' state.


////

<div class="language-text highlight"><span class="filename"><code>environment_requirements</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`blocks`：<samp>block_descriptor</samp> {#assets.schemas.common.definition.block.block_descriptor.json}

- The block types required nearby for the entity to breed.


//////

```mcschema
block_descriptor:
{
  string "name" : opt
  object "states" : opt
  {
    string "<any object property>" : opt
    integer "<any object property>" : opt
  }
  expression_node_string "tags"
}

```

////// html | div.result
/////// define
`name`：<samp>string</samp>


///////


/////// define
`states`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>


////////


//////// define
`<any object property>`：<samp>integer</samp>


////////



///////


/////// define
`tags`：<samp>expression_node_string</samp> {#assets.schemas.common.molang.expression_node_string.json}


///////

```mcschema
expression_node_string:
string

```

/////// html | div.result

///////



//////


```mcschema
block_descriptor:
string

```

////// html | div.result

//////




////// define
`count`：<samp>integer</samp>

- The number of the required block types nearby for the entity to breed.


//////


////// define
`radius`：<samp>integer</samp>

- How many blocks radius from the mob's center to search in for the required blocks. Bounded between 0 and 16.


//////


/////


////


//// define
`extra_baby_chance`：<samp>number</samp>

- Chance that up to 16 babies will spawn between 0.0 and 1.0, where 1.0 is 100%.


////


//// define
`inherit_tamed`：<samp>boolean</samp>

- If true, the babies will be automatically tamed if its parents are.


////


//// define
`love_filters`：<samp>entity_filters</samp> {#assets.schemas.common.definition.entity.entity_filters.json}

- The filters to run when attempting to fall in love.


////

```mcschema
entity_filters:
{
  sub_filter "any_of"
  sub_filter "all_of"
  sub_filter "none_of"
}

```

//// html | div.result
///// define
`any_of`：<samp>sub_filter</samp> {#assets.schemas.common.definition.entity.sub_filter.json}


/////

```mcschema
sub_filter:
{
  string "test" : opt
  string "subject" : opt
  string "operator" : opt
  string "value" : opt
}

```

///// html | div.result
////// define
`test`：<samp>string</samp>


//////


////// define
`subject`：<samp>string</samp>


//////


////// define
`operator`：<samp>string</samp>


//////


////// define
`value`：<samp>string</samp>


//////


/////


```mcschema
sub_filter:
array
{
  object "<any array element>" : opt
  {
    string "test" : opt
    string "subject" : opt
    string "operator" : opt
    string "value" : opt
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
`test`：<samp>string</samp>


///////


/////// define
`subject`：<samp>string</samp>


///////


/////// define
`operator`：<samp>string</samp>


///////


/////// define
`value`：<samp>string</samp>


///////


//////


/////




///// define
`all_of`：<samp>[sub_filter](#assets.schemas.common.definition.entity.sub_filter.json)</samp>


/////


///// define
`none_of`：<samp>[sub_filter](#assets.schemas.common.definition.entity.sub_filter.json)</samp>


/////


////



//// define
`mutation_factor`：<samp>object</samp>

- Determines how likely the babies are to NOT inherit one of their parent's variances. Values are between 0.0 and 1.0, with a higher number meaning more likely to mutate.


////

<div class="language-text highlight"><span class="filename"><code>mutation_factor</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`color`：<samp>number</samp>

- The percentage chance of a mutation on the entity's color.


/////


///// define
`extra_variant`：<samp>number</samp>

- The percentage chance of a mutation on the entity's extra variant type.


/////


///// define
`variant`：<samp>number</samp>

- The percentage chance of a mutation on the entity's variant type.


/////


////


//// define
`mutation_strategy`：<samp>string</samp>

- Strategy used for mutating variants and extra variants for offspring. Current valid alternatives are 'random' and 'none'.


////


//// define
`parent_centric_attribute_blending`：<samp>array</samp>

- [EXPERIMENTAL] List of attributes that should benefit from parent centric attribute blending. For example, horses blend their health, movement, and jump_strength in their offspring.


////

<div class="language-text highlight"><span class="filename"><code>parent_centric_attribute_blending</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`random_extra_variant_mutation_interval`：<samp>array</samp>

- Range used to determine random extra variant.


////

<div class="language-text highlight"><span class="filename"><code>random_extra_variant_mutation_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>integer</samp>


/////


////


//// define
`random_variant_mutation_interval`：<samp>array</samp>

- Range used to determine random variant.


////

<div class="language-text highlight"><span class="filename"><code>random_variant_mutation_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>integer</samp>


/////


////


//// define
`require_full_health`：<samp>boolean</samp>

- If true, the entity needs to be at full health before it can breed.


////


//// define
`require_tame`：<samp>boolean</samp>

- If true, the entities need to be tamed first before they can breed.


////


//// define
`transform_to_item`：<samp>item_descriptor</samp> {#assets.schemas.common.definition.item.item_descriptor.json}

- The breed item used will transform to this item upon successful interaction. Format: itemName:auxValue


////

```mcschema
item_descriptor:
string

```

//// html | div.result

////


```mcschema
item_descriptor:
{
  string "<any object property>" : opt
}

```

//// html | div.result
///// define
`<any object property>`：<samp>string</samp>


/////


////




///

