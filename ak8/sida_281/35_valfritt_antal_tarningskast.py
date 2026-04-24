import random

antal_kast = int(input("Hur manga tarningskast vill du gora? "))
treor = 0

for x in range(antal_kast):
    slumptal = random.randint(1, 6)
    if slumptal == 3:
        treor = treor + 1

andel_treor = treor / antal_kast * 100

print("Antal kast:", antal_kast)
print("Antal treor:", treor)
print("Andel treor:", round(andel_treor, 3), "%")
