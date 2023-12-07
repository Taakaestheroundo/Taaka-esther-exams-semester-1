# (i)A python program that prints the following patterns.
for x in range(1, 6):
    for z in range(1, x + 1,):
        print(z, end='')
    print()


#(ii)A recursive function to calculcate factorial of a given number n.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# function test with n = 5
n = 5
output = factorial(n)

print(f"The factorial of {n} is: {output}")    

# (iii)A python function that takes two parameters(a and b)and returns their sum.
def add(a, b):
    return a + b

# function testing with (a = 3) and (b = 4)
a = 3
b = 4
output = add(a, b)

print(f"The sum of {a} and {b} is: {output}")


#(iv)A python class named "car"with attributes:brand and year
class Car:
    def __init__(mine, brand, year):
        mine.brand = brand
        mine.year = year

    def display_info(mine):
        print(f"Car Information: Brand - {mine.brand}, Year - {mine.year}")

# types of cars sold:
car20 = Car("Mycars", 3900)
car10 = Car("Buses", 6732)

car20.display_info()
car10.display_info()

# (v) Creating an instance of the class about "cars"
my_car = Car("Horda", 2015)

# Display information about the car
my_car.display_info()