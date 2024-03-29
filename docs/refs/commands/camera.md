# /camera

> 文档版本：1.20.80.24

`/camera`命令Issues a camera instruction

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> pos <position:x y z> rot <xRot:value> <yRot:value>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`ease`: <!-- md:samp ease -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ease`||


`easeTime`: <!-- md:samp float -->

- 基本类型。

`easeType`: <!-- md:samp Easing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`linear`||
|`spring`||
|`in_quad`||
|`out_quad`||
|`in_out_quad`||
|`in_cubic`||
|`out_cubic`||
|`in_out_cubic`||
|`in_quart`||
|`out_quart`||
|`in_out_quart`||
|`in_quint`||
|`out_quint`||
|`in_out_quint`||
|`in_sine`||
|`out_sine`||
|`in_out_sine`||
|`in_expo`||
|`out_expo`||
|`in_out_expo`||
|`in_circ`||
|`out_circ`||
|`in_out_circ`||
|`in_bounce`||
|`out_bounce`||
|`in_out_bounce`||
|`in_back`||
|`out_back`||
|`in_out_back`||
|`in_elastic`||
|`out_elastic`||
|`in_out_elastic`||


`pos`: <!-- md:samp pos -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||


`position`: <!-- md:samp x y z -->

- 基本类型。

`rot`: <!-- md:samp rot -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`rot`||


`xRot`: <!-- md:samp value -->

- 基本类型。

`yRot`: <!-- md:samp value -->

- 基本类型。


/////

////

///

/// tab | `重载2`
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> pos <position:x y z> facing <lookAtEntity:target>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`ease`: <!-- md:samp ease -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ease`||


`easeTime`: <!-- md:samp float -->

- 基本类型。

`easeType`: <!-- md:samp Easing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`linear`||
|`spring`||
|`in_quad`||
|`out_quad`||
|`in_out_quad`||
|`in_cubic`||
|`out_cubic`||
|`in_out_cubic`||
|`in_quart`||
|`out_quart`||
|`in_out_quart`||
|`in_quint`||
|`out_quint`||
|`in_out_quint`||
|`in_sine`||
|`out_sine`||
|`in_out_sine`||
|`in_expo`||
|`out_expo`||
|`in_out_expo`||
|`in_circ`||
|`out_circ`||
|`in_out_circ`||
|`in_bounce`||
|`out_bounce`||
|`in_out_bounce`||
|`in_back`||
|`out_back`||
|`in_out_back`||
|`in_elastic`||
|`out_elastic`||
|`in_out_elastic`||


`pos`: <!-- md:samp pos -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||


`position`: <!-- md:samp x y z -->

- 基本类型。

`facing`: <!-- md:samp facing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtEntity`: <!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | `重载3`
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> pos <position:x y z> facing <lookAtPosition:x y z>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`ease`: <!-- md:samp ease -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ease`||


`easeTime`: <!-- md:samp float -->

- 基本类型。

`easeType`: <!-- md:samp Easing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`linear`||
|`spring`||
|`in_quad`||
|`out_quad`||
|`in_out_quad`||
|`in_cubic`||
|`out_cubic`||
|`in_out_cubic`||
|`in_quart`||
|`out_quart`||
|`in_out_quart`||
|`in_quint`||
|`out_quint`||
|`in_out_quint`||
|`in_sine`||
|`out_sine`||
|`in_out_sine`||
|`in_expo`||
|`out_expo`||
|`in_out_expo`||
|`in_circ`||
|`out_circ`||
|`in_out_circ`||
|`in_bounce`||
|`out_bounce`||
|`in_out_bounce`||
|`in_back`||
|`out_back`||
|`in_out_back`||
|`in_elastic`||
|`out_elastic`||
|`in_out_elastic`||


`pos`: <!-- md:samp pos -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||


`position`: <!-- md:samp x y z -->

- 基本类型。

`facing`: <!-- md:samp facing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtPosition`: <!-- md:samp x y z -->

- 基本类型。


/////

////

///

/// tab | `重载4`
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> pos <position:x y z>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`ease`: <!-- md:samp ease -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ease`||


`easeTime`: <!-- md:samp float -->

- 基本类型。

`easeType`: <!-- md:samp Easing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`linear`||
|`spring`||
|`in_quad`||
|`out_quad`||
|`in_out_quad`||
|`in_cubic`||
|`out_cubic`||
|`in_out_cubic`||
|`in_quart`||
|`out_quart`||
|`in_out_quart`||
|`in_quint`||
|`out_quint`||
|`in_out_quint`||
|`in_sine`||
|`out_sine`||
|`in_out_sine`||
|`in_expo`||
|`out_expo`||
|`in_out_expo`||
|`in_circ`||
|`out_circ`||
|`in_out_circ`||
|`in_bounce`||
|`out_bounce`||
|`in_out_bounce`||
|`in_back`||
|`out_back`||
|`in_out_back`||
|`in_elastic`||
|`out_elastic`||
|`in_out_elastic`||


