import numpy as np
# Задаем начальную систему линейных уравнений
A = np.array([[0.63, 0.05, 0.15, 0.34],
              [0.05, 0.34, 0.10, 0.32],
              [0.15, 0.10, 0.71, 0.42]])

len1 = len(A[:, 0])  # Считаем количество строк матрицы
len2 = len(A[0, :])  # Счмтаем количсетво столбцов матрицы

def printArr(A, len1, len2):
    "=======Функция печати матрицы на экран===================="
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
                print(" = ", end='')
        i += 1
        print(" |")
    print()

def forwardTrace(A, len1, len2):
    "========Функция расчета системы линейных уравнений========" 
    for g in range(len1):
        print("===============================================")
        max = abs(A[g][g])         # Максимальное значение для x в столбце
        max_index = g              # Запоминает место нового максимального элемента
        t1 = g

        while t1 < len1: # Цикл поиска максимума 
            if abs(A[t1][g]) > max:
                max = abs(A[t1][g])
                max_index = t1
            t1 += 1
 
        if max_index != g:         # Меняет местами нынешнюю строку со строкой максимума
            A[g][:], A[max_index][:] = A[max_index][:], A[g][:] 
                                                  
        amain = float(A[g][g])     # Значение коэфициента перед текущим x
 
        z = g
        while z < len2:            # Цикл изменяющий значения главной диагонали на 1, при помощи деления на amain
            A[g][z] = A[g][z] / amain             
            z += 1
        printArr(A, len1, len2)

        j = g + 1
        while j < len1:                            #отнимаем строку, умноженную на коэффицент
            b = A[j][g]                            #  от следующей, в результате получаем столбец нулей.
            z = g                                  #    Глобальный цикл выполняется до тех пор, пока
            while z < len2:                        #не получатся нули в нижней треугольной матрице
                A[j][z] = A[j][z] - A[g][z] * b
                z += 1
            j += 1
        printArr(A, len1, len2)
    A = backTrace(A, len1)                         #обратный ход метода Гаусса
    return A
 
 
 
def backTrace(A, len1):
    "========Функция обратного хода============================"
    i = len1 - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            A[j][len1] = A[j][len1] - A[j][i] * A[i][len1]
            j -= 1
        i -= 1
    print("===============================================")
    return A[:, len1]
 
print(" Система уравнений:")
printArr(A, len1, len2)
b = forwardTrace(A, len1, len2)
print("Ответ:")
for i in range(len(b)):
    print("x", i+1, "=", "%.3f" % b[i])