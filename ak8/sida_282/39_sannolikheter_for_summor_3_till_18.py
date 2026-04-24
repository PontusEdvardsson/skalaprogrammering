import random

antal_kast = 1000000

for sokt_summa in range(3, 19):
    antal = 0

    for x in range(antal_kast):
        summa = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        if summa == sokt_summa:
            antal = antal + 1

    sannolikhet = antal / antal_kast * 100
    print("Sannolikheten att fa", sokt_summa, "ar:", round(sannolikhet, 1), "%")
