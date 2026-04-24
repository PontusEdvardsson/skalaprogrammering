pund_tal = [2.20, 6.50, 6.80, 10.80, 5.80, 2.50, 34.60, 4.33, 38.93]

for pund in pund_tal:
    dollar = round(pund * 12.65 / 10.46, 2)
    print(pund, "pund motsvarar", dollar, "dollar.")
