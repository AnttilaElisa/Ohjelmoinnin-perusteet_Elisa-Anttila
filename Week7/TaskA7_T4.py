DELIMITER = ";"


class TIMESTAMP:
    def __init__(self, weekday: str, hour: str, consumption: float, price: float):
        self.weekday = weekday
        self.hour = hour
        self.consumption = consumption
        self.price = price


def readTimestamps(PFilename: str, PTimestamps: list) -> None:
    print(f'Reading file "{PFilename}".')
    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            lines = file.readlines()

            # Skip header row
            for line in lines[1:]:
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


def displayTimestamps(PTimestamps: list) -> None:
    print("Electricity usage:")
    for t in PTimestamps:
        total = t.consumption * t.price
        print(f" - {t.weekday} {t.hour}, price {t.price:.2f}, "
              f"consumption {t.consumption:.2f} kWh, total {total:.2f} €")
    return None


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = []
    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
