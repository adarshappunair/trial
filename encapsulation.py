class student:
    def __init__(self,marks):
        self.__marks=marks #private attribute 
    def get_marks(self):
        return self.__marks # getter method
    def set_marks(self,marks): # setter method
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks")
s=student(80)
print(s.get_marks())
s.set_marks(95)
print(s.get_marks())
s.set_marks(123)