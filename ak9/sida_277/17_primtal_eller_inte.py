tal = int(input("Skriv ett heltal: "))

if tal < 2:
    print(tal, "ar inte ett primtal.")
else:
    ar_primtal = True

    for n in range(2, tal):
        if tal % n == 0:
            ar_primtal = False

    if ar_primtal:
        print(tal, "ar ett primtal.")
    else:
        print(tal, "ar inte ett primtal.")

