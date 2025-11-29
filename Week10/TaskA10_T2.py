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
                if line:  # skip empty rows
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
    # 1. Initialize
    Values: list[int] = []

    # 2. Operate
    print("Program starting.")
    # 2.1 ask filename
    Filename = input("Insert filename: ").strip()

    # 2.2 read values
    readValues(Filename, Values)

    # 2.3 calculate sum of values
    Sum = sumOfValues(Values)

    # 2.4 calculate product of values
    Product = productOfValues(Values)

    # 2.5 display results
    print("# --- Sum of numbers --- #")
    print(Sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(Product)
    print("# --- Product of numbers --- #")

    # 3. Cleanup
    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
