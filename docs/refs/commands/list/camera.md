# `/camera`

> 文档版本：1.21.50.25

`/camera`命令command.camera.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> pos <position:x y z> rot <xRot:value> <yRot:value>
```

//// html | div.result
command.camera.1.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`ease`：<!-- md:samp ease -->

- 枚举类型。command.enum.ease.description单值枚举，请直接使用`ease`。

`easeTime`：<!-- md:samp float -->

- 基本类型。command.camera.easeTime.description

`easeType`：<!-- md:samp Easing -->

- 枚举类型。command.enum.easing.description枚举值如下：

  |值|描述|
  |---|---|
  |`linear`|command.enum.easing.linear|
  |`spring`|command.enum.easing.spring|
  |`in_quad`|command.enum.easing.in_quad|
  |`out_quad`|command.enum.easing.out_quad|
  |`in_out_quad`|command.enum.easing.in_out_quad|
  |`in_cubic`|command.enum.easing.in_cubic|
  |`out_cubic`|command.enum.easing.out_cubic|
  |`in_out_cubic`|command.enum.easing.in_out_cubic|
  |`in_quart`|command.enum.easing.in_quart|
  |`out_quart`|command.enum.easing.out_quart|
  |`in_out_quart`|command.enum.easing.in_out_quart|
  |`in_quint`|command.enum.easing.in_quint|
  |`out_quint`|command.enum.easing.out_quint|
  |`in_out_quint`|command.enum.easing.in_out_quint|
  |`in_sine`|command.enum.easing.in_sine|
  |`out_sine`|command.enum.easing.out_sine|
  |`in_out_sine`|command.enum.easing.in_out_sine|
  |`in_expo`|command.enum.easing.in_expo|
  |`out_expo`|command.enum.easing.out_expo|
  |`in_out_expo`|command.enum.easing.in_out_expo|
  |`in_circ`|command.enum.easing.in_circ|
  |`out_circ`|command.enum.easing.out_circ|
  |`in_out_circ`|command.enum.easing.in_out_circ|
  |`in_bounce`|command.enum.easing.in_bounce|
  |`out_bounce`|command.enum.easing.out_bounce|
  |`in_out_bounce`|command.enum.easing.in_out_bounce|
  |`in_back`|command.enum.easing.in_back|
  |`out_back`|command.enum.easing.out_back|
  |`in_out_back`|command.enum.easing.in_out_back|
  |`in_elastic`|command.enum.easing.in_elastic|
  |`out_elastic`|command.enum.easing.out_elastic|
  |`in_out_elastic`|command.enum.easing.in_out_elastic|


`pos`：<!-- md:samp pos -->

- 枚举类型。command.enum.pos.description单值枚举，请直接使用`pos`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.camera.position.description

`rot`：<!-- md:samp rot -->

- 枚举类型。command.enum.rot.description单值枚举，请直接使用`rot`。

`xRot`：<!-- md:samp value -->

- 基本类型。command.camera.xRot.description

`yRot`：<!-- md:samp value -->

- 基本类型。command.camera.yRot.description


/////

////

///

/// tab | 重载2
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> pos <position:x y z> facing <lookAtEntity:target>
```

//// html | div.result
command.camera.2.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`ease`：<!-- md:samp ease -->

- 枚举类型。command.enum.ease.description单值枚举，请直接使用`ease`。

`easeTime`：<!-- md:samp float -->

- 基本类型。command.camera.easeTime.description

`easeType`：<!-- md:samp Easing -->

- 枚举类型。command.enum.easing.description枚举值如下：

  |值|描述|
  |---|---|
  |`linear`|command.enum.easing.linear|
  |`spring`|command.enum.easing.spring|
  |`in_quad`|command.enum.easing.in_quad|
  |`out_quad`|command.enum.easing.out_quad|
  |`in_out_quad`|command.enum.easing.in_out_quad|
  |`in_cubic`|command.enum.easing.in_cubic|
  |`out_cubic`|command.enum.easing.out_cubic|
  |`in_out_cubic`|command.enum.easing.in_out_cubic|
  |`in_quart`|command.enum.easing.in_quart|
  |`out_quart`|command.enum.easing.out_quart|
  |`in_out_quart`|command.enum.easing.in_out_quart|
  |`in_quint`|command.enum.easing.in_quint|
  |`out_quint`|command.enum.easing.out_quint|
  |`in_out_quint`|command.enum.easing.in_out_quint|
  |`in_sine`|command.enum.easing.in_sine|
  |`out_sine`|command.enum.easing.out_sine|
  |`in_out_sine`|command.enum.easing.in_out_sine|
  |`in_expo`|command.enum.easing.in_expo|
  |`out_expo`|command.enum.easing.out_expo|
  |`in_out_expo`|command.enum.easing.in_out_expo|
  |`in_circ`|command.enum.easing.in_circ|
  |`out_circ`|command.enum.easing.out_circ|
  |`in_out_circ`|command.enum.easing.in_out_circ|
  |`in_bounce`|command.enum.easing.in_bounce|
  |`out_bounce`|command.enum.easing.out_bounce|
  |`in_out_bounce`|command.enum.easing.in_out_bounce|
  |`in_back`|command.enum.easing.in_back|
  |`out_back`|command.enum.easing.out_back|
  |`in_out_back`|command.enum.easing.in_out_back|
  |`in_elastic`|command.enum.easing.in_elastic|
  |`out_elastic`|command.enum.easing.out_elastic|
  |`in_out_elastic`|command.enum.easing.in_out_elastic|


