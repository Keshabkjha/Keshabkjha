#!/usr/bin/env python
# coding: utf-8

# 1. Write a program illustrating class definition and accessing class members. 

# In[ ]:


print("\t\t\t\t\tProgram1")
class classname:
    a="CSE"
    def __init__(self,xyz):
        self.xyz=xyz
    def show(self):
        print("name=",self.xyz)
s=classname("Keshab")
s.show()
print(classname.a)


# 2. Write a program to implement default constructor, parameterized constructor, 
# and destructor. 

# In[ ]:


print("\t\t\t\t\tProgram2")
class Students:
    # Default constructor
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
        print("Default constructor called with name",self.name,"and age",self.age)
a=Students()
class Student:
    # Parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Parameterized constructor called with name", self.name, "and age", self.age)
    # Destructor
    def __del__(self):
        print("Destructor called for", self.name)
# Creating objects using both constructors
s1 = Student("Alice", 20)
s2 = Student("Bob", 19)
# Deleting the objects explicitly
del s1
del s2


# 3. Create a Python class named Rectangle constructed by a length and width. 
#  Create a method called area which will compute the area of a rectangle. 

# In[ ]:


print("\t\t\t\tProgram3")
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
R=Rectangle(10,20)
print("Area:",R.area())


# 4. Create a class called Numbers, which has a single class attribute called 
# MULTIPLIER, and a constructor which takes the parameters x and y (these 
# should all be numbers). 
# a. Write an instance method called add which returns the sum of the 
# attributes x and y. 
# b. Write a class method called multiply, which takes a single number 
# parameter a and returns the product of a and MULTIPLIER. 
# c. Write a static method called subtract, which takes two number objects, b 
# and c, and returns b - c. 
# d. Write a method called value which returns a tuple containing the values of x 
# and y. 

# In[ ]:


print("\t\t\t\tProgram 4")
class Numbers:
    #class attribute
    MULTIPLIER = 42
    def __init__(self, x, y): #Constructor
        self.x = x #Instance attribute
        self.y = y

    def add(self): #instance method
        return self.x + self.y

    @classmethod #Class method
    def multiply(cls, a):
        return Numbers.MULTIPLIER*a

    @staticmethod #static method
    def subtract(b, c):
        return b - c

    def value(self): #Instance method
        return (self.x, self.y)
num=Numbers(10,20)
print(num.add())
print(num.multiply(2))
print(num.subtract(4,3))
print(num.value())


# 5. Create a class named as Student to store the name and marks in three 
# subjects. Use List to store the marks. 
# a. Write an instance method called compute to compute total marks and 
# average marks of a student. 
# b. Write a method called display to display student information. 

# In[ ]:


print("\t\t\t\tProgram 5")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks # a list of three marks

    def compute(self):
        # compute the total and average marks of a student
        total = sum(self.marks)
        average = total / len(self.marks)
        return total, average

    def display(self):
        # display the student information
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        total, average = self.compute()
        print(f"Total: {total}")
        print(f"Average: {average}")

# create a student object and test the methods
s1 = Student("Keshab Jha", [93, 95, 90])
s1.display()


# 6. Create a class Employee that keeps a track of the number of employees in an 
# organization and also stores their name, designation and salary details. 
# a. Write a method called getdata to take input (name, designation, salary) 
# from user. 
# b. Write a method called average to find average salary of all the employees 
# in the organization. 
# c. Write a method called display to print all the information of an employee.

# In[ ]:


print("\t\t\t\t\tProgram 6")
class Employee:
    num_employees = 0
    total_salary = 0
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
        Employee.num_employees += 1
        Employee.total_salary += salary
    def getdata(self):
        self.name = input("Enter name: ")
        self.designation = input("Enter designation: ")
        self.salary = float(input("Salary: "))
    def average():
        if Employee.num_employees > 0:
            return Employee.total_salary / Employee.num_employees
        else:
            return 0
    def display(self):
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
emp1 = Employee("Keshab", "Manager", 50000)
emp2 = Employee("Jha", "Engineer", 40000)
emp3 = Employee("Ravan", "Analyst", 30000)
print("Number of employees:", Employee.num_employees)
print("Average salary:", Employee.average())
emp1.display()
emp2.display()
emp3.display()
emp4 = Employee("", "",0)
emp4.getdata()
print("Number of employees:", Employee.num_employees)
print("Average salary:", Employee.average())


# 7. Create a Python class named Circle constructed by a radius. Use a class 
# variable to define the value of constant PI. 
# a. Write two methods to be named as area and circum to compute the area 
# and the perimeter of a circle respectively by using class variable PI. 
# b. Write a method called display to print area and perimeter

# In[ ]:


