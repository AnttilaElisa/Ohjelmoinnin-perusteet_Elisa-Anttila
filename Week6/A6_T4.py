def readFile(filename: str) -> str:
    with open(filename, "r", encoding="UTF-8") as f:
        return f.read()


def analyseNames(data: str) -> str:
    names = [name.strip() for name in data.split(";") if name.strip() != ""]

    if len(names) == 0:
        report = (
            "#### REPORT BEGIN ####\n"
            "No valid names found.\n"
            "#### REPORT END ####"
        )
        return report

    name_count = len(names)
    lengths = [len(name) for name in names]
    shortest = min(lengths)
    longest = max(lengths)
    average = sum(lengths) / name_count

    report = (
        "#### REPORT BEGIN ####\n"
        f"Name count - {name_count}\n"
        f"Shortest name - {shortest} chars\n"
        f"Longest name - {longest} chars\n"
        f"Average name - {average:.2f} chars\n"
        "#### REPORT END ####"
    )

    return report


def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ").strip()
    print(f'Reading names from "{filename}".')

    data = readFile(filename)

    print("Analysing names...")
    report = analyseNames(data)
    print("Analysis complete!")

    print(report)

    print("Program ending.")


if __name__ == "__main__":
    main()
