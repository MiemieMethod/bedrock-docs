# Breedable

> 文档版本：1.21.0.24

Defines the way an entity can get into the `love` state.

## 架构

```mcschema
breedable:
{
  boolean "allow_sitting" : opt
  boolean "blend_attributes" : opt
  number "breed_cooldown" : opt
  array "breed_items" : opt
  {
    descriptor "<any array element>"
  }
  descriptor "breed_items"
  object "breeds_with" : opt
  {
    string "baby_type" : opt
    event_object "breed_event"
    string "mate_type" : opt
  }
  array "breeds_with" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  boolean "causes_pregnancy" : opt
  object "deny_parents_variant" : opt
  {
    number "chance" : opt
    integer "max_variant" : opt
    integer "min_variant" : opt
  }
  object "environment_requirements" : opt
  {
    array "blocks" : opt
    {
      reference "<any array element>"
    }
    reference "blocks"
    number "count" : opt
    number "radius" : opt
  }
  array "environment_requirements" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  number "extra_baby_chance" : opt
  filters "love_filters"
  object "mutation_factor" : opt
  {
    number "color" : opt
    number "extra_variant" : opt
    number "variant" : opt
  }
  string "mutation_strategy" : opt
  array "parent_centric_attribute_blending" : opt
  vector_of_2_items "random_extra_variant_mutation_interval"
  vector_of_2_items "random_variant_mutation_interval"
  boolean "inherit_tamed" : opt
  boolean "require_full_health" : opt
  boolean "require_tame" : opt
  string "transform_to_item" : opt
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
`breed_cooldown`：<samp>number</samp>

- Time in seconds before the Entity can breed again.


////


//// define
`breed_items`：<samp>array</samp>

- The list of items that can be used to get the entity into the `love` state.


////

<div class="language-text highlight"><span class="filename"><code>breed_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- An item that can be used to get the entity into the `love` state.


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
  }
  0 "tags"
  string "item_tag" : opt
}

```

///// html | div.result
////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


//////


////// define
`item`：<samp>object</samp>

- An object that describes an item.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////



////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- [UNDOCUMENTED] A Molang expression ran against item or block to match.


//////

```mcschema
0:
string

```

////// html | div.result

//////



////// define
`item_tag`：<samp>string</samp>

- [UNDOCUMENTED] A tag to lookup item or block by.


//////


/////


```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
    identifier "item"
    object "item" : opt
    {
    }
    0 "tags"
    string "item_tag" : opt
  }
}

```

///// html | div.result
////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


//////


////// define
`item`：<samp>object</samp>

- An object that describes an item.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////



/////




////


//// define
`breed_items`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>

- The list of items that can be used to get the entity into the `love` state.


////



//// define
`breeds_with`：<samp>object</samp>

- An entity definitions that this entity can breed with.


////

<div class="language-text highlight"><span class="filename"><code>breeds_with</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`baby_type`：<samp>string</samp>

- The entity definition of this entity's babies.


/////


///// define
`breed_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object_filters.json}

- Event to run when this entity breeds.


/////

```mcschema
event_object:
{
  string "event" : opt
  string "target" : opt
  filters "filters"
}

```

///// html | div.result
////// define
`event`：<samp>string</samp>

- The event to fire.


//////


////// define
`target`：<samp>string</samp>

- The target of the event.


//////


////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


/////



///// define
`mate_type`：<samp>string</samp>

- The entity definition of this entity's mate.


/////


////


//// define
`breeds_with`：<samp>array</samp>

- The list of entity definitions that this entity can breed with.


////

<div class="language-text highlight"><span class="filename"><code>breeds_with</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- An entity definitions that this entity can breed with.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

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

- The percentage chance of denying the parents` variant.


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
`environment_requirements`：<samp>object</samp>

- A nearby block requirements to get the entity into the `love` state.


////

<div class="language-text highlight"><span class="filename"><code>environment_requirements</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`blocks`：<samp>array</samp>

- The block types required nearby for the entity to breed.


/////

<div class="language-text highlight"><span class="filename"><code>blocks</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>reference</samp> {#assets.schemas-blockception.general.block.reference.json}

- A block type required nearby for the entity to breed.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



```mcschema
reference:
{
  identifier "name"
  object "states" : opt
  {
    ['boolean', 'integer', 'string'] "\w*:?\w+" : opt
  }
  0 "tags"
}

```

////// html | div.result
/////// define
`name`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


///////


/////// define
`states`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`\w*:?\w+`：<samp>['boolean', 'integer', 'string']</samp>

- The key of property is the name of the block state/property, the value must be the same as the block properties accepted values.


////////


///////


/////// define
`tags`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- A condition using Molang queries that results to true/false that can be used to query for blocks with certain tags.


///////


//////




/////


///// define
`blocks`：<samp>[reference](#assets.schemas-blockception.general.block.reference.json)</samp>

- A block type required nearby for the entity to breed.


/////



///// define
`count`：<samp>number</samp>

- The number of the required block types nearby for the entity to breed.


/////


///// define
`radius`：<samp>number</samp>

- How many blocks radius from the mob's center to search in for the required blocks. Bounded between 0 and 16.


/////


////


//// define
`environment_requirements`：<samp>array</samp>

- The list of nearby block requirements to get the entity into the `love` state.


////

<div class="language-text highlight"><span class="filename"><code>environment_requirements</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A nearby block requirements to get the entity into the `love` state.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////



//// define
`extra_baby_chance`：<samp>number</samp>

- Chance that up to 16 babies will spawn between 0.0 and 1.0, where 1.0 is 100%.


////


//// define
`love_filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The filters to run when attempting to fall in love.


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

////


//// define
`random_extra_variant_mutation_interval`：<samp>vector_of_2_items</samp> {#assets.schemas-blockception.general.vectors.number2.json}

- Range used to determine random extra variant.


////

```mcschema
vector_of_2_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The X component.


/////


///// define
`1..1`：<samp>number</samp>

- The Y component.


/////


////



//// define
`random_variant_mutation_interval`：<samp>[vector_of_2_items](#assets.schemas-blockception.general.vectors.number2.json)</samp>

- Range used to determine random variant.


////


//// define
`inherit_tamed`：<samp>boolean</samp>

- If true, the babies will be automatically tamed if its parents are.


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
`transform_to_item`：<samp>string</samp>

- The feed item used will transform to this item upon successful interaction. Format: itemName:auxValue


////


///

