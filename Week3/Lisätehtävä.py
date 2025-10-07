#jos käyttäjätunnus = omaNimi ja ikä >= 18 ja käyttäjä in admin -> avataan admin sivu"
#Jos käyttäjänätunnus =omaNimi ja ikä >= 18 -> avataan käyttäjäsivu
#Jos ikä < 18 -> kerrotaan käyttäjälle: ikä ei riitä
#Jos käyttäjätunnus != omaNimi -> Pääsy kielletty

#Admin tunnuksilla valikko 1. Lisää uusi käyttäjä, 2. Tarkista laitteen toimista, 3. Exit
#Käyttäjäsivulla valikko 1. Tarkista omat tiedot, 2. Exit

print("Program starting.")
print("Anna käyttäjätunnuksesi ja ikäsi minulle >:)")
Käyttis = input("Käyttäjänimi: ")
Ikä = input("Ikä: ")
print("Ootsä muuten admin?")
admin = input("Ookko nää admin? (kyllä/ei): ")
if Käyttis == "Elisa" and Ikä >= 18 and admin == "yes":
    print("Mennään admmin sivuille...\n")
    print("Vaihtoehdot\n-1 Luo uusi käyttäjätunnus\n-2 Tsekkaa toiminta\n-3 Poistu")
    Valinta = int(input("Valintasi: "))
    if (Valinta == 1):
        print("")