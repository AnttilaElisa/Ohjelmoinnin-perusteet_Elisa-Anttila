# A7_T5 - Electricity consumption summary

DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")


class TIMESTAMP:
    def __init__(self, weekday: str, hour: str, consumption: float, price: float):
        self.weekday = weekday
        self.hour = hour
        self.consumption = consumption
        self.price = price


class DAY_USAGE:
    def __init__(self, weekday: str, usage: float = 0.0, cost: float = 0.0):
        self.weekday = weekday
        self.usage = usage
        self.cost = cost


def readTimestamps(PFilename: str, PTimestamps: list) -> None:
    print(f'Reading file "{PFilename}".')
    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines[1:]:  # skip header
                row = line.strip()
                if row == "":
                    continue
                columns = row.split(DELIMITER)
                ts = TIMESTAMP(columns[0], columns[1],
                               float(columns[2]), float(columns[3]))
                PTimestamps.append(ts)
    except FileNotFoundError:
        print(f'Error: file "{PFilename}" not found.')
    return None


def analyseTimestamps(PTimestamps: list, PResults: list) -> None:
    print("Analysing timestamps.")
    helper: list[DAY_USAGE] = []

    # initialize helper list for all weekdays
    for day in WEEKDAYS:
        helper.append(DAY_USAGE(day, 0.0, 0.0))

    # sum daily usage and cost
    for ts in PTimestamps:
        for day_usage in helper:
            if ts.weekday == day_usage.weekday:
                day_usage.usage += ts.consumption
                day_usage.cost += ts.consumption * ts.price

    # prepare formatted results
    PResults.append("### Electricity consumption summary ###")
    for d in helper:
        PResults.append(f" - {d.weekday} usage {d.usage:.2f} kWh, cost {d.cost:.2f} €")
    PResults.append("### Electricity consumption summary ###")
    return None


def displayResults(PResults: list) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps: list[TIMESTAMP] = []
    results: list[str] = []

    readTimestamps(filename, timestamps)
    analyseTimestamps(timestamps, results)
    displayResults(results)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
