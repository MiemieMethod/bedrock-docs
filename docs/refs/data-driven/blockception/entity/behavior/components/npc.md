# Npc

> 文档版本：1.21.0.24

Sets this entity as an NPC

## 架构

```mcschema
npc:
{
  object "npc_data" : opt
  {
    object "portrait_offsets" : opt
    {
      array "translate" : opt
      {
        number "0..0" : opt
        number "1..1" : opt
        number "2..2" : opt
      }
      array "scale" : opt
    }
    object "picker_offsets" : opt
    {
      array "translate" : opt
      array "scale" : opt
    }
    array "skin_list" : opt
    {
      object "<any array element>" : opt
      {
        integer "variant" : opt
        integer "mark_variant" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`npc_data`：<samp>object</samp>

- The data belonging to this npc.


////

<div class="language-text highlight"><span class="filename"><code>npc_data</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`portrait_offsets`：<samp>object</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>portrait_offsets</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`translate`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>translate</code></span><pre id="__code_1"><span></span></pre></div>

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


////// define
`scale`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`picker_offsets`：<samp>object</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>picker_offsets</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`translate`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>translate</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`scale`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`skin_list`：<samp>array</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>skin_list</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`variant`：<samp>integer</samp>

- UNDOCUMENTED.


///////


/////// define
`mark_variant`：<samp>integer</samp>

- UNDOCUMENTED.


///////


//////


/////


////


///

