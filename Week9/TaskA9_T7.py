########################################################
# Task A9_T7
# Developer Your_First_Name Your_Last_Name
# Date 2025-11-29
########################################################

import sys
import os

def showHelp() -> None:
    print("Usage: python {} <source_file> <destination_file>".format(sys.argv[0]))

def copyFile(PsrcFile: str, PdstFile: str) -> None:
    proceed = True
    if os.path.exists(PdstFile):
        overwrite = input(f'Destination file "{PdstFile}" exists. Overwrite? (y/n): ').strip().lower()
        if overwrite != "y":
            print("Copying aborted by user.")
            proceed = False

    if proceed:
        try:
            with open(PsrcFile, "r", encoding="utf-8") as src:
                data = src.read()
            with open(PdstFile, "w", encoding="utf-8") as dst:
                dst.write(data)
            print(f'Copying file "{PsrcFile}" to "{PdstFile}".')
        except Exception as e:
            print(f"Error occurred while copying: {e}")
            sys.exit(-1)

def main() -> None:
    print("Program starting.")

    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        print("Program ending.")
        return

    srcFile = sys.argv[1]
    dstFile = sys.argv[2]

    if not os.path.exists(srcFile):
        print(f'Source file "{srcFile}" does not exist.')
        sys.exit(-1)

    print(f'Source file "{srcFile}"')
    print(f'Destination file "{dstFile}"')

    copyFile(srcFile, dstFile)
    print("Program ending.")

if __name__ == "__main__":
    main()
