"""Personal Mini-Toolkit: small, friendly tools for everyday tasks."""

import random


def show_menu():
    """Display the toolkit menu and return the user's choice."""
    print("\n===== PERSONAL MINI-TOOLKIT =====")
    print("1. To-Do List")
    print("2. Simple Calculator")
    print("3. Number Guessing Game")
    print("4. Quit")
    return input("Choose an option (1-4): ").strip()


def todo_list_tool():
    """Let the user add, view, and remove tasks from a changing list."""
    tasks = []
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                print(f'Added "{task}" to your list.')
            else:
                print("A task cannot be blank. Please try again.")
        elif choice == "2":
            if tasks:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your list is empty. Add a task to get started!")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove yet.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                try:
                    number = int(input("Enter the task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f'Removed "{removed}" from your list.')
                    else:
                        print("That task number is not on the list.")
                except ValueError:
                    print("Please enter a whole number for the task number.")
        elif choice == "4":
            print("Returning to the main menu.")
            break
        else:
            print("That option is not available. Please choose 1, 2, 3, or 4.")


def calculator_tool():
    """Calculate the result of adding, subtracting, multiplying, or dividing."""
    print("\n--- Simple Calculator ---")
    try:
        first = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("You cannot divide by zero. Please try again with another number.")
                return
            result = first / second
        else:
            print(f'"{operator}" is not a supported operation. Choose +, -, *, or /.')
            return

        print(f"Result: {first:g} {operator} {second:g} = {result:g}")
    except ValueError:
        print("Please enter valid numbers. The calculator is ready to try again!")


def guessing_game_tool():
    """Run a loop-based game where the user guesses a secret number."""
    secret_number = random.randint(1, 10)
    attempts = 0
    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number from 1 to 10.")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < 1 or guess > 10:
                print("Keep your guess between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed {secret_number} in {attempts} attempt(s). Great job!")
                break
        except ValueError:
            print("Please enter a whole number from 1 to 10.")


def main():
    """Run the menu until the user chooses to quit."""
    print("Welcome to your Personal Mini-Toolkit!")
    while True:
        choice = show_menu()
        if choice == "1":
            todo_list_tool()
        elif choice == "2":
            calculator_tool()
        elif choice == "3":
            guessing_game_tool()
        elif choice == "4":
            print("Thanks for using the Personal Mini-Toolkit. Have a great day!")
            break
        else:
            print(f'"{choice}" is not a valid menu choice. Please enter 1, 2, 3, or 4.')


if __name__ == "__main__":
    main()