`pos`: <!-- md:samp pos -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||


`position`: <!-- md:samp x y z -->

- 基本类型。


/////

////

///

/// tab | `重载5`
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> rot <xRot:value> <yRot:value>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`ease`: <!-- md:samp ease -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ease`||


`easeTime`: <!-- md:samp float -->

- 基本类型。

`easeType`: <!-- md:samp Easing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`linear`||
|`spring`||
|`in_quad`||
|`out_quad`||
|`in_out_quad`||
|`in_cubic`||
|`out_cubic`||
|`in_out_cubic`||
|`in_quart`||
|`out_quart`||
|`in_out_quart`||
|`in_quint`||
|`out_quint`||
|`in_out_quint`||
|`in_sine`||
|`out_sine`||
|`in_out_sine`||
|`in_expo`||
|`out_expo`||
|`in_out_expo`||
|`in_circ`||
|`out_circ`||
|`in_out_circ`||
|`in_bounce`||
|`out_bounce`||
|`in_out_bounce`||
|`in_back`||
|`out_back`||
|`in_out_back`||
|`in_elastic`||
|`out_elastic`||
|`in_out_elastic`||


`rot`: <!-- md:samp rot -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`rot`||


`xRot`: <!-- md:samp value -->

- 基本类型。

`yRot`: <!-- md:samp value -->

- 基本类型。


/////

////

///

/// tab | `重载6`
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> facing <lookAtEntity:target>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`ease`: <!-- md:samp ease -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ease`||


`easeTime`: <!-- md:samp float -->

- 基本类型。

`easeType`: <!-- md:samp Easing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`linear`||
|`spring`||
|`in_quad`||
|`out_quad`||
|`in_out_quad`||
|`in_cubic`||
|`out_cubic`||
|`in_out_cubic`||
|`in_quart`||
|`out_quart`||
|`in_out_quart`||
|`in_quint`||
|`out_quint`||
|`in_out_quint`||
|`in_sine`||
|`out_sine`||
|`in_out_sine`||
|`in_expo`||
|`out_expo`||
|`in_out_expo`||
|`in_circ`||
|`out_circ`||
|`in_out_circ`||
|`in_bounce`||
|`out_bounce`||
|`in_out_bounce`||
|`in_back`||
|`out_back`||
|`in_out_back`||
|`in_elastic`||
|`out_elastic`||
|`in_out_elastic`||


`facing`: <!-- md:samp facing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtEntity`: <!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | `重载7`
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> facing <lookAtPosition:x y z>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`ease`: <!-- md:samp ease -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ease`||


`easeTime`: <!-- md:samp float -->

- 基本类型。

`easeType`: <!-- md:samp Easing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`linear`||
|`spring`||
|`in_quad`||
|`out_quad`||
|`in_out_quad`||
|`in_cubic`||
|`out_cubic`||
|`in_out_cubic`||
|`in_quart`||
|`out_quart`||
|`in_out_quart`||
|`in_quint`||
|`out_quint`||
|`in_out_quint`||
|`in_sine`||
|`out_sine`||
|`in_out_sine`||
|`in_expo`||
|`out_expo`||
|`in_out_expo`||
|`in_circ`||
|`out_circ`||
|`in_out_circ`||
|`in_bounce`||
|`out_bounce`||
|`in_out_bounce`||
|`in_back`||
|`out_back`||
|`in_out_back`||
|`in_elastic`||
|`out_elastic`||
|`in_out_elastic`||


`facing`: <!-- md:samp facing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtPosition`: <!-- md:samp x y z -->

- 基本类型。


/////

////

///

/// tab | `重载8`
```mcfunction
/camera <players:target> set <preset:CameraPresets> ease <easeTime:float> <easeType:Easing> default
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`ease`: <!-- md:samp ease -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ease`||


`easeTime`: <!-- md:samp float -->

- 基本类型。

`easeType`: <!-- md:samp Easing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`linear`||
|`spring`||
|`in_quad`||
|`out_quad`||
|`in_out_quad`||
|`in_cubic`||
|`out_cubic`||
|`in_out_cubic`||
|`in_quart`||
|`out_quart`||
|`in_out_quart`||
|`in_quint`||
|`out_quint`||
|`in_out_quint`||
|`in_sine`||
|`out_sine`||
|`in_out_sine`||
|`in_expo`||
|`out_expo`||
|`in_out_expo`||
|`in_circ`||
|`out_circ`||
|`in_out_circ`||
|`in_bounce`||
|`out_bounce`||
|`in_out_bounce`||
|`in_back`||
|`out_back`||
|`in_out_back`||
|`in_elastic`||
|`out_elastic`||
|`in_out_elastic`||


`default`: <!-- md:samp default -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`default`||



/////

////

///

/// tab | `重载9`
```mcfunction
/camera <players:target> set <preset:CameraPresets> pos <position:x y z> rot <xRot:value> <yRot:value>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`pos`: <!-- md:samp pos -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||


