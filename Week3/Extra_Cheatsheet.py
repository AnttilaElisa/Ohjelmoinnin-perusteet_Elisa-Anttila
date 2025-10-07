Children = 3
Hometown = "Lahti"

#Lista
TownsInFinland = ["Lahti,", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

RandomInformation = ["Mira", 48, True, Children, Hometown]

print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NumOTowns = len(TownsInFinland) #Vast: 6
print(TownsInFinland[NumOTowns-1])

Municipalities = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Town = ["Lahti,", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

MunicipalityandTowns = [Municipalities, Town]

print(MunicipalityandTowns[1][-2])

Town.sort()
print(Town)

Teacher = {
    'name' : 'Juha',
    'age' : 50,
    'city':'Lahti'
}

print(Teacher["name"])

Teacher['email']= 'juha.hyytiäinen@lab.fi'

print(Teacher)

for key in Teacher:
    print(key, end=" = ")
    print(Teacher[key])

Student = [
    {"name": "Mikko", "Age": 25, "city": "Tampere"},
    {"name": "Maija", "Age": 30, "city": "Espoo"},
    {"name": "Seppo", "Age": 35, "city": "Helsinki"}
]

print(Student[0])

Cities = {
    "Finland":["Tampere", "Espoo", "Helsinki"],
    "Sweden":["Stocholm", "Malmö"]
}

print(Cities["Finland"][0])

#For loop esimerkki
#Town = ["Lahti,", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

for town in Town:
    print(f"The town of {town}")
print(f"All of the towns {Town}")

for i in range(1,10): 
    print(i)

for i in range(1,10):
    print(i, end=" ")

print("")
for i in range(1, 10, 3):
    print(i)

#laskutoimituksia
Total = 0
for i in range(1,101):
    Total +=i
    print(Total)

print(Total)

for i in range(9):
    if i == 3:
        continue
    print(i)

# Opiskele loopit for ja while, sekä niihin liittyvät komennot continue ja break

# While loop esimerkki

# while 1 < 10:
#   print("Do not try me at home xddd")

i = 0
while i < 10:
    print(f"Iteration number: {i}")
    i += 1
  # i = i + 1

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False

while True:
    if input("Do you want to continue? ") != "yes":
        break
    else:  #Ei välttis tarvii
        continue