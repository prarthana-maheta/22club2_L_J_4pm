# # 3. Write a Python class BankAccount with attributes
# # like account_number, balance, date_of_opening and customer_name,
# # and methods like deposit, withdraw, and check_balance.
# #

def func(abc):
    return abc

# # Map
# # The map() function in python has the following syntax:
# #
# map(func, *iterables)
# #
# [1,2,3,4,5]
# # Where func is the function on which each element
# # in iterables (as many as they are) would be applied on.
# # Notice the asterisk(*) on iterables? It means there can be as many iterables as possible,
# # in so far func has that exact number as required input arguments. Before we move on to an example,
# # it's important that you note the following:
# #
# # In Python 2, the map() function returns a list. In Python 3, however,
# # the function returns a map object which is a generator object. To get the result as a list,
# # the built-in list() function can be called on the map object. i.e. list(map(func, *iterables))
# # The number of arguments to func must be the number of iterables listed.
# # dict1={"1":"one"}
# # print(dict1.items())
# # # Using map() to square each element of the data list
# data = [1, 2, 3, 4, 5]
# #
# # # Map function returns the map object
# map_object(1,4,9,16,25)
# 1*2*4*5=120
# take input from user and find factorial of that

# def func(a):
#     return a*a
# print(list(map(func, [1,2,3,4])))


# # lambda
# data=[1,2,3,4,5]
# squares = dict(map(lambda x: (x,x*x), data))
# print(squares)

# dict1={}
# for i in data:
#     dict1.update({i:i*i})
# print(dict1)


# # #

# # Lambda function
# # # A lambda function is a small anonymous function.
# # #
# # # A lambda function can take any number of arguments, but can only have one expression.
# #
# # # Why Use Lambda Functions?
# # # The power of lambda is better shown when you use them as an anonymous function inside another function.
# #
# lambda arguments : expression
# def sum(a):
#     return a+10
# print(sum(5))
 
# x = lambda a,b :  [a,b if a == 1 else print(b)]

# if a == 1:
#     print(a)

# else: 
#     print(b)

# print(x(1,5))
# #
# x = lambda a, b : a * b
# print(x(5, 6))
# # pets = ['cats', 'dogs', 'fishes', 'rabbits', 'hamsters', 'parrots', 'ferrets']
# # l1=[]
# # for word in pets[::-1]:
# #     l1.append(word)
# #     # print(word)
# # l1.sort()
# # print(l1)
# #
# # # pets=['a','c','d','b']
# # pets = ['cats', 'dogs', 'fishes', 'rabbits', 'hamsters', 'parrots', 'ferrets']
# # pets.sort(key=lambda word: word[::-1])
# # print(pets)
#
#
#
#
# # product = (lambda *a: a**2)
# # print("The product is:", product(10, 20))
#
# text = (lambda x="Java", y = " is", z = " my favourite": x + y + z)
# print(text("Python"))

# # Iterating the elements of the squares
# for i in squares:
#     print(i, end=" ")
# def square(x):
#     return x*x
# # Also, we can convert the map object into a list
# squares = list(map(square, data))
# print(f"Squares: {squares}")


# Python 3

# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [1, 2, 3, 4, 5]
#
# results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
#
# print(results)

# Filter
# While map() passes each element in the iterable through
# a function and returns the result of all elements having passed through the function,
# filter(), first of all, requires the function to return boolean values (true or false)
# and then passes each element in the iterable through the function,
# "filtering" away those that are false. It has the following syntax:
#
# filter(func, iterable)
#
# The following points are to be noted regarding filter():
#
# Unlike map(), only one iterable is required.
# The func argument is required to return a boolean type.
# If it doesn('t, filter simply returns the iterable passed to it. Also, as only one iterable is required, '
#             'it')s implicit that func must only take one argument.
# filter passes each element in the iterable through func
# and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".
#
#
# # Python 3
# dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

# palindromes = list(filter(lambda word: word == word[::-1], dromes))

# print(palindromes)


# cities = [
#     ("New York", 8500000),
#     ("Los Angeles", 4000000),
#     ("Chicago", 2700000),
#     ("Houston", 2300000),
#     ("Phoenix", 1600000),
#     ("Philadelphia", 1500000),
#     ("San Antonio", 1500000),
# ]

# x = list(filter(lambda x: x[1]>2000000, cities))
# print(x)


#
# Reduce
# reduce applies a function of two arguments cumulatively
# to the elements of an iterable, optionally starting with an initial argument. It has the following syntax:
#
# reduce(func, iterable,[ initial])
#

# Where func is the function on which each element
# in the iterable gets cumulatively applied to,
# and initial is the optional value that gets placed before the elements of the iterable in the calculation,
# and serves as a default when the iterable is empty. The following should be noted about reduce():
# 1. func requires two arguments, the first of which is the first element in iterable
# (if initial is not supplied) and the second element in iterable. If initial is supplied,
# then it becomes the first argument to func and the first element in iterable becomes the second element.
# 2. reduce "reduces" (I know, forgive me) iterable into a single value.

# Python 3
from functools import reduce

numbers = [1,2,3]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers,10)
print(result)


from functools import reduce

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: x, my_floats))
filter_result = list(filter(lambda name: name, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)


list1=[1]
list2=list1+list1
print(list2)

# def fibonacc i(count):
#     fib_list = [0, 1]
#     any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
#                                          range(2, count)))
#     return fib_list[:count]
# print(fibonacci(10))