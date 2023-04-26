import random

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    z = x + y
    a = int(input(f"{x} + {y} = "))
    
    if a == z:
        print("Correct!")
        break
    else:
        print("Incorrect")
        continue
