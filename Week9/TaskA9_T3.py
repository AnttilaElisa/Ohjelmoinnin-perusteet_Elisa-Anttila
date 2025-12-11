########################################################
# Task A9_T3
# Developer Your_First_Name Your_Last_Name
# Date 2025-11-29
########################################################

print("Program starting.")

filename = input("Insert filename: ")

try:
    file = open(filename, "r")
except:
    print("Error! File '{}' does not exist.".format(filename))
    raise SystemExit(1)

print("## {} ##".format(filename))

for line in file:
    print(line.rstrip())

file.close()

print("## {} ##".format(filename))

print("Program ending.")

