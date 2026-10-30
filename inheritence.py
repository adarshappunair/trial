# class new:
#    # a=12 #instance
#     def __init__(self,name,tech): # constructive method - this is used to create objects( creating a function in a class is called method)
#         self.name=name
#         self.tech=tech
# class team:

#     def __init__(self,team,league,best_player):
#         self.team=team
#         self.league=league
#         self.best_player=best_player


        

# obj=new('adarsh','python') #instantination
# print(obj.name)
# obj1=team('barcelona',"laliga","yamal")
# print(obj1.team,"-",obj1.league,"-",obj1.best_player)
# class car:
#     b="one"
#     def __init__(self,c,d,e):
#         self.c=c
#         self.d=d
#         self.e=e
#     def start():
#         print("hi")
#     def stop():
#         print("bye")
# f=car(1,2,3)
# g=car(9,0,7)
# print(car.b)
# print(f.c)
# print(g.e)
# car.start()
# car.stop()

# class animal:
#     def __init__(self,name ,age1):
#         self.name=name
#         self.age1=age1
#     def eat(self):
#         print(f"{self.name} is eating")
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#     def age(self):
#         print(self.name,"is",self.age1)
# class dog(animal):
#     def speak(self):
#         print("woof")
# class cat(animal):
#     def speak(self):
#         print(self.name,"meow")
# class mouse(animal):
#     def speak(self):
#         print("....")
# dog1=dog("jimmy",2)
# print(dog1.name)
# dog1.age()
# cat1=cat("mit",3)
# cat1.speak()
# cat1.sleep()
# class college:
#         def __init__(self,name,locality):
#             self.name=name
#             self.locality=locality
#         def college_info(self):
#             print(self.name,"is in this",self.locality)
# class department(college):
#         def __init__(self,name,locality, dname, hod):
#             super().__init__(name,locality)
#             self.dname=dname
#             self.hod=hod
#         def department_info(self):
#             print("college name :",self.name,"|Department name :",self.dname,"| HOD name :",self.hod)
# class student(college):
#         def __init__(self,name,locality, sname, roll):
#                 super().__init__(name,locality)
#                 self.sname=sname
#                 self.roll=roll
#         def student_info(self):
#             print("college name :",self.name,"|Student name :",self.sname,"| roll number :",self.roll)



# college1=department("srm","chennai","mech","rag")
# college1.department_info()
# student1=student("srm","chennai","Adarsh","001")
# student1.student_info()


# class student():
        
#         def __init__(self, sname, roll):
#                 self.sname=sname
#                 self.roll=roll
#         def __str__(self):
#             return f"{self.sname} roll number is,{self.roll}"
#         def __del__(self):
#                print("Object is deleted")

# student1=student("Adarsh","001")
# print(student1)
# class hod:
#         def __init__(self,hname,dep):
#             self.hname=hname
#             self.dep=dep
#         def hod_info(self):
#                return f"{self.hname} department is {self.dep}"
               
#         def __str__(self):
#               return f"{self.hname} department is {self.dep}"



# class teacher():
#         def __init__(self,tname, speciality,):
#                 # super().__init__(hname,dep)
#                 self.tname=tname
#                 self.speciality=speciality
#         def teacher_info(self):
#             #   super().hod_info()
#               return f"{self.tname} speciality  is {self.speciality}" 
#         def __str__(self):
                    
#                     return f"{self.tname} speciality  is {self.speciality}"
# class student(teacher,hod):
#         def __init__(self,sname, roll,tname, speciality,hname,dep):
#                 super().__init__(tname, speciality)
#                 hod.__init__(self,hname,dep)
#                 self.sname=sname
#                 self.roll=roll
#         def student_info(self):
#             super().teacher_info()
#             hod.hod_info(self)
#             return f"{self.sname} roll  is {self.roll}"
#         def __str__(self):
           
#             return f"{self.sname} roll  is {self.roll}"

# teacher=student("hop","001","jack","science","job","mech")
# print(teacher.student_info())



# # Create a class Student with attributes name and age. Create an object and print the details.
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


# student=student("adarsh","29")
# print(student.name,student.age)




# # Create a class Book with attributes title and author. Write a method to display the book details.
# class book:
#     def __init__(self,title,arthur):
#         self.title=title
#         self.arthur=arthur
#     def __str__(self):
#         return f"{self.title} is written by {self.arthur}"

# book=book("harry","jkr")
# print(book)



