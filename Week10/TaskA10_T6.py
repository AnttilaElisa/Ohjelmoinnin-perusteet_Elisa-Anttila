########################################################
# Task A10_Tx
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import sys
import copy
import time
from typing import Callable

def readValues(PFilename: str, PValues: list[int]) -> None:
    """Read integers from a dataset file into PValues list."""
    PValues.clear()
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    PValues.append(int(line))
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        return None
    return None

def bubbleSort(PNums: list[int]) -> list[int]:
    """Bubble sort implementation (returns sorted list)."""
    arr = PNums[:]  # work on a copy
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quickSort(PNums: list[int]) -> list[int]:
    """Quick sort implementation (returns sorted list)."""
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums) // 2]
    left = [x for x in PNums if x < pivot]
    middle = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]
    return quickSort(left) + middle + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    """Measure sorting time in nanoseconds."""
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime

def saveResults(PResults: list[str], PFilename: str) -> None:
    """Save results to a file."""
    try:
        with open(PFilename, "w") as f:
            for line in PResults:
                f.write(line + "\n")
        print(f"\nSaved results in files:\n\n{PFilename}")
    except Exception as e:
        print(f"Error saving results: {e}")
    return None

def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    Filename: str = ""

    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            Filename = input("Insert dataset filename: ").strip()
            readValues(Filename, Values)

        elif choice == "2":
            if not Values:
                print("No dataset loaded. Please read values first.")
                continue

            # Measure speeds
            builtin_time = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_time = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_time = measureSortingTime(quickSort, copy.deepcopy(Values))

            # Store results
            Results.clear()
            Results.append(f"Measured speeds for dataset '{Filename}':")
            Results.append(f" - Built-in sorted {builtin_time} ns")
            Results.append(f" - Buble sort {bubble_time} ns")
            Results.append(f" - Quick sort {quick_time} ns")

            # Display results
            print("\n" + "\n".join(Results))

        elif choice == "3":
            if not Results:
                print("No results to save. Measure speeds first.")
                continue
            result_file = input("Insert results filename: ").strip()
            saveResults(Results, result_file)

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.")

    # Cleanup
    Values.clear()
    Results.clear()
    print("\nProgram ending.")
    return None

if __name__ == "__main__":
    main()