print("\t\t\t\t\t\t\t Program 7")
class Circle:
    pi=3.14
    def __init__(self,radius):
      self.radius=radius
    def area(self):
      return Circle.pi*self.radius**2
    def circum(self):
      return 2*Circle.pi*self.radius
    def display(self):
      print(f"The area of the circle is {self.area()}")
      print(f"The Circumference of the circle is {self.circum()}")
r=Circle(9)
r.display()


# 8. Create a class called String that stores a string and all its status details such as 
# number of uppercase letters, lowercase letters, vowels ,consonants and space 
# in instance variables. 
# a. Write methods named as count_uppercase, count_lowercase, 
# count_vowels, count_consonants and count_space to count corresponding 
# values. 
# b. Write a method called display to print string along with all the values 
# computed by methods in (a). 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t\t\t Program 8")
class String:
    def __init__(self, s):
        self.s = s # store the string
        self.uppercase = 0 # store the number of uppercase letters
        self.lowercase = 0 # store the number of lowercase letters
        self.vowels = 0 # store the number of vowels
        self.consonants = 0 # store the number of consonants
        self.space = 0 # store the number of spaces

    def count_uppercase(self):
        # loop through the string and count uppercase letters
        for c in self.s:
            if c.isupper():
                self.uppercase += 1
    def count_lowercase(self):
        # loop through the string and count lowercase letters
        for c in self.s:
            if c.islower():
                self.lowercase += 1

    def count_vowels(self):
        # loop through the string and count vowels
        for c in self.s:
            if c.lower() in "aeiou":
                self.vowels += 1

    def count_consonants(self):
        # loop through the string and count consonants
        for c in self.s:
            if c.lower() in "bcdfghjklmnpqrstvwxyz":
                self.consonants += 1
    def count_space(self):
        # loop through the string and count spaces
        for c in self.s:
            if c == " ":
                self.space += 1

    def display(self):
        # print the string and all the values computed by methods
        print("String:", self.s)
        print("Uppercase:", self.uppercase)
        print("Lowercase:", self.lowercase)
        print("Vowels:", self.vowels)
        print("Consonants:", self.consonants)
        print("Space:", self.space)

# create an object of String class with a sample string
s = String("Hello World!")
# call all the methods to compute the values
s.count_uppercase()
s.count_lowercase()
s.count_vowels()
s.count_consonants()
s.count_space()
# call the display method to print the results
s.display()


# 9. Write a program that has a class called Fraction with attributes numerator and 
# denominator. 
# a. Write a method called getdata to enter the values of the attributes. 
# b. Write a method show to print the fraction in simplified form. 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t Program 9")
class Fraction:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def getdata(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))

    def show(self):
        gcd = self._gcd(self.numerator, self.denominator)

        # Simplify the fraction by dividing both the numerator and denominator by their gcd
        numerator = self.numerator // gcd
        denominator = self.denominator // gcd

        # Print the fraction
        print(f"{numerator}/{denominator}")

    def _gcd(self, a, b):
        # Find the greatest common divisor of two numbers using Euclid's algorithm
        if b == 0:
            return a
        return self._gcd(b, a % b)
fraction = Fraction()
fraction.getdata()
fraction.show()


# 10. Write a program that has a class Numbers with a list as an instance variable. 
# a. Write a method called insert_element that takes values from user. 
# b. Write a class method called find_max to find and print largest value in the 
# list. 

# In[ ]:


print("\t\t\t\t\t Program 10")
class Numbers:
    def __init__(self):
        self.num_list = []
    
    def insert_element(self):
        num = int(input("Enter value from the user: "))
        self.num_list.append(num)
    
    @classmethod
    def find_max(cls, num_list):
        max_num = max(num_list)
        print("The largest value in the list is:", max_num)
n = Numbers()
n.insert_element()
n.insert_element()
n.insert_element()
n.insert_element()
Numbers.find_max(n.num_list)


# 11. Write a program that has a class Point with attributes x and y. 
# a. Write a method called midpoint that returns a midpoint of a line joining two 
# points. 
# b. Write a method called length that returns the length of a line joining two 
# points. 

# In[ ]:


