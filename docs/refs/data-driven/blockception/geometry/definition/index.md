# 未命名

> 文档版本：1.21.50.25



## 架构

```mcschema
0:
{
  boolean "debug" : opt
  format_version "format_version"
  array "minecraft:geometry" : opt
  {
    object "<any array element>" : opt
    {
      object "description" : opt
      {
        string "identifier" : opt
        number "texture_width" : opt
        number "texture_height" : opt
        array "visible_bounds_offset" : opt
        {
          number "<any array element>" : opt
        }
        number "visible_bounds_width" : opt
        number "visible_bounds_height" : opt
      }
      array "bones" : opt
      {
        object "<any array element>" : opt
        {
          0 "binding"
          array "cubes" : opt
          {
            object "<any array element>" : opt
            {
              number "inflate" : opt
              boolean "mirror" : opt
              array "origin" : opt
              {
                number "<any array element>" : opt
              }
              array "pivot" : opt
              {
                number "0..0" : opt
                number "1..1" : opt
                number "2..2" : opt
              }
              boolean "reset" : opt
              array "rotation" : opt
              {
                number "<any array element>" : opt
              }
              array "size" : opt
              {
                number "0..0" : opt
                number "1..1" : opt
                number "2..2" : opt
              }
              object "uv" : opt
              {
                object "north" : opt
                {
                  array "uv" : opt
                  {
                    number "0..0" : opt
                    number "1..1" : opt
                  }
                  array "uv_size" : opt
                  string "material_instance" : opt
                }
                object "south" : opt
                {
                }
                object "east" : opt
                {
                }
                object "west" : opt
                {
                }
                object "up" : opt
                {
                }
                object "down" : opt
                {
                }
              }
              array "uv" : opt
              {
                number "0..0" : opt
                number "1..1" : opt
              }
            }
          }
          boolean "debug" : opt
          number "inflate" : opt
          object "locators" : opt
          {
            object "<any object property>" : opt
            {
              array "offset" : opt
              {
                number "<any array element>" : opt
              }
              array "rotation" : opt
              {
                number "<any array element>" : opt
              }
              boolean "ignore_inherited_scale" : opt
            }
            array "<any object property>" : opt
            {
              number "<any array element>" : opt
            }
          }
          boolean "mirror" : opt
          string "name" : opt
          string "parent" : opt
          array "pivot" : opt
          {
            number "0..0" : opt
            number "1..1" : opt
            number "2..2" : opt
          }
          object "poly_mesh" : opt
          {
            boolean "normalized_uvs" : opt
            array "normals" : opt
            {
              array "<any array element>" : opt
              {
                number "<any array element>" : opt
              }
            }
            string "polys" : opt
            array "polys" : opt
            {
              array "<any array element>" : opt
              {
                array "<any array element>" : opt
                {
                  number "0..0" : opt
                  number "1..1" : opt
                  number "2..2" : opt
                }
              }
            }
            array "positions" : opt
            {
              array "<any array element>" : opt
              {
                number "<any array element>" : opt
              }
            }
            array "uvs" : opt
            {
              array "<any array element>" : opt
              {
                number "<any array element>" : opt
              }
            }
          }
          integer "render_group_id" : opt
          array "rotation" : opt
          {
            number "0..0" : opt
            number "1..1" : opt
            number "2..2" : opt
          }
          array "texture_meshes" : opt
          {
            object "<any array element>" : opt
            {
              array "local_pivot" : opt
              {
                number "<any array element>" : opt
              }
              array "position" : opt
              {
                number "<any array element>" : opt
              }
              array "rotation" : opt
              {
                number "<any array element>" : opt
              }
              array "scale" : opt
              {
                number "<any array element>" : opt
              }
              string "texture" : opt
            }
          }
        }
      }
      string "cape" : opt
      object "item_display_transforms" : opt
      {
         "gui" : opt
         "firstperson_righthand" : opt
         "firstperson_lefthand" : opt
         "thirdperson_righthand" : opt
         "thirdperson_lefthand" : opt
         "ground" : opt
         "fixed" : opt
         "head" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`debug`：<samp>boolean</samp>

- UNDOCUMENTED.


////


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
`minecraft:geometry`：<samp>array</samp>

- The collection of geometries.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:geometry</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- Model specification.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`description`：<samp>object</samp>

- The descriptions of the geometry.


//////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`identifier`：<samp>string</samp>

- Entity definition and Client Block definition files refer to this geometry via this identifier.


///////


/////// define
`texture_width`：<samp>number</samp>

- Assumed width in texels of the texture that will be bound to this geometry.


///////


/////// define
`texture_height`：<samp>number</samp>

- Assumed height in texels of the texture that will be bound to this geometry.


///////


/////// define
`visible_bounds_offset`：<samp>array</samp>

- Offset of the visibility bounding box from the entity location point (in model space units).


///////

<div class="language-text highlight"><span class="filename"><code>visible_bounds_offset</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>number</samp>


////////


///////


/////// define
`visible_bounds_width`：<samp>number</samp>

- Width of the visibility bounding box (in model space units).


///////


/////// define
`visible_bounds_height`：<samp>number</samp>

- Height of the visible bounding box (in model space units).


///////


//////


////// define
`bones`：<samp>array</samp>

- Bones define the `skeleton` of the mob: the parts that can be animated, and to which geometry and other bones are attached.


//////

<div class="language-text highlight"><span class="filename"><code>bones</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- A bones specification.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`binding`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- useful for items. A molang expression specifying the bone name of the parent skeletal hierarchy that this bone should use as the root transform. Without this field it will look for a bone in the parent entity with the same name as this bone. If both are missing, it will assume a local skeletal hierarchy (via the `parent` field). If that is also missing, it will attach to the owning entity's root transform.


////////

```mcschema
0:
string

