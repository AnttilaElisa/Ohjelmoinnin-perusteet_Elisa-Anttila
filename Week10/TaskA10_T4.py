########################################################
# Task A10_Tx
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import sys

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    """Merge two sorted lists into PMerge."""
    i = j = 0
    while i < len(PLeft) and j < len(PRight):
        if PAsc:
            if PLeft[i] <= PRight[j]:
                PMerge.append(PLeft[i])
                i += 1
            else:
                PMerge.append(PRight[j])
                j += 1
        else:
            if PLeft[i] >= PRight[j]:
                PMerge.append(PLeft[i])
                i += 1
            else:
                PMerge.append(PRight[j])
                j += 1
    PMerge.extend(PLeft[i:])
    PMerge.extend(PRight[j:])
    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    """Sort PValues using merge sort (not in-place, but overwrite list)."""
    if len(PValues) <= 1:
        return None
    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]

    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    merged = []
    merge(left, right, merged, PAsc)

    PValues[:] = merged
    return None

def readValues(PFilename: str) -> list[int]:
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
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = input("Insert filename: ").strip()

    values = readValues(filename)

    print(f"Raw '{filename}' -> {', '.join(map(str, values))}")

    asc_values = values.copy()
    mergeSort(asc_values, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc_values))}")

    desc_values = values.copy()
    mergeSort(desc_values, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc_values))}")

    print("Program ending.")

if __name__ == "__main__":
    main()