print("\t\t\t\t\t Program 11")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def midpoint(self, other_point):
        x_mid = (self.x + other_point.x) / 2
        y_mid = (self.y + other_point.y) / 2
        return Point(x_mid, y_mid)
    
    def length(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        return (dx**2 + dy**2)**(1/2)

x1=float(input("x1:"))
x2=float(input("x2:"))
y1=float(input("y1:"))
y2=float(input("y2:"))
p1 = Point(x1, y1)
p2 = Point(x2, y2)

print("The midpoint of the line is:", p1.midpoint(p2).x, p1.midpoint(p2).y)
print("The length of the line is:",p1.length(p2))


# 12. Create a class called Complex. Write a menu driven program to read, display, 
# add and subtract two complex numbers by creating corresponding instance 
# methods. 

# In[ ]:


print("\t\t\t\t\tProgram12")
class Complex:
    def __init__(self,re,im):
        self.re=re
        self.im=im
    def display(self):
        if self.im>=0:
            print(self.re+self.im)
        else:
            print(self.re-self.im)
    def add(self,other):
        print(complex(self.re+other.re,self.im+other.im))
    def subtract(self,other):
        print(complex(self.re-other.re,self.im-other.im))
obj1=Complex(3,4)
obj2=Complex(5,6)
print("1. for display\n2. for add\n3. for subtract")
choice=int(input("Enter choice:"))
if choice==1:
    obj1.display()
    obj2.display()
elif choice==2:
    obj1.add(obj2)
elif choice==3:
    obj1.subtract(obj2)
    


# 13. Write a Program to illustrate the use of __str__(), __repr__(), __new__, 
# __doc__, __dict__, __name__ and __bases__ methods. 

# In[ ]:


print("\t\t\t\t\t\t\t\t Program 13")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        instance = super().__new__(cls)
        return instance

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        print(f"{self.name} earns {self.salary} dollars.")

print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__bases__)

person1 = Person("John", 25)
print(person1)

employee1 = Employee("Jane", 30, 5000)
print(employee1)
employee1.display()


# 14. Create a BankAccount class. Your class should support the following methods: 
# a. __init__(self, account_no) 
# b. deposit (self, account_no, amount) 
# c. withdraw (self, account_no, amount) 
# d. get_balance (self, account_no) 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t Program 14")
class BankAccount:
    def __init__(self, account_no):
        self.account_no = account_no

    def deposit(self, account_no, amount):
        if self.account_no == account_no:
            balance = self.get_balance(account_no)
            balance += amount
            self.set_balance(account_no, balance)
            return True
        else:
            return False

    def withdraw(self, account_no, amount):
        if self.account_no == account_no:
            balance = self.get_balance(account_no)
            if balance >= amount:
                balance -= amount
                self.set_balance(account_no, balance)
                return True
            else:
                return False
        else:
            return False
    def get_balance(self, account_no):
        if self.account_no == account_no:
            return self.get_balance_from_storage(account_no)
        else:
            return None
    def set_balance(self, account_no, balance):
        if self.account_no == account_no:
            self.set_balance_in_storage(account_no, balance)
        else:
            pass
    def get_balance_from_storage(self, account_no):
        return 1000
    def set_balance_in_storage(self, account_no, balance):
        pass
c=BankAccount(123456)
print(c.deposit(123456,5000))
print(c.withdraw(123456,300))
print(c.get_balance(123456))
print(c.set_balance(123456,7000))
print(c.get_balance_from_storage(123456))
print(c.set_balance_in_storage(123456,8000))


# 15. Write a program to illustrate the use of following built-in methods: 
# a. hasattr(obj,attr) 
# b. getattr(object, attribute_name [, default]) 
# c. setattr(object, name, value) 
# d. delattr(class_name, name)

# In[ ]:


print("\t\t\t\t\t\t\t\t Program 15")
class Student:
    RNo=19
    def __init__(self):
        self.name="Keshab"
        self.age=19
    def Illustrate(self):
        print("Illlustrating the use of following built in Methods")
a=Student()
print(hasattr(a,"name"))
print(hasattr(a,"nam"))
print(getattr(a,"name"))
print(getattr(a,"age"))
setattr(a,"age",8)
print(getattr(a,"age"))
print(delattr(Student,"RNo"))


  
  


# 16. Write a program to create class Employee. Display the personal information 
# and salary details of 5 employees using single inheritance.

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t Program 16")
class Employee:
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
    def display_personal_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        
    def display_salary_details(self):
        print(f"Salary: {self.salary}")
        print(f"Income Tax: {self.salary*0.1}")
        print(f"Net Salary: {self.salary - self.salary*0.1}\n")
class Display(Employee):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c,d)
emp1 = Display("Mandodri", 25, "F", 50000)
emp2 = Display("Ram", 30, "M", 60000)
emp3 = Display("Ravan", 35, "M", 70000)
emp4 = Display("Lucky", 40, "M", 80000)
emp5 = Display("Chhoti", 45, "F", 90000)
for emp in [emp1, emp2, emp3, emp4, emp5]:
    emp.display_personal_info()
    emp.display_salary_details()


# 17. WAP that extends the class Employee. Derive two classes Manager and Team 
# Leader from Employee class. Display all the details of the employee working 
# under a particular Manager and Team Leader. 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t Program 17")
class Employee:
  def __init__(self,name,salary):
    self.name=input("Name:")
    self.salary=float(input("Salary:"))
class Manager(Employee):
  def __init__(self,a,b):
    super().__init__(a,b)
  def show(self):
    print(self.name,"is Manager with salary",self.salary)
class TeamLeader(Employee):
  def __init__(self,a,b):
    super().__init__(a,b)
  def show(self):
    print(self.name,"is Team leader with salary",self.salary)
