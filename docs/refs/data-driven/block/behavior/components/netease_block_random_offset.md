# 未命名

> 文档版本：1.21.0.24

用于设置方块的偏移，能实现原版花朵的偏移效果。
注意：制作可偏移方块时，请尽量配套使用方块模型，当使用贴图方块随机偏移时，若相邻方块是不透明方块，则该方块对应的面会被裁切渲染！！普通贴图方块的物品栏渲染也可能会有异常！！
该组件会把方块的材质设置为透明，且不可与netease:render_layer的不透明材质一起共用，否则会出现渲染错误。

## 架构

```mcschema
netease:block_random_offset:
{
  array "x_scope" : opt
  {
    number "<any array element>" : opt
  }
  array "z_scope" : opt
  {
    number "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`x_scope`：<samp>array</samp>

- x轴方向的偏移范围，size为2的array，取值范围为0.0~1.0，如果两个值相同则为指定点。


////

<div class="language-text highlight"><span class="filename"><code>x_scope</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


//// define
`z_scope`：<samp>array</samp>

- z轴方向的偏移范围，size为2的array，取值范围为0.0~1.0，如果两个值相同则为指定点。


////

<div class="language-text highlight"><span class="filename"><code>z_scope</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


///