`pos`：<!-- md:samp pos -->

- 枚举类型。command.enum.pos.description单值枚举，请直接使用`pos`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.camera.position.description

`facing`：<!-- md:samp facing -->

- 枚举类型。command.enum.facing.description单值枚举，请直接使用`facing`。

`lookAtEntity`：<!-- md:samp target -->

- 基本类型。command.camera.lookAtEntity.description


/////

////

///

/// tab | 重载3
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> pos <position:x y z> facing <lookAtPosition:x y z>
```

//// html | div.result
command.camera.3.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`ease`：<!-- md:samp ease -->

- 枚举类型。command.enum.ease.description单值枚举，请直接使用`ease`。

`easeTime`：<!-- md:samp float -->

- 基本类型。command.camera.easeTime.description

`easeType`：<!-- md:samp Easing -->

- 枚举类型。command.enum.easing.description枚举值如下：

  |值|描述|
  |---|---|
  |`linear`|command.enum.easing.linear|
  |`spring`|command.enum.easing.spring|
  |`in_quad`|command.enum.easing.in_quad|
  |`out_quad`|command.enum.easing.out_quad|
  |`in_out_quad`|command.enum.easing.in_out_quad|
  |`in_cubic`|command.enum.easing.in_cubic|
  |`out_cubic`|command.enum.easing.out_cubic|
  |`in_out_cubic`|command.enum.easing.in_out_cubic|
  |`in_quart`|command.enum.easing.in_quart|
  |`out_quart`|command.enum.easing.out_quart|
  |`in_out_quart`|command.enum.easing.in_out_quart|
  |`in_quint`|command.enum.easing.in_quint|
  |`out_quint`|command.enum.easing.out_quint|
  |`in_out_quint`|command.enum.easing.in_out_quint|
  |`in_sine`|command.enum.easing.in_sine|
  |`out_sine`|command.enum.easing.out_sine|
  |`in_out_sine`|command.enum.easing.in_out_sine|
  |`in_expo`|command.enum.easing.in_expo|
  |`out_expo`|command.enum.easing.out_expo|
  |`in_out_expo`|command.enum.easing.in_out_expo|
  |`in_circ`|command.enum.easing.in_circ|
  |`out_circ`|command.enum.easing.out_circ|
  |`in_out_circ`|command.enum.easing.in_out_circ|
  |`in_bounce`|command.enum.easing.in_bounce|
  |`out_bounce`|command.enum.easing.out_bounce|
  |`in_out_bounce`|command.enum.easing.in_out_bounce|
  |`in_back`|command.enum.easing.in_back|
  |`out_back`|command.enum.easing.out_back|
  |`in_out_back`|command.enum.easing.in_out_back|
  |`in_elastic`|command.enum.easing.in_elastic|
  |`out_elastic`|command.enum.easing.out_elastic|
  |`in_out_elastic`|command.enum.easing.in_out_elastic|


`pos`：<!-- md:samp pos -->

- 枚举类型。command.enum.pos.description单值枚举，请直接使用`pos`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.camera.position.description

`facing`：<!-- md:samp facing -->

- 枚举类型。command.enum.facing.description单值枚举，请直接使用`facing`。

`lookAtPosition`：<!-- md:samp x y z -->

- 基本类型。command.camera.lookAtPosition.description


/////

////

///

/// tab | 重载4
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> pos <position:x y z>
```

//// html | div.result
command.camera.4.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`ease`：<!-- md:samp ease -->

- 枚举类型。command.enum.ease.description单值枚举，请直接使用`ease`。

`easeTime`：<!-- md:samp float -->

