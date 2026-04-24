ar = 0
varde = 2000000

while varde < 2500000:
    ar = ar + 1
    varde = varde * 1.025

print("Det tar", ar, "ar innan vardet ar minst 2500000 kr.")
print("Slutvarde:", round(varde, 2), "kr")

