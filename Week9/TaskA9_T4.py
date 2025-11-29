########################################################
# Task A9_T4
# Developer Your_First_Name Your_Last_Name
# Date 2025-11-29
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    feed = input("Insert Celsius: ")

    # Try converting to float
    try:
        c = float(feed)
    except:
        raise ValueError("could not convert string to float: '{}'".format(feed))

    # Check range
    if c < TEMP_MIN or c > TEMP_MAX:
        raise Exception("{} temperature out of range.".format(c))

    return c


print("Program starting.")

try:
    celsius = collectCelsius()
    print("You inserted {} °C".format(celsius))
except Exception as e:
    print(e)

print("Program ending.")