- 基本类型。command.camera.easeTime.description

`easeType`：<!-- md:samp Easing -->

- 枚举类型。command.enum.easing.description枚举值如下：

  |值|描述|
  |---|---|
  |`linear`|command.enum.easing.linear|
  |`spring`|command.enum.easing.spring|
  |`in_quad`|command.enum.easing.in_quad|
  |`out_quad`|command.enum.easing.out_quad|
  |`in_out_quad`|command.enum.easing.in_out_quad|
  |`in_cubic`|command.enum.easing.in_cubic|
  |`out_cubic`|command.enum.easing.out_cubic|
  |`in_out_cubic`|command.enum.easing.in_out_cubic|
  |`in_quart`|command.enum.easing.in_quart|
  |`out_quart`|command.enum.easing.out_quart|
  |`in_out_quart`|command.enum.easing.in_out_quart|
  |`in_quint`|command.enum.easing.in_quint|
  |`out_quint`|command.enum.easing.out_quint|
  |`in_out_quint`|command.enum.easing.in_out_quint|
  |`in_sine`|command.enum.easing.in_sine|
  |`out_sine`|command.enum.easing.out_sine|
  |`in_out_sine`|command.enum.easing.in_out_sine|
  |`in_expo`|command.enum.easing.in_expo|
  |`out_expo`|command.enum.easing.out_expo|
  |`in_out_expo`|command.enum.easing.in_out_expo|
  |`in_circ`|command.enum.easing.in_circ|
  |`out_circ`|command.enum.easing.out_circ|
  |`in_out_circ`|command.enum.easing.in_out_circ|
  |`in_bounce`|command.enum.easing.in_bounce|
  |`out_bounce`|command.enum.easing.out_bounce|
  |`in_out_bounce`|command.enum.easing.in_out_bounce|
  |`in_back`|command.enum.easing.in_back|
  |`out_back`|command.enum.easing.out_back|
  |`in_out_back`|command.enum.easing.in_out_back|
  |`in_elastic`|command.enum.easing.in_elastic|
  |`out_elastic`|command.enum.easing.out_elastic|
  |`in_out_elastic`|command.enum.easing.in_out_elastic|


`pos`：<!-- md:samp pos -->

- 枚举类型。command.enum.pos.description单值枚举，请直接使用`pos`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.camera.position.description


/////

////

///

/// tab | 重载5
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> rot <xRot:value> <yRot:value>
```

//// html | div.result
command.camera.5.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`ease`：<!-- md:samp ease -->

- 枚举类型。command.enum.ease.description单值枚举，请直接使用`ease`。

`easeTime`：<!-- md:samp float -->

- 基本类型。command.camera.easeTime.description

`easeType`：<!-- md:samp Easing -->

- 枚举类型。command.enum.easing.description枚举值如下：

  |值|描述|
  |---|---|
  |`linear`|command.enum.easing.linear|
  |`spring`|command.enum.easing.spring|
  |`in_quad`|command.enum.easing.in_quad|
  |`out_quad`|command.enum.easing.out_quad|
  |`in_out_quad`|command.enum.easing.in_out_quad|
  |`in_cubic`|command.enum.easing.in_cubic|
  |`out_cubic`|command.enum.easing.out_cubic|
  |`in_out_cubic`|command.enum.easing.in_out_cubic|
  |`in_quart`|command.enum.easing.in_quart|
  |`out_quart`|command.enum.easing.out_quart|
  |`in_out_quart`|command.enum.easing.in_out_quart|
  |`in_quint`|command.enum.easing.in_quint|
  |`out_quint`|command.enum.easing.out_quint|
  |`in_out_quint`|command.enum.easing.in_out_quint|
  |`in_sine`|command.enum.easing.in_sine|
  |`out_sine`|command.enum.easing.out_sine|
  |`in_out_sine`|command.enum.easing.in_out_sine|
  |`in_expo`|command.enum.easing.in_expo|
  |`out_expo`|command.enum.easing.out_expo|
  |`in_out_expo`|command.enum.easing.in_out_expo|
  |`in_circ`|command.enum.easing.in_circ|
  |`out_circ`|command.enum.easing.out_circ|
  |`in_out_circ`|command.enum.easing.in_out_circ|
  |`in_bounce`|command.enum.easing.in_bounce|
  |`out_bounce`|command.enum.easing.out_bounce|
  |`in_out_bounce`|command.enum.easing.in_out_bounce|
  |`in_back`|command.enum.easing.in_back|
  |`out_back`|command.enum.easing.out_back|
  |`in_out_back`|command.enum.easing.in_out_back|
  |`in_elastic`|command.enum.easing.in_elastic|
  |`out_elastic`|command.enum.easing.out_elastic|
  |`in_out_elastic`|command.enum.easing.in_out_elastic|


`rot`：<!-- md:samp rot -->

- 枚举类型。command.enum.rot.description单值枚举，请直接使用`rot`。

`xRot`：<!-- md:samp value -->

- 基本类型。command.camera.xRot.description

`yRot`：<!-- md:samp value -->

- 基本类型。command.camera.yRot.description


/////

////

///

/// tab | 重载6
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> facing <lookAtEntity:target>
```

