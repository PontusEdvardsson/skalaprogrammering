import random

ettor = 0

for x in range(1000):
    slumptal = random.randint(1, 6)
    if slumptal == 1:
        ettor = ettor + 1

print("Antal ettor:", ettor)
