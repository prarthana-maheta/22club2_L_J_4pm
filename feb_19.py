   
# # # # Python program showing 
# # # # abstract base class work 
# # # from abc import ABC, abstractmethod 
  
  
# # # class Polygon(ABC): 
  
# # #     @abstractmethod
# # #     def noofsides(self): 
# # #         pass
  
  
# # # class Triangle(Polygon): 
  
# # #     # overriding abstract method 
# # #     def noofsides(self,a): 
# # #         print("I have 3 sides",a) 
  
  
# # # # class Pentagon(Polygon): 
  
# # # #     # overriding abstract method 
# # # #     def noofsides(self): 
# # # #         print("I have 5 sides") 
  
  
# # # # class Hexagon(Polygon): 
  
# # # #     # overriding abstract method 
# # # #     def noofsides(self): 
# # # #         print("I have 6 sides") 
  
  
# # # # class Quadrilateral(Polygon): 
  
# # # #     # overriding abstract method 
# # # #     def noofsides(self): 
# # # #         print("I have 4 sides") 
  
  
# # # # Driver code 
# # # R = Triangle() 
# # # R.noofsides(1) 
  
# # # # K = Quadrilateral() 
# # # # K.noofsides() 
  
# # # # R = Pentagon() 
# # # # R.noofsides() 
  
# # # # K = Hexagon() 
# # # # K.noofsides() 

# # # import the time module
# # # import time

# # # # get the current time in seconds since the epoch
# # # seconds = time.time()

# # # print("Seconds since epoch =", seconds)	

# # # Output: Seconds since epoch = 1672214933.6804628

# # # import time

# # # # seconds passed since epoch
# # # # seconds = time.time()

# # # # # convert the time in seconds since the epoch to a readable format
# # # # local_time = time.ctime(seconds)

# # # # print("Local time:", local_time)

# # # print("1")
# # # time.sleep(10)
# # # print("2")

# # # from datetime import datetime

# # # # get the current date and time
# # # now = datetime.now()

# # # print(now)

# # # date_string = "25 December, 2022 14:57:56"
# # # print("date_string =", date_string)

# # # # use strptime() to create date object
# # # date_object = datetime.strptime(date_string, "%d %B, %Y %H:%M:%S")

# # # f_date_object =datetime.strftime(date_object, "%Y**%m**%d %H:%M:%S ")
# # # print("date_object =", type(date_object))
# # # print("date_object =", type(f_date_object))
# # # print(now-date_object)

# # from datetime import datetime
# # import pytz

# # local = datetime.now()
# # print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


# # tz_NY = pytz.timezone('America/New_York') 
# # datetime_NY = datetime.now(tz_NY)
# # print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

# # tz_London = pytz.timezone('Europe/London')
# # datetime_London = datetime.now(tz_London)
# # print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

# # from datetime import datetime

# # a = datetime(2022, 12, 28, 23, 55, 59, 342380)

# # print("Year =", a.year)
# # print("Month =", a.month)
# # print("Hour =", a.hour)
# # print("Minute =", a.minute)
# # print("Timestamp =", a.timestamp())
# # print(a.time())

# from datetime import datetime, date

# # using date()
# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)

# t3 = t1 - t2

# print("t3 =", t3)

# # using datetime()
# t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5
# print("t6 =", t6)

# print("Type of t3 =", type(t3)) 
# print("Type of t6 =", type(t6))  

from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

t3 = t1 - t2

print("t3 =", t3)