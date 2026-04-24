val = input("Skriv O om du vill berakna omkretsen eller A om du vill berakna arean. ")
diameter = float(input("Hur manga meter ar diametern? "))
radie = diameter / 2

if val == "O":
    print("O =", 3.14 * diameter, "m")
else:
    print("A =", 3.14 * radie * radie, "m2")
