# Experience Reward

> 文档版本：1.21.0.24

Defines the amount of experience rewarded when the entity dies or is successfully bred.

## 架构

```mcschema
experience_reward:
{
  ['string', 'number'] "on_bred" : opt
  ['string', 'number'] "on_death" : opt
}

```

/// html | div.result
//// define
`on_bred`：<samp>['string', 'number']</samp>

- A molang expression defining the amount of experience rewarded when this entity is successfully bred. An array of expressions adds each expression's result together for a final total.


////


//// define
`on_death`：<samp>['string', 'number']</samp>

- A molang expression defining the amount of experience rewarded when this entity dies. An array of expressions adds each expression's result together for a final total.


////


///

