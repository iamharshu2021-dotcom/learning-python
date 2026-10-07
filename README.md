# Day 2 - Conditional Statements in Python

This is my Day 2 task. It covers how a program makes decisions using conditions.

## File

- `day2_conditional.py` - contains all 6 examples

## How to run

```bash
python day2_conditional.py
```

Python 3.10 or newer is needed because Example 6 uses `match-case`.

## What I learned

| # | Example | Concept |
|---|---------|---------|
| 1 | Password check | `while True`, `if / else`, `break` |
| 2 | Compare x and y | `if / elif`, comparison operators (`>`, `<`, `==`) |
| 3 | Grade calculator | Logical operator `and`, ranges, `else` fallback |
| 4 | Even or Odd | Modulus operator `%` |
| 5 | Hogwarts house | `if / elif / else` with strings |
| 6 | Hogwarts house | `match-case` (cleaner alternative to many `elif`s) |

## Key points

- `if` runs a block only when its condition is `True`.
- `elif` checks another condition if the earlier ones were `False`.
- `else` runs when none of the conditions matched.
- `and` needs both conditions to be true, `or` needs at least one.
- `x % 2 == 0` is the standard way to check for an even number.
- `match-case` is useful when one value is compared against many options.

## Notes

- In Example 1 the loop stops after the first attempt because both branches use `break`. To allow retries, ask for the password inside the loop and only `break` on the correct one.
- In Example 3, a score below 60 now prints `Grade F` through the `else` block.
- In Example 6, a name that matches no case prints nothing. Add `case _:` to handle that.

## Author

Harsh Mishra
