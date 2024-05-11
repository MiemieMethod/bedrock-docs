# 未命名

> 文档版本：1.21.0.24

用于设置方块渲染时使用的材质。

## 架构

```mcschema
netease:render_layer:
{
  string "value" : opt
}

```

/// html | div.result
//// define
`value`：<samp>string</samp>

- 目前支持的材质有：
opaque：不透明，即“terrain_opaque”材质。默认为此项
alpha：全透明，即“terrain_alpha”材质，如火焰，该材质用于异形方块，用在方块类上但与其他方块重合时会出现闪烁，可以使用no_crop_face_block组件避免闪烁。
blend：半透明，即“terrain_blend”材质，如彩色玻璃。
optionalAlpha：局部透明，与alpha不同，alpha超过一定距离将不渲染，而optionalAlpha不会，能配合no_crop_face_block组件实现原版叶子效果。


////


///

