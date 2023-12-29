# 1. feladat
with open("osvenyek.txt", "r", encoding="utf-8") as file:
    osvenyeklist = [i.strip() for i in file]


with open("dobasok.txt", "r", encoding="utf-8") as file:
    dobasoklist = [int(i) for i in file.read().split()]

print("2. feladat")
print(f"A dobások száma: {len(dobasoklist) // 2}")
print(f"Az ösvények száma: {len(osvenyeklist)}")
print()



print("3. feladat")
osvstatisztika = {}
for index, elem in enumerate(osvenyeklist):
    osvstatisztika[index] = len(elem)

for index, elem in osvstatisztika.items():
    if elem == max(osvstatisztika.values()):
        print(f"Az egyik leghosszabb a(z) {index + 1}. ösvény, hossza: {elem} ")
        print()
        break


print("4. feladat")
while  not (1 <= (osv := int(input("Adja meg egy ösvény sorszámát!(1-50): "))) <= 50):
    print("1 és 50 között adj meg sorszámot!")


while not (2 <= (jatekosokszama := int(input("Adja meg a játékosok számát!(2-5): "))) <= 5):
    print("2 és 5 között adj meg sorszámot!")
print()



print("5. feladat")
statisztika = {i:osvenyeklist[osv-1].count(i) for i in osvenyeklist[osv-1]}
[print(f"{k}: {v} darab") for k, v in statisztika.items()]



# 6. feladat
with open("kulonleges.txt", "w", encoding="utf-8") as file:
    for index, mezotipus in enumerate(osvenyeklist[osv], start=1):
        if mezotipus != 'M':
            file.write(f"{index}\t{mezotipus}\n")




print("7. feladat")
osveny = len(osvenyeklist[osv]) * ["M"]
dobas2 = []
dobas2.extend(dobasoklist)
dobas = dobasoklist

körökszama = 0
jateklista = [0] * jatekosokszama

while all(len(osveny) >= i for i in jateklista):
    körökszama += 1
    for i in range(jatekosokszama):
       jateklista[i] += dobas.pop(0)
    # jateklista = [sz + dobas.pop(0) for sz in jateklista]

for key, value in enumerate(jateklista):
    if value >= len(osveny):
        print(f"A játkos a(z) {körökszama+1}. körben fejeződött be. A legtávolagg jutó(k) sorszáma: {int(key)+1}")
        break




osveny2 = osvenyeklist[osv-1]
korokszama2 = 0
# ebben van az 5 jatekos dobasainak osszege
# pl 0 elem az elso jatekos es dobott 120-at
jateklista2 = [0] * jatekosokszama
hosszabb = True
körökszama = 0
while all(len(osveny2) >= i for i in jateklista2) and hosszabb:
    körökszama += 1

    # itt dob minden jatekos
    for i in range(jatekosokszama):
        # dobas2 0 elem a kov. dobas
        jateklista2[i] += dobas2[0]

        try:
            if osveny2[jateklista2[i]-1] == "E":
                jateklista2[i] += dobas2[0]
        except IndexError:
            jateklista2[i] += dobas2[0]
            hosszabb = False

        try:
            if osveny2[jateklista2[i]-1] == "V":
                jateklista2[i] -= dobas2[0] 
        except IndexError:
            jateklista2[i] -= dobas2[0]
            hosszabb = False
        
        del dobas2[0]



print("8. feladat \nNyertes(ek): ", end=" ")
kegtdimenzioslist = [[i+1,e] for i,e in enumerate(jateklista2)]
rendezett1 = sorted(kegtdimenzioslist, key = lambda x: x[1])
nyomtatni = [sublist[0] for sublist in rendezett1[-2:]]
print(*nyomtatni)
del rendezett1[-2:]
rendezett2 = sorted(rendezett1, key = lambda x: x[0])
for i in rendezett2:
    print(f"{i[0]}. játékos, {i[1]}. mező")
