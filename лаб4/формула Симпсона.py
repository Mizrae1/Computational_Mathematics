import math
from sympy import *
import pylab

x = symbols("x")

# def func(x):
#     return log(x ** 2 + 3) / (2 * x)

def func(x):
    "Задаем данную функцию"
    return math.sin(x) / sqrt(1 - x ** 2) * math.exp(-1 - x)

def function(z):
    "========Функция расчета f(x), f(x)' и f(x)'' ================================"
    f = lambdify(x, z, 'numpy')
    return f

# def proiz_2(x):
#     return -(2 * math.cos(x) + (-1 + 3 * x ** 2 / (-1 + x ** 2)) * math.sin(x) / (1 - x ** 2) + 2 * x * (-math.cos(x) + math.sin(x)) / (1 - x ** 2)) * math.exp(-1 - x) / sqrt(1 - x ** 2)

# def proiz_4(x):
#     return (-4 * math.sin(x) - ((-1 + 3 * x ** 2 / (-1 + x ** 2)) * math.sin(x) - 6 * (1 - 5 * x ** 2 / (-1 + x ** 2) + 4 * x ** 4 / (-1 + x ** 2) ** 2) * math.sin(x) / (-1 + x ** 2) + 12 * x * (-1 + x ** 2 / (-1 + x ** 2)) * math.cos(x) / (-1 + x ** 2)) / (-1 + x ** 2) - 4 * (-math.cos(x) + x * (math.cos(x) + math.sin(x)) + math.sin(x)) / (-1 + x ** 2) + 2 * (-(-1 + 3 * x ** 2 /(-1 + x ** 2)) * math.cos(x) + 6 * x * (-1 + x ** 2 / (-1 + x ** 2)) * math.sin(x) / (-1 + x ** 2)) / (-1 + x ** 2) + 2 * (2 * math.cos(x) + 2 * math.sin(x) - x * (-math.cos(x) + math.sin(x))) / (-1 + x ** 2) + (-1 + 3 * x ** 2 / (-1 + x ** 2)) * math.sin(x) / (-1 + x ** 2) - (-1 + 3 * x ** 2 / (-1 + x ** 2)) * (-2 * math.cos(x) + (-1 + 3 * x ** 2 / (-1 + x ** 2)) * math.sin(x) / (-1 + x ** 2) + 2 * x * (-math.cos(x) + math.sin(x)) / (-1 + x ** 2)) / (1 - x ** 2) - 8 * x * (-math.cos(x) + math.sin(x)) / (-1 + x ** 2) ** 2 - 4 * x * (-math.cos(x) + x * (math.cos(x) + math.sin(x)) + math.sin(x)) / (-1 + x ** 2) ** 2 - 4 * x ** 2 * (math.cos(x) + math.sin(x)) / (-1 + x ** 2) ** 2 - 2 * x * (-2 * math.cos(x) - 2 * math.sin(x) - ((-1 + 3 * x ** 2 / (-1 + x ** 2)) * cos(x) - 6 * x *(-1 + x ** "||||||||||||||||" 2/(-1 + x^2))*sin(x)/(-1 + x^2))/(-1 + x^2) - 2*(-cos(x) + x*(cos(x) + sin(x)) + sin(x))/(-1 + x^2) + (-1 + 3*x^2/(-1 + x^2))*sin(x)/(-1 + x^2) + 2*x*(-cos(x) + sin(x))/(-1 + x^2) + 4*x^2*(-cos(x) + sin(x))/(-1 + x^2)^2 + 2*x*(-1 + 3*x^2/(-1 + x^2))*sin(x)/(-1 + x^2)^2)/(1 - x^2) - 2*(-1 + 3*x^2/(-1 + x^2))*sin(x)/(-1 + x^2)^2 + 2*x*(-cos(x) + sin(x))/(-1 + x^2) + 2*x*(-(-1 + 3*x^2/(-1 + x^2))*cos(x) + 6*x*(-1 + x^2/(-1 + x^2))*sin(x)/(-1 + x^2))/(-1 + x^2)^2 + 8*x^2*(-cos(x) + sin(x))/(-1 + x^2)^2 + 16*x^3*(-cos(x) + sin(x))/(-1 + x^2)^3 - 2*x*(-1 + 3*x^2/(-1 + x^2))*cos(x)/(-1 + x^2)^2 + 4*x*(-1 + 3*x^2/(-1 + x^2))*sin(x)/(-1 + x^2)^2 + 8*x^2*(-1 + 3*x^2/(-1 + x^2))*sin(x)/(-1 + x^2)^3 + 12*x^2*(-1 + x^2/(-1 + x^2))*sin(x)/(-1 + x^2)^3)*exp(-1 - x)/sqrt(1 - x^2)

y = sin(x) / sqrt(1 - x ** 2) * exp(-1 - x)
f_1 = y.diff(x) # Первая производаня
f_2 = f_1.diff(x) #Вторая производная
f_3 = f_2.diff(x)
f_4 = f_3.diff(x)
fz_4 = function(f_4)
print(f_4)
a = 0.1 # Наши границы интегрирования
b = 0.9
n1 = 10 # Наши границы разбиения
n2 = 20

print("Интегрируемая функция: f(x) = log(x^2 + 3) / (2x)")
print("Метод Симпсона")
def simpsona(a, b, n):
    x_proiz4 = [] # Массив для хранения данных погрешности
    h = (b - a) / n # Вычисляем шаг
    sum = 0
    
    xx = a + h
    for i in range(1, round(n / 2 + 1)):
        sum += 4 * func(xx) # Выичсляем сумму нечетных функций 4(y1 + y3 + ... yn-1)
        xx += 2 * h

    xx = a + 2 * h
    for i in range(1, round(n / 2)):
        sum += 2 * func(xx) # Выичсляем сумму четных функций 2(y2 + y4 + ... yn-2)
        xx += 2 * h

    # Считаем значение интегралла (h / 3) * (y0 + 4(y1 + y3 + ... yn-1) + 2(y2 + y4 + ... yn-2) + yn)
    result = (h / 3) * (func(a) + func(b) + sum) 

    for i in range(n): 
        # x_proiz4.append(diff(diff(diff(diff(func(x))))).subs(x, a + h * i)) 
        x_proiz4.append(fz_4(a + h * i))
    epsilon = ((b - a) ** 5 / (2880 * n ** 4))  * abs(max(x_proiz4)) # Считаем погрешность вычислений

    print("Результат:", "%.8f" % result)
    print("Погрешность:",  epsilon)

print("При n =", n1)
simpsona(a, b, n1) # Функция для n = 8
# print("При n =", n2)
# simpsona(a, b, n2) # Функция для n = 20