import calculator
from calculator import multiply
import geometry as geo
import greeting

greeting.greet("Sachin")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

calculator.add(num1, num2)
multiply(num1, num2)

geo.cal_area_rect(num1, num2)
geo.cal_rect_peri(num1, num2)
