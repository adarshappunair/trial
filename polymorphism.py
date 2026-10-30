# method overriding 
# class student:
#     def add(self):
#         return f"HI1"
# class teacher:
#     def add(self):
#         return f"hi2"
# s=student()
# t=student()
# print(s.add())
# print(t.add())
# creating same function in 2 classes to use it with 2 different objects is method overriding 
# method overloading 
# class student:
#     def add(self,a,b):
#         c=a+b
#         return c
#     def add(self,a,b,c):
#         d=a,b,c
#         return d
# s=student()
# print(s.add(2,3))
# print(s.add(2,3,5))
# Above code wont work ask you cant use 2 fucntions with same name as it wont run in python 
# class student:
#     def add(self,*a):
#         for i in a:
#             c=sum(a)
#             return c
    
# s=student()
# print(s.add(2,3))
# print(s.add(2,3,5))


# operator overloading
# class a:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __sub__(self,other):
#         return self.a-other.a,self.b-other.b
# p1=a(23,21)
# p2=a(12,18)
# p3=p1-p2
# print(p3)

# ducktyping
# class duck:
#     def sound(self):
#         return "quack"
# class dog:
#     def sound(self):
#         return "bark"
# class cat:
#     def sound(self):
#         return "cat"
# def make_sound(animal):
#     return animal.sound()
# animal1=duck()
# animal2=dog()
# animal3=cat()
# print(make_sound(animal1))




# Create Dog and Cat classes with a speak() method and write one function that works with both.

# class duck:
#     def sound(self):
#         return "quack"
# class dog:
#     def sound(self):
#         return "bark"
# class cat:
#     def sound(self):
#         return "cat"
# def make_sound(animal):
#     return animal.sound()
# animal1=duck()
# animal2=dog()
# animal3=cat()
# print(make_sound(animal1))


# Create PDF and WordDocument classes with a read() method and process both using the same function.
# class pdf:
#     def read(self):
#         f=open("new.pdf","w")
#         f.write("Learning Python is a journey, and every journey requires patience, practice, and patience again. When you practice Python every day, you become better at Python, and your confidence grows. Some people learn quickly, while other people learn slowly, but people who practice regularly often achieve better results. Learning requires effort, and effort produces progress. Progress makes learning enjoyable, and enjoyable learning encourages more practice. A good programmer writes code, reads code, tests code, and improves code. When code fails, the programmer studies the error, fixes the error, and tests the code again. Errors are useful because errors teach lessons, and lessons help programmers write better code. Better code is easier to read, easier to understand, and easier to maintain. Python is a popular language because Python is simple, Python is readable, and Python supports many useful libraries. Libraries make programming easier, and programming becomes easier when you understand the basics. The basics include variables, loops, lists, strings, dictionaries, functions, and files. Files store information, and information stored in files can be read later. Reading files, writing files, and updating files are important skills. Practice makes progress, and progress builds confidence. Confidence helps you solve problems, and solving problems improves your logic. Good logic helps you write good programs, and good programs solve real problems. Every problem has a solution, but finding the solution sometimes requires time, effort, and patience. Never stop learning, never stop practicing, and never stop improving. Learning takes time, practice takes effort, and improvement takes consistency. If you make mistakes, learn from mistakes. If your program fails, fix your program. If your logic is wrong, improve your logic. Keep practicing Python, keep writing code, and keep learning new concepts. The more you practice, the more you learn, and the more you learn, the better you become..")
#         f.close()
#         f=open("new.pdf","r")
#         return f.read()
# class word:
#     def read(self):
#         f=open("word.docx","w")
#         f.write("Learning Python is a journey, and every journey requires patience, practice, and patience again. When you practice Python every day, you become better at Python, and your confidence grows. Some people learn quickly, while other people learn slowly, but people who practice regularly often achieve better results. Learning requires effort, and effort produces progress. Progress makes learning enjoyable, and enjoyable learning encourages more practice. A good programmer writes code, reads code, tests code, and improves code. When code fails, the programmer studies the error, fixes the error, and tests the code again. Errors are useful because errors teach lessons, and lessons help programmers write better code. Better code is easier to read, easier to understand, and easier to maintain. Python is a popular language because Python is simple, Python is readable, and Python supports many useful libraries. Libraries make programming easier, and programming becomes easier when you understand the basics. The basics include variables, loops, lists, strings, dictionaries, functions, and files. Files store information, and information stored in files can be read later. Reading files, writing files, and updating files are important skills. Practice makes progress, and progress builds confidence. Confidence helps you solve problems, and solving problems improves your logic. Good logic helps you write good programs, and good programs solve real problems. Every problem has a solution, but finding the solution sometimes requires time, effort, and patience. Never stop learning, never stop practicing, and never stop improving. Learning takes time, practice takes effort, and improvement takes consistency. If you make mistakes, learn from mistakes. If your program fails, fix your program. If your logic is wrong, improve your logic. Keep practicing Python, keep writing code, and keep learning new concepts. The more you practice, the more you learn, and the more you learn, the better you become..")
#         f.close()
#         f=open("word.docx","r")
#         return f.read()
# def read1(pdfword):
#     return pdfword.read()