# # Create a class Rectangle with attributes length and width. Write a method to calculate and display the area.
# class rectangle:
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w
#     def area(self):
#         c=self.l*self.w

#         return f"Area of the said rectangle is {c}"

# rec=rectangle(2,4)
# print(rec.area())
    
        

# Create a class Circle with attribute radius. Write a method to calculate the area of the circle.
# class circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         a=3.14*self.r**2
#         return f"Area of the circle is {a}"

# circle=circle(4)
# print(circle.area())

# Create a class Car with attributes brand and price. Create a method to display the car details.
# class car:
#     def __init__(self, brand ,price):
#         self.brand=brand
#         self.price=price
#     def __str__(self):
#         return f"The brand for this car is {self.brand} and price is {self.price}"

# car=car("Kia",120000)
# print(car)



# Create a class Employee with attributes name and salary. Write a method to display employee details.
# class employee:
#     def __init__(self, name ,salary):
#         self.name=name
#         self.salary=salary
#     def __str__(self):
#         return f"The brand for this car is {self.name} and price is {self.salary}"

# car=employee("Kia",120000)
# print(employee)

# Create a class BankAccount with attribute balance. Write a method to deposit money and display the updated balance.
# class bankaccount:
    
#     def __init__(self,deposit):
#         self.bank_balance=2
#         self.deposit=deposit
#     def add(self):
#         new_balance=self.deposit+self.bank_balance
#         return f"your new balance is {new_balance}"

# bank=bankaccount(123333)
# print(bank.add())


# Create a class Temperature with attribute celsius. Write a method to convert it to Fahrenheit.
# class temp:
#     def __init__(self,c):
#         self.c=c
#     def convert(self):
#         f=self.c+32
#         return f" the conversion to Fahreneit is {f} "

# temp=temp(23)
# print(temp.convert())


        

# Create a class Product with attributes product_name and price. Write a method to display product details.
# class product:
#     def __init__(self,product_name,price):
#         self.price=price
#         self.product_name=product_name
#     def __str__(self):
#         return f"The {self.product_name} price is {self.price}"
# prod=product("Watch",23455)
# print(prod)



# Create a class Triangle with attributes base and height. Write a method to calculate the area of the triangle.
# class triangle:
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h
#     def area(self):
#         c=self.b*self.h*0.5

#         return f"Area of the said triangle is {c}"

# tri=triangle(2,4)
# print(tri.area())

# Part A: Multiple Inheritance (Using Interfaces)
# 1. Smart Phone
# Create two interfaces:
# Camera
# MusicPlayer
# Create a class SmartPhone that implements both interfaces.
# Methods:
# takePhoto()
# playMusic()

# class camera:
#     def __init__(self,pixel):
#         self.pixel=pixel
#     def camera_info(self):
#         return f"The camera pixel is {self.pixel}"
# class musicplayer:
#     def __init__(self,music_app):
#         self.music_app=music_app
#     def player_info(self):
#         return f"The music app name is {self.music_app}"
# class smartphone(camera,musicplayer):
#     def __init__(self,phone_model,pixel,music_app):
#         super().__init__(pixel)
#         musicplayer.__init__(self,music_app)
#         self.phone_model=phone_model
#     def phone_info(self):
#         super().camera_info()
#         musicplayer.player_info(self)
#         return f"The smart phone model is {self.phone_model} , the camera is {self.pixel} and music player is {self.music_app}"
#     def takePhoto(self):
#         print("Photo taken successfully!")

#     def playMusic(self):
#         print("Playing music on", self.music_app)

# smart=smartphone("nokia 630","12","spotify")
# print(smart.phone_info())
# smart.takePhoto()
# smart.playMusic()


# 2. Student Management System
# Create interfaces:
# Attendance
# Assignment
# Create class Student.
# Methods:
# markAttendance()
# submitAssignment()
# class student_info:
#     def __init__(self,attendence,assignment_date):
#         self.attendence=attendence
#         self.assignment_date=assignment_date

# class student(student_info):
#     def __init__(self,name,attendence, assignment_date):
#         super().__init__(attendence, assignment_date)
#         self.name=name
#     def markattendence(self):
#         return f"The attendence has been marked for {self.name}"
#     def submitassignment(self):
#         return f"The last date for assignment submission is {self.assignment_date}"

# student=student("adarsh","present","12.12.1935")
# print(student.markattendence())
# print(student.submitassignment())

        





