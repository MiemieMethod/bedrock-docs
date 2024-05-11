# 未命名

> 文档版本：1.21.0.24

用于配置自定义方块的方块属性。这些方块属性可以叠加，主要用于引擎对一些方块特性逻辑的判断。

## 架构

```mcschema
netease:block_properties:
{
  array "properties" : opt
  {
    string "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`properties`：<samp>array</samp>

- 所有属性字符串。


////

<div class="language-text highlight"><span class="filename"><code>properties</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>

- piston_block_grabber	被活塞推动时是否带动旁边方块
slime	主要用于变为移动方块（例如被活塞推）时修改对实体力的计算
breaks_when_fallen_on_by_heavy	当重力方块结束下落在该方块位置后，自身是否被毁坏
如果方块碰撞盒体积使用netease:aabb或minecraft:entity_collision改小可能会导致无法触发（目前可参考范围是边长0.4以下不会触发）。


/////


////


///

