# Movement Jump

> 文档版本：1.21.0.24

Move control that causes the mob to jump as it moves with a specified delay between jumps.

## 架构

```mcschema
jump:
{
  array "jump_delay" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "max_turn" : opt
}

```

/// html | div.result
//// define
`jump_delay`：<samp>array</samp>

- Delay after landing when using the slime move control.


////

<div class="language-text highlight"><span class="filename"><code>jump_delay</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`max_turn`：<samp>number</samp>

- The maximum number in degrees the mob can turn per tick.


////


///

