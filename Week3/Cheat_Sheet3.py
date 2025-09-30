#IF STATEMENT#
#print("Welcome to the program!")
#x = input("Enter the hour (0-23): ")
#hour = int(x)

#if(hour<7):
#   print("Zzz...")
#elif(hour<=8):
#    print("Time to go to class.")
#elif(hour<=12):
#    print("Morning classes are over, but you can still study in the afternoon.")
#else:
#    print("Maybe it's better to take a day off...Zzz...")

#print("\nThanks for visiting!")

 #

# print("Welcome to the temp app!")
# Temp = int(input("What is the temperature of CPU?: "))

#if(Temp > 80):
#   print("Warning, tempterature too high!")
#else:
#   print("All cool, keep on going!")

#num = int(input("Insert number: "))
#Answer = num % 2
#if Answer == 0:
#    print(f"Parillinen: {Answer}")
#else:
#    print(f"Pariton: {Answer}")

 #

#Temp = float(input("How hot is your computer?: "))
#if(Temp > 90):
#    print("you are toast! HAHAHAHA")
#elif(Temp > 80):
#    print("Warning!")
#else:
#    print("You're ok!")

#name1 = input("Anna nimi 1: ")
#name2 = input("Anna nimi 2: ")
#if(len(name1)>len(name2)):
#    print("nimi1 on pidempi kuin nimi2")
#elif(len(name1)<len(name2)):
#    print("nimi2 on pidempi kuin nimi1")
#else:
#    print("nimet ovat yhtä pitkät")

 #

#Town = "Lahti"
#Street = "Mukkulankatu"
#Building = 19

#Town = input("What town are you in?: ")
#Street = input("What street is that?: ")
#Building = input("And what's that building you're looking at?: ")
#if(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#    print("You're at LAB!")
#elif(Town == "Lahti" and (Street != "Mukkulankatu" and Building != 19)):
#     print("You're in the correct town, but check the street address again")
#elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#    print("You're completely lost...")

import random

#print(random.random())
print(random.randint(1, 6))

#Tehtävä: Tee kivi, sakset, paperi peli random -metodia käyttävä (yksinkertainen)

print("Pelataan kivi, sakset, paperi!")

import random

choises = ["kivi", "sakset", "paperi"]

computer_choise = random.choise(choises)

player_choise = input("valitse kivi, sakset tai paperi: ").lower()

print(f"Pelaaja valitsi: {player_choise}")
print(f"Tietokone valitsi: {computer_choise}")

if player_choise == computer_choise:
    print("Tasapeli!")
elif (player_choise == "kivi" and computer_choise == "sakset") or \
     (player_choise == "sakset" and computer_choise == "paperi") or \
     (player_choise == "paperi" and computer_choise == "kivi"):
    print("Pelaaja voittaa!")
else:
    print("Tietokone voittaa!")