# 特效接口<!-- md:flag china -->

本页列出中国版模组SDK中与粒子特效、序列帧特效、文字面板及后处理效果相关的客户端接口。这些接口均在客户端可用，服务端无法直接创建或控制特效，通常需通过事件通知客户端后在客户端执行。接口域总览入口见[中国版ModAPI接口域索引](modapi-interface-index.md)。

/// warning | 与国际版脚本API分开使用
本页接口属于中国版Python模组SDK客户端体系，与国际版`@minecraft/server`脚本API无关。粒子效果的资源文件定义（`.json`粒子文件）可与附加包共用，但接口调用方式不同。
///

## 粒子特效

粒子特效通过`ClientSystem`实例的`CreateEngineParticle`方法创建，返回`particleEntityId`作为后续组件操作的目标。粒子创建后默认处于停止状态，需调用`ParticleControlComp.Play()`播放。

### 创建与销毁

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `CreateEngineParticle(path,pos)` | 客户端 | `path:str`、`pos:tuple(float,float,float)` | `int`或`None` | 创建粒子特效，`path`为资源路径（含扩展名，如`effects/fire.json`）；返回`particleEntityId`。粒子创建后需调用`Play()`播放。 |
| `DestroyEntity(particleEntityId)` | 客户端 | `particleEntityId:int` | 无 | 销毁粒子特效实体，释放资源。 |

### 绑定（`CreateParticleEntityBind`）

将粒子绑定到实体，粒子会跟随实体移动。通过`GetEngineCompFactory().CreateParticleEntityBind(particleEntityId)`获取组件。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `Bind(bindEntityId,offset,rot,correction,isClientEntity)` | 客户端 | `bindEntityId:str`、`offset:tuple(float,float,float)`、`rot:tuple(float,float,float)`、`correction:bool`、`isClientEntity:bool` | `bool` | 将粒子绑定到实体脚下中心点，附加偏移量和旋转角度。`correction`开启后旋转角度以玩家为参照。`isClientEntity`为`True`时用于绑定客户端实体。 |

### 骨骼绑定（`CreateParticleSkeletonBind`）

将粒子绑定到骨骼模型的指定骨骼节点。通过`GetEngineCompFactory().CreateParticleSkeletonBind(particleEntityId)`获取组件。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `Bind(modelId,boneName,offset,rot)` | 客户端 | `modelId:int`、`boneName:str`、`offset:tuple(float,float,float)`、`rot:tuple(float,float,float)` | `bool` | 将粒子绑定到骨骼模型的指定骨骼，`modelId`来自模型组件的`GetModelId()`。 |

### 控制（`CreateParticleControl`）

控制粒子的播放、停止和位置。通过`GetEngineCompFactory().CreateParticleControl(particleEntityId)`获取组件。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `Play()` | 客户端 | 无 | 无 | 播放粒子特效。若粒子位于非当前维度，同时更新粒子所属维度。 |
| `Stop()` | 客户端 | 无 | 无 | 停止粒子特效播放。 |
| `Pause()` | 客户端 | 无 | 无 | 暂停粒子特效播放，可通过`Play()`继续。 |
| `SetPos(pos)` | 客户端 | `pos:tuple(float,float,float)` | 无 | 设置粒子在世界中的位置。 |
| `SetRot(rot)` | 客户端 | `rot:tuple(float,float,float)` | 无 | 设置粒子的旋转角度。 |
| `SetLayer(layer)` | 客户端 | `layer:int` | `bool` | 设置粒子渲染图层，影响半透明粒子的渲染顺序。 |

```python
import mod.client.extraClientApi as clientApi

class MyClientSystem(clientApi.GetClientSystemCls()):
    def SpawnFireEffect(self, pos):
        particleEntityId = self.CreateEngineParticle("effects/fire.json", pos)
        if particleEntityId is None:
            return
        controlComp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
        controlComp.Play()

    def BindParticleToPlayer(self, particleEntityId, playerId):
        bindComp = clientApi.GetEngineCompFactory().CreateParticleEntityBind(particleEntityId)
        bindComp.Bind(playerId, (0, 1.5, 0), (0, 0, 0))
```

## 序列帧特效

序列帧特效与粒子特效的操作模式相同：通过`ClientSystem.CreateEngineSfx`创建，获取`sfxEntityId`，再通过各组件控制。序列帧特效是平面纹理动画，适合爆炸、烟雾、闪光等效果。

### 创建（`ClientSystem`方法）

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `CreateEngineSfx(path,pos,rot,scale)` | 客户端 | `path:str`、`pos:tuple(float,float,float)`、`rot:tuple(float,float,float)`、`scale:float` | `int`或`None` | 创建序列帧特效，`path`为序列帧JSON资源路径；返回`sfxEntityId`。 |
| `CreateEngineSfxFromMs(path,pos,rot,scale)` | 客户端 | `path:str`、`pos:tuple(float,float,float)`、`rot:tuple(float,float,float)`、`scale:float` | `int`或`None` | 创建微软粒子（基于`minecraft:particle_emitter`格式）序列帧特效。 |

