# 1) string -- immutable,ordered

# s1='       royal limited pvt       ahmedabad  a  '

# indexing:
# print(s1[-2])

# slicing:

# print(s1[1::-1])

# print(s1.split('a'))
# print("456".join("123"))
# print(s1.strip())
# print(s1.replace(" ","*"))


# 2) list --- mutable,ordered

li=[1,2,3,4,4,5]
# print(li[1::2])

# li.append('tithi')
# li.insert(3,'tithi')
# li.extend(['tithi']*4)
# print(li)

# 3) tuple -- immutable, ordered

# print(tuple(li))
# tu=(1,2,4)
# li=list(tu)
# li.append(5)
# print(tuple(li))

# 4) functions:

# 1) signle
# 2)multiple
# 3)default
# 4) keyword
# 5)*args
# 6)**kwargs

# def first_func(first,second=1,*numbers,third=3):
#     print(first, second, numbers)
#     for i in numbers:
#         print(i)
#
# first_func(1,2,5,6,7,8,9,0,848,'huvhgf')

# keyword arbitary arguments

def first_func(first,second=1,*numbers,**data):
    print(first, second, numbers,data)
    print(data['key1'])
    print(f"{first}-{second},{numbers[0]}{numbers[1]}")
first_func(1,2,5,6,7,8,9,0,848,key1='huvhgf',key2="hgchdgchd")

