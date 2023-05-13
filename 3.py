#3. Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
x, y = int(input("type number1: ")), int(input("type number2: "))
     

# output
print("================================")
print("Table between {x} and {y} :")
for n in range(x,y+1):
    print("================================")
    print(f"Table of {n}")
    for z in range(1,13):
        result = n*z
        print(f"{n} x {str(z).ljust(3)} = {result}")