# 3. Online Banking
# Create interfaces:
# Deposit
# Withdraw
# Create class BankAccount.
# Methods:
# depositAmount()
# withdrawAmount()
# class transaction:
#     def __init__(self,deposit,withdraw):
#         self.deposit=deposit
#         self.withdraw=withdraw
# class bankaccount(transaction):
#     def __init__(self,accountno,deposit,withdraw):
#         super().__init__(deposit,withdraw)
#         self.accountno=accountno
#     def depositamount(self):
#         return f"The amount of {self.deposit} has been deposited to account no {self.accountno}"
#     def withdrawamount(self):
#         return f"The amount of {self.withdraw} has been withdrawed to account no {self.accountno}"
    


# bank=bankaccount("1234","23","0")
# print(bank.depositamount())




# 4. Vehicle Features
# Create interfaces:
# GPS
# Bluetooth
# Create class Car.
# Methods:
# navigate()
# connectBluetooth()

# class features:
#     def __init__(self,gps,bluetooth):
#         self.gps=gps
#         self.bluetooth=bluetooth
# class car(features):
#     def __init__(self,carmodel,gps,bluetooth):
#         super().__init__(gps,bluetooth)
#         self.carmodel=carmodel
#     def navigate(self):
#         if self.gps=="on":
#             return f"The gps feature has been activated "
#         else:
#             return f"The gps isnt on turn it on"
#     def connectbluetooth(self):
#         if self.bluetooth=="on":
#             return f"The bluetooth has been connected"
#         else:
#             return f"The bluetooth isnt turned on turn it on "
# car=car("0123","on","on")
# print(car.navigate())
# print(car.connectbluetooth())




# 5. Smart Watch
# Create interfaces:
# HeartRateMonitor
# StepCounter
# Create class SmartWatch.
# Methods:
# checkHeartRate()
# countSteps()

# class features:
#     def __init__(self,heartratemonitor,stepcounter):
#         self.heartratemonitor=heartratemonitor
#         self.stepcounter=stepcounter
# class smartwatch(features):
#     def __init__(self,heartratemonitor,stepcounter):
#         super().__init__(heartratemonitor,stepcounter)
#     def checkheartrate(self):
            
#         if self.heartratemonitor=="on":
#             return f"The Heart rate monitor feature has been activated "
#         else:
#             return f"The The Heart rate monitor isnt on turn it on"
#     def countsteps(self):
#         if self.stepcounter=="on":
#             return f"The Step counter is on you can start walking"
#         else:
#             return f"The step counter  isnt turned on turn it on "
# watch=smartwatch("on","of")
# print(watch.checkheartrate())
# print(watch.countsteps())
        



# 6. Employee Benefits
# Create interfaces:
# Bonus
# Insurance
# Create class Employee.
# Methods:
# calculateBonus()
# insuranceDetails()
# class benefits:
#     def __init__(self,bonuspec,insurance):
#         self.bonuspec=bonuspec
#         self.insurance=insurance
# class employee(benefits):
#     salaryplus=0
#     def __init__(self,salary, bonuspec, insurance):
#         super().__init__(bonuspec, insurance)
#         self.salary=salary
#     def calculatebonus(self):
#         employee.salaryplus= self.salary *(1+(self.bonuspec/100))
#         return f"The salary for this month with bonus is {employee.salaryplus}"
#     def insurancedetails(self):
#         return f"The insurance is renewed for next year "

# emp=employee(100,45,"on")
# print(emp.calculatebonus())
# print(emp.insurancedetails())
                        



# 7. E-Commerce System
# Create interfaces:
# Cart
# Payment
# Create class Customer.
# Methods:
# addToCart()
# makePayment()
# class cart:
#     def __init__(self,cart,quantity,payment):
#         self.cart=cart
#         self.payment=payment
#         self.quantity=quantity
# class customer(cart):
#     cart1={}
#     def __init__(self,cart, quantity, payment):
#         super().__init__(cart,quantity, payment)
#     def addtocart(self):
#         customer.cart1[self.cart]=self.quantity
#         return f"The item has beena added{customer.cart1}"
#     def payment(self):
#         return f"The payment for this cart has been transactioned "
# cart=customer("milk",2,23)
# print(cart.addtocart())
    

# 8. Hospital Management
# Create interfaces:
# Doctor
# Receptionist
# Create class HospitalStaff.
# Methods:
# diagnosePatient()
# registerPatient()
# class faculty:
#     def __init__(self,doctor,receptionist):
#         self.doctor=doctor
#         self.receptionist=receptionist
# class  hospitalstaff(faculty):
#     def __init__(self,doctor,receptionist):
#         super().__init__(doctor,receptionist)

