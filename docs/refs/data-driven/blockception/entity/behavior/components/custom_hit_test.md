# Custom Hit Test

> 文档版本：1.21.50.25

List of hitboxes for melee and ranged hits against the entity.

## 架构

```mcschema
custom_hit_test:
{
  array "hitboxes" : opt
  {
    object "<any array element>" : opt
    {
      number "width" : opt
      number "height" : opt
      array "pivot" : opt
      {
        number "0..0" : opt
        number "1..1" : opt
        number "2..2" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`hitboxes`：<samp>array</samp>

- Defines a hitbox size and pivot to test against.


////

<div class="language-text highlight"><span class="filename"><code>hitboxes</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- Defines a hitbox size and pivot to test against.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`width`：<samp>number</samp>

- Height of the hitbox in blocks. A negative value will be assumed to be 0.


//////


////// define
`height`：<samp>number</samp>

- Width and Depth of the hitbox in blocks. A negative value will be assumed to be 0.


//////


////// define
`pivot`：<samp>array</samp>

- The offset from the entity's anchor where the hitbox will spawn.


//////

<div class="language-text highlight"><span class="filename"><code>pivot</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>number</samp>


///////


/////// define
`1..1`：<samp>number</samp>


///////


/////// define
`2..2`：<samp>number</samp>


///////


//////


/////


////


///

