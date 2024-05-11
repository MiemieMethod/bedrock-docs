# Sound Definitions

> 文档版本：1.21.0.24

The collection of sound definitions this resourcepack has defined.

## 架构

```mcschema
sound_definition:
{
  format_version "format_version"
  object "sound_definitions" : opt
  {
    object "<any object property>" : opt
    {
      boolean "__use_legacy_max_distance" : opt
      string "category" : opt
      array "sounds" : opt
      {
        string "<any array element>" : opt
        object "<any array element>" : opt
        {
          boolean "is3D" : opt
          number "pitch" : opt
          number "volume" : opt
          boolean "stream" : opt
          string "name" : opt
          integer "weight" : opt
        }
      }
      ['number', 'null'] "max_distance" : opt
      ['number', 'null'] "min_distance" : opt
    }
  }
  string "__use_legacy_max_distance" : opt
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
`sound_definitions`：<samp>object</samp>

- UNDOCUMENTED: sound definitions.


////

<div class="language-text highlight"><span class="filename"><code>sound_definitions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any object property>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`__use_legacy_max_distance`：<samp>boolean</samp>

- Whenever or not use legacy distance checking.


//////


////// define
`category`：<samp>string</samp>

- The category this sound belongs to, for the user to control the volume on.


//////


////// define
`sounds`：<samp>array</samp>

- The collection of sounds minecraft can choice from.


//////

<div class="language-text highlight"><span class="filename"><code>sounds</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- The filepath to the sound, starts with `sounds/'.


///////


/////// define
`<any array element>`：<samp>object</samp>

- A collection of sounds to choice from.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`is3D`：<samp>boolean</samp>

- UNDOCUMENTED.


////////


//////// define
`pitch`：<samp>number</samp>

- The pitch of the audio, 1 is nomial.


////////


//////// define
`volume`：<samp>number</samp>

- The volume of the audio, 1 is nomial.


////////


//////// define
`stream`：<samp>boolean</samp>

- If marked true then minecraft will stream the audio.


////////


//////// define
`name`：<samp>string</samp>

- The filepath to the sound, starts with `sounds/'.


////////


//////// define
`weight`：<samp>integer</samp>

- UNDOCUMENTED.


////////


///////



//////


////// define
`max_distance`：<samp>['number', 'null']</samp>

- UNDOCUMENTED.


//////


////// define
`min_distance`：<samp>['number', 'null']</samp>

- UNDOCUMENTED.


//////


/////


////


//// define
`__use_legacy_max_distance`：<samp>string</samp>

- UNDOCUMENTED: use legacy Maximum distance.


////


///

