# 

def square(a):
    return a**2
a =int(input("Enter a number to find its square: "))
print(f"The Square of {a} is {square(a)}")


def multiply(a, b):
    return a * b
a = int(input("Enter first number to multiply: "))
b = int(input("Enter second number to multiply: ")) 
print(f"The product of {a} and {b} is {multiply(a, b)}")


def area_and_circumference(radius):
    area =math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference