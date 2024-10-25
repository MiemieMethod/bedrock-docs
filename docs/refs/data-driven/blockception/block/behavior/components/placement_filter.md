# Placement Filter

> 文档版本：1.21.50.25



## 架构

```mcschema
placement_filter:
{
  array "conditions" : opt
  {
    object "<any array element>" : opt
    {
      array "allowed_faces" : opt
      {
        string "<any array element>" : opt
      }
      array "block_filter" : opt
      {
        reference "<any array element>"
      }
    }
  }
}

```

/// html | div.result
//// define
`conditions`：<samp>array</samp>

- List of conditions where the block can be placed/survive. Limited to 64 conditions. Each condition is a JSON Object that must contain at least one (and can contain both) of the parameters allowed_faces or block_filter as shown below.


////

<div class="language-text highlight"><span class="filename"><code>conditions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`allowed_faces`：<samp>array</samp>

- List of any of the following strings describing which face(s) this block can be placed on: "up", "down", "north", "south", "east", "west", "side", "all". Limited to 6 faces.


//////

<div class="language-text highlight"><span class="filename"><code>allowed_faces</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>


///////


//////


////// define
`block_filter`：<samp>array</samp>

- List of blocks that this block can be placed against in the "allowed_faces" direction. Limited to 64 blocks. Each block in this list can either be specified as a String (block name) or as a BlockDescriptor. A BlockDescriptor is an object that allows you to reference a block (or multiple blocks) based on its tags, or based on its name and states. The fields of a BlockDescriptor are described below.


//////

<div class="language-text highlight"><span class="filename"><code>block_filter</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>reference</samp> {#assets.schemas-blockception.general.block.reference.json}

- [Experimental]


///////

```mcschema
identifier:
string

```

/////// html | div.result

///////



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

/////// html | div.result
//////// define
`name`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


////////


//////// define
`states`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`\w*:?\w+`：<samp>['boolean', 'integer', 'string']</samp>

- The key of property is the name of the block state/property, the value must be the same as the block properties accepted values.


/////////


////////


//////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- A condition using Molang queries that results to true/false that can be used to query for blocks with certain tags.


////////

```mcschema
0:
string

```

//////// html | div.result

////////



///////




//////


/////


////


///

