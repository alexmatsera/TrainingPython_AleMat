#!/usr/bin/env python
# coding: utf-8

# Task 1:
# Create a script that can calculate squares of the next geometric figures:
# circle, rectangle triangle(with an angle 90 degrees), rectangle
import math
r =  int (input("Введіть радіус кола: "))     # here you should set the raduis of the circle
a =  int (input("Введіть меньшу сторону прямокутника (прямокутного трикутника): "))     # here you should set the first side of the rectangle
b: int =  int (input("Введіть більшу сторону прямокутника (прямокутного трикутника): "))     # here you should set the second side of the rectangle

circle_square = math.pi*(r**2)     # here you should define a formula of the circle
rec_triangle_square = (a * b)/2  # here you should define a formula of the rectangle triangle
rectangle_square = (a * b)      # here you should define a formula of the rectangle

print(f'Circle: r={r}, S={circle_square}')
print(f'Rectangle triangle: a={a}, b={b}, S={rec_triangle_square}')
print(f'Rectangle: a={a}, b={b}, S={rectangle_square}')