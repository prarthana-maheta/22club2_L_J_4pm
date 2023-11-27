# brand="brand"
# thisdict = {"&":"Ford",
#             "model":{None:"bnv" },
#             "123": 1964,
#             "&":"tata"
#             }
# print(thisdict)
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
# my=[1,2,3]
# print(thisdict["brand"])
# functions:
# print(type(thisdict))
# print(len(thisdict))
# print(list(thisdict))
# print(dict(my))

# Accessing dict:
ths=[1,2,3]
this1=['Ford','maruti','1964']

thisdict = {
    "brand": "Ford",
    1: "Mustang",
    "year": 1964
}

# print(thisdict["year"])
# #
# print(thisdict.get("yea",thisdict.get('brand')))
#
# print(thisdict.keys())
# # #
# print(thisdict.values())

# x=thisdict.items()
# print(x)

# for i,j in thisdict.items():
#     # print(i,j)
#     print(thisdict.get(i,"no"))


# add data to dict:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1969,
    # "year": "blue",
}

 #before the change
car['price'] = '92 Lac'
car['price'] = '94 Lac'
# car["year"] = None
# print(car) # after the change

# change values of dict:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018


# update dict:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.update({"year":1234},yea=1234,name='hi')
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

# remove items:
#
# # 1) pop()
# thisdict = {
#   "0": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)
#
# # 2)popitem()
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# 3)del
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict['band']
# print(thisdict)

# 4)clear()
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)
# thisdict['a']=1
# print(thisdict)

# 5)copy()
# c=[2,3]
# a=[1,2]
# b=c.copy()
# del a
# print(b)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# del thisdict
# # print(thisdict)
# print(mydict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

# 6) setdefault()
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.setdefault("color", "white"))
# print(car)
# print(car.setdefault("color", "black"))
# car.update({"color": "red"})
# car.update({"color": "pink"})
# print(car)
# print(x)

# 7) fromkeys()
# x = ('key1', 'key2', 'key3')
# y=(1,2)
# thisdict = dict.fromkeys(x,y)
# thisdict=dict(zip(x,y))
# print(thisdict)

# nested dict:
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
# myfamily = {
#    "child1":None,
#   "child2" : child2,
#   "child3" : child3
# }
# #
# print(myfamily)
#
# print(myfamily["child2"]["name"])
# print(myfamily.get("child2").get("name"))

# child1 = {
#     "name": "Emil",
#     "year": 2004
# }
# child2 = {
#     "name": "Tobias",
#     "year": 2007
# }
# child3 = {
#     "name": "Linus",
#     "year": 2011
# }
# myfamily = {
#     "child1": "abc",
#     "child2": "abc",
#     "child3": "abc"
# }

# for key,value in myfamily.items():
#     print(key)
#     # myfamily[key]="abc"
#     # print(myfamily)
#     # print(value)
#
#     if "child1" == key or "child2" in key :
#         print("found")
#
# if "child1" in myfamily.keys():
#     print("yes")

# l1=['a', 'b', 'c', 'd', 'e', 'f']
# l2=[1, 2, 3, 4, 5]
# print(dict(zip(l1,l2)))



# create a dict with 5 key value pairs, where key should be roll num, values should be student:
#
# 1: print  the student name when user enter the roll numbers
# 2: add more students to the dict
# 3: take roll number from user, check is roll number exists in the dict than update the name of the student