#     def diagnosepatient(self):
#         return f"The doctor {self.doctor} will diagnose the next patient "
#     def registerpatient(self):
#         return f"The front desk receptionist {self.receptionist} will register the next patient in the line"
# hos=hospitalstaff("jack","jon")
# print(hos.diagnosepatient())
# print(hos.registerpatient())




# 9. Smart Device
# Create interfaces:
# WiFi
# Bluetooth
# GPS
# Create class MobileDevice.
# Implement all methods.

# class features:
#     def __init__(self,wifi,bluetooth,gps):
#         self.wifi=wifi
#         self.bluetooth=bluetooth
#         self.gps=gps

# class mobiledevice(features):
#         def __init__(self,wifi,bluetooth,gps):
#             super().__init__(wifi,bluetooth,gps)

#         def navigate(self):
#             if self.gps=="on":
#                 return f"The gps feature has been activated "
#             else:
#                 return f"The gps isnt on turn it on"
#         def connectbluetooth(self):
#             if self.bluetooth=="on":
#                 return f"The bluetooth has been connected"
#             else:
#                 return f"The bluetooth isnt turned on turn it on "
#         def connectwifi(self):
#             if self.wifi=="on":
#                 return f"THe wifi is on"
#             else:
#                 return f"the wifi is turned off turn it on"
# mob=mobiledevice("on","on","off")
# print(mob.navigate())
# print(mob.connectbluetooth())
# print(mob.connectwifi())



# 10. College Portal
# Create interfaces:
# Examination
# Library
# Create class StudentPortal.
# Methods:
# writeExam()
# issueBook()
# class examination:
#     def __init__(self, exam):
#         self.exam = exam

#     def writeExam(self):
#         if self.exam == "on":
#             return f"The student is allowed to write the exam"
#         else:
#             return f"The student is not allowed to write the exam"


# class library:
#     def __init__(self, book):
#         self.book = book

#     def issueBook(self):
#         if self.book == "on":
#             return f"The book has been issued"
#         else:
#             return f"The book cannot be issued"


# class studentportal(examination, library):
#     def __init__(self, exam, book):
#         examination.__init__(self, exam)
#         library.__init__(self, book)


# student = studentportal("on", "on")
# print(student.writeExam())
# print(student.issueBook())


# Part B: Multilevel Inheritance
# 1. Person → Employee → Manager
# Create classes:
# Person
# Employee
# Manager
# Display:
# Name
# Employee ID
# Department
# class person:
#     def __init__(self,name):
#         self.name=name
        
# class employee(person):
#     def __init__(self,name,employeid):
#         super().__init__(name)
#         self.employeid=employeid
# class manager(employee):
#     def __init__(self,name,employeid,department):
#         super().__init__(name,employeid)
#         self.department=department
#     def Employeeinfo(self):
#         return f"The employee : {self.name}'s employee id is : {self.employeid} and they are working in {self.department} "
# a=manager("adarsh","2wsd2","It")
# print(a.Employeeinfo())








# 2. Animal → Dog → Puppy
# Methods:
# eat()
# bark()
# weep()
# class animal():
#     def __init__(self,gender):
#         self.gender=gender
# class dog(animal):
#     def __init__(self,name,gender):
#         super().__init__(gender)
#         self.name=name
# class puppy(dog):
#     def __init__(self,name,gender,age):
#         super().__init__(name, gender)
#         self.age=age
#     def eat(self):
#         return  f" {self.name} is eating" 
#     def bark(self):
#         return f" {self.name} is barking as {self.gender} is {self.age} years old"
#     def weep(self):
#         if self.age <=1:
#             return f"{self.name} is crying  as {self.gender} is only {self.age} years old and a puppy"
#         else:
#             return f"{self.name} is crying  as {self.gender} is bored"

# animal=puppy("jon","he",1)
# print(animal.eat())
# print(animal.bark())
# print(animal.weep())




# 3. Vehicle → Car → ElectricCar
# Methods:
# start()
# drive()
# chargeBattery()


# class vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         return f"The {self.brand} vehicle has started"


# class car(vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def drive(self):
#         return f"The {self.brand} {self.model} is driving"


# class electriccar(car):
#     def __init__(self, brand, model, battery):
#         super().__init__(brand, model)
#         self.battery = battery

#     def chargeBattery(self):
#         return f"The battery is charging and the current battery level is {self.battery}%"


# car1 = electriccar("Tesla", "Model 3", 80)

