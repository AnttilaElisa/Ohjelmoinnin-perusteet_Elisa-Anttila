DELIMITER = ";"


def readValues(FileName: str) -> str:
    File = open(FileName, "r", encoding="utf-8")
    Values = ""

    for Line in File:
        Line = Line.strip()
        Values += Line + DELIMITER

    File.close()

    if Values.endswith(DELIMITER):
        Values = Values[:-1]

    return Values


def analyseValues(PValues: str) -> str:
    Count = 0
    Sum = 0
    Greatest = 0
    Average = 0
    CurrentValueStr = ""

    for Character in PValues:
        if Character == DELIMITER:
            Value = int(CurrentValueStr)
            if Value > Greatest:
                Greatest = Value
            Sum += Value
            Count += 1
            CurrentValueStr = ""
        else:
            CurrentValueStr += Character

    if CurrentValueStr != "":
        Value = int(CurrentValueStr)
        if Value > Greatest:
            Greatest = Value
        Sum += Value
        Count += 1

    Average = Sum / Count

    Results = "Count;Sum;Greatest;Average\n"
    Results += "{0};{1};{2};{3:.2f}\n".format(Count, Sum, Greatest, Average)

    return Results


def displayResults(FileName: str, Results: str):
    print("#### Number analysis - START ####")
    print('File "{}" results:'.format(FileName))
    print(Results)
    print("#### Number analysis - END ####")


def main():
    print("Program starting.")
    FileName = input("Insert filename: ")
    Values = readValues(FileName)
    Results = analyseValues(Values)
    displayResults(FileName, Results)
    print("Program ending.")


if __name__ == "__main__":
    main()

