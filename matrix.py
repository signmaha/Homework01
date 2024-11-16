def get_matrix(n, m, value):
    matrix = []
    for i in range (n): #внешний цикл для строк
        mat = []
    for j in range (m):#внутренний цикл для столбцов
        mat.append(value)
    matrix.append(mat)
    return(matrix)

result1 = get_matrix(2, 2, 3)
result2 = get_matrix(3, 6, 15)
result3 = get_matrix(5, 12, 60)
print(result1)
print(result2)
print(result3)
