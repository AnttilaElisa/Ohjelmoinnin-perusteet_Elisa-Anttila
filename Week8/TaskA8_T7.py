from drawLib import drawSquare, drawCircle, drawHexagon, saveSvg
import svgwrite

def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing()

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print("Insert square")
            drawSquare(Dwg)
        elif choice == 2:
            print("Insert circle")
            drawCircle(Dwg)
        elif choice == 3:
            drawHexagon(Dwg)
        elif choice == 4:
            saveSvg(Dwg)
        elif choice == 0:
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice!\n")

    print("Program ending.")


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


if __name__ == "__main__":
    main()
