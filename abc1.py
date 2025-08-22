"""
list=[]
n= int(input("Enter the length of list"))
for i in range(n):
    k= int(input("Enter the ele: "))
    list.append(k)

print(list)"""

'''
abc = [[1,2],[3,4]]

print(abc[1][1])'''


'''a = int(input("enter the starting point: "))
b = int(input("Enter the ending point: "))

for num in range(a, b+1):
    if num < 2:
        continue
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break 
    if prime==True:
        print(num)'''


# password = "admin"
# attempts = 3

# while attempts > 0:
#     enter_Pass = input("Enter password: ")

#     if enter_Pass == password:
#         print("Access granted!")
#         break
#     else:
#         attempts = attempts-1
#         if attempts > 0:
#             print("Wrong password. You have", {attempts}, "left.")
#         else:
#             print("Access denied.")

# def calculator():
#     print("choose your choice: ")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter choice: ")

#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))

#     if choice == '1':
#         result = a + b
#         print("Addition is : ", result)
#     elif choice == '2':
#         result = a - b
#         print("sub is: ", result)
#     elif choice == '3':
#         result = a * b
#         print("Product is : ", result)
#     elif choice == '4':
#             result = a / b
#             print("Div is : ", result)
#     else:
#         print("Enter valid number.")


#calculator()



# def iplist(list):
#     normal_List = []
#     for i in list:
#         if type(i) == list:
#             normal_List.append(iplist(i))
#         else:
#             normal_List.append(i)
#     return normal_List


# print(iplist([1, 2, [3, 4], [5, [6, 7]]]))



# def flatten(lst):
#     flat_list = []
#     for i in lst:
#         if type(i) == list:
#             flat_list.extend(flatten(i))
#         else:
#             flat_list.append(i)
#     return flat_list


# print(flatten([1, [2], [[3]], [[[4]]], [[[[5]]]]]))



# def twosum():
#     arr = [1, 3, 5, 8, 2];
#     target = 10
#     result = []
    
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 result.append((i,j))
    
#     return result


# print(twosum())


# username = "abc"

# print(username)

# username = "xyz"

# print(username)


# def two_sum(arr, target):
#     arr = sorted(arr)
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target:
#             return [arr[left], arr[right]]
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1

#     return None 
