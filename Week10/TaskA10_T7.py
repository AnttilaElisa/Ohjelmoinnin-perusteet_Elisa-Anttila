########################################################
# Task A10_Tx
# Developer First_name Last_name
# Date YYYY-MM-DD
########################################################

import random

random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int):
    """
    Randomly places mines (value 9) into the PMineField.
    """
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    placed = 0
    while placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1
    return None

def calculateNearbys(PMineField: list[list[int]]) -> None:
    """
    Calculates nearby mine counts for each non-mine cell.
    """
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            # Check all 8 neighbors
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if PMineField[nr][nc] == 9:
                            count += 1
            PMineField[r][c] = count
    return None

def generateMinefield(
        PMineField: list[list[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    """
    Generates a minefield with given dimensions and mine count.
    """
    PMineField.clear()
    for i in range(PRows):
        PMineField.append([0] * PCols)

    layMines(PMineField, PMines)
    calculateNearbys(PMineField)
    return None

def showBoard(PMineField: list[list[int]]) -> None:
    """Print the minefield row by row."""
    if not PMineField:
        print("No board generated yet.")
        return
    for row in PMineField:
        print(row)

def saveBoard(PMineField: list[list[int]], filename: str) -> None:
    """Save the minefield to a file in comma-separated format."""
    try:
        with open(filename, "w") as f:
            for row in PMineField:
                line = ",".join(map(str, row))
                f.write(line + "\n")
        print(f"Board saved to {filename}")
    except Exception as e:
        print(f"Error saving board: {e}")

def main() -> None:
    PMineField: list[list[int]] = []
    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            try:
                rows = int(input("Insert rows: ").strip())
                cols = int(input("Insert columns: ").strip())
                mines = int(input("Insert mines: ").strip())
                generateMinefield(PMineField, rows, cols, mines)
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == "2":
            showBoard(PMineField)

        elif choice == "3":
            if not PMineField:
                print("No board generated yet.")
                continue
            filename = input("Insert results filename: ").strip()
            saveBoard(PMineField, filename)

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
