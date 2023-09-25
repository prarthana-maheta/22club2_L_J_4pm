# l1=[1,2,3]
# print(l1)
# for i in l1:
#     print(i)
    # print("hello") if i == 4 else print("hii")
# a=1
# if a==1:
#     print("a")
#     print("1")
#     print("2")
# else:
#     print("1")
#     print("6")


#     print("3")
# else:
#     print("a")
#
# if 5==3:
#         print("5")
#     elif 1==1:
#         print("1")
#     elif 6==2:
#             print("3")
#     else:
#         print("2")
# else:
#     print("3")

    #     del l1[1]
    # else:
    #     print("hello")
#
#
# print(l1)
#
# take input as your name, check whether your name entered is correct or not
#
# find greater number from two numbers
#
# find maxnimum number between three elements
#
# to check whether a person is eligible for voting
#
# check whether person is senior citizen
#
# write a program to check whether a number is positive or negative
#
# write  program to check whether a number is odd or even
# #
# a=5
# b=5
# c=3
# #
#
# if a>b and a==b or b>c:
#     print(a)



# if "a">"sd":
#     print("rdf")

# a="india"
# b=12
#
# ab=['india',12]
#
# if 12 in ab:
#     print(a)
# else:
#     print(b)





# looping through string
# a="banana"
# list1=[]
# for i in a:
#     list1.append(i)
#     # print(i)
# print(list1)

# looping through list
# fruits = ["apple", "1", "cherry"]
# for x in fruits:
#     for y in x:
#         print(y)
#     print(x)




# With the break statement we can stop the
# loop before it has looped through all the items:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]
# i=0
# for x in fruits:
#     i+=1
#
#     print(x,i)
#     if x == "banana":
#         print("continue", x, i)
#         continue
# a=[1,2]
# for i in a:
#     pass

# a = 1
# Exit the loop when x is "banana", but
# this time the break comes before the print:
#
# fruits = [[1,"2","3"], "banana", "cherry"]
# for x in fruits:
#     for _ in x:
#         _+=1
#         for i in _ :
#             print(i)
#         if x == "banana":
#             print(x)
#             print(_)
#             break
#     print(x)


# With the continue statement we can stop
# the current iteration of the loop, and continue
# with the next:

# fruits = ["apple", "banana", "cherry"]
# for x in fruits[::-1]:
#     for y in x:
#         print(y)
#   # if x == "banana":
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
# # for x in reversed(fruits):
# #   # if x == "banana":
# #     print(x)
#
# # print(list(reversed(fruits)))
# print(fruits)
# # print(fruits.reverse())
# fruits.reverse()
# print(fruits)
# for loops cannot be empty, but if you for some
# reason have a for loop with no content, put in
# the pass statement to avoid getting an error.
#
# for x in [0, 1, 2]:
#
#     print(x)

# having an empty for loop like this,
# would raise an error without the pass statement

# pop()


# The range()
# function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# for x in range():
#   print(x)
# a=[1,2,3,4,5]
#
# for x in range(len(a)-1):
#     print(a[x])

# print(range(1,5))

#start,stop,increment
# for x in range(2, 30, 3):
#   print(x)

Example 1: Print the first 10 natural numbers using for loop.
Example 2: Python program to print all the even numbers within the given range.
Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
Example 4: Python program to calculate the sum of all the odd numbers within the given range.
Example 5: Python program to print a multiplication table of a given number

# input_data=int(input())
#
# for i in range(1,len(input_data)):


# Example 6: Python program to count the total number of digits in a number.
# Example 7: Python program that accepts a word from the user and reverses it.
# Example 8: Python program to count the number of even and odd numbers from a series of numbers.
# Example 9: Python program to find the factorial of a given number.






#######################1############
# # between 0 to 10
# # there are 11 numbers
# # therefore, we set the value
# # of n to 11
# n = 11
#
# # since for loop starts with
# # the zero indexes we need to skip it and
# # start the loop from the first index
# for i in range(1, n):
#     print(i)



#######################2########################
# # if the given range is 10
# given_range = 10
#
# for i in range(given_range):
#
#     # if number is divisble by 2
#     # then it's even
#     if i % 2 == 0:
#         # if above condition is true
#         # print the number
#         print(i)


################3##############

# # if the given number is 10
# given_number = 10
#
# # set up a variable to store the sum
# # with initial value of 0
# sum = 0
#
# # since we want to include the number 10 in the sum
# # increment given number by 1 in the for loop
# for i in range(1, given_number + 1):
#     sum += i
#
# # print the total sum at the end
# print(sum)


###############4##############

# # if the given range is 10
# given_range = 10
#
# # set up a variable to store the sum
# # with initial value of 0
# sum = 0
#
# for i in range(given_range):
#
#     # if i is odd, add it
#     # to the sum variable
#     if i % 2 != 0:
#         sum += i
#
# # print the total sum at the end
# print(sum)


################5#####################


# # if the given range is 10
# given_number = input()
#
# for i in range(11):
#     print(f"{given_number}x{i}=",given_number * i)


####################6#####################

#
# # if the given number is 129475
# given_number = 12345
# # for i in given_number:
# #     print(i)
# # # since we cannot iterate over an integer
# # # in python, we need to convert the
# # # integer into string first using the
# # # str() function
# given_number = str(given_number)
# #
# # # declare a variable to store
# # # the count of digits in the
# # # given number with value 0
# count = 0
# #
# for i in given_number:
#     if i.isdigit():
#         count += 1
# #
# # # print the total count at the end
# print(count)




# gn=list(given_number)
# print(len(gn))



#######################7#################

# # input string from user
# given_string = input()
# print(given_string[::-1])
#
# # an empty string variable to store
# # the given string in reverse
# reverse_string = ""
#
# # iterate through the given string
# # and append each element of the given string
# # to the reverse_string variable
# for i in given_string:
#     reverse_string = i + reverse_string
#
# # print the reverse_string variable
# print(reverse_string)




#################10##################

# given list of numbers
# num_list = list(input())
# print(type(num_list))
# print(num_list)
# iterate through the list elemets
# using for loop
# e=0
# o=0
# for i in num_list:
#
#     # if divided by 2, all even
#     # number leave a remainder of 0
#     if i % 2 == 0:
#         e+=1
#         print(i, "is an even number.")
#
#     # if remainder is not zero
#     # then it's an odd number
#     else:
#         o+=1
#         print(i, "is an odd number.")
#
# print(o,e)


######################9#################

#
# # given number
# given_number = 5
#
# # since 1 is a factor
# # of all number
# # set the factorial to 1
# factorial = 1
#
# # iterate till the given number
# for i in range(1, given_number + 1):
#     factorial = factorial * i
#     print(factorial)
#
# print("The factorial of ", given_number, " is ", factorial)

