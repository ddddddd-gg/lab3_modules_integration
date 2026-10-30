# ввод размерности
from flask import Flask, jsonify

app = Flask(__name__)


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


# ввод размерности
def size_input():
    x = 0
    while x < 1:
        x = input('Введите целое положительно число: ')
        try:
            x =  float(x)
        except:
            print("Недопустимый ввод, повторите попытку")
            x = 0
            continue
        else:
            x = round(x)
            if x < 1:
                print('Ввод должен быть больше 0!')
        return x

# ввод элементов матрицы
def elements_input():
    x = 0
    crct = True

    while(crct):
        x = input("Введите число: ")
        try:
            x = float(x)
        except:
            print("Ввод должен быть вещественным числом, повторите попытку")
        else:
            break
    return x


# заполнение матрицы
def matrix_filling(e_matrix, n, m):
    for i in range(n):
        print(f"Введите элементы для {i+1} строки")
        for j in range(m):
            e_matrix[i][j] = elements_input()
    return e_matrix    # возвращаем заполненную матрицу


# создание матрицы
@app.route('/input', methods=['GET'])
def matrix_create():
    print("*Размер матрицы задается в виде целого положительного числа")
    print("Введите количество строк ->")
    n = size_input()
    print("Введите количество столбцов ->")
    m = size_input()
    
    e_matrix = e_matrix_create(n, m)
    matrix = matrix_filling(e_matrix, n, m)

    if matrix is None:
        return jsonify({'error': 'Данные матрицы отсутствуют'}), 400
    else: 
        return jsonify({'matrix': matrix}), 200

if __name__ == '__main__':
    app.run(port=5000)
