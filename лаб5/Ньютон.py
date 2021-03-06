import math

# Задаем массив значений х
x = [0.01, 0.06, 0.11, 0.16, 0.21, 0.26, 0.31, 0.36, 0.41, 0.46, 0.51, 0.56]

# Задаем массив значений y
y = [[0 for i in range(len(x))] for j in range(len(x))]
y[0][0] = 0.991824; y[1][0] =  0.951935; y[2][0] = 0.91365; y[3][0] = 0.876905; 
y[4][0] = 0.841638; y[5][0] = 0.807789; y[6][0] = 0.775301; y[7][0] = 0.74412;
y[8][0] = 0.714193; y[9][0] = 0.68547; y[10][0] = 0.657902; y[11][0] = 0.631442;

def factorial(n):
    "Функция нахождения факториала"
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def proiz_1(xx):
    "Функция вычисления первой производной интерполяцым многочленом Ньютона"
    h = x[1] - x[0] # Вычисляем шаг
    t = (xx - x[0]) / h 

    sum = y[0][1]
    sum += ((2 * t - 1) / factorial(2)) * y[0][2]
    sum += (((3 * t ** 2 - 6 * t + 2) / factorial(3)) * y[0][3])
    sum += ((4 * t ** 3 - 18 * t ** 2 + 22 * t - 6) / factorial(4)) * y[0][4]
    sum += ((5 * t ** 4 - 40 * t ** 3 + 105 * t ** 2 - 100 * t + 24) / factorial(5)) * y[0][5]
    return sum / h

def proiz_2(xx):
    "Функция вычисления второй производной интерполяцым многочленом Ньютона"
    h = x[1] - x[0]
    t = (xx - x[0]) / h

    sum = y[0][2]
    sum += ((6 * t - 6) / factorial(3)) * y[0][3]
    sum += (((12 * t ** 2 - 36 * t + 22) / factorial(4)) * y[0][4])
    sum += ((20 * t ** 3 - 120 * t ** 2 + 210 * t - 100) / factorial(5)) * y[0][5]
    return sum / (h ** 2)

# Расчитываем значения прясых разниц 
for i in range(1, len(x)):
    for j in range(len(x) - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# for i in range(len(x)):
#     print("%.3f" %x[i], end = "\t")
#     for j in range(len(x) - i):
#         print("%.8f" %y[i][j], end = "\t")
#     print("")

print("  x   |   y    |    y'   |   y''  ")
for i in range(len(x)):
    print("", x[i], "|", "%.4f" % y[i][0], "|", "%.4f" % proiz_1(x[i]),"|", "%.4f" % proiz_2(x[i]))

