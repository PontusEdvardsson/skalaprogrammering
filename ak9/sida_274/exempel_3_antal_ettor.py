import random

etta = 0

for n in range(1, 601):
    slumptal = random.randint(1, 6)
    if slumptal == 1:
        etta = etta + 1

print("Antal ettor:", etta)

