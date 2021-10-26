import math
s_1 = float(input('Введите площадь квадрата'))
s_2 = float(input('Введите площадь круга'))
a = math.sqrt(s_1)

if a >= (s_2 / math.pi):
    print('Круг входит в квадрат')
else:
    print('Круг не входит в квадрат')
if a * math.sqrt(2) <= (s_2 / math.pi):
    print('Квадрат входит в круг')
else:
    print('Квадрат не входит в круг')
    
