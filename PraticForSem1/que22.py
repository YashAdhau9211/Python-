side1 = float(input("Side 1 = "))
side2 = float(input("Side 2 = "))
side3 = float(input("Side 3 = "))

if side1 == side2 == side3:
    print("The Triangle is a Equlateral Triange.")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("The Triangle is a Isosecls Triange.")
else:
    print("The Triangle is a Scalean Triange.")