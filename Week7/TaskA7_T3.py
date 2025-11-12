WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()

    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Error: File "{PFilename}" not found.')
        return

    for line in lines[1:]:
        line = line.strip()
        if line == "":
            continue
        PRows.append(line)
    return


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    WeekdayTimestampAmount = [0, 0, 0, 0, 0, 0, 0]

    for row in PRows:
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                WeekdayTimestampAmount[i] += 1

    PResults.clear()
    PResults.append("### Timestamp analysis ###")
    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")
    PResults.append("### Timestamp analysis ###")
    return


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for result in PResults:
        print(result)
    return


def main() -> None:
    print("Program starting.")
    
    rows: list[str] = []
    results: list[str] = []

    filename = input("Insert filename: ").strip()
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)

    rows.clear()
    results.clear()
    print("Program ending.")
    return


if __name__ == "__main__":
    main()
