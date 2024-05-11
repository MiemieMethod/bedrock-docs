# 未命名

> 文档版本：1.21.0.24

用于设置方块的碰撞盒。
注意事项：
1.无碰撞箱的方块请将collision的每个项都设置为0
2.有碰撞箱的方块，clip的范围需要小于或等于collision的范围，否则弹射物命中时会异常
3.aabb的min不要小于[-1, -1, -1]，max不要大于[2, 2, 2]

## 架构

```mcschema
netease:aabb:
{
  object "collision" : opt
  {
    array "min" : opt
    {
      number "<any array element>" : opt
    }
    array "max" : opt
    {
      number "<any array element>" : opt
    }
  }
  array "collision" : opt
  {
    object "<any array element>" : opt
    {
      expression_node_no_version "enable"
      array "min" : opt
      {
        number "<any array element>" : opt
      }
      array "max" : opt
      {
        number "<any array element>" : opt
      }
    }
  }
  object "clip" : opt
  {
    array "min" : opt
    {
      number "<any array element>" : opt
    }
    array "max" : opt
    {
      number "<any array element>" : opt
    }
  }
  array "clip" : opt
  {
    object "<any array element>" : opt
    {
      expression_node_no_version "enable"
      array "min" : opt
      {
        number "<any array element>" : opt
      }
      array "max" : opt
      {
        number "<any array element>" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`collision`：<samp>object</samp>

- 计算与物体碰撞时用的碰撞盒。


////

<div class="language-text highlight"><span class="filename"><code>collision</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`min`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>min</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>number</samp>


//////


/////


///// define
`max`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>max</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>number</samp>


//////


/////


////


//// define
`collision`：<samp>array</samp>

- 计算与物体碰撞时用的碰撞盒。


////

<div class="language-text highlight"><span class="filename"><code>collision</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`enable`：<samp>expression_node_no_version</samp> {#assets.schemas.common.molang.expression_node_no_version.json}

- 控制是否开启该碰撞箱
目前仅支持is_connect查询，详见netease:connection。


//////

```mcschema
expression_node_no_version:
string

```

////// html | div.result

//////


```mcschema
expression_node_no_version:
boolean

```

////// html | div.result

//////


```mcschema
expression_node_no_version:
number

```

////// html | div.result

//////




////// define
`min`：<samp>array</samp>

- min的三个值必须小于等于max的三个值。


//////

<div class="language-text highlight"><span class="filename"><code>min</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>number</samp>


///////


//////


////// define
`max`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>max</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>number</samp>


///////


//////


/////


////



//// define
`clip`：<samp>object</samp>

- 计算射线检测时用的碰撞盒。如准心选取及弹射物碰撞。
（那么当该AABB没有体积时，准心与弹射物都会无视这个方块）。


////

<div class="language-text highlight"><span class="filename"><code>clip</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`min`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>min</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>number</samp>


//////


/////


///// define
`max`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>max</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>number</samp>


//////


/////


////


//// define
`clip`：<samp>array</samp>

- 计算射线检测时用的碰撞盒。如准心选取及弹射物碰撞。
（那么当该AABB没有体积时，准心与弹射物都会无视这个方块）。


////

<div class="language-text highlight"><span class="filename"><code>clip</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`enable`：<samp>[expression_node_no_version](#assets.schemas.common.molang.expression_node_no_version.json)</samp>

- 控制是否开启该碰撞箱
目前仅支持is_connect查询，详见netease:connection。


//////


////// define
`min`：<samp>array</samp>

- min的三个值必须小于等于max的三个值。


//////

<div class="language-text highlight"><span class="filename"><code>min</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>number</samp>


///////


//////


////// define
`max`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>max</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>number</samp>


///////


//////


/////


////



///

