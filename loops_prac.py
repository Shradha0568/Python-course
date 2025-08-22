# counting positive numbers in a list

list1 = [1, -2, 3, -4, 5, 6, -7, 8, -9, 10]
positive_num_count =0

for i in list1:
    if i > 0:
        positive_num_count += 1
    
print(f"Number of positive numbers in the list: {positive_num_count}")

#sum of the even numbers in a list
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for num in list2:
    if num%2 ==0:
        sum +=num

print(f"Sum of even numbers in the list: {sum}")


string1 = "Shradha"
reversed_string = ""
for i in range(0, len(string1)):
    reversed_string = string1[i] + reversed_string

print(f"Reversed string: {reversed_string}")


password = "admin"
attempts = 3

while attempts > 0:
    enter_Pass = input("Enter password: ")

    if enter_Pass == password:
        print("Access granted!")
        break
    else:
        attempts = attempts-1
        if attempts > 0:
            print("Wrong password. You have", {attempts}, "left.")
        else:
            print("Access denied.")
            