# print(car1.start())
# print(car1.drive())
# print(car1.chargeBattery())


# 4. Account → SavingsAccount → PremiumAccount
# Methods:
# deposit()
# withdraw()
# addInterest()

# class account:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self):
#         return f"The balance after deposit is {self.balance + 1000}"


# class savingsaccount(account):
#     def __init__(self, balance, withdraw):
#         super().__init__(balance)
#         self.withdraw = withdraw

#     def withdrawamount(self):
#         return f"The balance after withdrawal is {self.balance - self.withdraw}"


# class premiumaccount(savingsaccount):
#     def __init__(self, balance, withdraw, interest):
#         super().__init__(balance, withdraw)
#         self.interest = interest

#     def addInterest(self):
#         return f"The balance after adding interest is {self.balance + self.balance * self.interest / 100}"


# a = premiumaccount(10000, 500, 5)

# print(a.deposit())
# print(a.withdrawamount())
# print(a.addInterest())

# 5. College → Department → Student
# Store:
# College Name
# Department Name
# Student Name
# Display all details.

# class college:
#     def __init__(self, college_name):
#         self.college_name = college_name

# class department(college):
#     def __init__(self, college_name, department_name):
#         super().__init__(college_name)
#         self.department_name = department_name

# class student(department):
#     def __init__(self, college_name, department_name, student_name):
#         super().__init__(college_name, department_name)
#         self.student_name = student_name

#     def __str__(self):
#         return f"College Name: {self.college_name}\nDepartment Name: {self.department_name}\nStudent Name: {self.student_name}"

# s = student("SRM", "Computer Science", "Adarsh")
# print(s)

# 6. Book → ReferenceBook → DigitalReferenceBook
# Methods:
# showBook()
# showReference()
# showDigital()

# class book:
#     def __init__(self, name):
#         self.name = name

#     def showBook(self):
#         return f"The book name is {self.name}"


# class referencebook(book):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def showReference(self):
#         return f"The reference book is for {self.subject}"


# class digitalreferencebook(referencebook):
#     def __init__(self, name, subject, format):
#         super().__init__(name, subject)
#         self.format = format

#     def showDigital(self):
#         return f"The digital book format is {self.format}"
#     def full(self):
#         return f"The book {self.name} is about {self.subject} and it's also available in {self.format}"


# b = digitalreferencebook("Python Basics", "Programming", "PDF")

# print(b.showBook())
# print(b.showReference())
# print(b.showDigital())
# print(b.full())

# 7. Person → Teacher → ClassTeacher
# Methods:
# showPerson()
# showTeacher()
# showClassTeacher()

# class person:
#     def __init__(self, name):
#         self.name = name

#     def showPerson(self):
#         return f"The person's name is {self.name}"


# class teacher(person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def showTeacher(self):
#         return f"{self.name} teaches {self.subject}"


# class classteacher(teacher):
#     def __init__(self, name, subject, classname):
#         super().__init__(name, subject)
#         self.classname = classname

#     def showClassTeacher(self):
#         return f"{self.name} is the class teacher of {self.classname}"


# t = classteacher("Adarsh", "Python", "Class 10")

# print(t.showPerson())
# print(t.showTeacher())
# print(t.showClassTeacher())




# 8. Mobile → AndroidPhone → SamsungPhone
# Methods:
# call()
# installApp()
# samsungPay()

# class mobile:
#     def __init__(self, brand):
#         self.brand = brand

#     def call(self):
#         return f"The {self.brand} mobile is making a call"


# class androidphone(mobile):
#     def __init__(self, brand, os):
#         super().__init__(brand)
#         self.os = os

#     def installApp(self):
#         return f"An app has been installed on {self.os}"


# class samsungphone(androidphone):
#     def __init__(self, brand, os, payment):
#         super().__init__(brand, os)
#         self.payment = payment

#     def samsungPay(self):
#         return f"Samsung Pay is {self.payment}"


# s = samsungphone("Samsung", "Android", "available")

# print(s.call())
# print(s.installApp())
# print(s.samsungPay())


# 9. Employee → Developer → SeniorDeveloper
# Methods:
# showEmployee()
# showDeveloper()
# showSeniorDeveloper()

# class employee:
#     def __init__(self, name):
#         self.name = name

#     def showEmployee(self):
#         return f"The employee name is {self.name}"


# class developer(employee):
#     def __init__(self, name, language):
#         super().__init__(name)
#         self.language = language

#     def showDeveloper(self):
#         return f"{self.name} is a developer working with {self.language}"