```

//////// html | div.result

////////



//////// define
`cubes`：<samp>array</samp>

- This is the list of cubes associated with this bone.


////////

<div class="language-text highlight"><span class="filename"><code>cubes</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>object</samp>

- A single cube.


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`inflate`：<samp>number</samp>

- Grow this box by this additive amount in all directions (in model space units), this field overrides the bone's inflate field for this cube only.


//////////


////////// define
`mirror`：<samp>boolean</samp>

- Mirrors this cube about the unrotated x axis (effectively flipping the east / west faces), overriding the bone's `mirror` setting for this cube.


//////////


////////// define
`origin`：<samp>array</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>origin</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- This point declares the unrotated lower corner of cube (smallest x/y/z value in model space units).


///////////


//////////


////////// define
`pivot`：<samp>array</samp>

- If this field is specified, rotation of this cube occurs around this point, otherwise its rotation is around the center of the box. Note that in 1.12 this is flipped upside-down, but is fixed in 1.14.


//////////

<div class="language-text highlight"><span class="filename"><code>pivot</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`0..0`：<samp>number</samp>

- If this field is specified, rotation of this cube occurs around this point, otherwise its rotation is around the center of the box. Note that in 1.12 this is flipped upside-down, but is fixed in 1.14.


///////////


/////////// define
`1..1`：<samp>number</samp>

- If this field is specified, rotation of this cube occurs around this point, otherwise its rotation is around the center of the box. Note that in 1.12 this is flipped upside-down, but is fixed in 1.14.


///////////


/////////// define
`2..2`：<samp>number</samp>

- If this field is specified, rotation of this cube occurs around this point, otherwise its rotation is around the center of the box. Note that in 1.12 this is flipped upside-down, but is fixed in 1.14.


///////////


//////////


////////// define
`reset`：<samp>boolean</samp>

- UNDOCUMENTED.


//////////


////////// define
`rotation`：<samp>array</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The cube is rotated by this amount (in degrees, x-then-y-then-z order) around the pivot.


///////////


//////////


////////// define
`size`：<samp>array</samp>

- The cube extends this amount relative to its origin (in model space units).


//////////

<div class="language-text highlight"><span class="filename"><code>size</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`0..0`：<samp>number</samp>

- The cube extends this amount relative to its origin (in model space units).


///////////


/////////// define
`1..1`：<samp>number</samp>

- The cube extends this amount relative to its origin (in model space units).


///////////


/////////// define
`2..2`：<samp>number</samp>

- The cube extends this amount relative to its origin (in model space units).


///////////


//////////


////////// define
`uv`：<samp>object</samp>

- This is an alternate per-face uv mapping which specifies each face of the cube. Omitting a face will cause that face to not get drawn.


//////////

<div class="language-text highlight"><span class="filename"><code>uv</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`north`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the x and y axes, and faces the -z axis.


///////////

<div class="language-text highlight"><span class="filename"><code>north</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result
//////////// define
`uv`：<samp>array</samp>

- Specifies the uv origin for the face. For this face, it is the upper-left corner, when looking at the face with y being up.


////////////

<div class="language-text highlight"><span class="filename"><code>uv</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result
///////////// define
`0..0`：<samp>number</samp>

- The x component of the uv.


/////////////


///////////// define
`1..1`：<samp>number</samp>

- The y component of the uv.


/////////////


////////////


//////////// define
`uv_size`：<samp>array</samp>

- The face maps this many texels from the uv origin. If not specified, the box dimensions are used instead.


////////////

<div class="language-text highlight"><span class="filename"><code>uv_size</code></span><pre id="__code_1"><span></span></pre></div>

//////////// html | div.result

////////////


//////////// define
`material_instance`：<samp>string</samp>

- Specifies the UV's for the face that stretches.


////////////


///////////


/////////// define
`south`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the x and y axes, and faces the z axis.


///////////

<div class="language-text highlight"><span class="filename"><code>south</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`east`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the z and y axes, and faces the x axis.


///////////

<div class="language-text highlight"><span class="filename"><code>east</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`west`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the z and y axes, and faces the -x axis.


///////////

<div class="language-text highlight"><span class="filename"><code>west</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`up`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the x and z axes, and faces the y axis.


///////////

<div class="language-text highlight"><span class="filename"><code>up</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`down`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the x and z axes, and faces the -y axis.


///////////

<div class="language-text highlight"><span class="filename"><code>down</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


//////////


////////// define
`uv`：<samp>array</samp>

- This is an alternate per-face uv mapping which specifies each face of the cube. Omitting a face will cause that face to not get drawn.


//////////

<div class="language-text highlight"><span class="filename"><code>uv</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`0..0`：<samp>number</samp>

- The x component of the uv.


///////////


/////////// define
`1..1`：<samp>number</samp>

- The y component of the uv.


///////////


//////////



/////////


////////


//////// define
`debug`：<samp>boolean</samp>


////////


//////// define
`inflate`：<samp>number</samp>

- Grow this box by this additive amount in all directions (in model space units).


////////


//////// define
`locators`：<samp>object</samp>

- This is a list of locators associated with this bone. A locator is a point in model space that tracks a particular bone as the bone animates (by maintaining it's relationship to the bone through the animation).


////////

<div class="language-text highlight"><span class="filename"><code>locators</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`offset`：<samp>array</samp>

- Position of the locator in model space.


//////////

<div class="language-text highlight"><span class="filename"><code>offset</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Position of the locator in model space.


///////////


//////////


////////// define
`rotation`：<samp>array</samp>

- Rotation of the locator in model space.


//////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Rotation of the locator in model space.


///////////


//////////


////////// define
`ignore_inherited_scale`：<samp>boolean</samp>

- Discard scale inherited from parent bone.


//////////


/////////


///////// define
`<any object property>`：<samp>array</samp>

- This is a list of locators associated with this bone. A locator is a point in model space that tracks a particular bone as the bone animates (by maintaining it's relationship to the bone through the animation).


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>number</samp>

- Position of the locator in model space.


//////////


/////////



////////


//////// define
`mirror`：<samp>boolean</samp>

- Mirrors the UV's of the unrotated cubes along the x axis, also causes the east/west faces to get flipped.


////////


//////// define
`name`：<samp>string</samp>

- Animation files refer to this bone via this identifier.


////////


//////// define
`parent`：<samp>string</samp>

- Bone that this bone is relative to. If the parent bone moves, this bone will move along with it.


////////


//////// define
`pivot`：<samp>array</samp>

- The bone pivots around this point (in model space units).


////////

<div class="language-text highlight"><span class="filename"><code>pivot</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>number</samp>


/////////


///////// define
`1..1`：<samp>number</samp>


/////////


///////// define
`2..2`：<samp>number</samp>


/////////


////////


//////// define
`poly_mesh`：<samp>object</samp>

- ***EXPERIMENTAL*** A triangle or quad mesh object. Can be used in conjunction with cubes and texture geometry.


////////

<div class="language-text highlight"><span class="filename"><code>poly_mesh</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`normalized_uvs`：<samp>boolean</samp>

- If true, UVs are assumed to be [0-1]. If false, UVs are assumed to be [0-texture_width] and [0-texture_height] respectively.


/////////


///////// define
`normals`：<samp>array</samp>

- Vertex normals. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and UVs sections.


/////////

<div class="language-text highlight"><span class="filename"><code>normals</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>array</samp>

- Vertex normals. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and UVs sections.


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Vertex normals. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and UVs sections.


///////////


//////////


/////////


///////// define
`polys`：<samp>string</samp>

- If not specifying vertex indices, arrays of data must be a list of tris or quads, set by making this property either `tri_list` or `quad_list`.


/////////


///////// define
`polys`：<samp>array</samp>

- Poly element indices, as an array of polygons, each an array of either three or four vertices, each an array of indices into positions, normals, and UVs (in that order).


/////////

<div class="language-text highlight"><span class="filename"><code>polys</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>array</samp>

- Poly element indices, as an array of polygons, each an array of either three or four vertices, each an array of indices into positions, normals, and UVs (in that order).


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>array</samp>


///////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result
//////////// define
`0..0`：<samp>number</samp>

- The index of the position.


////////////


//////////// define
`1..1`：<samp>number</samp>

- The index of the normal vertex.


////////////


//////////// define
`2..2`：<samp>number</samp>

- The index of the uv vertex.


////////////


///////////


//////////


/////////



///////// define
`positions`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>positions</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>array</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Vertex positions for the mesh. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the normals and UVs sections.


///////////


//////////


/////////


///////// define
`uvs`：<samp>array</samp>

- Vertex UVs. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and normals sections.


/////////

<div class="language-text highlight"><span class="filename"><code>uvs</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>array</samp>

- Vertex UVs. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and normals sections.


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Vertex UVs. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and normals sections.


///////////


//////////


/////////


////////


//////// define
`render_group_id`：<samp>integer</samp>


////////


//////// define
`rotation`：<samp>array</samp>

- This is the initial rotation of the bone around the pivot, pre-animation (in degrees, x-then-y-then-z order).


////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>number</samp>

- in degrees.


/////////


///////// define
`1..1`：<samp>number</samp>

- in degrees.


/////////


///////// define
`2..2`：<samp>number</samp>

- in degrees.


/////////


////////


//////// define
`texture_meshes`：<samp>array</samp>

- ***EXPERIMENTAL*** Adds a mesh to the bone's geometry by converting texels in a texture into boxes.


////////

<div class="language-text highlight"><span class="filename"><code>texture_meshes</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`local_pivot`：<samp>array</samp>

- The pivot point on the texture (in *texture space* not entity or bone space) of the texture geometry.


//////////

<div class="language-text highlight"><span class="filename"><code>local_pivot</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The pivot point on the texture (in *texture space* not entity or bone space) of the texture geometry.


///////////


//////////


////////// define
`position`：<samp>array</samp>

- The position of the pivot point after rotation (in *entity space* not texture or bone space) of the texture geometry.


//////////

<div class="language-text highlight"><span class="filename"><code>position</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The position of the pivot point after rotation (in *entity space* not texture or bone space) of the texture geometry.


///////////


//////////


////////// define
`rotation`：<samp>array</samp>

- The rotation (in degrees) of the texture geometry relative to the offset.


//////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The rotation (in degrees) of the texture geometry relative to the offset.


///////////


//////////


////////// define
`scale`：<samp>array</samp>

- The scale (in degrees) of the texture geometry relative to the offset.


//////////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The scale (in degrees) of the texture geometry relative to the offset.


///////////


//////////


////////// define
`texture`：<samp>string</samp>

- The friendly-named texture to use.


//////////


/////////


////////


///////


//////


////// define
`cape`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`item_display_transforms`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>item_display_transforms</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`gui`


///////


/////// define
`firstperson_righthand`


///////


/////// define
`firstperson_lefthand`


///////


/////// define
`thirdperson_righthand`


///////


/////// define
`thirdperson_lefthand`


///////


/////// define
`ground`


///////


/////// define
`fixed`


///////


/////// define
`head`


///////


//////


/////


////


///



```mcschema
0:
{
  boolean "debug" : opt
  string "format_version" : opt
  object "(^geometry.[\:a-zA-Z0-9_\-\.]+|format_version)" : opt
  {
    array "bones" : opt
    {
      object "<any array element>" : opt
      {
        array "bind_pose_rotation" : opt
        {
          number "0..0" : opt
          number "1..1" : opt
          number "2..2" : opt
        }
        array "cubes" : opt
        {
          object "<any array element>" : opt
          {
            number "inflate" : opt
            boolean "mirror" : opt
            array "origin" : opt
            {
              number "0..0" : opt
              number "1..1" : opt
              number "2..2" : opt
            }
            array "size" : opt
            {
              number "0..0" : opt
              number "1..1" : opt
              number "2..2" : opt
            }
            array "uv" : opt
            {
              number "0..0" : opt
              number "1..1" : opt
            }
          }
        }
        boolean "debug" : opt
        number "inflate" : opt
        object "locators" : opt
        {
          array "<any object property>" : opt
          {
            number "<any array element>" : opt
          }
        }
        boolean "mirror" : opt
        string "name" : opt
        boolean "neverRender" : opt
        string "parent" : opt
        array "pivot" : opt
        {
          number "0..0" : opt
          number "1..1" : opt
          number "2..2" : opt
        }
        object "poly_mesh" : opt
        {
          boolean "normalized_uvs" : opt
          array "positions" : opt
          {
            number "0..0" : opt
            number "1..1" : opt
            number "2..2" : opt
          }
          array "normals" : opt
          {
            number "0..0" : opt
            number "1..1" : opt
            number "2..2" : opt
          }
          array "polys" : opt
          {
            array "<any array element>" : opt
            {
              number "0..0" : opt
              number "1..1" : opt
              number "2..2" : opt
            }
          }
        }
        integer "render_group_id" : opt
        boolean "reset" : opt
        array "rotation" : opt
        {
          number "0..0" : opt
          number "1..1" : opt
          number "2..2" : opt
        }
        array "texture_meshes" : opt
        {
          object "<any array element>" : opt
          {
            string "texture" : opt
            array "local_pivot" : opt
            {
              number "0..0" : opt
              number "1..1" : opt
              number "2..2" : opt
            }
            array "position" : opt
            {
              number "0..0" : opt
              number "1..1" : opt
              number "2..2" : opt
            }
            array "rotation" : opt
            {
              number "0..0" : opt
              number "1..1" : opt
              number "2..2" : opt
            }
            array "scale" : opt
            {
              number "0..0" : opt
              number "1..1" : opt
              number "2..2" : opt
            }
          }
        }
      }
    }
    string "cape" : opt
    boolean "debug" : opt
    integer "texturewidth" : opt
    integer "textureheight" : opt
    number "visible_bounds_width" : opt
    number "visible_bounds_height" : opt
    array "visible_bounds_offset" : opt
    {
      number "0..0" : opt
      number "1..1" : opt
      number "2..2" : opt
    }
  }
}

