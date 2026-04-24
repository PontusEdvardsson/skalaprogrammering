import random

treor = 0
antal_kast = 6000

for x in range(antal_kast):
    slumptal = random.randint(1, 6)
    if slumptal == 3:
        treor = treor + 1

print("Antal treor:", treor)
print("Andel treor:", (treor / antal_kast) * 100, "%")
