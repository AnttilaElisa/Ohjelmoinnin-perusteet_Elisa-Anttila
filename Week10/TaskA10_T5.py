########################################################
# Task A10_Tx
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import sys

def recursiveFactorial(PNum: int) -> int:
    """Calculate factorial recursively."""
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    try:
        # Ask user for input
        user_input = input("Insert factorial: ").strip()
        num = int(user_input)

        # Display results
        print(f"Factorial {num}!")
        result = recursiveFactorial(num)
        print(f"{num} = {result}")

    except ValueError:
        print("Error: Please enter a valid integer.")
        sys.exit(1)

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
