saldo = 0

for n in range(10):
    saldo = saldo * 1.03 + 10000

print("Det finns", round(saldo, 2), "kr pa kontot direkt efter den 10:e insattningen.")
