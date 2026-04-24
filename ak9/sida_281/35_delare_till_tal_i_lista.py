tal = int(input("Skriv ett heltal: "))
delare = []

for n in range(1, tal + 1):
    if tal % n == 0:
        delare.append(n)

print(tal, "ar delbart med:", delare)