`position`: <!-- md:samp x y z -->

- 基本类型。

`rot`: <!-- md:samp rot -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`rot`||


`xRot`: <!-- md:samp value -->

- 基本类型。

`yRot`: <!-- md:samp value -->

- 基本类型。


/////

////

///

/// tab | `重载10`
```mcfunction
/camera <players:target> set <preset:CameraPresets> pos <position:x y z> facing <lookAtEntity:target>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`pos`: <!-- md:samp pos -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||


`position`: <!-- md:samp x y z -->

- 基本类型。

`facing`: <!-- md:samp facing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtEntity`: <!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | `重载11`
```mcfunction
/camera <players:target> set <preset:CameraPresets> pos <position:x y z> facing <lookAtPosition:x y z>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`pos`: <!-- md:samp pos -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||


`position`: <!-- md:samp x y z -->

- 基本类型。

`facing`: <!-- md:samp facing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtPosition`: <!-- md:samp x y z -->

- 基本类型。


/////

////

///

/// tab | `重载12`
```mcfunction
/camera <players:target> set <preset:CameraPresets> pos <position:x y z>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`pos`: <!-- md:samp pos -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||


`position`: <!-- md:samp x y z -->

- 基本类型。


/////

////

///

/// tab | `重载13`
```mcfunction
/camera <players:target> set <preset:CameraPresets> rot <xRot:value> <yRot:value>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`rot`: <!-- md:samp rot -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`rot`||


`xRot`: <!-- md:samp value -->

- 基本类型。

`yRot`: <!-- md:samp value -->

- 基本类型。


/////

////

///

/// tab | `重载14`
```mcfunction
/camera <players:target> set <preset:CameraPresets> facing <lookAtEntity:target>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`facing`: <!-- md:samp facing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtEntity`: <!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | `重载15`
```mcfunction
/camera <players:target> set <preset:CameraPresets> facing <lookAtPosition:x y z>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`facing`: <!-- md:samp facing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtPosition`: <!-- md:samp x y z -->

- 基本类型。


/////

////

///

/// tab | `重载16`
```mcfunction
/camera <players:target> set <preset:CameraPresets> default
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`set`: <!-- md:samp set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`preset`: <!-- md:samp CameraPresets -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:first_person`||
|`minecraft:free`||
|`minecraft:third_person`||
|`minecraft:third_person_front`||
|`example:example_free`||
|`example:example_player_effects`||
|`example:example_player_listener`||


`default`: <!-- md:samp default -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`default`||



/////

////

///

/// tab | `重载17`
```mcfunction
/camera <players:target> clear
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`clear`: <!-- md:samp clear -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`clear`||



/////

////

///

/// tab | `重载18`
```mcfunction
/camera <players:target> fade time <fadeInSeconds:float> <holdSeconds:float> <fadeOutSeconds:float> color <red:int> <green:int> <blue:int>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`fade`: <!-- md:samp fade -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`fade`||


`time`: <!-- md:samp time -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`time`||


`fadeInSeconds`: <!-- md:samp float -->

- 基本类型。

`holdSeconds`: <!-- md:samp float -->

- 基本类型。

`fadeOutSeconds`: <!-- md:samp float -->

- 基本类型。

`color`: <!-- md:samp color -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`color`||


`red`: <!-- md:samp int -->

- 基本类型。

`green`: <!-- md:samp int -->

- 基本类型。

`blue`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | `重载19`
```mcfunction
/camera <players:target> fade time <fadeInSeconds:float> <holdSeconds:float> <fadeOutSeconds:float>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`fade`: <!-- md:samp fade -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`fade`||


`time`: <!-- md:samp time -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`time`||


`fadeInSeconds`: <!-- md:samp float -->

- 基本类型。

`holdSeconds`: <!-- md:samp float -->

- 基本类型。

`fadeOutSeconds`: <!-- md:samp float -->

- 基本类型。


/////

////

///

/// tab | `重载20`
```mcfunction
/camera <players:target> fade color <red:int> <green:int> <blue:int>
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`fade`: <!-- md:samp fade -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`fade`||


`color`: <!-- md:samp color -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`color`||


`red`: <!-- md:samp int -->

- 基本类型。

`green`: <!-- md:samp int -->

- 基本类型。

`blue`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | `重载21`
```mcfunction
/camera <players:target> fade
```

//// html | div.result
///// define
`players`: <!-- md:samp target -->

- 基本类型。

`fade`: <!-- md:samp fade -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`fade`||



/////

////

///
