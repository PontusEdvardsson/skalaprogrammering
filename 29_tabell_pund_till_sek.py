pund_tal = [2.20, 6.50, 6.80, 10.80, 5.80, 2.50, 34.60, 4.33, 38.93]

for pund in pund_tal:
    sek = round(pund * 12.65, 2)
    print(pund, "pund motsvarar", sek, "kr.")
