# NPC Dialogue

> 文档版本：1.21.0.24

Specifies the dialogue scenes.

## 架构

```mcschema
dialogue:
{
  format_version "format_version"
  object "minecraft:npc_dialogue" : opt
  {
    array "scenes" : opt
    {
      object "<any array element>" : opt
      {
        array "buttons" : opt
        {
          object "<any array element>" : opt
          {
            string "name" : opt
            rawtext "name"
            array "commands" : opt
            {
              string "<any array element>" : opt
            }
          }
        }
        string "npc_name" : opt
        rawtext "npc_name"
        array "on_close_commands" : opt
        {
          string "<any array element>" : opt
        }
        array "on_open_commands" : opt
        {
          string "<any array element>" : opt
        }
        string "scene_tag" : opt
        string "text" : opt
        rawtext "text"
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
`minecraft:npc_dialogue`：<samp>object</samp>

- Specifies the dialogue of an npc.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:npc_dialogue</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`scenes`：<samp>array</samp>

- The different scenes.


/////

<div class="language-text highlight"><span class="filename"><code>scenes</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>

- A single scene specification.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`buttons`：<samp>array</samp>

- This is where you can create buttons for your NPC.


///////

<div class="language-text highlight"><span class="filename"><code>buttons</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- This is where you can create buttons for your NPC.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`name`：<samp>string</samp>

- Set the text that is going to be displayed on your NPC’s button.


/////////


///////// define
`name`：<samp>rawtext</samp> {#assets.schemas-blockception.general.rawtext.rawtext.json}

- Set the text that is going to be displayed on your NPC’s button.


/////////

```mcschema
rawtext:
{
  array "rawtext" : opt
  {
    string "<any array element>" : opt
    object "<any array element>" : opt
    {
      string "translate" : opt
      array "with" : opt
      {
        string "<any array element>" : opt
        object "<any array element>" : opt
        {
          array "rawtext" : opt
        }
      }
    }
    object "<any array element>" : opt
    {
      string "text" : opt
    }
    object "<any array element>" : opt
    {
      string "selector" : opt
    }
    object "<any array element>" : opt
    {
      object "score" : opt
      {
        string "name" : opt
        string "objective" : opt
      }
    }
  }
}

```

///////// html | div.result
////////// define
`rawtext`：<samp>array</samp>

- The raw text component, which consists of an array of text components.


//////////

<div class="language-text highlight"><span class="filename"><code>rawtext</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>string</samp>


///////////


/////////// define
`<any array element>`：<samp>object</samp>

- A text component that will attempt to translate the given key through the languages files.


///////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result
//////////// define
`translate`：<samp>string</samp>

- The key to translate.


////////////


//////////// define
`with`：<samp>array</samp>

- Specifies for the translator that additional text component needs to be inserted, this will cause the translator to look for variables in the translation text and replaced them with the corresponding 'With' text component.


////////////

<div class="language-text highlight"><span class="filename"><code>with</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`<any array element>`：<samp>string</samp>


/////////////


///////////// define
`<any array element>`：<samp>object</samp>

- Specifies that this 'with' component needs to be processed.


/////////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////////// html | div.result
////////////// define
`rawtext`：<samp>array</samp>

- The raw text component, which consists of an array of text components.


//////////////

<div class="language-text highlight"><span class="filename"><code>rawtext</code></span><pre id="__code_1"><span></span></pre></div>

////////////// html | div.result

//////////////


/////////////



////////////


///////////


/////////// define
`<any array element>`：<samp>object</samp>

- A simple text component, will display the text raw (without processing).


///////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result
//////////// define
`text`：<samp>string</samp>

- The text to display.


////////////


///////////


/////////// define
`<any array element>`：<samp>object</samp>

- A text component that turns a selector into text, will usually display like: `Player1, Player2 and Player3`.


///////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result
//////////// define
`selector`：<samp>string</samp>

- The selector to target, for dialogue files, you can use @initiator.


////////////


///////////


/////////// define
`<any array element>`：<samp>object</samp>

- A text component that grabs the score from an given target and turns its value of a specified score.


///////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result
//////////// define
`score`：<samp>object</samp>

- The score text component.


////////////

<div class="language-text highlight"><span class="filename"><code>score</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`name`：<samp>string</samp>

- A selector, player name (can be fake), or * to target who is reading the message.


/////////////


///////////// define
`objective`：<samp>string</samp>

- The scoreboard objective to retrieve the value of.


/////////////


////////////


///////////



//////////


/////////




///////// define
`commands`：<samp>array</samp>

- allows you to add commands which will be run in-game when the button is pressed.


/////////

<div class="language-text highlight"><span class="filename"><code>commands</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>string</samp>

- The commands to execute.


//////////


/////////


////////


///////


/////// define
`npc_name`：<samp>string</samp>

- This is where you can add or change a name for your NPC dialogue box. This is an optional property that is useful for dynamically changing NPC names.


///////


/////// define
`npc_name`：<samp>[rawtext](#assets.schemas-blockception.general.rawtext.rawtext.json)</samp>

- This is where you can add or change a name for your NPC dialogue box. This is an optional property that is useful for dynamically changing NPC names.


///////



/////// define
`on_close_commands`：<samp>array</samp>

- This is where you can define which commands will fire when the NPC dialogue box closes.


///////

<div class="language-text highlight"><span class="filename"><code>on_close_commands</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>

- A minecraft command to execute.


////////


///////


/////// define
`on_open_commands`：<samp>array</samp>

- This is where you can define which commands will fire when the NPC dialogue box opens.


///////

<div class="language-text highlight"><span class="filename"><code>on_open_commands</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>

- A minecraft command to execute.


////////


///////


/////// define
`scene_tag`：<samp>string</samp>

- This is the name you will use to call this scene in-game. This is a required property.


///////


/////// define
`text`：<samp>string</samp>

- This is where you enter the dialogue you want your NPC to display in-game for this scene. You can type the dialogue text directly here or use raw text if you are using a language file. This is an optional property, but without it your NPC dialogue box will be empty.


///////


/////// define
`text`：<samp>[rawtext](#assets.schemas-blockception.general.rawtext.rawtext.json)</samp>

- This is where you enter the dialogue you want your NPC to display in-game for this scene. You can type the dialogue text directly here or use raw text if you are using a language file. This is an optional property, but without it your NPC dialogue box will be empty.


///////



//////


/////


////


///

