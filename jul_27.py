# # Datatypes in Python:
# """
# Numeric: int, float, complex
# a = 7 + 3i, b = 5 + 7i
# (7 + 3i)(5 + 7i)
#
#
# a = 7 + 3j
# b = 5 + 7j
# print(a * b)
#
#
# collections:
# string: Ordered & Immutable Collection Of Characters
# """
# s1='Students of this batch are going to rock the INDIAN software industry!'
# # index: 	 0123456789..................
# # -ve index
# # :	 ......................................................987654321
# # print(s1[-2])
# # print(type(s1))
# print(s1)
# # s1[0]='1'
# # print(s1)
# # print(s1[len(s1)-1])
# s2=s1[::69]
# print(s2)
# s2=s1[:7:2]
# print(s1[:7:2])
# print(s1)
# print(s2)
s1="1=====100 fesfsrsdfcfghdre"

# print(s1[:100])
# s1[0]='1'
# print(s1)
# # # slicing
# s2 = s1[9 : 69]
# print(s1)	# Slicing will always return new data
# print(s2)

# print(s1[600])
# print(s1[12 : 600])
# print(s1[12 : ])
# print(s1[ : 60])
# print(s1[ : ])

# print(s1[60])
# print(s1[-3])
"""
print(s1[0])

print(s1[30 : 3])
print("The end")
print(s1[-25 : -5])
print(s1[-30 : 50])
print(s1[30 : -3])

print(s1[4 : -3])


print(s1[3 : 55 : 3])
print(s1[55 : 3 : -1])
print(s1[ : : -1])
print(s1[ : : -3])
print(String[1:5:2])
"""

# methods vs. functions
# function_name(oprand)
# oprand.method_name(arguments)

# Case related methods:
#slice
s1='ROYAL TECHNOSOFT limited'
# s1[]
# ROYAL
# TECHNOSOFT
# limited
# ROYAL limited







# s2=s1[:5]
# s3=s1[-7:]
# print(f"{s2} {s3}")
# Output:




# *****New task to perform********

s1='strings are IMMUTABLE so, methods of strings cannot change the original string. Instead'
#
# Output:- 1) print IMMUTABLE using slicing s1[12:22
#          2) print Insted using slicing
#          3) skip alternate character and print the new string

# print(s1[12:22])
# print(s1[-7:])
# print(s1[::2])


# 'Royal Technosoft Limited'
# 'I am learning python'

# print(s2)

# indian
# royal
# technosoft
'Students of this batch are going to rock the INDIAN software industry!'



# output: s1 bdha first letters capitilize
#         indian in lower case
#         all the s1 string should in upper case
#         all the s1 string should be in lower case
#         software industry  in uppercase
s1='Students .of this batch are going to rock the INDIAN software industry!'
# indian
# class--capitize---()
# s1[5]='abc'
print(s1)
# print(s1.capitalize())
# print(len(s1))
# # print(s2)	# strings are IMM so, methods of strings cannot change the original string. Instead, they will return a new string.
# print( s1.capitalize())
# print( s1[5].capitalize())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())

# len(s1)
# print()
# input()
# type()