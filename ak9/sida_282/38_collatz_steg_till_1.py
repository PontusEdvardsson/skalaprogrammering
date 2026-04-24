for start in range(1, 101):
    n = start
    steg = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        steg = steg + 1

    print("Talet", start, "kraver", steg, "steg till 1")