emp1=Manager("",0)
emp1.show()
emp2=TeamLeader("",0)
emp2.show()


# 18. Write a program that has a class Point. Define another class Location which 
# has two objects (Location and destination) of class Point. Also, define a function 
# in Location that prints the reflection on the y-axis. 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t\t\t\t Program 18")
class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
class Location:
  def __init__(self,location,destination):
    self.location =location
    self.destination = destination
  def reflection_on_y_axis(self):
    # Calculate the reflection of the points on the y-axis
    reflection_location = Point(-self.location.x, self.location.y)
    reflection_destination = Point(-self.destination.x, self.destination.y)     
    # Print the reflection points
    print(f"Reflection of location point: ({reflection_location.x}, {reflection_location.y})")
    print(f"Reflection of destination point: ({reflection_destination.x}, {reflection_destination.y})")
loc = Location(Point(3, 4),Point(5,6))
loc.reflection_on_y_axis()


# 19. WAP that create a class Student having attribute as name and age and Marks 
# class inheriting Students class with its own attributes marks1, marks2 and 
# marks3 as marks in 3 subjects. Also, define the class Result that inherits the 
# Marks class with its own attribute total. Every class has its own display() 
# method to display the corresponding details. Use __init__() and super() to 
# implement the above classes. 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t Program 19")
class Student:
  def __init__(self,name,age):
    self.name=input("")
    self.age=int(input())
  def show(self):
    print("Name:",self.name)
    print("Age:",self.age)
class Result(Student):
  def __init__(self,marks1,marks2,marks3):
    self.marks1=int(input("Maths:"))
    self.marks2=int(input("Python:")) 
    self.marks3=int(input("Physics:"))
  def showR(self):
    print("Marks is",self.marks1)
    print("Marks is",self.marks2)
    print("Marks is",self.marks3)
class Marks(Result):
  def __init__(self,a,b,c):
    super().__init__(a,b,c)
  def showM(self):
    print("Total:",self.marks1+self.marks2+self.marks3)
st1=Student("","")
st1.show()
st3=Marks(0,0,0)
st3.showR()
st3.showM()


# 20. Write a program that create a class Distance with members km and metres. 
# Derive classes School and office which store the distance from your house to 
# school and office along with other details. 

# In[ ]:


print("\t\t\t\t\t\t\t\t Program 20")
class Distance:
    def __init__(self, km, metres):
        self.km =int(input("Km:"))
        self.metres = int(input("Metres:"))
    def display(self):
        print(f"{self.km} km and {self.metres} metres")
class School(Distance):
    def __init__(self, km, metres, name, address, phone):
        self.name = input("School name:")
        self.address =input("School Address:")
        self.phone = int(input("School phone:"))
        super().__init__(km, metres)
    def display(self):
        print(f"Distance from house: ", end="")
        super().display()
class Office(Distance):
    def __init__(self, km, metres, name, address, email):
        self.name =input("Office name:")
        self.address = input("Office address:")
        self.email = input("Office email:")
        super().__init__(km, metres)
    def display(self):
        print(f"Distance from house: ", end="")
        super().display()
school = School(0,0, "", "",0 )
school.display()
office = Office(0,0, "", "", "")
office.display()


# 21. Write a program to create an abstract class Vehicle. Derive three classes Car, 
# Motorcycle and Truck from it. Define appropriate methods and print the details 
# of vehicle. 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t\t Program 21")
from abc import ABC,abstractmethod
class Vehicle(ABC):
  def __init__(self,maker,model,color,year):
    self.maker=input("Maker:")
    self.model=input("model:")
    self.color=input("color:")
    self.year=int(input("year:"))
  @abstractmethod
  def vehicle_type(self):
    pass
  @abstractmethod
  def engine_type(self):
    pass
  def details(self):
    print(f'Type of vehicle is {self.vehicle_type()}')
    print(f"Maker of the {self.vehicle_type()} is {self.maker}")
    print(f"Model of the {self.vehicle_type()} is {self.model}")
    print(f"Engine type of {self.vehicle_type()} is {self.engine_type()}")
    print(f"color of the {self.vehicle_type()} is {self.color}")
    print(f"Manufacturing year of {self.vehicle_type()} is {self.year}")
class Car(Vehicle):
  def __init__(self,maker,model,color,year,no_door):
    super().__init__(maker,model,color,year)
    self.no_door=input("No. of doors:")
  def vehicle_type(self):
    return "Car"
  def engine_type(self):
    e=input("Engine Type:")
    return e
  def details(self):
    super().details()
    print(f"No. of door in {self.vehicle_type()} is {self.no_door}")
class Motorcycle(Vehicle):
  def __init__(self,maker,model,color,year,milage):
    super().__init__(maker,model,color,year)
    self.milage=input("Milage:")
  def vehicle_type(self):
    return "Motorcycle"
  def engine_type(self):
    e=input("Engine Type:")
    return e
  def details(self):
    super().details()
    print(f"Milage of {self.vehicle_type()} is {self.milage}")