# pdf=pdf()
# word=word()
# print(read1(pdf))



# Write a function that accepts any object supporting len().

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def __len__(self):
#         return len(self.marks)

# class teacher:
#     def __init__(self, name, subjects):
#         self.name = name
#         self.subjects = subjects

#     def __len__(self):
#         return len(self.subjects)

# def count(obj):
#     return len(obj)

# s1 = student("Adarsh", [90, 85, 78])
# t1 = teacher("Rahul", ["Python", "Java"])

# print(count(s1))
# print(count(t1))



# Create a custom class that supports Python's len() function using __len__().
# class one:
#     def __init__(self,word1):
#         self.__word1=word1 #private attribute
#     def __len__(self):  #getter method
#         return len(self.__word1) 
# class two:
#     def __init__(self,word2):
#         self.__word2=word2
#     def __len__(self):
#         return len(self.word2)
# def main(obj):
#     return len(obj)
# s1=one("adarsh")
# print(main(s1))




# Create a custom class that supports the + operator using __add__().
# class student:
#     def __init__(self, *a):
#         self.a = a
#     def __add__(self,*a):
#         c = sum(self.a)
#         return c
# class teacher:
#     def __init__(self, *b):
#         self.b = b
#     def __add__(self,*b):
#         c = sum(self.b)
#         return c
# def one(obj):
#      return obj.__add__()

# s1=student(23,32,12)
# s2=teacher(2,55,12)
# print(one(s1))
# print(one(s2))

# print()
    



# Create two unrelated classes that implement a common behavior without inheritance.
class one:
    def __init__(self, a):
        self.a = a
    def power(self):
        c= self.a**2
        return c
class two:
     def __init__(self, b):
            self.b = b
     def power(self):
                c=self.b**3
                return c
def main(obj):
    return obj.power()
one=one(2)
two=two(3)
print(main(one))
print(main(two))




# Design a payment processor that works with CreditCardPayment and UPIPayment objects.
class CreditCardPayment:
    def payment(self, amount):
        return f"Paid Rs.{amount} using Credit Card"

class UPIPayment:
    def payment(self, amount):
        return f"Paid Rs.{amount} using UPI"

def main(obj):
    return obj.payment(500)

c1 = CreditCardPayment()
u1 = UPIPayment()

print(main(c1))
print(main(u1))



# Write a function that accepts any iterable and prints its elements.
class one:
    
    def __init__(self,a):
            self.a=a
        
    def it1(self):
            while self.a<1000:
                 self.a=self.a*3
                 print(self.a)
class two:
    def __init__(self,b):
        self.b=b
        
    def it1(self):
            while self.b<1000:
                 self.b=self.b*4
                 print(self.b)
def main(obj):
    return obj.it1()

o1 = one(12)
o2 = two(4)

main(o1)
main(o2)



# Demonstrate what happens when an object lacks a required method and handle the error.





# Implement a duck-typed notification system that supports both email and SMS notifications.