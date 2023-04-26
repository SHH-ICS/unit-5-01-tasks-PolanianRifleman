import random

while True:

    a = input("What is your first value? ")

    try:
        a = float(a)
    except ValueError:
        print("INVALID INPUT. ENTER NUMBER")
        continue

    b = input("what is your second value? ")

    try:
        b = float(b)
    except ValueError:
        print("INVALID INPUT. ENTER NUMBER")
        continue

    try:
        c = random.randint(a,b)
    except ValueError:
        print("INVALID INPUT. PLEASE ENTER SMALLER NUMBER FIRST")
        continue
    
    c = random.randint(a,b)

    print("Your random output is " + str(c))
    break