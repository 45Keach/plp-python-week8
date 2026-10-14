# Personal Mini-Toolkit

A beginner-friendly Python menu program with three tools: a To-Do List, a Simple Calculator, and a Number Guessing Game.

## How to run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run `python toolkit.py` (or `python3 toolkit.py` on some systems).
5. Choose a menu number and follow the prompts. Choose `4` to quit.

## Tools

- **To-Do List:** Add, view, and remove tasks. The list changes while the program runs.
- **Simple Calculator:** Add, subtract, multiply, or divide two numbers, with input and division-by-zero checks.
- **Number Guessing Game:** Guess a random number from 1 to 10; hints help you find it.

## Concepts practiced

Menu loops, `if` / `elif` / `else`, lists, `for` loops, input validation, exception handling, random numbers, and f-strings.

## Reflection

The hardest part was making the menu return reliably after each tool without ending the whole program. The bug that took the longest to think through was handling invalid input without letting a number conversion crash the program. I used `try` and `except` around inputs that need to be numbers. I also checked for division by zero in the calculator. The to-do list helped me understand how a list can change as a program runs. Testing each menu option made it easier to catch small issues and improve the messages. With one more week, I would save tasks to a file so they are still there after the program closes.

## Screenshots

The `screenshots/` folder contains terminal-style examples showing the main menu, graceful handling of an invalid menu choice, and each tool in action.
