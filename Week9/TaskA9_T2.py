########################################################
# Task A9_T2
# Developer Your_First_Name Your_Last_Name
# Date 2025-11-29
########################################################

import sys

print("Program starting.")

user_input = input("Insert exit code(0-255): ")

try:
    exit_code = int(user_input)
except ValueError:
    print("Error! '{}' is not a valid integer.".format(user_input))
    sys.exit(1)

if exit_code < 0 or exit_code > 255:
    print("Error! Exit code must be between 0 and 255.")
    sys.exit(1)

print("Clean exit")
sys.exit(exit_code)
