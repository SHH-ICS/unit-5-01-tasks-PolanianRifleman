import math

while True:

    a = input("What is the length of side a? ")

    try:
        a = float(a)
    except ValueError:
        print("INVALID INPUT. ENTER A NUMBER")
        continue

    b = input("What is the lenght of side b? ")

    try:
        b = float(b)
    except ValueError:
        print("INVALID INPUT. ENTER A NUMBER")
        continue
    
    c = math.sqrt((a**2) + (b**2))

    print("Your hypotenuse is " + str(c))
    break