//// html | div.result
command.camera.6.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`ease`：<!-- md:samp ease -->

- 枚举类型。command.enum.ease.description单值枚举，请直接使用`ease`。

`easeTime`：<!-- md:samp float -->

- 基本类型。command.camera.easeTime.description

`easeType`：<!-- md:samp Easing -->

- 枚举类型。command.enum.easing.description枚举值如下：

  |值|描述|
  |---|---|
  |`linear`|command.enum.easing.linear|
  |`spring`|command.enum.easing.spring|
  |`in_quad`|command.enum.easing.in_quad|
  |`out_quad`|command.enum.easing.out_quad|
  |`in_out_quad`|command.enum.easing.in_out_quad|
  |`in_cubic`|command.enum.easing.in_cubic|
  |`out_cubic`|command.enum.easing.out_cubic|
  |`in_out_cubic`|command.enum.easing.in_out_cubic|
  |`in_quart`|command.enum.easing.in_quart|
  |`out_quart`|command.enum.easing.out_quart|
  |`in_out_quart`|command.enum.easing.in_out_quart|
  |`in_quint`|command.enum.easing.in_quint|
  |`out_quint`|command.enum.easing.out_quint|
  |`in_out_quint`|command.enum.easing.in_out_quint|
  |`in_sine`|command.enum.easing.in_sine|
  |`out_sine`|command.enum.easing.out_sine|
  |`in_out_sine`|command.enum.easing.in_out_sine|
  |`in_expo`|command.enum.easing.in_expo|
  |`out_expo`|command.enum.easing.out_expo|
  |`in_out_expo`|command.enum.easing.in_out_expo|
  |`in_circ`|command.enum.easing.in_circ|
  |`out_circ`|command.enum.easing.out_circ|
  |`in_out_circ`|command.enum.easing.in_out_circ|
  |`in_bounce`|command.enum.easing.in_bounce|
  |`out_bounce`|command.enum.easing.out_bounce|
  |`in_out_bounce`|command.enum.easing.in_out_bounce|
  |`in_back`|command.enum.easing.in_back|
  |`out_back`|command.enum.easing.out_back|
  |`in_out_back`|command.enum.easing.in_out_back|
  |`in_elastic`|command.enum.easing.in_elastic|
  |`out_elastic`|command.enum.easing.out_elastic|
  |`in_out_elastic`|command.enum.easing.in_out_elastic|


`facing`：<!-- md:samp facing -->

- 枚举类型。command.enum.facing.description单值枚举，请直接使用`facing`。

`lookAtEntity`：<!-- md:samp target -->

- 基本类型。command.camera.lookAtEntity.description


/////

////

///

