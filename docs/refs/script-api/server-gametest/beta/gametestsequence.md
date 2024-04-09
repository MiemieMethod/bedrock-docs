# `GameTestSequence`

> 文档版本：1.21.0.20

`GameTestSequence`类。script_api.@minecraft/server-gametest.gametestsequence.description

## 方法

/// define
`thenExecute`


///

script_api.@minecraft/server-gametest.gametestsequence.thenexecute.description

```js
thenExecute(callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.gametestsequence.callback.thenexecute.description


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- script_api.@minecraft/server-gametest.gametestsequence.thenexecute.return


////

///


/// define
`thenExecuteAfter`


///

script_api.@minecraft/server-gametest.gametestsequence.thenexecuteafter.description

```js
thenExecuteAfter(delayTicks: int32, callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`delayTicks`：`int32`

- script_api.@minecraft/server-gametest.gametestsequence.delayticks.thenexecuteafter.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.gametestsequence.callback.thenexecuteafter.description


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- script_api.@minecraft/server-gametest.gametestsequence.thenexecuteafter.return


////

///


/// define
`thenExecuteFor`


///

script_api.@minecraft/server-gametest.gametestsequence.thenexecutefor.description

```js
thenExecuteFor(tickCount: int32, callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`tickCount`：`int32`

- script_api.@minecraft/server-gametest.gametestsequence.tickcount.thenexecutefor.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.gametestsequence.callback.thenexecutefor.description


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- script_api.@minecraft/server-gametest.gametestsequence.thenexecutefor.return


////

///


/// define
`thenFail`


///

script_api.@minecraft/server-gametest.gametestsequence.thenfail.description

```js
thenFail(errorMessage: string): void
```

/// html | div.result
//// define
`errorMessage`：`string`

- script_api.@minecraft/server-gametest.gametestsequence.errormessage.thenfail.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.gametestsequence.thenfail.return


////

///


/// define
`thenIdle`


///

script_api.@minecraft/server-gametest.gametestsequence.thenidle.description

```js
thenIdle(delayTicks: int32): GameTestSequence
```

/// html | div.result
//// define
`delayTicks`：`int32`

- script_api.@minecraft/server-gametest.gametestsequence.delayticks.thenidle.description


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- script_api.@minecraft/server-gametest.gametestsequence.thenidle.return


////

///


/// define
`thenSucceed`


///

script_api.@minecraft/server-gametest.gametestsequence.thensucceed.description

```js
thenSucceed(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.gametestsequence.thensucceed.return


////

///


/// define
`thenWait`


///

script_api.@minecraft/server-gametest.gametestsequence.thenwait.description

```js
thenWait(callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.gametestsequence.callback.thenwait.description


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- script_api.@minecraft/server-gametest.gametestsequence.thenwait.return


////

///


/// define
`thenWaitAfter`


///

script_api.@minecraft/server-gametest.gametestsequence.thenwaitafter.description

```js
thenWaitAfter(delayTicks: int32, callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`delayTicks`：`int32`

- script_api.@minecraft/server-gametest.gametestsequence.delayticks.thenwaitafter.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.gametestsequence.callback.thenwaitafter.description


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- script_api.@minecraft/server-gametest.gametestsequence.thenwaitafter.return


////

///

