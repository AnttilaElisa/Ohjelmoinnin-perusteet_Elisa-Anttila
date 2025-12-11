########################################################
# Task A10_Tx
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################


import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    """Read integers from a text file into PValues list."""
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line: 
                    try:
                        value = int(line)
                        PValues.append(value)
                    except ValueError:
                        print(f"Error: Non-integer value '{line}' found in file.")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    return None

def sumOfValues(PValues: list[int]) -> int:
    """Return the sum of integers in PValues."""
    Sum = 0
    for v in PValues:
        Sum += v
    return Sum

def productOfValues(PValues: list[int]) -> int:
    """Return the product of integers in PValues."""
    Product = 1
    for v in PValues:
        Product *= v
    return Product

def main() -> None:
    Values: list[int] = []

    print("Program starting.")
    Filename = input("Insert filename: ").strip()

    readValues(Filename, Values)

    Sum = sumOfValues(Values)

    Product = productOfValues(Values)

    print("# --- Sum of numbers --- #")
    print(Sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(Product)
    print("# --- Product of numbers --- #")

    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()

