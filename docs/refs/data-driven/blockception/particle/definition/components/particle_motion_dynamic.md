# Particle Motion Dynamic Component For 1.10.0

> 文档版本：1.21.0.24

This component specifies the dynamic properties of the particle, from a simulation standpoint what forces act upon the particle? These dynamics alter the velocity of the particle, which is a combination of the direction of the particle and the speed. Particle direction will always be in the direction of the velocity of the particle.

## 架构

```mcschema
particle_motion_dynamic:
{
  array "linear_acceleration" : opt
  {
    0 "<any array element>"
  }
  0 "linear_drag_coefficient"
  0 "rotation_acceleration"
  0 "rotation_drag_coefficient"
}

```

/// html | div.result
//// define
`linear_acceleration`：<samp>array</samp>

- The linear acceleration applied to the particle. Units are blocks/sec/sec


////

<div class="language-text highlight"><span class="filename"><code>linear_acceleration</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}


/////

```mcschema
0:
string

```

///// html | div.result

/////


```mcschema
0:
number

```

///// html | div.result

/////




////


//// define
`linear_drag_coefficient`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Using the equation: `acceleration = -linear_drag_coefficient*velocity` where velocity is the current direction times speed. Think of this as air-drag. The higher the value, the more drag evaluated every frame


////


//// define
`rotation_acceleration`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Acceleration applies to the rotation speed of the particle.


////


//// define
`rotation_drag_coefficient`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Drag applied to rotation.


////


///

