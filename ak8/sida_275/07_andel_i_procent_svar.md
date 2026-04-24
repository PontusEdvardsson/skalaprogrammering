# Uppgift 7

## a)

Ett fungerande program ar:

```python
delen = float(input("Ange delen utan enhet."))
helheten = float(input("Ange helheten utan enhet."))
andelen = delen / helheten
print("Andelen ar", round(andelen * 100), "%")
```

Om delen ar `23` och helheten ar `84` skrivs ungefarligt detta ut:

```text
Andelen ar 27 %
```

## b)

Andelen multipliceras med `100` for att omvandla ett decimaltal till procent.

Exempel:

```text
0.2738 = 27.38 %
```
