#
# # class Example:
# #     def __init__(self,name):
# #         self.name=name
# #         print("Instance Created")
# #     # Defining __call__ method
# #     def __call__(self):
# #         print("Instance is called via special method")
# #         return 1
# #     def display(self):
# #         print("in display method")
# # # Instance created
# # e = Example("royal")
# # # __call__ method will be calledpr
# # # e()
# # e.display()
# # print(e())
# #
# #
# # class Product:
# #     # def __init__(self):
# #     #     print("Instance Created")
# #     # Defining __call__ method
# #     def __call__(self, a, b):
# #         print(a * b)
# #     def multi(self,a,b):
# #         print(a*b)
# # # Instance created
# # ans = Product()
# # # __call__ method will be called
# # ans(10, 20)
# # demo = Product()
# # ans.multi(10,20)
#
# #
# # # The __str__() Function
# # # The __str__() function controls what should be returned when the class object is represented as a string.
# #
# # # The string representation of an object WITHOUT the __str__() function:
# # #
# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #
# # p1 = Person("John", 36)
# #
# # print(p1)
# #
# # # The string representation of an object WITH the __str__() function:
# #
# # class Person:
#   # def __init__(self, name, age):
#   #   self.name = name
#   #   self.age = age
#
# #   def __str__(self):
# #     return f"aapne object call krvaya hai, methoda call kro"
# #   def display(age):
# #     return "123"
# #
# # p1 = Person()
# #
# # print(p1)
# # a=p1.display()
# # print(a)
#
# # class A:
# #
# #   def __dev__(self):
#
#
#
# # Inheritance
# #
# # A-->B
# # #
# # A--->B-->C
# # #
# # a,b-->c
# # #
# # A--->b,c-->d
#
# # Python Inheritance
# # Inheritance allows us to define a class that inherits all the methods and properties from another class.
# #
# # Parent class is the class being inherited from, also called base class.
# #
# # Child class is the class that inherits from another class, also called derived class.
#
# # 1)Single Inheritance:
#
# # class ParentClass:
# #     def __init__(self,name):
# #         self.name=name
# #
# #     def display(self,name):
# #         name="hello"+name
# #         return name
# #
# # class ChildClass(ParentClass):
# #     # name="POI"
# #     def display(self,n):
# #         self.n =n
# #         name=self.name
# #         return name,self.n
# #
# # a=ChildClass("XYZ")
# # # b=a.display("PKM")
# # name,n=a.display("PKM")
# # print(name,n)
#
# # 2)Multilevel Inhertiance:

# class SuperClass:
#     # Super class code here
#
# class DerivedClass1(SuperClass):
#     # Derived class 1 code here
#     super()
#
# class DerivedClass2(DerivedClass1):
#     super()
#
# x=DerivedClass2()
#     Derived class 2 code here
# clas example:
# class ParentClass:
#     # pass
#     def display(self):
#         return "ParentClass.display()"
# #
# # # 3) Multiple INheritance:
# class MostParentClass:
#     # pass
#     # def display(self):
#     #     return "MostParentClass.display()"
#
#
# class ChildSubClass(MostParentClass,ParentClass):
#     # def display(self):
#     #     return "ChildSubClass.display()"
#     pass
# #
# #
# obj = ChildSubClass()
# print(obj.display())
#
#
# # Create a class named Person, with firstname and lastname properties, and a printname method:
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def __call__(self):
#         print("call")
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# # Use the Person class to create an object, and then execute the printname method:
#
# x = Person("John", "Doe")
# x.printname()
# x()
#
# # Create a class named Student, which will inherit the properties and methods from the Person class:
#
# # class Student(Person):
# #     pass
# #
# # a=Student("abc","ayz")
# # a()
#
# # x = Student("Mike", "Olsen")
# # x.printname()
#
# # class Person:
# #   def __init__(self, fname, lname):
# #     self.firstname = fname
# #     self.lastname = lname
# #   def printname(self):
# #     print(self.firstname, self.lastname)
# #
# # class Student(Person):
# #     def __init__(self,firstname,lastname):
#         super().__init__(firstname,lastname)
#         self.firstname="PKM"
#         self.lastname="PKM"
#
#     def print2(self):
#         print(self.firstname, self.lastname)
#       # pass
# # Use the Student class to create an object, and then execute the printname method:
# x = Student("Mike", "Olsen")
# x.printname()
# class Polygon:
#     # Initializing the number of sides
#     def __init__(self, no_of_sides):
#         print("in polgon __init__")
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#     def inputSides(self):
#
#         self.sides = [1,2,3]
#     # method to display the length of each side of the polygon
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
# class Triangle(Polygon):
#     # Initializing the number of sides of the triangle to 3 by
#     # calling the __init__ method of the Polygon class
#     # def __display__
#     def __init__(self):
#         print("in triangle __init__")
#         Polygon.__init__(self,3)
#     def findArea(self):
#         a, b, c = self.sides
#         super().dispSides()
#         # calculate the semi-perimeter
#         # s = (a + b + c) / 2
#         # Using Heron's formula to calculate the area of the triangle
#         # area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         # print('The area of the triangle is %0.2f' %area)
# # Creating an instance of the Triangle class
# t = Triangle()
# # Prompting the user to enter the sides of the triangle
# t.inputSides()
# # # Displaying the sides of the triangle
# t.dispSides()
# # Calculating and printing the area of the triangle
# t.findArea()



# Method overriding
# However, what if the same method is present in both the superclass and subclass?
#
# In this case, the method in the subclass overrides the method in the superclass. This concept is known as method overriding in Python.

class Animal:
    # attributes and method of the parent class
    name = ""

    def eat(self):
        print(f"I can eat name")

# inherit from Animal
# class Dog(Animal):
#
#     # override eat() method
#     # super.eat()
#     # super.eat()
#     def eat(self,a):
#         print(f"I can eat {a}")
#     def eat(self):
#         # super().eat()
#         print("I like to eat bones")
#
# # create an object of the subclass
# labrador = Animal()
# # # call the eat() method on the labrador object
# labrador.eat()



# how to overcome
#
#
# class Animal:
#     name = ""
#
#     def eat(self):
#         print("I can eat")
#
#
# # inherit from Animal
# class Dog(Animal):
#
#     # override eat() method
#     def eat(self):
#         # call the eat() method of the superclass using super()
#         super().eat()
#
#         print("I like to eat bones")
#
#
# # create an object of the subclass
# labrador = Dog()
# labrador.eat()


# create a class  name as Rectangle that takes length and width of the rectangle
# calculate area = that will calcuate the area of the rectangle
# calculate area  the square



# class Shape:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
# class Rectangle(Shape):
#     def calculate_area_rec(self):
#         return self.length * self.width
#
#     def calculate_square(self):
#         return self.length ** 2
#
#     def calculate_triangle(self):
#         return (self.length * self.width ) * 1/2
#
# area = Rectangle(1,1)
# print(area.calculate_area_rec())