### 绑定

`CreateFrameAniEntityBind(sfxEntityId)`：绑定到实体。`CreateFrameAniSkeletonBind(sfxEntityId)`：绑定到骨骼模型骨骼节点。接口签名与粒子绑定相同，详见[粒子特效绑定](#绑定createparticleentitybind)。

### 控制（`CreateFrameAniControl`）

通过`GetEngineCompFactory().CreateFrameAniControl(sfxEntityId)`获取组件，接口与粒子控制组件相同（`Play()`、`Stop()`、`Pause()`、`SetPos()`、`SetRot()`、`SetLayer()`）。

## 文字面板

文字面板用于在世界空间中显示悬浮文字，可绑定实体跟随移动。通过`GetEngineCompFactory().CreateTextBoard(levelId)`获取`TextBoardComponentClient`实例。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `CreateTextBoardInWorld(text,textColor,boardColor,faceCamera)` | 客户端 | `text:str`、`textColor:tuple(float,float,float,float)`、`boardColor:tuple(float,float,float,float)`或`None`、`faceCamera:bool` | `int`或`None` | 在世界中创建文字面板，`textColor`和`boardColor`为RGBA值（范围0到1）；返回`boardId`，创建失败返回`None`。 |
| `RemoveTextBoard(boardId)` | 客户端 | `boardId:int` | `bool` | 删除指定文字面板，释放资源。 |
| `SetBoardText(boardId,text)` | 客户端 | `boardId:int`、`text:str` | `bool` | 更新文字面板的显示文字内容。 |
| `SetBoardPos(boardId,pos)` | 客户端 | `boardId:int`、`pos:tuple(float,float,float)` | `bool` | 设置文字面板的世界坐标位置。 |
| `SetBoardBackgroundColor(boardId,color)` | 客户端 | `boardId:int`、`color:tuple(float,float,float,float)` | `bool` | 设置文字面板背景颜色，RGBA值范围0到1。 |
| `SetBoardTextColor(boardId,color)` | 客户端 | `boardId:int`、`color:tuple(float,float,float,float)` | `bool` | 设置文字面板文字颜色，RGBA值范围0到1。 |
| `BindEntityToBoard(boardId,entityId,offset)` | 客户端 | `boardId:int`、`entityId:str`、`offset:tuple(float,float,float)` | `bool` | 将文字面板绑定到实体，面板随实体移动；`offset`为相对于实体的偏移量。 |
| `UnBindEntityToBoard(boardId)` | 客户端 | `boardId:int` | `bool` | 解除文字面板与实体的绑定。 |
| `SetBoardDepthTest(boardId,enable)` | 客户端 | `boardId:int`、`enable:bool` | `bool` | 设置文字面板是否进行深度测试，关闭后面板始终显示在其他物体之上。 |

```python
import mod.client.extraClientApi as clientApi

levelId = clientApi.GetLevelId()
textBoardComp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)

# 在世界坐标创建文字面板
boardId = textBoardComp.CreateTextBoardInWorld(
    "Hello World",
    (1.0, 1.0, 1.0, 1.0),  # 白色文字
    (0.0, 0.0, 0.0, 0.8),  # 半透明黑色背景
    True                    # 始终朝向摄像机
)

if boardId is not None:
    # 绑定到玩家头顶
    playerId = clientApi.GetLocalPlayerId()
    textBoardComp.BindEntityToBoard(boardId, playerId, (0, 2.5, 0))
```

## 后处理效果

后处理效果接口位于`接口\后处理`目录，包含渐晕、模糊、色彩分级、镜头效果与完全自定义后处理管线，均为客户端接口。通过对应组件工厂创建后处理组件实例后调用。

| 组件 | 创建方法 | 主要接口 | 说明 |
| --- | --- | --- | --- |
| 渐晕 | `CreatePostProcess(levelId)` + 渐晕类 | `SetVignetteIntensity(intensity)`、`SetVignetteStart(start)` | 屏幕边缘渐暗效果。 |
| 模糊 | `CreatePostProcess(levelId)` + 模糊类 | `SetBlurRadius(radius)` | 全屏或局部模糊效果。 |
| 色彩分级 | `CreatePostProcess(levelId)` + 色彩类 | `SetColorMatrix(matrix)` | 全屏色彩矩阵变换。 |
| 镜头效果 | `CreatePostProcess(levelId)` + 镜头类 | `SetLensFlare(enable)`等 | 镜头光晕、色差等光学效果。 |
| 自定义 | `CreatePostProcess(levelId)` + 自定义类 | `SetCustomShader(path)` | 自定义GLSL/HLSL着色器后处理管线。 |

/// note | 后处理接口依赖平台支持
部分后处理效果在低端设备或关闭高级图形设置时不会生效。建议通过`GetPlatform()`和设备性能检测决定是否启用后处理。
///