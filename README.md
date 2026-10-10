# Day 4 - List, Tuple, Dictionary

In this day I learned the basic Python data structures: List, Tuple and Dictionary. Set is added as a bonus.

The code is in `day4_list_tuple_dictionary.py`. Every concept has a short explanation in the comments.

## Topics covered

### List
- Ordered and changeable, written with `[]`
- Indexing and slicing
- Add items: `append()`, `insert()`
- Remove items: `remove()`, `pop()`
- Functions: `len()`, `max()`, `min()`, `sum()`, `sort()`
- Looping with `for`

### Tuple
- Ordered but not changeable, written with `()`
- Indexing
- Methods: `count()`, `index()`
- Unpacking

### Dictionary
- Key-value pairs, written with `{}`
- Access with `dict[key]` and `get()`
- Add, update and remove items
- `keys()`, `values()`, `items()`
- Looping and checking if a key exists

### Set (bonus)
- Unique items only, no index
- `add()`, `remove()`
- Union, intersection, difference

## Comparison

| Type | Bracket | Ordered | Changeable | Duplicates |
|------|---------|---------|------------|------------|
| List | `[]` | Yes | Yes | Allowed |
| Tuple | `()` | Yes | No | Allowed |
| Dictionary | `{k: v}` | Yes | Yes | Keys must be unique |
| Set | `{}` | No | Yes | Not allowed |

## How to run

```
python day4_list_tuple_dictionary.py
```

## Folder structure

```
Day4/
├── README.md
└── day4_list_tuple_dictionary.py
```
