def main() -> None:
    values = []
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            filename = input("Insert filename: ")
            values = readValues(filename)
        elif choice == 2:
            print(f"Amount of values {len(values)}\n")
        elif choice == 3:
            total = calculateSum(values)
            print(f"Sum of values {total}\n")
        elif choice == 4:
            avg = calculateAverage(values)
            print(f"Average of values {avg}\n")
        else:
            print("Invalid choice!\n")

    print("Program ending.")


def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


def readValues(filename: str) -> list[float]:
    values = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    values.append(float(line))
    except FileNotFoundError:
        print("File not found.\n")
    except ValueError:
        print("File contains invalid values.\n")
    return values


def calculateSum(values: list[float]) -> float:
    return round(sum(values), 1)


def calculateAverage(values: list[float]) -> float:
    if not values:
        return 0.0
    return round(sum(values) / len(values), 1)


if __name__ == "__main__":
    main()