```

/// html | div.result
//// define
`debug`：<samp>boolean</samp>

- UNDOCUMENTED.


////


//// define
`format_version`：<samp>string</samp>

- A version that tells minecraft what type of data format can be expected when reading this file.


////


//// define
`(^geometry.[\:a-zA-Z0-9_\-\.]+|format_version)`：<samp>object</samp>

- Geometry specification.


////

<div class="language-text highlight"><span class="filename"><code>(^geometry.[\:a-zA-Z0-9_\-\.]+|format_version)</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`bones`：<samp>array</samp>

- The bones definitions.


/////

<div class="language-text highlight"><span class="filename"><code>bones</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>

- The bone definition.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`bind_pose_rotation`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>bind_pose_rotation</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`0..0`：<samp>number</samp>


////////


//////// define
`1..1`：<samp>number</samp>


////////


//////// define
`2..2`：<samp>number</samp>


////////


///////


/////// define
`cubes`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>cubes</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`inflate`：<samp>number</samp>


/////////


///////// define
`mirror`：<samp>boolean</samp>


/////////


///////// define
`origin`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>origin</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>number</samp>


//////////


////////// define
`1..1`：<samp>number</samp>


//////////


////////// define
`2..2`：<samp>number</samp>


//////////


/////////


///////// define
`size`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>size</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>number</samp>


//////////


////////// define
`1..1`：<samp>number</samp>


//////////


////////// define
`2..2`：<samp>number</samp>


//////////


/////////


///////// define
`uv`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>uv</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>number</samp>


//////////


////////// define
`1..1`：<samp>number</samp>


//////////


/////////


////////


///////


/////// define
`debug`：<samp>boolean</samp>


///////


/////// define
`inflate`：<samp>number</samp>


///////


/////// define
`locators`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>locators</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>array</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>number</samp>


/////////


////////


///////


/////// define
`mirror`：<samp>boolean</samp>


///////


/////// define
`name`：<samp>string</samp>


///////


/////// define
`neverRender`：<samp>boolean</samp>


///////


/////// define
`parent`：<samp>string</samp>


///////


/////// define
`pivot`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>pivot</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`0..0`：<samp>number</samp>


////////


//////// define
`1..1`：<samp>number</samp>


////////


//////// define
`2..2`：<samp>number</samp>


////////


///////


/////// define
`poly_mesh`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>poly_mesh</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`normalized_uvs`：<samp>boolean</samp>

- UNDOCUMENTED.


////////


//////// define
`positions`：<samp>array</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>positions</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>number</samp>


/////////


///////// define
`1..1`：<samp>number</samp>


/////////


///////// define
`2..2`：<samp>number</samp>


/////////


////////


//////// define
`normals`：<samp>array</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>normals</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>number</samp>


/////////


///////// define
`1..1`：<samp>number</samp>


/////////


///////// define
`2..2`：<samp>number</samp>


/////////


////////


//////// define
`polys`：<samp>array</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>polys</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>number</samp>


//////////


////////// define
`1..1`：<samp>number</samp>


//////////


////////// define
`2..2`：<samp>number</samp>


//////////


/////////


////////


///////


/////// define
`render_group_id`：<samp>integer</samp>

- UNDOCUMENTED.


///////


/////// define
`reset`：<samp>boolean</samp>

- UNDOCUMENTED.


///////


/////// define
`rotation`：<samp>array</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`0..0`：<samp>number</samp>


////////


//////// define
`1..1`：<samp>number</samp>


////////


//////// define
`2..2`：<samp>number</samp>


////////


///////


/////// define
`texture_meshes`：<samp>array</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>texture_meshes</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`texture`：<samp>string</samp>


/////////


///////// define
`local_pivot`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>local_pivot</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>number</samp>


//////////


////////// define
`1..1`：<samp>number</samp>


//////////


////////// define
`2..2`：<samp>number</samp>


//////////


/////////


///////// define
`position`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>position</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>number</samp>


//////////


////////// define
`1..1`：<samp>number</samp>


//////////


////////// define
`2..2`：<samp>number</samp>


//////////


/////////


///////// define
`rotation`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>number</samp>


//////////


////////// define
`1..1`：<samp>number</samp>


//////////


////////// define
`2..2`：<samp>number</samp>


//////////


/////////


///////// define
`scale`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>number</samp>


//////////


////////// define
`1..1`：<samp>number</samp>


//////////


////////// define
`2..2`：<samp>number</samp>


//////////


/////////


////////


///////


//////


/////


///// define
`cape`：<samp>string</samp>

- UNDOCUMENTED.


/////


///// define
`debug`：<samp>boolean</samp>

- UNDOCUMENTED.


/////


///// define
`texturewidth`：<samp>integer</samp>

- UNDOCUMENTED: texturewidth.


/////


///// define
`textureheight`：<samp>integer</samp>

- UNDOCUMENTED: textureheight.


/////


///// define
`visible_bounds_width`：<samp>number</samp>

- UNDOCUMENTED: visible bounds width.


/////


///// define
`visible_bounds_height`：<samp>number</samp>

- UNDOCUMENTED: visible bounds height.


/////


///// define
`visible_bounds_offset`：<samp>array</samp>

- UNDOCUMENTED: visible bounds offset.


/////

<div class="language-text highlight"><span class="filename"><code>visible_bounds_offset</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


////// define
`2..2`：<samp>number</samp>


//////


/////


////


///



```mcschema
0:
{
  boolean "debug" : opt
  format_version "format_version"
  array "minecraft:geometry" : opt
  {
    object "<any array element>" : opt
    {
      object "description" : opt
      {
        string "identifier" : opt
        number "texture_width" : opt
        number "texture_height" : opt
        array "visible_bounds_offset" : opt
        {
          number "<any array element>" : opt
        }
        number "visible_bounds_width" : opt
        number "visible_bounds_height" : opt
      }
      array "bones" : opt
      {
        object "<any array element>" : opt
        {
          0 "binding"
          array "cubes" : opt
          {
            object "<any array element>" : opt
            {
              number "inflate" : opt
              boolean "mirror" : opt
              array "origin" : opt
              {
                number "<any array element>" : opt
              }
              array "pivot" : opt
              {
                number "0..0" : opt
                number "1..1" : opt
                number "2..2" : opt
              }
              boolean "reset" : opt
              array "rotation" : opt
              {
                number "<any array element>" : opt
              }
              array "size" : opt
              {
                number "0..0" : opt
                number "1..1" : opt
                number "2..2" : opt
              }
              object "uv" : opt
              {
                object "north" : opt
                {
                  array "uv" : opt
                  {
                    number "0..0" : opt
                    number "1..1" : opt
                  }
                  array "uv_size" : opt
                  string "material_instance" : opt
                }
                object "south" : opt
                {
                }
                object "east" : opt
                {
                }
                object "west" : opt
                {
                }
                object "up" : opt
                {
                }
                object "down" : opt
                {
                }
              }
              array "uv" : opt
              {
                number "0..0" : opt
                number "1..1" : opt
              }
            }
          }
          boolean "debug" : opt
          number "inflate" : opt
          object "locators" : opt
          {
            object "<any object property>" : opt
            {
              array "offset" : opt
              {
                number "<any array element>" : opt
              }
              array "rotation" : opt
              {
                number "<any array element>" : opt
              }
              boolean "ignore_inherited_scale" : opt
            }
            array "<any object property>" : opt
            {
              number "<any array element>" : opt
            }
          }
          boolean "mirror" : opt
          string "name" : opt
          string "parent" : opt
          array "pivot" : opt
          {
            number "0..0" : opt
            number "1..1" : opt
            number "2..2" : opt
          }
          object "poly_mesh" : opt
          {
            boolean "normalized_uvs" : opt
            array "normals" : opt
            {
              array "<any array element>" : opt
              {
                number "<any array element>" : opt
              }
            }
            string "polys" : opt
            array "polys" : opt
            {
              array "<any array element>" : opt
              {
                array "<any array element>" : opt
                {
                  number "0..0" : opt
                  number "1..1" : opt
                  number "2..2" : opt
                }
              }
            }
            array "positions" : opt
            {
              array "<any array element>" : opt
              {
                number "<any array element>" : opt
              }
            }
            array "uvs" : opt
            {
              array "<any array element>" : opt
              {
                number "<any array element>" : opt
              }
            }
          }
          integer "render_group_id" : opt
          array "rotation" : opt
          {
            number "0..0" : opt
            number "1..1" : opt
            number "2..2" : opt
          }
          array "texture_meshes" : opt
          {
            object "<any array element>" : opt
            {
              array "local_pivot" : opt
              {
                number "<any array element>" : opt
              }
              array "position" : opt
              {
                number "<any array element>" : opt
              }
              array "rotation" : opt
              {
                number "<any array element>" : opt
              }
              array "scale" : opt
              {
                number "<any array element>" : opt
              }
              string "texture" : opt
            }
          }
        }
      }
      string "cape" : opt
    }
  }
}

