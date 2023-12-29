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

