# Roman to Decimal (Python)

A command-line tool that converts Roman numerals into decimal numbers. Built as a beginner Python project to practice dictionaries, loops and conditions.

## Features
- Converts Roman numerals like `XIV` to `14` and `MCMXCIV` to `1994`
- Handles the subtraction rule (`IV` = 4, `IX` = 9, `XC` = 90 and so on)
- Accepts lower case and upper case input
- Shows an error if the input has letters that are not Roman numerals
- Runs in a loop until you type `q`
- Includes tests using `assert`

## Roman numeral values
| Letter | I | V | X | L | C | D | M |
|---|---|---|---|---|---|---|---|
| Value | 1 | 5 | 10 | 50 | 100 | 500 | 1000 |

## How it works
1. Each letter is looked up in a dictionary to get its value.
2. The program goes through the letters from left to right.
3. If a letter is **smaller** than the letter after it, its value is **subtracted**. Otherwise, it is **added**.

Example with `XIV`:

```
X (10) -> next is I (1), not bigger -> add 10   -> total 10
I (1)  -> next is V (5), bigger     -> subtract -> total 9
V (5)  -> no next letter            -> add 5    -> total 14
```

## Requirements
- Python 3.6 or newer (no extra libraries needed)

## How to run
```
python roman.py
```
Type a Roman numeral and press Enter. Type `q` to quit.

## Example
```
Enter a Roman numeral (or q to quit): XIV
Decimal: 14

Enter a Roman numeral (or q to quit): MCMXCIV
Decimal: 1994

Enter a Roman numeral (or q to quit): ix
Decimal: 9

Enter a Roman numeral (or q to quit): ABC
Error: use only the letters I, V, X, L, C, D, M.

Enter a Roman numeral (or q to quit): q
```

## Functions
| Function | What it does |
|---|---|
| `roman_to_decimal(text)` | Returns the decimal number, or `None` if the input is invalid |
| `main()` | Menu loop that asks for input and prints the result |

## Run the tests
```
python test_roman.py
```
If everything works, it prints `All tests passed`.

## Project structure
```
RomanToDecimal/
├── roman.py        # conversion logic and command-line menu
├── test_roman.py   # tests using assert
├── .gitignore      # ignores __pycache__
└── README.md
```

## What I learned
- A dictionary stores each Roman letter and its value, so I can look values up quickly.
- Looping with `range(len(text))` gives me the position of each letter, so I can compare it with the next one.
- Using `and` to combine conditions, and checking `i + 1 < len(text)` first, avoids an error on the last letter.
- A small typo (`value[...]` instead of `value < VALUES[...]`) caused a `TypeError`. Reading the error message helped me find and fix it.
- Returning `None` for invalid input keeps the conversion logic separate from the printing.

## Limitations
- It does not reject badly formed numerals like `IIII` or `VX`. It just calculates a value for them.
- It only converts Roman to decimal, not the other way round.

## Ideas for improvement
- Reject invalid numerals using a regex
- Add decimal to Roman conversion
- Limit the input to numbers from 1 to 3999