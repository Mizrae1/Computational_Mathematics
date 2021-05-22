import math
from sympy import *

x = Symbol("x")
y = Symbol("y")

def func(x, y):
	"Задаем данную функцию"
	return round(1 + (1 - x) * math.sin(y) - (2 + x) * y, 4) 

# Задаем начальные данные 
h = 0.1 
x = []
y = [0]
yi = [0]

# Считаем первые 3 значения функции метод Рунге-Кутты 
def rungeKutte(x, y):
	k1 = func(x, y)
	k2 = func(x + h / 2, y + (h * k1) / 2)
	k3 = func(x + h / 2, y + (h * k2) / 2)
	k4 = func(x + h, y + (h * k3))
	return y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Считаем остольные значения функции метод Адамса 
def adams(x, y, i):
	return y[i-1] + h / 24 * (55 * func(x[i-1],y[i-1]) - 59 * func(x[i-2],y[i-2]) + 37 * func(x[i-3],y[i-3]) - 9 * func(x[i-4],y[i-4]))

# Считаем значения функции метод Эйлера с пересчетом 
def euler(x, y, X):
	Y = y + h * func(x, y)
	return y + 0.5 * h * (func(x, y) + func(X, Y))	

# Считаем значения х с шагом h 
for i in range(11):
	x.append(i * h)

print("Adams:")
for i in range(1,4):
	y.append(rungeKutte(x[i-1], y[i-1]))
	print("The value at", "%.1f" % x[i], "is", "%.4f" % y[i])

for i in range(4,11):
	y.append(adams(x, y, i))
	print("The value at", "%.1f" % x[i], "is", "%.4f" % y[i])

print("Euler recalculation:")
for i in range(1,11):
	yi.append(euler(x[i-1], yi[i-1], x[i]))
	print("The value at", "%.1f" % x[i], "is", "%.4f" % yi[i])