/// tab | 重载7
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> facing <lookAtPosition:x y z>
```

//// html | div.result
command.camera.7.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`ease`：<!-- md:samp ease -->

- 枚举类型。command.enum.ease.description单值枚举，请直接使用`ease`。

`easeTime`：<!-- md:samp float -->

- 基本类型。command.camera.easeTime.description

`easeType`：<!-- md:samp Easing -->

- 枚举类型。command.enum.easing.description枚举值如下：

  |值|描述|
  |---|---|
  |`linear`|command.enum.easing.linear|
  |`spring`|command.enum.easing.spring|
  |`in_quad`|command.enum.easing.in_quad|
  |`out_quad`|command.enum.easing.out_quad|
  |`in_out_quad`|command.enum.easing.in_out_quad|
  |`in_cubic`|command.enum.easing.in_cubic|
  |`out_cubic`|command.enum.easing.out_cubic|
  |`in_out_cubic`|command.enum.easing.in_out_cubic|
  |`in_quart`|command.enum.easing.in_quart|
  |`out_quart`|command.enum.easing.out_quart|
  |`in_out_quart`|command.enum.easing.in_out_quart|
  |`in_quint`|command.enum.easing.in_quint|
  |`out_quint`|command.enum.easing.out_quint|
  |`in_out_quint`|command.enum.easing.in_out_quint|
  |`in_sine`|command.enum.easing.in_sine|
  |`out_sine`|command.enum.easing.out_sine|
  |`in_out_sine`|command.enum.easing.in_out_sine|
  |`in_expo`|command.enum.easing.in_expo|
  |`out_expo`|command.enum.easing.out_expo|
  |`in_out_expo`|command.enum.easing.in_out_expo|
  |`in_circ`|command.enum.easing.in_circ|
  |`out_circ`|command.enum.easing.out_circ|
  |`in_out_circ`|command.enum.easing.in_out_circ|
  |`in_bounce`|command.enum.easing.in_bounce|
  |`out_bounce`|command.enum.easing.out_bounce|
  |`in_out_bounce`|command.enum.easing.in_out_bounce|
  |`in_back`|command.enum.easing.in_back|
  |`out_back`|command.enum.easing.out_back|
  |`in_out_back`|command.enum.easing.in_out_back|
  |`in_elastic`|command.enum.easing.in_elastic|
  |`out_elastic`|command.enum.easing.out_elastic|
  |`in_out_elastic`|command.enum.easing.in_out_elastic|


`facing`：<!-- md:samp facing -->

- 枚举类型。command.enum.facing.description单值枚举，请直接使用`facing`。

`lookAtPosition`：<!-- md:samp x y z -->

- 基本类型。command.camera.lookAtPosition.description


/////

////

///

/// tab | 重载8
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> default
```

//// html | div.result
command.camera.8.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`ease`：<!-- md:samp ease -->

- 枚举类型。command.enum.ease.description单值枚举，请直接使用`ease`。

`easeTime`：<!-- md:samp float -->

- 基本类型。command.camera.easeTime.description

`easeType`：<!-- md:samp Easing -->

- 枚举类型。command.enum.easing.description枚举值如下：

  |值|描述|
  |---|---|
  |`linear`|command.enum.easing.linear|
  |`spring`|command.enum.easing.spring|
  |`in_quad`|command.enum.easing.in_quad|
  |`out_quad`|command.enum.easing.out_quad|
  |`in_out_quad`|command.enum.easing.in_out_quad|
  |`in_cubic`|command.enum.easing.in_cubic|
  |`out_cubic`|command.enum.easing.out_cubic|
  |`in_out_cubic`|command.enum.easing.in_out_cubic|
  |`in_quart`|command.enum.easing.in_quart|
  |`out_quart`|command.enum.easing.out_quart|
  |`in_out_quart`|command.enum.easing.in_out_quart|
  |`in_quint`|command.enum.easing.in_quint|
  |`out_quint`|command.enum.easing.out_quint|
  |`in_out_quint`|command.enum.easing.in_out_quint|
  |`in_sine`|command.enum.easing.in_sine|
  |`out_sine`|command.enum.easing.out_sine|
  |`in_out_sine`|command.enum.easing.in_out_sine|
  |`in_expo`|command.enum.easing.in_expo|
  |`out_expo`|command.enum.easing.out_expo|
  |`in_out_expo`|command.enum.easing.in_out_expo|
  |`in_circ`|command.enum.easing.in_circ|
  |`out_circ`|command.enum.easing.out_circ|
  |`in_out_circ`|command.enum.easing.in_out_circ|
  |`in_bounce`|command.enum.easing.in_bounce|
  |`out_bounce`|command.enum.easing.out_bounce|
  |`in_out_bounce`|command.enum.easing.in_out_bounce|
  |`in_back`|command.enum.easing.in_back|
  |`out_back`|command.enum.easing.out_back|
  |`in_out_back`|command.enum.easing.in_out_back|
  |`in_elastic`|command.enum.easing.in_elastic|
  |`out_elastic`|command.enum.easing.out_elastic|
  |`in_out_elastic`|command.enum.easing.in_out_elastic|


`default`：<!-- md:samp default -->

- 枚举类型，可选。command.enum.default.description单值枚举，请直接使用`default`。


/////

////

///

/// tab | 重载9
```mcfunction
/camera <players:target> set <preset:CameraPresets> pos <position:x y z> rot <xRot:value> <yRot:value>
```

//// html | div.result
command.camera.9.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`pos`：<!-- md:samp pos -->

- 枚举类型。command.enum.pos.description单值枚举，请直接使用`pos`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.camera.position.description

`rot`：<!-- md:samp rot -->

- 枚举类型。command.enum.rot.description单值枚举，请直接使用`rot`。

`xRot`：<!-- md:samp value -->

- 基本类型。command.camera.xRot.description