# class seniordeveloper(developer):
#     def __init__(self, name, language, experience):
#         super().__init__(name, language)
#         self.experience = experience

#     def showSeniorDeveloper(self):
#         return f"{self.name} is a senior developer with {self.experience} years of experience"


# e = seniordeveloper("Adarsh", "Python", 5)

# print(e.showEmployee())
# print(e.showDeveloper())
# print(e.showSeniorDeveloper())


# 10. University → Department → Professor
# Store:
# University Name
# Department
# Professor Name
# Display all information.

# class university:
#     def __init__(self, university_name):
#         self.university_name = university_name

# class department(university):
#     def __init__(self, university_name, department_name):
#         super().__init__(university_name)
#         self.department_name = department_name

# class professor(department):
#     def __init__(self, university_name, department_name, professor_name):
#         super().__init__(university_name, department_name)
#         self.professor_name = professor_name

#     def __str__(self):
#         return f"University Name: {self.university_name}\nDepartment: {self.department_name}\nProfessor Name: {self.professor_name}"

# p = professor("SRM University", "Computer Science", "Ravi")

# print(p)


# Part C: Programs with User Input
# 1. Salary Calculation
# Create:
# Employee → Manager → SeniorManager
# Input:
# Basic Salary
# Calculate:
# HRA
# DA
# Bonus
# Net Salary

# class employee:
#     def __init__(self,salary):
#         self.salary=salary
# bonus=0
# hra=0
# class manager(employee):
#     def __init__(self,salary,bonus):
#         super().__init__(salary)
#         self.bonus=bonus
#     def bonus1(self):
#         bonus=self.salary*(self.bonus/100)
        
#         print (f"The salary with bonus {self.salary*(self.bonus/100)} is {self.salary *(1+(self.bonus/100))}")
#         return bonus
#     def hra(self):
#         hra=self.salary*0.20
        
#         print( f"HRA: {self.salary*0.20}")
#         return hra
# da=0
# netsal=0
# class senior_manager(manager):
#     def __init__(self,salary,bonus):
#         super().__init__(salary,bonus)
#     def da(self):
#         da=self.salary*0.10
        
#         print( f"DA: {self.salary*0.10}")
#         return da
#     def net_salary(self):
#         netsal = self.salary + self.bonus1() + self.hra() + self.da()
#         return netsal

# a=int(input("Enter the salary amount"))
# b=int(input("enter the bonus percentage"))
# emp=senior_manager(a,b)
# print("Net salary:", emp.net_salary())

        

    





# 2. Student Result System
# Hierarchy:
# Student → UGStudent → PGStudent
# Input:
# Marks
# Display:
# Total
# Average
# Grade

class student:
    def __init__(self,eng,maths,science):
        self.eng=eng
        self.maths=maths
        self.science=science
avg=0
total=0
mark=[]
subject=[]

class ugsstudent(student):
    def __init__(self,eng,maths,science):
        super().__init__(eng,maths,science)
    def total(self):
        return f"Total is {self.eng+self.maths+self.science}"
    def avg(self):
        avg=(self.eng+self.maths+self.science)/3
        return f"Average is {(self.eng+self.maths+self.science)/3}"
    
    def grade(self):
        avg=(self.eng+self.maths+self.science)/3
        marks = [self.eng, self.maths, self.science,avg]
        subjects = ["English", "Maths", "Science","Average"]

        for i in range(0, len(marks), 1):
            if marks[i] >= 95:
                print(subjects[i], "Grade: A+")
            elif marks[i] >= 85:
                print(subjects[i], "Grade: A")
            elif marks[i] >= 70:
                print(subjects[i], "Grade: B")
            elif marks[i] >= 50:
                print(subjects[i], "Grade: C")
            else:
                print(subjects[i], "Grade: Fail")
class pgstudent(ugsstudent):
    def __init__(self,eng,maths,science):
        super().__init__(eng,maths,science)

eng = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))

clas = pgstudent(eng, maths, science)

clas.grade()
print(clas.total())
print(clas.avg())



# 3. Bank Interest Calculation
# Account → Savings → PremiumSavings
# Input:
# Amount
# Calculate:
# Interest
# Maturity Amount

# 4. Vehicle Rental System
# Vehicle → Car → LuxuryCar
# Input:
# Number of Days
# Calculate:
# Rental Amount

# 5. Hospital Billing System
# Patient → InPatient → SpecialRoomPatient
# Input:
# Room Charges
# Doctor Fees
# Calculate:
# Total Bill


