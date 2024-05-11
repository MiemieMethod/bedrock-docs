# Game Event Movement Tracking

> 文档版本：1.21.0.24

Allows an entity to emit `entityMove`, `swim` and `flap` game events, depending on the block the entity is moving through. It is added by default to every mob. Add it again to override its behavior.

## 架构

```mcschema
game_event_movement_tracking:
{
  boolean "emit_flap" : opt
  boolean "emit_move" : opt
  boolean "emit_swim" : opt
}

```

/// html | div.result
//// define
`emit_flap`：<samp>boolean</samp>

- If true, the `flap` game event will be emitted when the entity moves through air.


////


//// define
`emit_move`：<samp>boolean</samp>

- If true, the `entityMove` game event will be emitted when the entity moves on ground or through a solid.


////


//// define
`emit_swim`：<samp>boolean</samp>

- If true, the `swim` game event will be emitted when the entity moves through a liquid.


////


///

