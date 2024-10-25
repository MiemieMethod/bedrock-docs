# Nameable

> 文档版本：1.21.50.25

Allows this entity to be named (e.g. using a name tag).

## 架构

```mcschema
nameable:
{
  boolean "allow_name_tag_renaming" : opt
  boolean "always_show" : opt
  trigger "default_trigger"
  array "name_actions" : opt
  {
    object "<any array element>" : opt
    {
      string "name_filter" : opt
      event_object "on_named"
    }
  }
  object "name_actions" : opt
  {
  }
}

```

/// html | div.result
//// define
`allow_name_tag_renaming`：<samp>boolean</samp>

- If true, this entity can be renamed with name tags.


////


//// define
`always_show`：<samp>boolean</samp>

- If true, the name will always be shown.


////


//// define
`default_trigger`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Trigger to run when the entity gets named.


////

```mcschema
trigger:
string

```

//// html | div.result

////


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


/////


///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions for this trigger to execute.


/////


///// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


/////

```mcschema
subject:
string

```

///// html | div.result

/////



////


```mcschema
trigger:
array
{
  object "<any array element>" : opt
  {
    string "event" : opt
    filters "filters"
    subject "target"
  }
}

```

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////




//// define
`name_actions`：<samp>array</samp>

- Describes the special names for this entity and the events to call when the entity acquires those names.


////

<div class="language-text highlight"><span class="filename"><code>name_actions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- Describes the special names for this entity and the events to call when the entity acquires those names.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`name_filter`：<samp>string</samp>

- List of special names that will cause the events defined in `on_named` to fire.


//////


////// define
`on_named`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to be called when this entity acquires the name specified in `name_filter'.


//////

```mcschema
event_object:
{
  filters "filters"
  string "event" : opt
  string "target" : opt
}

```

////// html | div.result
/////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


///////


/////// define
`event`：<samp>string</samp>

- The event to fire.


///////


/////// define
`target`：<samp>string</samp>

- The target of the event.


///////


//////



/////


////


//// define
`name_actions`：<samp>object</samp>

- Describes the special names for this entity and the events to call when the entity acquires those names.


////

<div class="language-text highlight"><span class="filename"><code>name_actions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////



///

