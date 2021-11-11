
import math
if __name__ == '__main__':
    s_1 = float(input('Введите площадь треугольника'))
    s_2 = float(input('Введите площадь круга'))
    a = math.sqrt(s_1 / math.sin(60))
    r_1 = s_2 / math.pi / 2
    r_2 = a / math.sqrt(3)
    if r_2 <= r_1:
        print('Треугольник вписан в окружность')
    else:
        print('Треугольник не вписан в окружность')
    r_3 = a / (2 * math.sqrt(3))
    if r_3 >= r_1:
        print('Окружность вписана в треугольник')
    else:
        print('Окружность не вписана в треугольник')
