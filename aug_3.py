# s1 = "Abc"
# # s2 = "5⁴"
# # s3 = "②⓪②②"
# # s4 = "½"
# # s5 = "二千二十二"
#
# # methods starting from is: All these methods return True or False
#
# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())
#
s1 = "a"
s2 = "AlakhPandya"
s3 = "9876543210"
s4 = "AlakhPandya9876543210"
# print(s2.isnumeric())
# print(s2.isalpha())
# print(s4.isalnum())
# print(s3.isdecimal())
# print(s3.isdigit())
# print(s1.isascii())
# #
# #
# # s5 = "₹5000"

# s6 = "ab@cb"
# print(s6.isidentifier())
# # #
# # #
s7 = "   \t  "
print(s7.isspace())
print(s7.isprintable())
# #
# # """
# # The difference between isnumeric, isdigit & isdecimal
# # """
# # """
# # print(s4.isdecimal())   # only recognizes digits from 0 to 9 and nothing else.
# # print(s4.isdigit())     # also recognizes subscript, superscript, circled numbers
# # print(s4.isnumeric())   # also recognizes roman numerals, vulgar fractions, digits from other languages
# #
# # print(s5.isnumeric())
# # """
# #
# #
# #
# #
# #
# # # list(strings)
# # # [] datatype list
s6 = ('students of this batch aregoing to rock\n the indian software '
      'industry!\nBecause they are very sincere.\nThey also do their homework on time.        ')
# print(s6)
# s7=s6.split("\n")
# s7[0]="2222"#return list
# print(s7)
# # # print(s6.split("z"))
# print(s6.split(" ", 25))
# # #
# # # print(s6.rsplit(" ",3))
# # # print(s6.split(" "))
# #
# # # # print(s6)
# print(s6.split("\n"))
# print(s6.splitlines())
# #
# s7 = "Harsh is a good boy.
# But, this sentence has an error."
# a="1"

# b="123"
# s8 = ['a','b']
# s9 = "".join(s8)
# print(s9)
# #
# # # print(" ".join(s8))
# #
# # s6 = '            students         of this batch are going batch are to rock the indian software industry!         '
# print(s6.partition("batch"))
# # # print(s6.partition("are are")) #return tuple
# # # print(s6.rpartition("batch"))
# #
s6="  a b c "
print(s6.strip(" "))
s8 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$h$$$$$$$$$Happy$$Birthday!$$$$$$$$$$$$$$$$$"

print(s8.replace("$", " "))


# """
#
# s8 = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Happy$$Birthday!$$$$$$$$$$$$$$$$$"
print(s8.lstrip("$"))
print(s8.rstrip("$"))
# print(s8.strip("$"))
# """
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
