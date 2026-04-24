hittad = False

for x in range(-20, 21):
    if 4 * x == 2 * x + 11:
        print("x =", x)
        hittad = True

if hittad == False:
    print("Jag hittar inte losningen.")
