"""with open("osvenyek.txt", "r", encoding="utf-8") as file:
    osvenyeklist = [i.strip() for i in file]


with open("dobasok.txt", "r", encoding="utf-8") as file:
    dobasoklist = [i for i in file.read()]


print("2. feladat")
print(f"A dobások száma: {len(dobasoklist) // 2}")
print(f"Az ösvények száma: {len(osvenyeklist)}")
print()

osvstatisztika = {}
for index, elem in enumerate(osvenyeklist):
    osvstatisztika[index] = len(elem)


print("3. feladat")
for index, elem in osvstatisztika.items():
    if elem == max(osvstatisztika.values()):
        print(f"Az egyik leghosszabb a(z) {index + 1}. ösvény, hossza: {elem} ")
        print()
        break


print("4. feladat")
while  not (1 <= (osv := int(input("Adja meg egy ösvény sorszámát!(1-50): "))) <= 50):
    print("1 és 50 között adj meg sorszámot!")

while not (2 <= int(input("Adja meg a játékosok számát!(2-5): ")) <= 5):
    print("2 és 5 között adj meg sorszámot!")
print()


print("5. feladat")
statisztika = {i:osvenyeklist[osv-1].count(i) for i in osvenyeklist[osv-1]}
[print(f"{k}: {v} darab") for k, v in statisztika.items()]


"""

"""osveny = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
dobas = [2, 4, 6, 5, 6, 1, 4, 1, 3, 4, 5, 1, 2, 4, 6, 2, 3, 3, 5, 5, 6, 2, 1, 3, 4, 4, 2, 6, 2 ,4, 5, 6, 3, 2, 1, 2, 3, 1, 1,6 ,4, 1 ,4 ,4 ,3 ,6 ,1 ,4 ,2 ,6, 2 ,4, 5 ,5 ,1, 4 ,5, 3 ,4 ,6 ,6, 5, 2, 2, 4,1, 1 ,5 ,5 ,5, 2]
osvenyhossza = len(osveny)
jatekosokszama = 3
adatok = [
    ["korokszama", 0]

]


for i in range(jatekosokszama):
    adatok.append(
        {
            "dobasosszeg": 0,
            "dobasok": []
        }
    )

kilep = True
while kilep:
    for i in range(jatekosokszama):

        if adatok[i]["dobasosszeg"].append(dobas[adatok[i]["dobasosszeg"])]) > osvenyhossza:
              adatok[i]["dobasosszeg"].append(dobas.index(adatok[i]["dobasosszeg"]))
              kilep = False
"""

osveny = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
dobas = [2, 4, 6, 5, 6, 1, 4, 1, 3, 4, 5, 1, 2, 4, 6, 2, 3, 3, 5, 5, 6, 2, 1, 3, 4, 4, 2, 6, 2 ,4, 5, 6, 3, 2, 1, 2, 3, 1, 1,6 ,4, 1 ,4 ,4 ,3 ,6 ,1 ,4 ,2 ,6, 2 ,4, 5 ,5 ,1, 4 ,5, 3 ,4 ,6 ,6, 5, 2, 2, 4,1, 1 ,5 ,5 ,5, 2]
osvenyhossza = len(osveny)
jatekosokszama = 1

szamlalo = dobas[0]
for index, elem in enumerate(osveny):
    if len(dobas) > 0:
  
        if index == szamlalo-1:
            print(elem, szamlalo, dobas[0])
            del dobas[0]
            szamlalo += dobas[0]
        else:
            print(elem)
        
    else:
        break

print(sum(dobas))