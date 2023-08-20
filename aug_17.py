#while
# i = 1
# while i <= 6:
#   print(i)
#   i += 1


#while with break
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

#while with continue
# i = 0
# while i < 6:
#   pass



# A function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.
# def abc():
#   print("Hello from a function")
#
# abc()

# def my_function(a):
#     print(a + " Refsnes")
# my_function("123")
# my_function("234")
# my_function("356")

#
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# A parameter is the variable listed inside the parentheses in the function definition.
#
# An argument is the value that is sent to the function when it is called

# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Emil", "Refsnes")


# ********Arbitrary Arguments, *args
# arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
    print(kids)
    for i in kids:
        print("The youngest child is " + i)
#
my_function("Emil", "Tobias", "Linus")
# ()

# Keyword Arguments
# You can also send arguments with the key = value syntax.
# def my_function(child3, child2, child1):
#   print("The youngest child is " + factorialchild3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments
# that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.

# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#
# my_function(fname = "Tobias", lname = "Refsnes")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)