```

/// html | div.result
//// define
`debug`：<samp>boolean</samp>

- UNDOCUMENTED.


////


//// define
`format_version`：<samp>[format_version](#assets.schemas-blockception.general.format_version.json)</samp>


////


//// define
`minecraft:geometry`：<samp>array</samp>

- The collection of geometries.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:geometry</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- Model specification.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`description`：<samp>object</samp>

- The descriptions of the geometry.


//////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`identifier`：<samp>string</samp>

- Entity definition and Client Block definition files refer to this geometry via this identifier.


///////


/////// define
`texture_width`：<samp>number</samp>

- Assumed width in texels of the texture that will be bound to this geometry.


///////


/////// define
`texture_height`：<samp>number</samp>

- Assumed height in texels of the texture that will be bound to this geometry.


///////


/////// define
`visible_bounds_offset`：<samp>array</samp>

- Offset of the visibility bounding box from the entity location point (in model space units).


///////

<div class="language-text highlight"><span class="filename"><code>visible_bounds_offset</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>number</samp>


////////


///////


/////// define
`visible_bounds_width`：<samp>number</samp>

- Width of the visibility bounding box (in model space units).


///////


/////// define
`visible_bounds_height`：<samp>number</samp>

- Height of the visible bounding box (in model space units).


///////


//////


////// define
`bones`：<samp>array</samp>

- Bones define the `skeleton` of the mob: the parts that can be animated, and to which geometry and other bones are attached.


//////

<div class="language-text highlight"><span class="filename"><code>bones</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- A bones specification.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`binding`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- useful for items. A molang expression specifying the bone name of the parent skeletal hierarchy that this bone should use as the root transform. Without this field it will look for a bone in the parent entity with the same name as this bone. If both are missing, it will assume a local skeletal hierarchy (via the `parent` field). If that is also missing, it will attach to the owning entity's root transform.


////////


//////// define
`cubes`：<samp>array</samp>

- This is the list of cubes associated with this bone.


////////

<div class="language-text highlight"><span class="filename"><code>cubes</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>object</samp>

- A single cube.


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`inflate`：<samp>number</samp>

- Grow this box by this additive amount in all directions (in model space units), this field overrides the bone's inflate field for this cube only.


//////////


////////// define
`mirror`：<samp>boolean</samp>

- Mirrors this cube about the unrotated x axis (effectively flipping the east / west faces), overriding the bone's `mirror` setting for this cube.


//////////


////////// define
`origin`：<samp>array</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>origin</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- This point declares the unrotated lower corner of cube (smallest x/y/z value in model space units).


///////////


//////////


////////// define
`pivot`：<samp>array</samp>

- If this field is specified, rotation of this cube occurs around this point, otherwise its rotation is around the center of the box. Note that in 1.12 this is flipped upside-down, but is fixed in 1.14.


//////////

<div class="language-text highlight"><span class="filename"><code>pivot</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`0..0`：<samp>number</samp>

- If this field is specified, rotation of this cube occurs around this point, otherwise its rotation is around the center of the box. Note that in 1.12 this is flipped upside-down, but is fixed in 1.14.


///////////


/////////// define
`1..1`：<samp>number</samp>

- If this field is specified, rotation of this cube occurs around this point, otherwise its rotation is around the center of the box. Note that in 1.12 this is flipped upside-down, but is fixed in 1.14.


///////////


/////////// define
`2..2`：<samp>number</samp>

- If this field is specified, rotation of this cube occurs around this point, otherwise its rotation is around the center of the box. Note that in 1.12 this is flipped upside-down, but is fixed in 1.14.


///////////


//////////


////////// define
`reset`：<samp>boolean</samp>

- UNDOCUMENTED.


//////////


////////// define
`rotation`：<samp>array</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The cube is rotated by this amount (in degrees, x-then-y-then-z order) around the pivot.


///////////


//////////


////////// define
`size`：<samp>array</samp>

- The cube extends this amount relative to its origin (in model space units).


//////////

<div class="language-text highlight"><span class="filename"><code>size</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`0..0`：<samp>number</samp>

- The cube extends this amount relative to its origin (in model space units).


///////////


/////////// define
`1..1`：<samp>number</samp>

- The cube extends this amount relative to its origin (in model space units).


///////////


/////////// define
`2..2`：<samp>number</samp>

- The cube extends this amount relative to its origin (in model space units).


///////////


//////////


////////// define
`uv`：<samp>object</samp>

- This is an alternate per-face uv mapping which specifies each face of the cube. Omitting a face will cause that face to not get drawn.


//////////

<div class="language-text highlight"><span class="filename"><code>uv</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`north`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the x and y axes, and faces the -z axis.


///////////

<div class="language-text highlight"><span class="filename"><code>north</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`south`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the x and y axes, and faces the z axis.


///////////

<div class="language-text highlight"><span class="filename"><code>south</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`east`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the z and y axes, and faces the x axis.


///////////

<div class="language-text highlight"><span class="filename"><code>east</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`west`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the z and y axes, and faces the -x axis.


///////////

<div class="language-text highlight"><span class="filename"><code>west</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`up`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the x and z axes, and faces the y axis.


///////////

<div class="language-text highlight"><span class="filename"><code>up</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


/////////// define
`down`：<samp>object</samp>

- Specifies the UV's for the face that stretches along the x and z axes, and faces the -y axis.


///////////

<div class="language-text highlight"><span class="filename"><code>down</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result

///////////


//////////


////////// define
`uv`：<samp>array</samp>

- This is an alternate per-face uv mapping which specifies each face of the cube. Omitting a face will cause that face to not get drawn.


//////////

<div class="language-text highlight"><span class="filename"><code>uv</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`0..0`：<samp>number</samp>

- The x component of the uv.


///////////


/////////// define
`1..1`：<samp>number</samp>

- The y component of the uv.


///////////


//////////



/////////


////////


//////// define
`debug`：<samp>boolean</samp>


////////


//////// define
`inflate`：<samp>number</samp>

- Grow this box by this additive amount in all directions (in model space units).


////////


//////// define
`locators`：<samp>object</samp>

- This is a list of locators associated with this bone. A locator is a point in model space that tracks a particular bone as the bone animates (by maintaining it's relationship to the bone through the animation).


////////

<div class="language-text highlight"><span class="filename"><code>locators</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`offset`：<samp>array</samp>

- Position of the locator in model space.


//////////

<div class="language-text highlight"><span class="filename"><code>offset</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Position of the locator in model space.


///////////


//////////


////////// define
`rotation`：<samp>array</samp>

- Rotation of the locator in model space.


//////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Rotation of the locator in model space.


///////////


//////////


////////// define
`ignore_inherited_scale`：<samp>boolean</samp>

- Discard scale inherited from parent bone.


//////////


/////////


///////// define
`<any object property>`：<samp>array</samp>

- This is a list of locators associated with this bone. A locator is a point in model space that tracks a particular bone as the bone animates (by maintaining it's relationship to the bone through the animation).


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>number</samp>

- Position of the locator in model space.


//////////


/////////



////////


//////// define
`mirror`：<samp>boolean</samp>

- Mirrors the UV's of the unrotated cubes along the x axis, also causes the east/west faces to get flipped.


////////


//////// define
`name`：<samp>string</samp>

- Animation files refer to this bone via this identifier.


////////


//////// define
`parent`：<samp>string</samp>

- Bone that this bone is relative to. If the parent bone moves, this bone will move along with it.


////////


//////// define
`pivot`：<samp>array</samp>

- The bone pivots around this point (in model space units).


////////

<div class="language-text highlight"><span class="filename"><code>pivot</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>number</samp>


/////////


///////// define
`1..1`：<samp>number</samp>


/////////


///////// define
`2..2`：<samp>number</samp>


/////////


////////


//////// define
`poly_mesh`：<samp>object</samp>

- ***EXPERIMENTAL*** A triangle or quad mesh object. Can be used in conjunction with cubes and texture geometry.


////////

<div class="language-text highlight"><span class="filename"><code>poly_mesh</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`normalized_uvs`：<samp>boolean</samp>

- If true, UVs are assumed to be [0-1]. If false, UVs are assumed to be [0-texture_width] and [0-texture_height] respectively.


/////////


///////// define
`normals`：<samp>array</samp>

- Vertex normals. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and UVs sections.


/////////

<div class="language-text highlight"><span class="filename"><code>normals</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>array</samp>

- Vertex normals. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and UVs sections.


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Vertex normals. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and UVs sections.


///////////


//////////


/////////


///////// define
`polys`：<samp>string</samp>

- If not specifying vertex indices, arrays of data must be a list of tris or quads, set by making this property either `tri_list` or `quad_list`.


/////////


///////// define
`polys`：<samp>array</samp>

- Poly element indices, as an array of polygons, each an array of either three or four vertices, each an array of indices into positions, normals, and UVs (in that order).


/////////

<div class="language-text highlight"><span class="filename"><code>polys</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>array</samp>

- Poly element indices, as an array of polygons, each an array of either three or four vertices, each an array of indices into positions, normals, and UVs (in that order).


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>array</samp>


///////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////////// html | div.result
//////////// define
`0..0`：<samp>number</samp>

- The index of the position.


////////////


//////////// define
`1..1`：<samp>number</samp>

- The index of the normal vertex.


////////////


//////////// define
`2..2`：<samp>number</samp>

- The index of the uv vertex.


////////////


///////////


//////////


/////////



///////// define
`positions`：<samp>array</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>positions</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>array</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Vertex positions for the mesh. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the normals and UVs sections.


///////////


//////////


/////////


///////// define
`uvs`：<samp>array</samp>

- Vertex UVs. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and normals sections.


/////////

<div class="language-text highlight"><span class="filename"><code>uvs</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>array</samp>

- Vertex UVs. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and normals sections.


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- Vertex UVs. Can be either indexed via the `polys` section, or be a quad-list if mapped 1-to-1 to the positions and normals sections.


///////////


//////////


/////////


////////


//////// define
`render_group_id`：<samp>integer</samp>


////////


//////// define
`rotation`：<samp>array</samp>

- This is the initial rotation of the bone around the pivot, pre-animation (in degrees, x-then-y-then-z order).


////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>number</samp>

- in degrees.


/////////


///////// define
`1..1`：<samp>number</samp>

- in degrees.


/////////


///////// define
`2..2`：<samp>number</samp>

- in degrees.


/////////


////////


//////// define
`texture_meshes`：<samp>array</samp>

- ***EXPERIMENTAL*** Adds a mesh to the bone's geometry by converting texels in a texture into boxes.


////////

<div class="language-text highlight"><span class="filename"><code>texture_meshes</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`local_pivot`：<samp>array</samp>

- The pivot point on the texture (in *texture space* not entity or bone space) of the texture geometry.


//////////

<div class="language-text highlight"><span class="filename"><code>local_pivot</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The pivot point on the texture (in *texture space* not entity or bone space) of the texture geometry.


///////////


//////////


////////// define
`position`：<samp>array</samp>

- The position of the pivot point after rotation (in *entity space* not texture or bone space) of the texture geometry.


//////////

<div class="language-text highlight"><span class="filename"><code>position</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The position of the pivot point after rotation (in *entity space* not texture or bone space) of the texture geometry.


///////////


//////////


////////// define
`rotation`：<samp>array</samp>

- The rotation (in degrees) of the texture geometry relative to the offset.


//////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The rotation (in degrees) of the texture geometry relative to the offset.


///////////


//////////


////////// define
`scale`：<samp>array</samp>

- The scale (in degrees) of the texture geometry relative to the offset.


//////////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>number</samp>

- The scale (in degrees) of the texture geometry relative to the offset.


///////////


//////////


////////// define
`texture`：<samp>string</samp>

- The friendly-named texture to use.


//////////


/////////


////////


///////


//////


////// define
`cape`：<samp>string</samp>

- UNDOCUMENTED.


//////


/////


////


///




