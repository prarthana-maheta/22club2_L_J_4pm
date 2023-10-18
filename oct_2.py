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
#     print("yes")
#   i += 1

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     continue
#     print("yes")
#   i += 1
# li=[]
#while with continue
# i = 0
# while i < 6:
#     pass



# A function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.
# def abc_def():
#   print("Hello from a function")
#
# abc_def()

# def my_function(a):
#     print(a + " Refsnes")
# my_function("abc")
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
# def my_function(kidss,*kids,):
#     print(kids)
#     for i in kids:
#         # "Emil"
#         print("The youngest child is " + i)
#
# my_function("Emil", "Tobias", "Linus","123","456")


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# def my_function(child2, child1,child3):
#   print("The youngest child is " ,child3)
#
# my_function(child1="Emil", child2="Tobias", child3="Linus")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments
# that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.


# {
#     "fname":"1",
#     "lname":"2"
# }


# def my_function(abc,rtyc,hdhvsgcv,*fgc,**kid):
#   print(kid["fname"] + kid["lname"])
#
# my_function("wswdw","Sdsfc","dfcdc","weswdsf",fname = (input("enter one number")), lname = (input("enter one number")))


# def my_function(kidss):
#     print(kidss)
#     # for i in kids:
#     #     # "Emil"
#     #     print("The youngest child is " + i)
#
# my_function()


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

