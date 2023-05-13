#Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can be divided on x,y

x = int(input("type number1: "))
y = int(input("type number2: "))

#output
for n in range(1,101):
    if n%x == 0 and n%y == 0:
        print(n)
