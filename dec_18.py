# Single inheritance in python
# Base class
# class Parent_class:
#     # Constructor
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def Employee_Details(self):
#         return self.id, self.name
#     def Employee_check(self):
#         if self.id > 500000:
#             return " Valid Employee "
#         else:
#             return " Invalid Employee "
# class Child_class(Parent_class):
#     def End(self):
#         print(" END OF PROGRAM ")
# Employee1 = Parent_class("Employee1", 600445)
# print(Employee1.Employee_Details(), Employee1.Employee_check())
# Employee2 = Child_class("Employee2", 198754)
# print(Employee2.Employee_Details(), Employee2.Employee_check())
# Employee2.End()


# Multiple Inhertiance
# class SuperClass1:
#     # features of SuperClass1
#
# class SuperClass2:
#     # features of SuperClass2
#
# class MultiDerived(SuperClass1, SuperClass2):
#     # features of SuperClass1 + SuperClass2 + MultiDerived class


# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth.")
#
# class WingedAnimal:
#     def mammal_info(self):
#         print("Winged animals can flap.")
#
# class Bat(Mammal, WingedAnimal):
#     pass
#
# # create an object of Bat class
# b1 = Bat()
#
# b1.mammal_info()
# b1.winged_animal_info()

# MRO

# class SuperClass1:
#     def info(self):
#         print("Super Class 1 method called")
#
# class SuperClass2:
#     def info(self):
#         super().info()
#
# class Derived(SuperClass2, SuperClass1):
#     pass
#
# d1 = Derived()
# d1.info()


# class A:
#     pass
# class B:
#     pass
# class C(A, B):
#     pass
# class D(B, A):
#     pass
# class E(C,D):
#     pass


# __mro__, mro()
# class A:
#     def myname(self):
#         print(" I am a class A")
# class B(A):
#     def myname(self):
#         print(" I am a class B")
# class C(B):
#     def myname(self):
#         print("I am a class C")
#     # classes ordering
# class D(C):
#     pass
# # it prints the lookup order
# # print(D.__mro__)
# print(C.mro())


# 111111
# class A:
#     def myyname(self):
#         print("I am a class A")
# class B:
#     def myyname(self):
#         print("I am a class B")
# class C(B,A):
#     def myyname(self):
#         print("I am a class C")
# c = C()
# print(c.myname())


# 2222
class A:
      def __init__(self,name):
          self.name=name #"PKM"
      def __call__(self):
          return self.name
      def method(self):
        print(f"A.method() called with {self.name}")
class B:
    def __init__(self, name):
        super().__init__("XYZ")
        self.name = name
    def method(self):
        print("B.method() called")
class C(B,A):
  pass
class D(C):
  pass

d = D("PKM")
print(d())
d.method()


# Example: + Operator Overloading in Python
# To overload the + operator, we will need to implement __add__() function in the class.
#
# With great power comes great responsibility. We can do whatever we like inside
# this function. But it is more sensible to return the Point object of the coordinate sum.

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)
#
# p1 = Point(1, 2)
# p2 = Point(2, 3)
#
# print(p1+p2)
#
# # Output: (3,5)

#
# Operator	Expression	Internally
# Addition	p1 + p2 	p1.__add__(p2)
# Subtraction	p1 - p2 	p1.__sub__(p2)
# Multiplication	p1 * p2 	p1.__mul__(p2)
# Power	p1 ** p2	 p1.__pow__(p2)
# Division	p1 / p2 	p1.__truediv__(p2)
# Floor Division	p1 // p2	 p1.__floordiv__(p2)
# Remainder (modulo)	p1 % p2	  p1.__mod__(p2)
# Bitwise Left Shift	p1 << p2	 p1.__lshift__(p2)
# Bitwise Right Shift	p1 >> p2	 p1.__rshift__(p2)
# Bitwise AND	p1 & p2	  p1.__and__(p2)
# Bitwise OR	p1 | p2  	p1.__or__(p2)
# Bitwise XOR	p1 ^ p2  	p1.__xor__(p2)
# Bitwise NOT	~p1	  p1.__invert__()


# Method overloading
# class Human:
#     def sayHello(self, name):
#         if name is not None:
#             print('Hello ' + name)
#         # else:
#         #    print ('Hello ')
#
#     def sayHello(self, name):
#         print('Hello ')
#         # return 1
#
# obj = Human()
# # print(obj.sayHello())
# print(obj.sayHello('Rambo'))


