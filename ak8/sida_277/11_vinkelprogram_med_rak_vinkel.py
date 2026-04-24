v = float(input("Ange vinkelns storlek. "))

if v < 90:
    print("Vinkeln ar spetsig.")
elif v == 90:
    print("Vinkeln ar rat.")
elif v == 180:
    print("Vinkeln ar rak.")
else:
    print("Vinkeln ar trubbig.")
