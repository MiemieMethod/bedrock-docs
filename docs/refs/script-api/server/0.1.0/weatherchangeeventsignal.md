# `WeatherChangeEventSignal`

> 文档版本：1.21.0.24

`WeatherChangeEventSignal`类。script_api.mojang-minecraft.weatherchangeeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.weatherchangeeventsignal.subscribe.description

```js
subscribe(callback: (arg: WeatherChangeEvent) => void): (arg: WeatherChangeEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../weatherchangeevent/">WeatherChangeEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.weatherchangeeventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../weatherchangeevent/">WeatherChangeEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.weatherchangeeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.weatherchangeeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: WeatherChangeEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../weatherchangeevent/">WeatherChangeEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.weatherchangeeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.weatherchangeeventsignal.unsubscribe.return


////

///

