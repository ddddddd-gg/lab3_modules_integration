# модуль обработки

# создание пустой матрицы
def e_matrix_create(n, m):
    e_matrix = []
    for i in range(n):
        e_matrix.append(list())
        for j in range(m):
            e_matrix[i].append(0)
    return e_matrix    # возвращем пустую (заполненную нулями) матрицу


# получение количества строк и столбцов 
def get_n_m(matrix):
    n = 0
    m = 0
    for sublist in matrix:
        n += 1
        for items in sublist:
            m += 1
    m = int(m/n)
    return (n, m)    #возвращаем размерность матрицы


# транспонирование матрицы
def matrix_transpose(matrix):
        n, m = get_n_m(matrix)
        t_matrix = e_matrix_create(m, n)
        for i in range(n):
            for j in range(m):
                t_matrix[j][i] = matrix[i][j]
        return t_matrix    # возвращаем транспонированную матрицу