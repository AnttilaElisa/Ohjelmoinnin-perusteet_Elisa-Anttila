from timeLib import readTimestamps, calculateYears, calculateMonths, calculateWeekdays, MONTHS, WEEKDAYS

def main() -> None:
    print("Program starting.")
    timestamps = []

    filename = input("Insert filename: ")
    readTimestamps(filename, timestamps)

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            year = int(input("Insert year: "))
            count = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {count}\n")
        elif choice == 2:
            month = input("Insert month: ")
            if month not in MONTHS:
                print("Invalid month name.\n")
                continue
            count = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}\n")
        elif choice == 3:
            weekday = input("Insert weekday: ")
            if weekday not in WEEKDAYS:
                print("Invalid weekday name.\n")
                continue
            count = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}\n")
        else:
            print("Invalid choice!\n")

    print("Program ending.")


def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


if __name__ == "__main__":
    main()
