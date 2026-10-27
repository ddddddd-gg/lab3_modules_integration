# модуль вывода
try:
    import matrix_processing
except:
    pass



# функция для расчета наиболее длинного элемента (для ровного столбика)
def max_length(n, m, matrix):
    lens = []
    for i in range(n):
        for j in range(m):
            lens.append(len(str(matrix[i][j])))
    maxlen = max(lens)
    return maxlen

# вывод
def matrix_output(matrix):
    try:
        t_matrix = matrix_processing.matrix_transpose(matrix)
        n, m = matrix_processing.get_n_m(t_matrix)
    except:
        print("Критическая ошибка, модуль matrix_processinh.py не найден")
    else:
        maxlen = max_length(n, m, t_matrix) + 2
        for i in range(n):
            line = ""
            for j in range(m):
                if j == 0:
                    line += "| "
                if n > 1:
                    d = int(maxlen - len(str(t_matrix[i][j])))
                else:
                    d = 1
                line += str(t_matrix[i][j]) + d*" " 
                if j == m-1:
                    line += "|"
            print(str(line))
