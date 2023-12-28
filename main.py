with open("osvenyek.txt", "r", encoding="utf-8") as file:
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
print


print("5. feladat")
statisztika = {i:osvenyeklist[osv-1].count(i) for i in osvenyeklist[osv-1]}
[print(f"{k}: {v} darab") for k, v in statisztika.items()]


"""with open("kulonleges.txt", "w", encoding="utf-8") as file:
    for i in osvenyeklist[osv-1]:
        file.read("KURVAANYD")"""

