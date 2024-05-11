# Genetics

> 文档版本：1.21.0.24

Defines the way a mob's genes and alleles are passed on to it's offspring, and how those traits manifest in the child. Compatible parent genes are crossed together, the alleles are handed down from the parents to the child, and any matching genetic variants fire off JSON events to modify the child and express the traits.

## 架构

```mcschema
genetics:
{
  number "mutation_rate" : opt
  array "genes" : opt
  {
    object "<any array element>" : opt
    {
      integer "allele_range" : opt
      object "allele_range" : opt
      {
        integer "range_min" : opt
        integer "range_max" : opt
      }
      array "genetic_variants" : opt
      {
        object "<any array element>" : opt
        {
          event_object "birth_event"
           "both_allele" : opt
          integer "either_allele" : opt
          integer "hidden_allele" : opt
           "main_allele" : opt
          number "mutation_rate" : opt
        }
      }
      string "name" : opt
    }
  }
}

```

/// html | div.result
//// define
`mutation_rate`：<samp>number</samp>

- Chance that an allele will be replaced with a random one instead of the parent's allele during birth.


////


//// define
`genes`：<samp>array</samp>

- The list of genes that this entity has and will cross with a partner during breeding.


////

<div class="language-text highlight"><span class="filename"><code>genes</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- The list of genes that this entity has and will cross with a partner during breeding.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`allele_range`：<samp>integer</samp>

- The range of positive integer allele values for this gene. Spawned mobs will have a random number in this range assigned to them.


//////


////// define
`allele_range`：<samp>object</samp>

- The range of positive integer allele values for this gene. Spawned mobs will have a random number in this range assigned to them.


//////

<div class="language-text highlight"><span class="filename"><code>allele_range</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`range_min`：<samp>integer</samp>

- Lower bound of the vaues.


///////


/////// define
`range_max`：<samp>integer</samp>

- Upper bound of the vaues.


///////


//////



////// define
`genetic_variants`：<samp>array</samp>

- The list of genetic variants for this gene. These check for particular allele combinations and fire events when all of them are satisfied.


//////

<div class="language-text highlight"><span class="filename"><code>genetic_variants</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- The genetic variant for this gene. These check for particular allele combinations and fire events when all of them are satisfied.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`birth_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to run when this mob is created and matches the above allele conditions.


////////

```mcschema
event_object:
{
  filters "filters"
  string "event" : opt
  string "target" : opt
}

```

//////// html | div.result
///////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


/////////


///////// define
`event`：<samp>string</samp>

- The event to fire.


/////////


///////// define
`target`：<samp>string</samp>

- The target of the event.


/////////


////////



//////// define
`both_allele`

- If this value is non-negative, compare both the mob's main and hidden alleles with this value for a match with both. Can also be a range of integers.


////////


//////// define
`either_allele`：<samp>integer</samp>

- If this value is non-negative, compare both the mob's main and hidden alleles with this value for a match with either. Can also be a range of integers.


////////


//////// define
`hidden_allele`：<samp>integer</samp>

- If this value is non-negative, compare the mob's hidden allele with this value for a match. Can also be a range of integers.


////////


//////// define
`main_allele`

- If this value is non-negative, compare the mob's main allele with this value for a match. Can also be a range of integers.


////////


//////// define
`mutation_rate`：<samp>number</samp>

- If this value is non-negative, overrides the chance for this gene that an allele will be replaced with a random one instead of the parent's allele during birth. Non-negative values greater than 1 will be the same as the value 1.


////////


///////


//////


////// define
`name`：<samp>string</samp>

- The name of the gene.


//////


/////


////


///

