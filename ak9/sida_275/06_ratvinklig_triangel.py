a = int(input("Ange den kortaste sidan: "))
b = int(input("Ange den nast kortaste sidan: "))
c = int(input("Ange den langsta sidan: "))

if a * a + b * b == c * c:
    print("Triangeln ar ratvinklig.")
else:
    print("Triangeln ar inte ratvinklig.")

