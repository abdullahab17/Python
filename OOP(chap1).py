from datetime import datetime
from math import sqrt
# class Employee:
#     # Create __init__() method
#     def __init__(self, name, salary=0):
#         # Create the name and salary attributes
#         self.name = name
#         self.salary = salary
#
#     # From the previous lesson
#     def give_raise(self, amount):
#         self.salary += amount
#
#     def monthly_salary(self):
#         return self.salary / 12
#
#
# emp = Employee("Korel Rossi")
# print(emp.name)
# print(emp.salary)
#
# class Employee:
#
#     def __init__(self, name, salary=0):
#         self.name = name
#         # Modify code below to check if salary is positive
#         if salary > 0:
#             self.salary = salary
#         else:
#             self.salary = 0
#             print("Invalid Salary")
#
#         # ...Other methods omitted for brevity ...
#
#
# emp = Employee("Korel Rossi", -1000)
# print(emp.name)
# print(emp.salary)

# class Employee:
#
#     def __init__(self, name, salary=0):
#         self.name = name
#         if salary > 0:
#             self.salary = salary
#         else:
#             self.salary = 0
#             print("Invalid salary!")
#
#         # Add the hire_date attribute and set it to today's date
#         self.hire_date = datetime.today()
#
#
# # ...Other methods omitted for brevity ...
#
# emp = Employee("Korel Rossi", -1000)
# print(emp.name)
# print(emp.salary)

# Write the class Point as outlined in the instructions
from math import sqrt
class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def distance_to_origin(self):
        sq= sqrt(self.x **2 + self.y**2)
        return sq
    def reflect(self,axis):
        self.axis=axis
        if axis == 'x':
            self.y =- self.y
        else:
            self.x = - self.x
pt=Point(x=3.0)
pt.reflect('y')
print((pt.x,pt.y))
pt.y=4
print(pt.distance_to_origin())