# class Base:
#   def method(self, param2):
#      print("cheeses",param2)
#
# class NotBase(Base):
#   def method(self):
#       super().method(param2="abc")
#       print("dill")
#
# obj = NotBase()
# obj.method()

# x=y=5,10
# res= x == y
# print(res)



# class University:
#     def __init__(self):
#         self.name = 'Yele University'
#         print("You are in University Class Constructor")
#     def show(self):
#         print('You are in University class disp method')
# class College(University):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Yale School of Medicine'
#         print('You are in college Class Constructor')
#     def show(self):
#         print('College class instance method:', self.name)
# college = College()
# college.show()
# college.disp()







# class Taxi:
#     # __model ='abc'
#     def __init__(self, model, capacity, variant):
#         self.__model = model
#         self.__capacity = capacity
#         self.__variant = variant
#     def getModel(self):
#         return self.__model
#     def getCapacity(self):
#         return self.__capacity
#     def setCapacity(self, capacity):
#         self.__capacity = capacity
#     def getVariant(self):
#         return self.__variant
#     def setVariant(self, variant):
#         self.__variant = variant
# class Vehicle(Taxi):
#
#     def __init__(self, model, capacity, variant, color):
#         super().__init__(model, capacity, variant)
#         self.__color = color
#     def vehicleInfo(self):
#         return (self.getModel() + " " + self.getVariant()
#                 +" in " + self.__color + self.__model+ " with " + self.getCapacity() + " seats")
#
# # v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
# # print(v1.vehicleInfo())
# # print(v1.getModel())
# v2 = Vehicle("Fortuner", "7", "MT2755", "White")
# # print(v2._getModel())
# print(v2.vehicleInfo())




# class Vehicle:
#
#     name="BMW"
#     def __call__(self, *args, **kwargs):
#         name="FERRARI"
#         return name
#     def __str__(self):
#         name="AUDI"
#         return name
#     def __init__(self):
#         self.name="MERCEDES"
#     def display(self):
#         self.name="HONDA"
#         return self.name
#
# v=Vehicle()
# print(v.name)
# print(v())


# num=4
# i=1
#
# if num%i == 0:
#     print(num%i)
#     i+=1
#     print(i)
#     if i == 1:
#         print("Prime")

# print([1,2,3]+[1,2,3])
# [1,1]
# [1,2,1]
# [1,,3,1]
# [1,2,4,4,1]
# [1,3,6,8,5,1]

# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# pascal_triangle(6)


# Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is
# derived from a single parent class. In other words, we can say one parent class and multiple child classes

# class Vehicle:
#     def info(self):
#         print("This is Vehicle")
#
# class Car(Vehicle):
#     def car_info(self, name):
#         print("Car name is:", name)
#
# class Truck(Vehicle):
#     def info(self, name="CITY"):
#         super().info()
#         print("Truck name is:", name)
# # obj1 = Car()
# # obj1.info()
# # obj1.car_info('BMW')
#
# obj2 = Truck()
# obj2.info()
# obj2.info('Ford')




# Hybrid Inheritance
# When inheritance is consists of multiple types or
# a combination of different inheritance is called hybrid inheritance.
#
# class Vehicle:
#     def __init__(self):
#         print("inside init")
#         self.v="NOOO"
#     def vehicle_info(self):
#         print("Inside Vehicle class",self.v)
# class Car(Vehicle):
#     def vehicle_info(self):
#         self.v="YESS"
#         print("Inside Car class",self.v)
# class Truck(Vehicle):
#     def car_info(self):
#         print("Inside Truck class",self.v)
# # Sports Car can inherits properties of Vehicle and Car
# class SportsCar(Car, Vehicle):
#     def car_infoo(self):
#         print("Inside SportsCar class")
# # create object
# s_car = SportsCar()
# # s_car.vehicle_info()
# s_car.vehicle_info()
# s_car.sports_car_info()





# class method
# class methods demo

# class Student:
#     # class variable
#     school_name = 'ABC School'
#
#     # constructor
#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age
#
#     # instance method
#     @classmethod
#     def show(cls,name):
#         # access instance variables and class variables
#         print('Student:',name)
#
#     # instance method
#     def change_age(self, new_age):
#         # modify instance variable
#         self.age = new_age
#
#     # class method
#     @classmethod
#     def modify_school_name(cls,new_name):
#         # modify class variable
#         cls.school_name = new_name
#         print(cls.school_name)
#         cls.show(new_name)
#
# s1 = Student("Harry", 12)

# call instance methods
# s1.show()
# s1.change_age(14)

# call class method
# Student.modify_school_name('XYZ School')
# call instance methods
# s1.show()



