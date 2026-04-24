import random

antal_tior = 0

for _ in range(10000):
    slumptal = random.randint(1, 10)
    if slumptal == 10:
        antal_tior = antal_tior + 1

print("Antalet tior:", antal_tior)

