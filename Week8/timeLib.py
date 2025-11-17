from datetime import datetime

# Constants
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list) -> None:
    """Read timestamps from a file and append datetime objects to PTimestamps list."""
    try:
        with open(PFilename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    dt = datetime.strptime(line, "%Y-%m-%d %H:%M")
                    PTimestamps.append(dt)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid timestamp format in file.")


def calculateYears(PYear: int, PTimestamps: list) -> int:
    return sum(1 for ts in PTimestamps if ts.year == PYear)


def calculateMonths(PMonth: str, PTimestamps: list) -> int:
    month_index = MONTHS.index(PMonth) + 1  # datetime months start at 1
    return sum(1 for ts in PTimestamps if ts.month == month_index)


def calculateWeekdays(PWeekday: str, PTimestamps: list) -> int:
    weekday_index = WEEKDAYS.index(PWeekday)  # Monday = 0
    return sum(1 for ts in PTimestamps if ts.weekday() == weekday_index)