`yRot`：<!-- md:samp value -->

- 基本类型。command.camera.yRot.description


/////

////

///

/// tab | 重载10
```mcfunction
/camera <players:target> set <preset:CameraPresets> pos <position:x y z> facing <lookAtEntity:target>
```

//// html | div.result
command.camera.10.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`pos`：<!-- md:samp pos -->

- 枚举类型。command.enum.pos.description单值枚举，请直接使用`pos`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.camera.position.description

`facing`：<!-- md:samp facing -->

- 枚举类型。command.enum.facing.description单值枚举，请直接使用`facing`。

`lookAtEntity`：<!-- md:samp target -->

- 基本类型。command.camera.lookAtEntity.description


/////

////

///

/// tab | 重载11
```mcfunction
/camera <players:target> set <preset:CameraPresets> pos <position:x y z> facing <lookAtPosition:x y z>
```

//// html | div.result
command.camera.11.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`pos`：<!-- md:samp pos -->

- 枚举类型。command.enum.pos.description单值枚举，请直接使用`pos`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.camera.position.description

`facing`：<!-- md:samp facing -->

- 枚举类型。command.enum.facing.description单值枚举，请直接使用`facing`。

`lookAtPosition`：<!-- md:samp x y z -->

- 基本类型。command.camera.lookAtPosition.description


/////

////

///

/// tab | 重载12
```mcfunction
/camera <players:target> target_entity <entity:target>
```

//// html | div.result
command.camera.12.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`targetEntity`：<!-- md:samp target_entity -->

- 枚举类型。command.enum.target_entity.description单值枚举，请直接使用`target_entity`。

`entity`：<!-- md:samp target -->

- 基本类型。command.camera.entity.description


/////

////

///

/// tab | 重载13
```mcfunction
/camera <players:target> target_entity <entity:target> target_center_offset <xTargetCenterOffset:float> <yTargetCenterOffset:float> <zTargetCenterOffset:float>
```

//// html | div.result
command.camera.13.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`targetEntity`：<!-- md:samp target_entity -->

- 枚举类型。command.enum.target_entity.description单值枚举，请直接使用`target_entity`。

`entity`：<!-- md:samp target -->

- 基本类型。command.camera.entity.description

`targetCenterOffset`：<!-- md:samp target_center_offset -->

- 枚举类型。command.enum.target_center_offset.description单值枚举，请直接使用`target_center_offset`。

`xTargetCenterOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xTargetCenterOffset.description

`yTargetCenterOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yTargetCenterOffset.description

`zTargetCenterOffset`：<!-- md:samp float -->

- 基本类型。command.camera.zTargetCenterOffset.description


/////

////

///

/// tab | 重载14
```mcfunction
/camera <players:target> remove_target
```

//// html | div.result
command.camera.14.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`removeTarget`：<!-- md:samp remove_target -->

- 枚举类型。command.enum.remove_target.description单值枚举，请直接使用`remove_target`。


/////

////

///

/// tab | 重载15
```mcfunction
/camera <players:target> set <preset:CameraPresets> view_offset <xViewOffset:float> <yViewOffset:float>
```

//// html | div.result
command.camera.15.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`view_offset`：<!-- md:samp view_offset -->

- 枚举类型。command.enum.view_offset.description单值枚举，请直接使用`view_offset`。

`xViewOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xViewOffset.description

`yViewOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yViewOffset.description


/////

////

///

/// tab | 重载16
```mcfunction
/camera <players:target> set <preset:CameraPresets> entity_offset <xEntityOffset:float> <yEntityOffset:float> <zEntityOffset:float>
```

//// html | div.result
command.camera.16.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`entity_offset`：<!-- md:samp entity_offset -->

- 枚举类型。command.enum.entity_offset.description单值枚举，请直接使用`entity_offset`。

`xEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xEntityOffset.description

`yEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yEntityOffset.description

`zEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.zEntityOffset.description


/////

////

///

/// tab | 重载17
```mcfunction
/camera <players:target> set <preset:CameraPresets> rot <xRot:value> <yRot:value> view_offset <xViewOffset:float> <yViewOffset:float>
```

//// html | div.result
command.camera.17.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`rot`：<!-- md:samp rot -->

- 枚举类型。command.enum.rot.description单值枚举，请直接使用`rot`。

`xRot`：<!-- md:samp value -->

- 基本类型。command.camera.xRot.description

`yRot`：<!-- md:samp value -->

- 基本类型。command.camera.yRot.description

`view_offset`：<!-- md:samp view_offset -->

- 枚举类型。command.enum.view_offset.description单值枚举，请直接使用`view_offset`。

`xViewOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xViewOffset.description

`yViewOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yViewOffset.description


/////

////

///

/// tab | 重载18
```mcfunction
/camera <players:target> set <preset:CameraPresets> rot <xRot:value> <yRot:value> entity_offset <xEntityOffset:float> <yEntityOffset:float> <zEntityOffset:float>
```

//// html | div.result
command.camera.18.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`rot`：<!-- md:samp rot -->

- 枚举类型。command.enum.rot.description单值枚举，请直接使用`rot`。

`xRot`：<!-- md:samp value -->

- 基本类型。command.camera.xRot.description

`yRot`：<!-- md:samp value -->

- 基本类型。command.camera.yRot.description

`entity_offset`：<!-- md:samp entity_offset -->

- 枚举类型。command.enum.entity_offset.description单值枚举，请直接使用`entity_offset`。

`xEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xEntityOffset.description

`yEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yEntityOffset.description

`zEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.zEntityOffset.description


/////

////

///

/// tab | 重载19
```mcfunction
/camera <players:target> set <preset:CameraPresets> view_offset <xViewOffset:float> <yViewOffset:float> entity_offset <xEntityOffset:float> <yEntityOffset:float> <zEntityOffset:float>
```

//// html | div.result
command.camera.19.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`view_offset`：<!-- md:samp view_offset -->

- 枚举类型。command.enum.view_offset.description单值枚举，请直接使用`view_offset`。

`xViewOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xViewOffset.description

`yViewOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yViewOffset.description

`entity_offset`：<!-- md:samp entity_offset -->

- 枚举类型。command.enum.entity_offset.description单值枚举，请直接使用`entity_offset`。

`xEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xEntityOffset.description

`yEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yEntityOffset.description

`zEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.zEntityOffset.description


/////

////

///

/// tab | 重载20
```mcfunction
/camera <players:target> set <preset:CameraPresets> rot <xRot:value> <yRot:value> view_offset <xViewOffset:float> <yViewOffset:float> entity_offset <xEntityOffset:float> <yEntityOffset:float> <zEntityOffset:float>
```

//// html | div.result
command.camera.20.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`rot`：<!-- md:samp rot -->

- 枚举类型。command.enum.rot.description单值枚举，请直接使用`rot`。

`xRot`：<!-- md:samp value -->

- 基本类型。command.camera.xRot.description

`yRot`：<!-- md:samp value -->

- 基本类型。command.camera.yRot.description

`view_offset`：<!-- md:samp view_offset -->

- 枚举类型。command.enum.view_offset.description单值枚举，请直接使用`view_offset`。

`xViewOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xViewOffset.description

`yViewOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yViewOffset.description

`entity_offset`：<!-- md:samp entity_offset -->

- 枚举类型。command.enum.entity_offset.description单值枚举，请直接使用`entity_offset`。

`xEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.xEntityOffset.description

`yEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.yEntityOffset.description

`zEntityOffset`：<!-- md:samp float -->

- 基本类型。command.camera.zEntityOffset.description


/////

////

///

/// tab | 重载21
```mcfunction
/camera <players:target> set <preset:CameraPresets> pos <position:x y z>
```

//// html | div.result
command.camera.21.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`pos`：<!-- md:samp pos -->

- 枚举类型。command.enum.pos.description单值枚举，请直接使用`pos`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.camera.position.description


/////

////

///

/// tab | 重载22
```mcfunction
/camera <players:target> set <preset:CameraPresets> rot <xRot:value> <yRot:value>
```

//// html | div.result
command.camera.22.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`rot`：<!-- md:samp rot -->

- 枚举类型。command.enum.rot.description单值枚举，请直接使用`rot`。

`xRot`：<!-- md:samp value -->

- 基本类型。command.camera.xRot.description

`yRot`：<!-- md:samp value -->

- 基本类型。command.camera.yRot.description


/////

////

///

/// tab | 重载23
```mcfunction
/camera <players:target> set <preset:CameraPresets> facing <lookAtEntity:target>
```

//// html | div.result
command.camera.23.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`facing`：<!-- md:samp facing -->

- 枚举类型。command.enum.facing.description单值枚举，请直接使用`facing`。

`lookAtEntity`：<!-- md:samp target -->

- 基本类型。command.camera.lookAtEntity.description


/////

////

///

/// tab | 重载24
```mcfunction
/camera <players:target> set <preset:CameraPresets> facing <lookAtPosition:x y z>
```

//// html | div.result
command.camera.24.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`facing`：<!-- md:samp facing -->

- 枚举类型。command.enum.facing.description单值枚举，请直接使用`facing`。

`lookAtPosition`：<!-- md:samp x y z -->

- 基本类型。command.camera.lookAtPosition.description


/////

////

///

/// tab | 重载25
```mcfunction
/camera <players:target> set <preset:CameraPresets> default
```

//// html | div.result
command.camera.25.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`set`：<!-- md:samp set -->

- 枚举类型。command.enum.set.description单值枚举，请直接使用`set`。

`preset`：<!-- md:samp CameraPresets -->

- 枚举类型。command.enum.camerapresets.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:first_person`|command.enum.camerapresets.minecraft:first_person|
  |`minecraft:follow_orbit`|command.enum.camerapresets.minecraft:follow_orbit|
  |`minecraft:free`|command.enum.camerapresets.minecraft:free|
  |`minecraft:third_person`|command.enum.camerapresets.minecraft:third_person|
  |`minecraft:third_person_front`|command.enum.camerapresets.minecraft:third_person_front|
  |`minecraft:fixed_boom`|command.enum.camerapresets.minecraft:fixed_boom|


