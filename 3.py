import math

x = float(input())
y = float(input())
R1 = float(input())
R2 = float(input())

r = math.sqrt(x ** 2 + y ** 2)

if R1 < r < R2:
    print("Принадлежит")
else:
    print("Не принадлежит")
