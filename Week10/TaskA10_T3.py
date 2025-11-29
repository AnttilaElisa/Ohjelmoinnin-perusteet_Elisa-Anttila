########################################################
# Task A10_Tx
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import sys

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    """Sort PValues in-place using bubble sort."""
    n = len(PValues)
    for i in range(n - 1):  # outer loop for passes
        for j in range(n - i - 1):  # inner loop for comparisons
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
            else:
                if PValues[j] < PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
    return None

def readValues(PFilename: str) -> list[int]:
    """Read integers from file into a list."""
    values = []
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    values.append(int(line))
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    return values

def main() -> None:
    print("Program starting.")
    # CLI argument or prompt
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = input("Insert filename: ").strip()

    values = readValues(filename)

    # Raw
    print(f"Raw '{filename}' -> {', '.join(map(str, values))}")

    # Ascending
    asc_values = values.copy()
    bubbleSort(asc_values, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc_values))}")

    # Descending
    desc_values = values.copy()
    bubbleSort(desc_values, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc_values))}")

    print("Program ending.")

if __name__ == "__main__":
    main()
