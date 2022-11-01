# import math Library
import math

print("Укажите x: ")
x = float(input())

y = pow(pow(x, 2) + pow(math.e, math.cos(x)) + math.sin(x),
        math.sqrt(math.sin(math.pi * pow(x, 2)) + math.log(pow(x, 2))))

print("Ответ", y)