class Truck(Vehicle):
  def __init__(self,maker,model,color,year,no_wheels):
    super().__init__(maker,model,color,year)
    self.no_wheels=input("No of wheels:")
  def vehicle_type(self):
    return"Truck"
  def engine_type(self):
    e=input("Engine Type:")
    return e
  def details(self):
    super().details()
    print(f"No of vehicle in {self.vehicle_type()} is {self.no_wheels} ")
c=Car("","","",0,"")
c.details()
m=Motorcycle("","","",0,"")
m.details()
t=Truck("","","",0,"")
t.details()


# 22. Write a program that has a class Polygon. Derive two classes Rectangle and 
# triangle from polygon and write methods to get the details of their dimensions 
# and hence calculate the area.

# In[ ]:


print("\t\t\t\t\t\t\t\t\t Program 22")
class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = []
    def get_dimensions(self):
        self.sides = []
        for i in range(self.num_sides):
            side = float(input(f"Enter the length of side {i+1}: "))
            self.sides.append(side)
    def calculate_area(self):
        pass
class Rectangle(Polygon):
    def __init__(self,a):
        super().__init__(a)
        print("dimensions of Rectangle:")
    def calculate_area(self):
            length = self.sides[0]
            width = self.sides[1]
            Length=self.sides[2]
            Width=self.sides[3]
            area = length * width
            if Length==length and Width==width:
                return area
            else:
                raise ValueError("Invalid dimensions for a rectangle.")
class Triangle(Polygon):
    def __init__(self,a):
          super().__init__(a)
          print("dimensions of Triangle:")
    def calculate_area(self):
            a= self.sides[0]
            b = self.sides[1]
            c = self.sides[2]
            s=(a+b+c)*1/2
            area=(s*(s-a)*(s-b)*(s-c))**1/2
            if s>=0:
                return area
            else:
                ValueError("Invalid Dimensions for Triangle")
rectangle = Rectangle(4)
rectangle.get_dimensions()
rectangle_area = rectangle.calculate_area()
print("Rectangle Area:", rectangle_area)
triangle = Triangle(3)
triangle.get_dimensions()
triangle_area = triangle.calculate_area()
print("Triangle Area:", triangle_area)


# 23. Write a program that extends the class Shape to calculate the area of a circle 
# and a cone .(use super to inherit base class methods)

# In[ ]:


print("\t\t\t\t\t\t\t Program 23")
import math
class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius =float(input("Radius of Circle:"))
    def area(self):
        return math.pi * self.radius * self.radius
class Cone(Shape):
    def __init__(self, radius, height):
        super().__init__()
        self.radius = float(input("Radius of Cone:"))
        self.height = float(input("Height of Cone:"))
    def area(self):
        base_area = math.pi * self.radius * self.radius
        side_area = math.pi * self.radius * math.sqrt(self.radius * self.radius + self.height * self.height)
        return base_area + side_area
circle = Circle(0)
circle_area = circle.area()
print(f"Area of Circle: {circle_area:.2f}")
cone = Cone(0,0)
cone_area = cone.area()
print(f"Cone area: {cone_area:.2f}")


# 24. Write a program to demonstrate hybrid inheritance and show MRO for each 
# class. 
# 

# In[ ]:


print("\t\t\t\t\t\t\t Program 24")
class A:
    def show_a(self):
        print("Base class A")

class B(A):
    def show_b(self):
        print("Class B from A")

class C(A):
    def show_c(self):
        print("Class C from A")

class D(B, C):
    def show_d(self):
        print("Class D from B and C")
a = D()
a.show_a()
a.show_b()
a.show_c()
a.show_d()
print(A.mro())
print(B.mro())
print(D.mro())


# 25. Write a program to overload + operator to multiply to fraction object of fraction 
# class which contain two instance variable numerator and denominator. Also, 
# define the instance method simplify() to simplify the fraction objects. 
# 

# In[ ]:


