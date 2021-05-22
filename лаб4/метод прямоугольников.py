import math
from sympy import *
# import sympy

x = Symbol("x")

def func(x):
    "Задаем данную функцию"
    return math.sin(x) / sqrt(1 - x ** 2) * math.exp(-1 - x)

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
# print("Метод средних прямоугольников")
def prymoygolnik(a, b, n):
    "Функция вычисляет интергал методом прямоугольников"
    x_proiz2 = [] # Массив для хранения данных погрешности
    h = (b - a) / n # Вычисляем шаг
    sum =0 
    # sum = (func(a) + func(b)) / 2
    print("Сумма равна:")
    print("I =", h , "* (",  end="")  
    for i in range(n):
    	print(" +", "%.4f" % func(a + h * (i + 0.5)), end="")
    	sum += func(a + h * (i + 0.5)) # Считаем сумму f(X i - 1/2)
    	x_proiz2.append(fz_2(a + h * i))
    	# x_proiz2.append(diff(diff(func(x))).subs(x, a + h * i))
    result = h * sum # Считаем значение интегралла hi * sum(f(X i - 1/2))
    print(") =", "%.4f" % result)
    epsilon = ((b - a) ** 3 / (24 * n ** 2))  * abs(max(x_proiz2)) # Считаем погрешность вычислений 
    print("Результат:", "%.8f" % result)
    print("Погрешность:", epsilon)

print("Центральных прямоугольников")     
print("При n =", n1)    
prymoygolnik(a, b, n1) # Функция для n = 8 
print("При n =", n2)
prymoygolnik(a, b, n2) # Функция для n = 20 