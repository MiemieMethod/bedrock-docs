# 事件、存储与多人

InnerCore的运行逻辑主要围绕回调、可更新对象、保存作用域和网络包组织。资料将这些机制用于旧Android客户端模组中的交互、长期机制、配置保存和多人同步。

/// warning | 服务端权威原则
InnerCore资料把单人世界的主机也视作服务端。所有会影响世界、玩家数据或重要进度的逻辑都应以服务端为准；客户端只负责显示、输入和必要请求。不要把客户端包或客户端变量当作可信数据。
///

## 回调

回调用于注册事件处理器。基本形式如下：

```javascript
Callback.addCallback("EventName", function(/* arguments */) {
  // handle event
}, 0);
```

第三个参数是优先级，数值越大越早执行。资料建议不要使用过大的优先级，通常限制在0到9即可。

自定义事件可使用`Callback.invokeCallback`调用：

```javascript
Callback.addCallback("MyMod:HelloWorld", function(who) {
  alert("Hello, " + who + "!");
});

Callback.invokeCallback("MyMod:HelloWorld", "World");
```

/// danger | 不要在事件内部注册事件
如果在回调函数内部继续调用`Callback.addCallback`，每次事件触发都会新增处理器，最终导致重复执行和性能问题。
///

资料把事件粗略分为方块建造与破坏、世界交互、实体与玩家、维度与世界、界面、服务端内部事件和自定义事件。处理事件时应遵循“先判断、再执行昂贵逻辑”的原则，因为同一旧客户端可能同时运行多个模组。

## 可更新对象

可更新对象是带`update`方法的对象。它们按刻执行，适合临时循环、动画、机制处理和需要动态结束的逻辑。

```javascript
const StopwatchActionbar = {
  ticking: 0,
  update: function() {
    this.ticking++;
    if (this.ticking % 20 == 0) {
      Game.tipMessage(this.ticking / 20);
    }
  }
};

Callback.addCallback("LocalLevelLoaded", function() {
  Updatable.addLocalUpdatable(StopwatchActionbar);
});
```

资料指出，设置`remove = true`可从更新列表中移除对象，设置`noupdate = true`可暂时停止更新。客户端可更新对象适合界面与视觉效果；服务端可更新对象适合机制、玩家状态和世界逻辑。

## 配置

`__config__`用于读取和保存客户端设置。它对应模组目录中的`config.json`和可选的`config.info.json`。

```javascript
__config__.getBool("change_quantum_suit_recipe");
__config__.getInteger("energy_text.scale");
__config__.getString("energy_text.pos");
```

设置值后需要保存：

```javascript
__config__.set("energy_text.y", 60);
__config__.set("energy_text.pos", "left");
__config__.save();
```

资料建议用`checkAndRestore`恢复缺失值或错误类型：

```javascript
__config__.checkAndRestore({
  change_quantum_suit_recipe: true,
  energy_text: {
    pos: "right",
    scale: 135,
    y: 30
  }
});
```

配置更适合客户端偏好，例如界面位置、显示比例和个人开关。服务器设置若需要下发，应通过网络包或同步数据传递。

## 保存

较大的世界数据和玩家数据使用`Saver`。资料推荐使用具名保存作用域，不建议在新项目中继续依赖旧`ReadSaves`和`WriteSaves`回调。

```javascript
Saver.addSavesScope("AbstractMod.Tanks", function(data) {
  placedTanksByDimension = data || {};
}, function() {
  return placedTanksByDimension;
});
```

保存函数返回的对象可以包含嵌套对象和数组。读取函数收到的对象可能为空对象，因此不能只用`data != null`判断是否有数据。复杂实例可通过`Saver.registerObjectSaver`和`Saver.registerObject`保存，并在对象销毁时忽略它，避免无效实例继续写入存档。

/// note | 方块实体资料缺口
知识库中的英文`storage/tile-entities.md`和`blocks/block-entities.md`只是“未本地化”占位。俄文翻译中有对应标题和概要，但本次没有足够英文正文可核验。因此这里不展开旧InnerCore方块实体API，只记录保存系统和多人资料中对方块实体客户端/服务端拆分的原则。
///

## 客户端与服务端

资料把多人开发分为客户端和服务端两侧：

- 客户端知道自身显示、输入、加载区块和视觉信息。
- 服务端拥有世界、重要玩家数据和机制状态。
- 客户端不能直接信任自身数据去修改世界。
- 视觉计算尽量放在客户端，重要结果由服务端保存和验证。

资料列出许多事件的客户端/服务端对应关系。例如`LocalTick`是客户端刻，`ServerPlayerTick`是服务端玩家刻；`ItemUseLocal`是客户端物品使用，`ItemUse`是服务端物品使用；`EntityAddedLocal`是客户端实体加入，`EntityAdded`是服务端实体加入。

## 客户端包

客户端包由服务端发送到客户端并在客户端执行，适合通知某个玩家显示动画、提示、粒子或同步可见数据。

```javascript
Network.addClientPacket("packet.example.start_animation", function(data) {
  if (!data.text) {
    return;
  }
  animator.init(data.text);
});

Callback.addCallback("ExpLevelAdd", function(level, playerUid) {
  const client = Network.getClientForPlayer(playerUid);
  if (client != null) {
    client.send("packet.example.start_animation", { text: level });
  }
});
```

资料特别提醒，服务端数值ID和客户端数值ID可能不同。发送物品或方块ID到客户端后，应使用`Network.serverToLocalId`转换。

## 服务端包

服务端包由客户端发送到服务端并在服务端执行。它们适合把客户端输入转化为服务端请求，但必须进行验证。

```javascript
Network.addServerPacket("packet.example.wall_break_learning", function(client, data) {
  const playerUid = client.getPlayerUid();
  const position = Entity.getPosition(playerUid);
  const region = BlockSource.getDefaultForActor(playerUid);
  // 在服务端验证玩家是否确实可能触发该行为。
});
```

/// danger | 永远保护服务端包
资料中的示例展示了错误的客户端包可被滥用。每个服务端包都应验证发送者、距离、目标方块、状态、权限和数据范围。对恶意请求可以忽略，严重时可断开客户端。
///

包的数量不是问题，关键是每个包只处理必要任务。把许多行为混在一个包中会增加验证难度，也更容易引入安全漏洞。
