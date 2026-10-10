# Day 5 - Types of Errors in Python

In this day I learned the common types of errors in Python, why they happen, and how to handle them using `try` and `except`.

The code is in `day5_types_of_errors.py`. Every error has a short explanation in the comments and a small example that you can run.

## Topics covered

### Types of errors
- `SyntaxError`: wrong Python grammar, for example a missing colon or bracket
- `IndentationError`: wrong spaces at the start of a line
- `NameError`: using a variable that is not defined
- `TypeError`: using the wrong data type, for example adding a string and an integer
- `ValueError`: right type but wrong value, for example `int("hello")`
- `IndexError`: list index out of range
- `KeyError`: dictionary key not found
- `ZeroDivisionError`: dividing by zero
- `AttributeError`: method or attribute does not exist
- `ModuleNotFoundError` (`ImportError`): module cannot be imported
- `FileNotFoundError`: file does not exist
- Logical error: no error message, but the output is wrong

### Handling errors
- `try`, `except`, `else`, `finally`
- Handling more than one error type
- Catching any error with `Exception`
- Raising our own error with `raise`

## Three main categories

| Category | When it happens | Example |
|----------|-----------------|---------|
| Syntax error | Before the program runs | Missing colon |
| Runtime error (exception) | While the program runs | Division by zero |
| Logical error | Program runs but gives a wrong answer | Wrong formula |

## How to run

```
python day5_types_of_errors.py
```

## Folder structure

```
Day5/
├── README.md
└── day5_types_of_errors.py
```