from math import gcd
print("\t\t\t\t\t\t\t\t\t Program 25")
class Fraction:
    def __init__(self, num, deno):
        self.num =num
        self.deno = deno
    def __str__(self):
        return f"{self.num}/{self.deno}"
    def simplify(self):
        gcd = self.gcd(self.num, self.deno)
        return Fraction(self.num//gcd,self.deno//gcd)
    def gcd(self, a, b):
        if b==0:
            raise ValueError("Denominator can never be zero")
        else:
            return gcd(a,b)
    def __add__(self, other):
        new_num = self.num *other.deno+other.num*self.deno
        new_deno = self.deno *other.deno
        return Fraction(new_num, new_deno)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_deno = self.deno * other.deno
        return Fraction(new_num, new_deno)
num1 = int(input("Enter numerator for fraction 1: "))
deno1 = int(input("Enter denominator for fraction 1: "))
f1 = Fraction(num1, deno1)
print(f"Fraction1:{f1}")
num2 = int(input("Enter numerator for fraction 2: "))
deno2 = int(input("Enter denominator for fraction 2: "))
f2 = Fraction(num2, deno2)
print(f"Fraction:{f2}")   
result=f1+f2
print(result)
result.simplify()
print(f"Simplified result:{result}")
result = f1 * f2
print(result)   
result.simplify() 
print(f"Simplified Result:{result}")


# 26. Write a program to compare two-person object based on their age by 
# overloading > operator. 

# In[ ]:


print("\t\t\t\t\t\t\t\t Program 26")
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __gt__(self,other):
    return self.age>other.age
n1=input("Name of one Person:")
a1=int(input("Age of one Person:"))
n2=input("Name of other Person:")
a2=int(input("Age of other Person:"))
p1=Person(n1,a1)
p2=Person(n2,a2)
print(f"Age of One Person is greater than other:{p1>p2}")
print(f"Age of other is greater than one:{p2>p1}")


# 27. Write a program to overload inoperator.

# In[ ]:


print("\t\t\t\t\t\t\t Program 27")
class NumberSet:
    def __init__(self, numbers):
        self.numbers = numbers

    def __contains__(self, number):
        return number in self.numbers


# Example usage:
user_input = input("Enter a list : ")
user_set = user_input.split(",")

my_set = NumberSet(user_set)

search_number = input("Enter an item to search: ")

if search_number in my_set:
    print(f"{search_number} is present in the list.")
else:
    print(f"{search_number} is not present in the list.")


# 28. WAP to create a Complex class having real and imaginary as it attributes. 
# Overload the +,-,/,* and += operators for objects of Complex class. 

# In[ ]:


print("\t\t\t\t\t\t\t Program 28")
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        if denom == 0:
            raise ZeroDivisionError("Denominator can never be zero")
        return Complex((self.real * other.real + self.imag * other.imag) / denom,
                       (self.imag * other.real - self.real * other.imag) / denom)

    def __iadd__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self
r1 = float(input("Enter the real part of the first complex number: "))
i1 = float(input("Enter the imaginary part of the first complex number: "))
c1 = Complex(r1, i1)
print(f"First Complex number:{c1}")
r2 = float(input("Enter the real part of the second complex number: "))
i2 = float(input("Enter the imaginary part of the second complex number: "))
c2 = Complex(r2, i2)
print(f"Other Complex number:{c2}")
print(f"Addition of two Complex Number:{c1 + c2}") 
print(f"Substraction of two Complex Number:{c1 - c2}") 
print(f"Multiplication of two Complex Number:{c1 * c2}") 
print(f"True Division of two Complex Number:{c1 / c2}")
c1 += c2
print(f"__iadd__ of two Complex Number:{c1}")


# 29. Write a program to inspect the object using type() ,id(), isinstance(), issubclass() 
# and callable() built-in function. 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t Program 29")
class MyClass:
    pass
def my_function():
    pass
my_instance = MyClass()
print("Type of my_instance:", type(my_instance))
print("Type of my_function:", type(my_function))
print("ID of my_instance:", id(my_instance))
print("ID of my_function:", id(my_function))
print("Is my_instance an instance of MyClass?", isinstance(my_instance, MyClass))
print("Is my_instance an instance of str?", isinstance(my_instance, str))
print("Is MyClass a subclass of object?", issubclass(MyClass, object))
print("Is MyClass a subclass of str?", issubclass(MyClass, str))
print("Is my_instance callable?", callable(my_instance))
print("Is my_function callable?", callable(my_function))


# 30. WAP to inspect the program code using the functions of inspect module.

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t\t Program 30")
import inspect
class A(object):
	pass
print(inspect.isclass(A))


# 31. Write a program to create a new list containing the first letters of every 
# element in an already existing list. 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t Program 31")
a=["Ram","Shyam","Sita","Radha"]
b=[]
for i in a:
  b.append(i[0])
print(b)


# 32. Write a program using reduce() function to calculate the sum of first 10 natural numbers.

# In[ ]:


print("\t\t\t\t\t\t\t Program")
from functools import reduce
def sum_numbers(a, b):
    return a + b
numbers = range(1, 11)
sum_of_numbers = reduce(sum_numbers, numbers)
print("Sum of the first 10 natural numbers:", sum_of_numbers)


# 33. Write a program that convert a list of temperatures in Celsius into Fahrenheit 
# using map() function. 
# 

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t Program 33")
def c_to_f(c):
  return (c * 9/5) + 32
celsius_input=input("List of Temperatures in Celsius :")
celsius_list = [float(i) for i in celsius_input.split()]
fahrenheit_list = list(map(c_to_f, celsius_list))
print(fahrenheit_list)


# 34. Write a program that creates an iterator to print squares of numbers.

# In[ ]:


print("\t\t\t\t\t\t\t\t\t\t\t\t Program 34")
class Square:
    def __init__(self,limit):
        self.limit = limit
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.limit:
            result = self.current** 2
            self.current += 1
            return result
        else:
            raise StopIteration
n=int(input("Enter a number:"))
squares = Square(n)
for square in squares:
    print(square)


# 35. Write a program that create a custom iterator to create even numbers.

# In[ ]:


class EvenNumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            even_number = self.current
            self.current += 2
            return even_number
        else:
            raise StopIteration
n=int(input("Enter a number:"))
iterator = EvenNumberIterator(n)
for number in iterator:
    print(number)


# 36. Write a program to create a generator that starts counting from 0 and raise an 
# exception when counter is equal to 10. 

# In[1]:


def counter():
  i = 0
  while True:
    if i == 10:
      raise Exception("Counter reached 10")
    yield i
    i += 1
gen = counter()
for x in gen:
  print(x)


# 37. Write a program to create a generator to print the Fibonacci number. 

# In[ ]:


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Example usage:
generator = fibonacci_generator()
n=int(input("Enter a number:"))
for i in range(n):
    print(next(generator))


# 38. Write a program to create an arithmetic calculator using tkinter.

# In[2]:


from tkinter import *
root=Tk()
root.title("Calculator by Keshabkjha")
root.geometry("650x490")
root.attributes("-fullscreen",False)
entry = Entry(root,font=('sans-serif', 20, 'bold'), width=17, insertwidth = 2,bd=10,fg="black",bg="lightgrey",relief=RIDGE)
entry.grid(row=0, column=0,columnspan=5, padx=0, pady=10)
def button_click(char):
    x= entry.get()
    entry.delete(0, END)
    entry.insert(END, str(x) + str(char))

def button_clear():
    entry.delete(0, END)

def button_equal():
    result = eval(entry.get())
    entry.delete(0, END)
    entry.insert(END, result)
button1 = Button(root,text="1", padx=40, pady=20, bg="lightgrey",command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20,bg="lightgrey", command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, bg="lightgrey",command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20,bg="lightgrey", command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20,bg="lightgrey", command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20,bg="lightgrey", command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20,bg="lightgrey", command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20,bg="lightgrey", command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20,bg="lightgrey", command=lambda: button_click(9))
button10 = Button(root, text="0", padx=40, pady=20,bg="lightgrey", command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20,bg="lightgrey", command=lambda: button_click('+'))
button_subtract = Button(root, text="-", padx=40, pady=20,bg="lightgrey", command=lambda: button_click('-'))
button_multiply = Button(root, text="*", padx=40, pady=20,bg="lightgrey", command=lambda: button_click('*'))
button_divide = Button(root, text="/", padx=40, pady=20,bg="lightgrey", command=lambda: button_click('/'))
button_equal = Button(root, text="=", padx=90, pady=20,bg="bisque", command=button_equal)
button_clear = Button(root, text="Clear", padx=30, pady=20,bg="tomato", command=button_clear)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button10.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equal.grid(row=6, column=0, columnspan=3)
button_clear.grid(row=5, column=2)
root.mainloop()


# 39. Write a program to draw colored shapes (line, rectangle, oval) on canvas. 

# In[3]:


from tkinter import *
root=Tk()
root.geometry("750x500")
root.title("Drawing coloured shape on canvas")
root.attributes("-fullscreen",False)
c=Canvas(root,width=250,height=300)
line=c.create_line(108,120,320,40,fill="green")
oval=c.create_oval(80,30,140,150,fill="yellow")
rectangle=c.create_rectangle(40, 400, 80, 80, fill='grey')
c.pack(anchor=CENTER,expand=True)
root.mainloop()


# 40. Write a program to create a window that disappears automatically after 5 
# seconds. 

# In[4]:


from tkinter import *
jha=Tk()
jha.title("auto close window")
jha.geometry("750x600")
jha.after(5000,lambda:jha.destroy())
jha.mainloop()


# 41. Write a program to create a button and a label inside the frame widget. Button 
# should change the color upon hovering over the button and label should 
# disappear on clicking the button. 

# In[5]:


# Change the color upon hovering over Button in Tkinter
from tkinter import *
win= Tk()
win.title("Hovering button and hiding label")
win.geometry("750x650")
frame=Frame(win,width=700,height=500)
frame.pack()
frame.place(anchor="center",relx=0.5,rely=0.5)
label=Label(frame,text="welcome students",font=20)
label.pack(pady=24)
#Define functions
def on_enter(e):
    button.config(background='OrangeRed3', foreground= "white")

def on_leave(e):
    button.config(background= 'SystemButtonFace', foreground= 'black')
def hide_label():
    label.pack_forget()
    
button= Button(frame, text= "Click Me", font= ('Helvetica 13 bold'))
button.pack(pady= 20)

#Bind the Enter and Leave Events to the Button
button.bind('<Enter>', on_enter)      # Bind hover event
button.bind('<Leave>', on_leave)      # Bind click event
button.configure(command=hide_label)  # Bind click event
win.mainloop()


# 42. Write a program to create radio-buttons (Male, Female, and Transgender) and 
# a label. Default selection should be on Female and the label must display the 
# current selection made by user. 
# 

# In[6]:


# create radio button
from tkinter import *
win=Tk()
gender = StringVar()
gender.set("Female")  # Default selection

label = Label(win, text="Selected gender: Female")
label.pack()

def update_label():
    selected_gender = gender.get()
    label.config(text=f"Selected gender: {selected_gender}")
    

# create radio button
Radiobutton(win,text='Male',variable=gender,value="Male",command=update_label).pack()
Radiobutton(win,text='Female',variable=gender,value="Female",command=update_label).pack()
Radiobutton(win,text='Transgender',variable=gender,value="Transgender",command=update_label).pack()

mylabel=Label(win,text=gender.get())
mylabel.pack()

win.mainloop()


# 43. Write a program to display a menu on the menu bar.

# In[7]:


from tkinter import Tk,Menu
root=Tk()
menu_bar=Menu(root)
fileMenu=Menu(menu_bar,tearoff=0)
fileMenu.add_command(label="Stop",command=root.destroy)
fileMenu.add_command(label="kill",command=root.destroy)
menu_bar.add_cascade(label="File",menu=fileMenu)
root.config(menu=menu_bar)
root.mainloop()


# 44. Write a NumPy program to create an array of (3, 4) shape, multiply every 
# element value by 3 and display the new array. 
# 

# In[8]:


import numpy as np

# Create the array of shape (3, 4)
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Multiply every element by 3
new_arr = arr * 3

# Display the new array
print(new_arr)


# 45. Write a NumPy program to compute the multiplication of two given matrixes. 

# In[7]:


import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.matmul(A, B)
print(C)
#or
C = A @ B
print(C)


# 46. Write a Program to create a series from a list, numpy array and dict. 

# In[10]:


# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Create a list, a numpy array and a dictionary
listt=["keshab",11,"jha"]
mylist = list(listt)
ser1 = pd.Series(mylist)
print("Series from a list:")
print(ser1)
myarr = np.arange(11)
ser2 = pd.Series(myarr)
print("\nSeries from a NumPy array:")
print(ser2)
mydict = {'K': 11, 'E': 5, 's': 19, 'H': 8, 'a': 1,'b':2}
ser3 = pd.Series(mydict)
print("\nSeries from a dictionary:")
print(ser3)


# 47. Write a Program to convert a numpy array to a dataframe of given shape.

# In[5]:


# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Create a numpy array of 12 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Specify the shape of the dataframe (rows, columns)
shape = (4, 3)

# Reshape the array to match the shape of the dataframe
arr = arr.reshape(shape)

# Convert the array to a dataframe
df = pd.DataFrame(arr)

# Print the dataframe
print(df)


# In[ ]:





# 48. Write a program to count number of missing values in each column. 

# In[6]:


# Import pandas library
import pandas as pd
data = {
    'Column1': [1, 2, None, 4, 5],
    'Column2': [None, 2, 3, None, 6],
    'Column3': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)
# Count number of missing values in each column
missing_count = df.isnull().sum()

# Print the result
print(missing_count)


# 49. Write a program to replace missing values in a column of a dataframe by the 
# mean value of that column. 
# 

# In[19]:


# Import pandas library
import pandas as pd

# Create a sample dataframe with missing values
df = pd.DataFrame({'A': [1, 2, 3, None, 5], 'B': [6, None, 8, 9, 10]})

# Print the original dataframe
print("Original dataframe:")
print(df)
# Replace the missing values with the mean value of the corresponding column
df['A'].fillna(df['A'].mean(),inplace=True)
df['B'].fillna(df['B'].mean(),inplace=True)

# Print the updated dataframe
print("Updated dataframe:")
print(df)


# 50. Write a Pandas program to create a line plot of the opening, closing stock 
# prices of Alphabet Inc. between two specific dates. Use the 
# alphabet_stock_data.csv file to extract data.

# In[11]:


import pandas as pd
# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a dataframe
df = pd.read_csv("alphabet_stock_data.csv")

# Convert the Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Filter the dataframe by the two specific dates
start_date = "2023-04-26"
end_date = "2023-05-26"
df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Plot the opening and closing prices as line plots
plt.plot(df["Date"], df["Open"], label="Open")
plt.plot(df["Date"], df["Close"], label="Close")

# Add title, labels and legend
plt.title("Alphabet Inc. Stock Prices between {} and {}".format(start_date, end_date))
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

# Show the plot
plt.show()

