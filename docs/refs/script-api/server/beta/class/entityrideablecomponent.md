# `EntityRideableComponent`

> 文档版本：1.21.0.20

`EntityRideableComponent`类。

## 属性

/// define
`controllingSeat`


///

```js
read-only controllingSeat: int32
```


/// define
`crouchingSkipInteract`


///

```js
read-only crouchingSkipInteract: boolean
```


/// define
`interactText`


///

```js
read-only interactText: string
```


/// define
`passengerMaxWidth`


///

```js
read-only passengerMaxWidth: float
```


/// define
`pullInEntities`


///

```js
read-only pullInEntities: boolean
```


/// define
`riderCanInteract`


///

```js
read-only riderCanInteract: boolean
```


/// define
`seatCount`


///

```js
read-only seatCount: int32
```


## 方法

/// define
addRider

- ```js
addRider(rider: Entity): boolean
```



///


/// define
ejectRider

- ```js
ejectRider(rider: Entity): void
```



///


/// define
ejectRiders

- ```js
ejectRiders(): void
```



///


/// define
getFamilyTypes

- ```js
getFamilyTypes(): string[]
```



///


/// define
getRiders

- ```js
getRiders(): Entity[]
```



///


/// define
getSeats

- ```js
getSeats(): Seat[]
```



///

