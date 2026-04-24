import random

summa12 = 0
antal_kast = 1000000

for x in range(antal_kast):
    summa = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    if summa == 12:
        summa12 = summa12 + 1

andel = summa12 / antal_kast * 100

print("Sannolikheten att fa 12 ar", round(andel, 1), "%")
