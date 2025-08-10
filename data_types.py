# Object Types / Data Types

#Number: 

import sys;
# In python when you create a variable, it is actually a reference to an object in memory.
# when you get the reference count of an object, it tells you how many references point to that object in memory.
#but when you get the reference count of uninitialized variable it returns random number because it is not pointing to any object in memory.
print(sys.getrefcount('abc'))
print(sys.getrefcount('arsewar'))

# there is no datatype of variable in python, there are data types of the reference.
# so when you create a variable a=5 it is actually the reference to an object of type 'int' in memory.

l1 = [1, 2, 3]
l2 = l1
l1[0] = 10
print(l2)  # Output: [10, 2, 3]
# l2 is a reference to the same object as l1, so when you change l1, l2 also changes.


list1 = [2,3,4]
list2 = list1
list2 = [2,3,4]
list1[0]= 10
print(list1)  # Output: [10, 3, 4]
print(list2)  # Output: [2, 3, 4]
# list2 is now a reference to a new object in memory, so when you change list1, list2 does not change.
# This is because when you assign a new list to list2, it creates a new object in memory and list2 now points to that new object.
# list2 is now a reference to a new object in memory, so it does not change list1.

#Numbers

a = 5
b = 10
c = 15

print(a + b)  # Output: 15
print(a - b)  # Output: -5  
print(a * b)  # Output: 50
print(a / b)  # Output: 0.5
print(a // b)  # Output: 0  
print(a % b)  # Output: 5
print(a ** b)  # Output: 9765625    
print(a & b)  # Output: 0
print(a | b)  # Output: 15  
print(a ^ b)  # Output: 15
print(a << b)  # Output: 5120
print(a >> b)  # Output: 0
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a < b)  # Output: True
print(a > b)  # Output: False
print(a <= b)  # Output: True
print(a >= b)  # Output: False 
print(a is b)  # Output: False this checks the memory location of the objects even tough they have same value
print(a is not b)  # Output: True 

import math
print(math.sqrt(25))  # Output: 5.0
print(math.pow(2, 3))  # Output: 8.0   
print(math.ceil(2.3))  # Output: 3 (gives closest integer greater than or equal to the number)
print(math.floor(2.7))  # Output: 2 (gives closest integer less than or equal to the number)
print(math.pi)  # Output: 3.141592653589793
print(math.e)  # Output: 2.718281828459045
print(math.factorial(5))  # Output: 120
print(math.gcd(12, 15))  # Output: 3
print(math.log(100, 10))  # Output: 2.0
print(math.log2(8))  # Output: 3.0\
print(math.trunc(2.7))  # Output: 2 (gives the integer near to zere)

#complex numbers
complex_num = 3 + 4j
print(complex_num.real)  # Output: 3.0  
print(complex_num.imag)  # Output: 4.0
print(complex_num.conjugate())  # Output: (3-4j)
print(complex_num + 2)  # Output: (5+4j)
print(complex_num - 2)  # Output: (1+4j)    
print(complex_num * 2)  # Output: (6+8j)
print(complex_num / 2)  # Output: (1.5+2j)
print(complex_num ** 2)  # Output: (-7+24j)


#random numbers
import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10

list_of_choices = [1, 2, 3, 4, 5]
print(random.choice(list_of_choices))  # Output: Random choice from the list



#Strings

str1 = "Hello World"
sliced_str = str1[0:5]  # Output: 'Hello'
print(sliced_str)
sliced_str = str1[0:12:2]
print(sliced_str)  # Output: 'Hlo ol'
sliced_str = str1[::-1]  # Output: 'dlroW olleH'

str1.lower()  # Output: 'hello world'
str1.strip()  # Output: 'Hello World' (removes leading and trailing whitespace)
str1.replace("Hello", "Hi")  # Output: 'Hi World'
str1.split(" ")  # Output: ['Hello', 'World']
str1.find("World")  # Output: 6 (returns the index of the first occurrence of the substring)
str1.count("o")  # Output: 2 (counts the number of occurrences of the substring)
lst = ['a','b','c']

str2 = ''.join(lst)  # Output: 'abc' (joins the list into a string)

#Lists
list1 = [1, 2, 3, 4, 5]
list1.append(6)  # Output: [1, 2, 3, 4, 5, 6]
list1.extend([7, 8])  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
list1.insert(0, 0)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]
list1.remove(3)  # Output: [0, 1, 2, 4, 5, 6, 7, 8]
list1.pop()  # Output: 8 (removes and returns the last element)
list1.sort()  # Output: [0, 1, 2, 4, 5, 6, 7]
list1.reverse()  # Output: [7, 6, 5, 4, 2, 1, 0]
list1.index(4)  # Output: 3 (returns the index of the first occurrence of the element)
list1.count(2)  # Output: 1 (counts the number of occurrences of the element)
list1.clear()  # Output: [] (removes all elements from the list)

#dictionaries here order matters

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict1.get('a')  # Output: 1 (returns the value for the given key)
dict1['d'] = 4  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} (adds a new key-value pair)
dict1.pop('b')  # Output: {'a': 1, 'c': 3, 'd': 4} (removes the key-value pair for the given key) have to provide key to remove
dict1.keys()  # Output: dict_keys(['a', 'c', 'd'])
dict1.values()  # Output: dict_values([1, 3, 4])
dict1.items()  # Output: dict_items([('a', 1), ('c', 3), ('d', 4)]) item is a key-value pair here ('a',1) is the item.

for key, value in dict1.items():
    print(f"{key}: {value}")  # Output: a: 1, c: 3, d: 4 (iterates over the key-value pairs)    

#Tuples  (immutables)
tuple1 = (1, 2, 3, 4, 5) 
print(tuple1[0])  # Output: 1 (accessing an element)



