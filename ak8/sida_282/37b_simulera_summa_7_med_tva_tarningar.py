import random

summa7 = 0
antal_kast = 1000000

for x in range(antal_kast):
    summa = random.randint(1, 6) + random.randint(1, 6)
    if summa == 7:
        summa7 = summa7 + 1

andel = summa7 / antal_kast * 100

print("Sannolikheten att fa 7 ar", round(andel, 1), "%")
