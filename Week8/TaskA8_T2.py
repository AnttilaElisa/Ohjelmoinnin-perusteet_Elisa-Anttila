from calcLib import add, subtract, multiply, divide

def main() -> None:
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice in (1, 2, 3, 4):
            x = askValue("first")
            y = askValue("second")
            
            try:
                if choice == 1:
                    result = add(x, y)
                    op = "+"
                elif choice == 2:
                    result = subtract(x, y)
                    op = "-"
                elif choice == 3:
                    result = multiply(x, y)
                    op = "*"
                elif choice == 4:
                    result = divide(x, y)
                    op = "/"
                
                print(f"{x} {op} {y} = {result}\n")
            except ValueError as e:
                print(f"Error: {e}\n")
        else:
            print("Invalid choice!\n")

    print("Program ending.")


def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")


def askChoice() -> int:
    return int(input("Your choice: "))


def askValue(PPrompt: str) -> float:
    return float(input(f"Insert {PPrompt} value: "))


if __name__ == "__main__":
    main()
