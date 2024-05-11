# minecraft:behavior.python_custom

> 文档版本：1.21.0.24

通过配置behavior_pack/entities中生物json的behavior，增加自定义behavior节点，并在python实现对应节点的逻辑，以实现自定义的生物行为。

## 架构

```mcschema
minecraft:behavior_python_custom:
{
  integer "priority" : opt
  string "module_path" : opt
  string "class_name" : opt
  object "arg_dict" : opt
  {
  }
  array "control_flags" : opt
  {
    string "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`priority`：<samp>integer</samp>

- 行为的优先级。


////


//// define
`module_path`：<samp>string</samp>

- 行为的python模块路径，以 "." 分隔。


////


//// define
`class_name`：<samp>string</samp>

- 行为的python类名。


////


//// define
`arg_dict`：<samp>object</samp>

- 行为的参数，会被传至python实例中。


////

<div class="language-text highlight"><span class="filename"><code>arg_dict</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////


//// define
`control_flags`：<samp>array</samp>

- 控制标志，包含相同控制标志的行为被为冲突，同一时刻下冲突的行为最多只有一个会被执行。可用的标志有move, look, jump。


////

<div class="language-text highlight"><span class="filename"><code>control_flags</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


///

