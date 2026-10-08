# Day 3 - Python Loops

Is day maine Python ke **loops** practice kiye: `while` loop aur `for` loop.

## Topics Covered

- Repeating output (`print` multiple times)
- `while` loop (counting, reverse counting, sum, tables, digit counter)
- `for` loop with a list
- `for` loop with `range()` (start, stop, step)
- Taking user input with `input()` and `int()`

## Practice List

| # | Topic | Concept |
|---|-------|---------|
| 0 | Print "meow" 3 times | Basic repetition |
| 1 | Print "hello world" 4 times | `while` loop |
| 2 | Print "hello world" 3 times | `for` loop with a list |
| 3 | `"hello world\n" * 3` | String multiplication (not ideal, loops are better) |
| 4 | Print 1 to 10 | `while` loop |
| 5 | Print 10 to 1 | `while` loop (reverse) |
| 6 | Sum of 1 to 10 | `while` loop + accumulator |
| 7 | Multiplication table | `while` loop + `input()` |
| 8 | Digit counter | `while` loop + `//` operator |
| 9 | Print 1 to 10 | `for` + `range(1, 11)` |
| 10 | Even numbers 2 to 20 | `for` + `range(2, 21, 2)` |
| 11 | Print fruits | `for` loop over a list |
| 12 | Multiplication table | `for` + `range()` + `input()` |

## How to Run

```bash
python day3.py
```

Kuch practice programs number maangte hain (table aur digit counter), to run karte waqt input dena hoga.

## Key Learnings

- `while` loop tab use hota hai jab condition pe repeat karna ho; `i += 1` bhoolna nahi warna infinite loop ban jayega.
- `for` loop tab best hai jab pata ho kitni baar ya kis list pe chalana hai.
- `range(start, stop, step)` mein `stop` include nahi hota.
- `num // 10` last digit hata deta hai, isse digit count nikalta hai.

## Files

- `day3.py` - all practice code
- `README.md` - this file
