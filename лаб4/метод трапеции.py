import math
import cmath
from sympy import *

x = Symbol("x")

# def func(x):
#     "Задаем данную функцию"
#     return log(x ** 2 + 3) / (2 * x)

def func(x):
    "Задаем данную функцию"
    return math.sin(x) / sqrt(1 - x ** 2) * math.exp(-1 - x)

# def proiz_2(x):
#     return -(2 * math.cos(x) + (-1 + 3 * x ** 2 / (-1 + x ** 2)) * math.sin(x) / (1 - x ** 2) + 2 * x * (-math.cos(x) + math.sin(x)) / (1 - x ** 2)) * math.exp(-1 - x) / sqrt(1 - x ** 2)

def function(z):
    "========Функция расчета f(x), f(x)' и f(x)'' ================================"
    f = lambdify(x, z, 'numpy')
    return f

y = sin(x) / sqrt(1 - x ** 2) * exp(-1 - x)
f_1 = y.diff(x) # Первая производаня
f_2 = f_1.diff(x) #Вторая производная
fz_2 = function(f_2)
a = 0.1 # Определаем заданные границы интергралла а и b 
b = 0.9
n1 = 10 # Количество разбиейний
n2 = 20

print("Интегрируемая функция: f(x) = log(x^2 + 3) / (2x)")
print("Метод трапеции")
def trapeciya( a, b, n):
    "Функция вычисляет интергал методом трапеции"
    x_proiz2 = [] # Массив для хранения данных погрешности
    result = 0
    h = (b - a) / n # Вычисляем шаг
    print("Сумма равна:")
    print("I =", h , "* ([(", " %.4f" % func(a), "+", "%.4f" % func(b), ") / 2]",  end="")  
    for i in range(n):
        if i != 0: 
            print(" +", "%.4f" % (func(a + i * h) + func(a + (i + 1) * h)), end="")
        # Считаем 1/2 * (hi * (yi-1 + y))
        result += (func(a + i * h) + func(a + (i + 1) * h))
        x_proiz2.append(fz_2(a + h * i))
        # x_proiz2.append(diff(diff(func(x))).subs(x, a + h * i))
    result = result * h / 2
    print(" ) =", "%.4f" % result)
    epsilon = ((b - a) ** 3 / (12 * n ** 2)) * abs(max(x_proiz2)) # Считаем погрешность вычислений   
    print("Результат:", "%.8f" % result)
    print("Погрешность:", epsilon)

print("При n =", n1) 
trapeciya(a, b, n1) # Функция для n = 8
# print("При n =", n2)
# trapeciya(a, b, n2) # Функция для n = 20