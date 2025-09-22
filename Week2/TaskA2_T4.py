#Prompt the user to insert the minutes spent on each previous topic task.
#Calculate the sum and the average. Display those in the example program run format(Note! precision).
#Make sure to calculate the required average for two decimal digits and later integer as rounded integer
# (precision 0 + type conversion).

#Example program run:

#Program starting.
print("Program starting.")
#Estimate how many minutes you spent on programming...
print("Estimate how many minutes you spent on programmin...")

#A1_T1: 3
Task1 = float(input("A1_T1: "))
#A1_T2: 7
Task2 = float(input("A1_T2: "))
#A1_T3: 9
Task3 = float(input("A1_T3: "))
#A1_T4: 8
Task4 = float(input("A1_T4: "))
#A1_T5: 13
Task5 = float(input("A1_T5: "))
#A1_T6: 14
Task6 = float(input("A1_T6: "))
#A1_T7: 21
Task7 = float(input("A1_T7: "))

Total = Task1+Task2+Task3+Task4+Task5+Task6+Task7

#In total you spent 75 minutes on programming.
print(f"\nIn total you spent {Total} minutes on programming.")
Average = float(Total/7)
#Average per task was 10.71 min and same rounded to the nearest integer 11 min.
print(f"Average per task was {round(Average,2)} min and same rounded to the nearest integer {round(Average)} min")

#Program ending.
print("\nprogram ending.")