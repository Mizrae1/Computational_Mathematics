import numpy as np 
# Задаем начальную систему линейных уравнений
A = np.array([[0.63, 0.05, 0.15],
             [0.05, 0.34, 0.10],
             [0.15, 0.10, 0.71]])

B = np.array([0.34,
              0.32, 
              0.42]) 
# Задаем точность
epsilon = 0.001 


# Печатаем матрицу 
for i in range ( len(A) ):
    print("| ", end='') 
    for j in range ( len(A[i]) ):
        if j < 3:
            print("%.2f" %A[i][j], "* x", j+1 , end='')
        else:
            print("%.2f" %A[i][j], end='')
        j += 1
        if j < 3:
            print(" + ", end='')
        if j == 3:
            print(" = ", B[i], end='')
    i += 1
    print(" |") 
print()

# Задаем начальные нулевые значение x
x = np.zeros_like(B)

for j in range(100): 
    if j != 0:
        print("Итерация", j, ":", x)
    # Создаем массив для хранений новых значений x
    x_new = np.zeros_like(x) 

    # Алгоритм Якоби
    for i in range(len(A)): 
        sum1 = A[i, :i] @ x[:i] 
        sum2 = A[i, i + 1:] @ x[i + 1:]
        x_new[i] = (B[i] - sum1 - sum2) / A[i, i] 

    # Проверка на достижение точности
    if np.allclose(x, x_new, atol=epsilon): 
        break 
    # Присваиваем x новые посчитанные значения
    x = x_new 

print("\nОтвет:")
for i in range(len(B)):
    print("x", i+1, "=", "%.3f" % x[i])
