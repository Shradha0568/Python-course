# age group categotization (<13 are children, 13-19 are teens, 20-64 are adults, 65+ are seniors)

age= int(input("Enter your age: "))
if age < 13:
    print("You are a child.")  
elif age >= 13 and age <= 19:
    print("You are a teen.")
elif age >= 20 and age <= 64:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior.")
else:
    print("Invalid age entered.")

# movie ticket price categorization:
#  (prizes based on age: 12 for adults, 8 for children, everyone gets 2rs discount on wednesday) 
    
age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()  
if day == "wednesday":
    discount = 2
else:
    discount = 0
if age < 13:
    price = 8 - discount
    print(f"Your ticket price is: {price}rs")
elif age >= 13:
    price = 12 - discount
    print(f"Your ticket price is: {price}rs")   

# fruit ripe categorization:
# (if fruit is banana, it is ripe if color is yellow,it is unripe if color is green, and it is overripe if color is brown)

fruit= 'banana'
color = 'yellow'
if fruit == "banana":
    if color == "yellow":
        print("The banana is ripe.")
    elif color == "green":
        print("The banana is unripe.")
    elif color == "brown":
        print("The banana is overripe.")
    else:
        print("Unknown color for banana.")

#choose the mode of transportation based on distance:
# (if distance is less than 3km, walk, if distance is between 3-15km use bike more than 15km use car)

distance = int(input("Enter the distance in km: "))

if(distance<3):
    print("You can walk.")
elif(distance >3 and distance <=15):
    print("you can use bike.")
elif(distance >15):
    print("You can use car.")


#password strength checker:
# (if password is less than 6 characters, it is weak, if it is between 6-12 characters, it is moderate, and if it is more than 12 characters, it is strong) 
password = input("Enter your password: ")

if len(password) < 6:
    print("Your password is weak.")
elif 6 <= len(password) <= 12:
    print("Your password is moderate.")
elif len(password) > 12:
    print("Your password is strong.")

#leap year checker:
# (if year is divisible by 4 and not divisible by 100, it is a leap year, if it is divisible by 400, it is a leap year, otherwise it is not a leap year)
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

