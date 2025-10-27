#The following code should calculate the area of a rectangle based on the user inputs.

#Fix the example code below without altering defined function names or function parameters. Fixed code must produce similar results as is in the expected program runs. The code must also be fixed to match the requirements in the provided style guide.

#def askDimension(PPrompt: str) -> float:
#   Feed = input("Insert number: ")
#   return Feed

#Width = askNumber("width")
#Height = askNumber("height")

#def calcRectangleArea(PWidth: float, PHeight: float) -> float:
#   PWidth = Area * PHeight
#   return Sum

#Area = calculateArea()
#print("")
#print("Area is {Area}²")
#print("end")

#Expected program runs

#run 1 run 2 run 3
#Program starting.
#Insert width: 2
#Insert height: 3

#Area is 6.0²
#Program ending.

def askDimension(PPrompt: str) -> float:
    value = float(input(f"Insert {PPrompt}: "))
    return value

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    area = PWidth * PHeight
    return area

def main():
    print("Program starting.")
    width = askDimension("width")
    height = askDimension("height")
    print()
    area = calcRectangleArea(width, height)
    print(f"Area is {area}²")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()