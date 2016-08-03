#!/usr/bin/env python

# views.py
def basic_addition(num1, num2):

    the_sum = num1 + num2

    print the_sum
    
    return the_sum

def basic_subtraction(num1, num2):

    the_sum = num1 - num2

    print the_sum

    return the_sum

# urls.py
# url(r'basic_addition/(?P<pk>\d+)', 'def_class.basic_addition'),

basic_addition(5,2)

basic_subtraction(10,5)

# models.py
class Shape: 
    area = 25

class Rectangle(Shape):
    sides = 4
    width = 5
    height = 5

    def area(self):
        new_area = self.width * self.height

        self.area = new_area

        return new_area

class Triangle(Shape):
    sides = 3
    
    side1_width = 3
    side2_width = 6
    side3_width = 3

    def area(self):
        

# class State:
#     name = 

# # import_stuff.py

# new_rect = Rectangle()

# new_rect.width = 10

# new_rect.height = 8

# print new_rect.area()

# rect2 = Rectangle()

# rect2.width = 20
# rect2.height = 15

# print rect2.area()
# print new_rect.area

# new_shape = Shape()

# new_shape.area = 30

# print new_shape.area

# new_rect = Rectangle()

# print new_rect.sides
# print new_rect.width
# print new_rect.height

