# 5. Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
#
# 6. Write a python program to remove duplicate, empty, and None values
example=["abc","",None,"abc",None]
second=[]
for i in example:

    if i not in second:
        second.append(i)



print(second)