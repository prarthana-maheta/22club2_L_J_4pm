# # Collections in Python
# """
# Ordered     Immutable   string      "ahfahdxsd"
# Ordered     Mutable     list        [1,2,3]
# Ordered     Immutable   tuple       (1,2,3)
# Unordered   Mutable     set         {1,2,3,5}
# Unordered   Mutable     Dict         {"name":"prarthana"}
#
# Two special collections:
# strings: Ordered & Immutable collections of characters              " "/ ' '
# dictionaries: Unordered & Mutable collections of key-value pairs
# """
#
# # # list: Ordered & Mutable collection of members
list1=[1,2,3,4,5,6,7,8,91,0]
# numbers = [33,12, 0, -125, 44, 33, 4791234, -5592, 33]
# # index     0  1    2     3   4
# #          -9 -8    -7
# print(len(list1))
# print(type(list1))
# s='123456789'
# # s=123456789
# print(list(s))
# list1[0]="x"
# # print(list1)
# list1=[1,2,3,4,5,6,7,8,91,0]
# print(list1)
# # print(list1[3::2])
# # print(numbers[2:8])
# #
# print altrenate elements from list
# #
# perform addition between first and last element


# print(len(numbers)-1)

# numbers = [33,12, 0, -125, 44, 33, 4791234, -5592, 33]

#
# numbers=["12","96"]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))



#
numbers=[33, 0, -125, 44, 33, 4791234, 8863, 33]
#
#
# # print(min(numbers))
# # print(max(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))
# mix_veg = [1.23, 1.1, 1]
# # print(mix_veg)
# print(min(mix_veg))
# print(sorted(numbers,reverse=True))
# # list1=list(s1)
# print(list1)

# print(numbers[2:5:1])
"""
print(len(numbers))
print(numbers)
print(type(numbers))
characters = list('Krushnam')
print(characters)

print(min(numbers))
print(max(numbers))
sorted_numbers = sorted(numbers)    # sorted() will always give you a NEW LIST
print(numbers)
print(sorted_numbers)

print(sorted(numbers, reverse=True))

vegetables = ["carrot", "tomato", "potato", "spinach", "cucumber", "beetroot", "onion", "Lemon"]
print(vegetables)
print(min(vegetables))
print(max(vegetables))

mix_veg = ["carrot", 3, "tomato", 1.5, "spinach", -0.5]
print(mix_veg)
# print(min(mix_veg))
"""
# Ordered means
"""
+ve & -ve Index numbers of each element
Accessing through +ve or -ve index
slicing is exactly the same as it was in strings

print(numbers[3])
print(mix_veg[3])
print(numbers[2 : -2 : 2])
"""


# li= ["carrot", "tomato", "potato", "spinach", "cucumber", "beetroot", "onion", "Lemon"]
# vegetables = ["carrot", "tomato","1", "spinach", "cucumber", "beetroot", "onion", "Lemon"]
# print(vegetables)
# print(min(vegetables))
# print(max(vegetables))
# print(sorted(vegetables,reverse=True))
# print(len(vegetables))
# print((type(vegetables)))

numbers=[33, 10, -125, 44, 33, 4791234, -5592, 33]

#
# numbers[0]=3333
# print(numbers)

#
numbers.append({1:"one"})
# print(numbers)
# numbers.insert(0,{"abc":"qys"})
numbers.extend([1,2,3])
print(numbers)
# # numbers.append("12345")
# print(numbers)
# # Mutable
# # # numbers[3] = 119.8
# # # print(numbers)
# #
# # # list methods
# # numbers.append(2000)
# #
# # numbers.append(3000)
# # print(numbers)
# # numbers.append(3000)
# # numbers.append(3000)
# # print(numbers)
# # numbers.append(3000)
# # print(numbers)
# #
# # numbers=[1,2,3]
# # print(numbers)
# # numbers.clear()
# print(numbers)
# # numbers.append(1)
#
numbers=[33, 10, -125, 44, 33, 4791234, -5592, 33]
del numbers[2]
print(numbers)
#

# print(numbers.count(10))
#
# s1="aaaaaa"
# print(s1.count('s',2,4))
# print(numbers.count('s'))



li=[1,2,3,4,5,6,7,8,9,0]
# output:
# [1,3,5,7,9]
# [1,0]
# [1,2,3,4,5,6,7,8,9,0,"i",55]
# [1,2,55,3,4,5,6,7,8,9,0]
# print(li[2:4].count(3))
li=[23,24,3,2,4,5,6,7,8,9,0]
# li.remove(2)
# li.clear()
# del li[0]
li.pop()
print(li)