`default`：<!-- md:samp default -->

- 枚举类型，可选。command.enum.default.description单值枚举，请直接使用`default`。


/////

////

///

/// tab | 重载26
```mcfunction
/camera <players:target> clear
```

//// html | div.result
command.camera.26.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`clear`：<!-- md:samp clear -->

- 枚举类型。command.enum.clear.description单值枚举，请直接使用`clear`。


/////

////

///

/// tab | 重载27
```mcfunction
/camera <players:target> fade time <fadeInSeconds:float> <holdSeconds:float> <fadeOutSeconds:float> color <red:int> <green:int> <blue:int>
```

//// html | div.result
command.camera.27.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`fade`：<!-- md:samp fade -->

- 枚举类型。command.enum.fade.description单值枚举，请直接使用`fade`。

`time`：<!-- md:samp time -->

- 枚举类型。command.enum.time.description单值枚举，请直接使用`time`。

`fadeInSeconds`：<!-- md:samp float -->

- 基本类型。command.camera.fadeInSeconds.description

`holdSeconds`：<!-- md:samp float -->

- 基本类型。command.camera.holdSeconds.description

`fadeOutSeconds`：<!-- md:samp float -->

- 基本类型。command.camera.fadeOutSeconds.description

`color`：<!-- md:samp color -->

- 枚举类型。command.enum.color.description单值枚举，请直接使用`color`。

`red`：<!-- md:samp int -->

- 基本类型。command.camera.red.description

`green`：<!-- md:samp int -->

- 基本类型。command.camera.green.description

`blue`：<!-- md:samp int -->

- 基本类型。command.camera.blue.description


/////

////

///

/// tab | 重载28
```mcfunction
/camera <players:target> fade time <fadeInSeconds:float> <holdSeconds:float> <fadeOutSeconds:float>
```

//// html | div.result
command.camera.28.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`fade`：<!-- md:samp fade -->

- 枚举类型。command.enum.fade.description单值枚举，请直接使用`fade`。

`time`：<!-- md:samp time -->

- 枚举类型。command.enum.time.description单值枚举，请直接使用`time`。

`fadeInSeconds`：<!-- md:samp float -->

- 基本类型。command.camera.fadeInSeconds.description

`holdSeconds`：<!-- md:samp float -->

- 基本类型。command.camera.holdSeconds.description

`fadeOutSeconds`：<!-- md:samp float -->

- 基本类型。command.camera.fadeOutSeconds.description


/////

////

///

/// tab | 重载29
```mcfunction
/camera <players:target> fade color <red:int> <green:int> <blue:int>
```

//// html | div.result
command.camera.29.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`fade`：<!-- md:samp fade -->

- 枚举类型。command.enum.fade.description单值枚举，请直接使用`fade`。

`color`：<!-- md:samp color -->

- 枚举类型。command.enum.color.description单值枚举，请直接使用`color`。

`red`：<!-- md:samp int -->

- 基本类型。command.camera.red.description

`green`：<!-- md:samp int -->

- 基本类型。command.camera.green.description

`blue`：<!-- md:samp int -->

- 基本类型。command.camera.blue.description


/////

////

///

/// tab | 重载30
```mcfunction
/camera <players:target> fade
```

//// html | div.result
command.camera.30.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.camera.players.description

`fade`：<!-- md:samp fade -->

- 枚举类型。command.enum.fade.description单值枚举，请直接使用`fade`。


/////

////

///
