# Shareables

> 文档版本：1.21.50.25

Defines a list of items the mob wants to share or pick up. Each item must have the following parameters:

## 架构

```mcschema
shareables:
{
  boolean "all_items" : opt
  integer "all_items_max_amount" : opt
  integer "all_items_surplus_amount" : opt
  integer "all_items_want_amount" : opt
  array "items" : opt
  {
    object "<any array element>" : opt
    {
      boolean "admire" : opt
      boolean "barter" : opt
      boolean "consume_item" : opt
      string "craft_into" : opt
      identifier "item"
      integer "item_aux" : opt
      integer "max_amount" : opt
      integer "pickup_limit" : opt
      integer "priority" : opt
      boolean "stored_in_inventory" : opt
      integer "surplus_amount" : opt
      integer "want_amount" : opt
      boolean "pickup_only" : opt
    }
  }
  boolean "singular_pickup" : opt
}

```

/// html | div.result
//// define
`all_items`：<samp>boolean</samp>

- A bucket for all other items in the game. Note this category is always least priority items.


////


//// define
`all_items_max_amount`：<samp>integer</samp>

- Maximum number of this item the mob will hold.


////


//// define
`all_items_surplus_amount`：<samp>integer</samp>

- Number of this item considered extra that the entity wants to share.


////


//// define
`all_items_want_amount`：<samp>integer</samp>

- Number of this item this entity wants to share.


////


//// define
`items`：<samp>array</samp>

- List of items that the entity wants to share.


////

<div class="language-text highlight"><span class="filename"><code>items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- An Item that the entity wants to share.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`admire`：<samp>boolean</samp>

- Mob will admire the item after picking up by looking at it. For this to happen the mob needs to have an Admire component and an Admire goal.


//////


////// define
`barter`：<samp>boolean</samp>

- Mob will barter for the item after picking it up. For this to work the mob needs to have a Barter component and a Barter goal.


//////


////// define
`consume_item`：<samp>boolean</samp>

- Determines whether the mob will consume the item or not.


//////


////// define
`craft_into`：<samp>string</samp>

- Defines the item this entity wants to craft with the item defined above. Should be an item name.


//////


////// define
`item`：<samp>identifier</samp> {#assets.schemas-blockception.general.item.identifier.json}

- The name of the item.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`item_aux`：<samp>integer</samp>

- Aux value for the item.


//////


////// define
`max_amount`：<samp>integer</samp>

- Maximum number of this item the mob will hold.


//////


////// define
`pickup_limit`：<samp>integer</samp>

- Maximum number of this item the mob will pick up during a single goal tick.


//////


////// define
`priority`：<samp>integer</samp>

- Prioritizes which items the entity prefers. 0 is the highest priority.


//////


////// define
`stored_in_inventory`：<samp>boolean</samp>

- Determines whether the mob will try to put the item in its inventory if it has the inventory component and if it can't be equipped.


//////


////// define
`surplus_amount`：<samp>integer</samp>

- Number of this item considered extra that the entity wants to share.


//////


////// define
`want_amount`：<samp>integer</samp>

- Number of this item this entity wants to have.


//////


////// define
`pickup_only`：<samp>boolean</samp>

- Determines whether the mob can only pickup the item and not drop it.


//////


/////


////


//// define
`singular_pickup`：<samp>boolean</samp>

- Determines whether the mob can only pickup one item at a time.


////


///