# static method:
#
# Static methods are a special case of methods. Sometimes, you’ll write code that belongs to a class,
#     but that doesn’t use the object itself at all. It is a utility method and doesn’t
# need an object (self parameter) to complete its operation. So we declare it as a static method.
# Also, we can call it from another method of a class.

#
# class Employee(object):
#
#     def __init__(self, name, salary, project_name):
#         self.name = name
#         self.salary = salary
#         self.project_name = project_name
#
#     # @staticmethod
#     def gather_requirement(project_name):
#         if project_name == 'ABC Project':
#             requirement = ['task_1', 'task_2', 'task_3']
#         else:
#             requirement = ['task_1']
#         return requirement
# #
#     # instance method
#     def work(self):
#         # call static method from instance method
#         requirement = self.gather_requirement(self.project_name)
#         for task in requirement:
#             print('Completed', task)
#
# emp = Employee('Kelly', 12000, 'ABC Project')
# emp.work()
# print(Employee.gather_requirement("ABC Project"))


#
# 3 type methods


# Difference #1: Primary Use
#
# Class method Used to access or modify the class state. It can modify the class state by changing the
# value of a class variable that would apply across all the class objects.
#
# The instance method acts on an object’s attributes. It can modify the object state by
# changing the value of instance variables.
# Static methods have limited use because they don’t have access to the attributes of an object
#
# (instance variables) and class attributes (class variables). However,
# they can be helpful in utility such as conversion form one type to another.


# c
# Difference #2: Method Defination
#
# All three methods are defined inside a class, and it is pretty similar to defining a regular function.
#
# Any method we create in a class will automatically be created as an instance method.
# We must explicitly tell Python that it is a class method or static method.
#
# Use the @classmethod decorator or the classmethod() function to define the class method
# Use the @staticmethod decorator or the staticmethod() function to define a static method.

# class Student:
#     # class variables
#     school_name = 'ABC School'
#     # constructor
#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age
#     # instance variables
#     def show(self):
#         print(self.name, self.age, Student.school_name)
#     @classmethod
#     def change_School(cls, name):
#         print(self.name)
#         cls.school_name = name
#         print(cls.school_name)
#         cls.show()
#     @staticmethod
#     def find_notes(subject_name):
#         print(school_name)
#         return ['chapter 1', 'chapter 2', 'chapter 3']
#
# # print(Student.find_notes('python'))
# s1=Student('pkm','50')
# # s1.show()
# s1.change_School('Royal')
# Student.change_School('Rooooyal')

# Student.show(self=self)
# Difference #3: Method Call
# Class methods and static methods can be called using ClassName or by using a class object.
# The Instance method can be called only using the object of the class.

# Difference #4: Attribute Access
# Both class and object have attributes. Class attributes include class variables,
# and object attributes include instance variables.
#
# The instance method can access both class level and object attributes. Therefore, It can modify the object state.
# Class methods can only access class level attributes. Therefore, It can modify the class state.
# A static method doesn’t have access to the class attribute and instance attributes.
# Therefore, it cannot modify the class or object state.

# class Student:
#     # class variables
#     school_name = 'ABC School'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # instance method
#     def show(self):
#         # access instance variables
#         print('Student:', self.name, self.age)
#         # access class variables
#         print('School:', self.school_name)
#
#     @classmethod
#     def change_School(cls, name):
#         # access class variable
#         print('Previous School name:', cls.school_name)
#         cls.school_name = name
#         print('School name changed to', Student.school_name)
#
#     @staticmethod
#     def find_notes(subject_name):
#         # can't access instance or class attributes
#         return ['chapter 1', 'chapter 2', 'chapter 3']
#
# # create object
# jessa = Student('Jessa', 12)
# # call instance method
# jessa.show()
#
# # call class method
# Student.change_School('XYZ School')


# Difference #5: Class Bound and Instance Bound
# An instance method is bound to the object, so we can access them using the object of the class.
# Class methods and static methods are bound to the class. So we should access them using the class name.
#
#
# class Student:
#     def __init__(self, roll_no): self.roll_no = roll_no
#
#     # instance method
#     def show(self):
#         print('In Instance method')
#
#     @classmethod
#     def change_school(cls, name):
#         print('In class method')
#
#     @staticmethod
#     def find_notes(subject_name):
#         print('In Static method')
#
#
# # create two objects
# jessa = Student(12)
#
# # instance method bound to object
# print(jessa.show)
#
# # class method bound to class
# print(jessa.change_school)
#
# # static method bound to class
# print(jessa.find_notes)
