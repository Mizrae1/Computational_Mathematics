import math
from sympy import *

x = Symbol("x")
y = Symbol("y")

def func(x, y):
 	return x + math.sin(y / sqrt(2)) 

def printData(x, data):
	for i in range(len(data)):
		print("The value at", "%.1f" % x[i], "is", "%.4f" % data[i])

# Задаем начальные данные 	
x = 0.8
xn = 1.8
h = 0.1
Y = 1.3
y = Y

euler = []
euler.append(Y)
euler_recal = []
euler_recal.append(y)
x_value = []
x_value.append(x)

# Цикл реализует метож Эйлера и метод Эйлера с пересчетом 
while x <= xn:
	# Считаем значение функции методом Эйлера
	Y = y + h * func(x, y)
	euler.append(Y)
	y += 0.5 * h * (func(x, y) + func(x + h, Y))
	# Пересчитываем полученное значение
	euler_recal.append(y)
	x += h
	x_value.append(x)

# Задаем данные для проверки 
x = 0.8
y = 1.3
runge_kutte = []
runge_kutte.append(y)

# Цикл реализует метод Рунге-Кутты 
while x <= xn:
	k1 = func(x, y)
	k2 = func(x + h / 2, y + (h * k1) / 2)
	k3 = func(x + h / 2, y + (h * k2) / 2)
	k4 = func(x + h, y + (h * k3))
	y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
	runge_kutte.append(y)
	x += h

print("Euler:")
printData(x_value, euler)
print("Euler recalculation:")
printData(x_value, euler_recal)
print("Runge-Kutte:")
printData(x_value, runge_kutte)



print("===================================================")
fi = []
df = []
x = 0.8
h = 0.1
y = 1.3
fi.append(func(x, y))
print("Runge-Kutte:")
for i in range (3):
	k1 = func(x, y)
	k2 = func(x + h / 2, y + (h * k1) / 2)
	k3 = func(x + h / 2, y + (h * k2) / 2)
	k4 = func(x + h, y + (h * k3))
	y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
	print("The value at", "%.1f" % x, "is", "%.4f" % y)
	x += h
	fi.append(func(x, y))
j = 0
print("Adams:")
for i in range (3, 10):
	df.append(fi[i] - fi[i - 1])
	df.append(fi[i] - 2 * fi[i - 1] + fi[i - 2])
	df.append(fi[i] - 3 * fi[i - 1] + 3 * fi[i - 2] - fi[i - 3])
	y += h * (fi[i] + (h * df[j]) / 2 + (5 * h ** 2 * df[j + 1]) / 12 + (3 * h ** 3 * df[j + 2]) / 8)
	j += 3
	x += h
	fi.append(func(x, y))
	print("The value at", "%.1f" % x, "is", "%.4f" % y)