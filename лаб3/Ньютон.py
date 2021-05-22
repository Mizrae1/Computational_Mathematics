
def factorial(n):
    "Функция нахождения факториала"
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def t_cal1(t, n):
    "Функция расчета t * (t - i)"
    temp = t
    for i in range(1, n):
        temp = temp * (t - i)
    return temp

def t_cal2(t, n):
    "Функция расчета t * (t + i)"
    temp = t
    for i in range(1, n):
        temp = temp * (t + i)
    return temp

# Задаем массив значений х
x = [1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.37, 1.375, 1.380, 1.385, 1.390, 1.395, 1.400]

# Задаем массив значений y
y = [[0 for i in range(len(x))] for j in range(len(x))]
y[0][0] = 4.25562; y[1][0] = 4.35325; y[2][0] = 4.45522; y[3][0] = 4.56184; 
y[4][0] = 4.67344; y[5][0] = 4.79038; y[6][0] = 4.91306; y[7][0] = 5.04192;
y[8][0] = 5.17744; y[9][0] = 5.32016; y[10][0] = 5.47069; y[11][0] = 5.62968; y[12][0] = 5.76999;

# Задаем массив значений аргумента 
value = [1.32, 1.345, 1.353, 1.388, 1.41]

print("Интерполяция многочленом Ньютона:")
g = 0
# Расчитываем значения прясых разностей 
for i in range(1, len(x)):
    for j in range(len(x) - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# Выводи таблицы значений х, y и прямых разностей 

for i in range(len(x)):
    print("%.3f" %x[i], end = "\t")
    for j in range(len(x) - i):
        print("%.3f" %y[i][j], end = "\t")
    print("")
    
while g in range(len(value)):
    if g <= len(value) / 2:    # Принятие решения какую формулу Ньютона использовать
        sum = y[0][0]
        t = (value[g] - x[0]) / (x[1] - x[0]) # Считаем t = (x - x0) / h 
        # Цикл для нахождения расчета значения в точке
        for i in range(1,len(x)):
            sum += (t_cal1(t, i) * y[0][i]) / factorial(i)

    else:
        sum = y[len(x) - 1][0]
        t = (value[g] - x[len(x) - 1]) / (x[1] - x[0])
        for i in range(1,len(x)):
            sum = sum + (t_cal2(t, i) * y[len(x) - (i+1)][i]) / factorial(i)


    print("Значение в узле", value[g], "равно", round(sum, 5))
    g += 1
  