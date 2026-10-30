try:
    from flask import Flask, request, jsonify
except:
    print("Критическая ошибка")
else:

    app = Flask(__name__)

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

    # функция для расчета наиболее длинного элемента (для ровного столбика)
    def max_length(n, m, matrix):
        lens = []
        for i in range(n):
            for j in range(m):
                lens.append(len(str(matrix[i][j])))
        maxlen = max(lens)
        return maxlen


    # вывод 
    @app.route('/output', methods=['POST'])
    def matrix_output():
        data = request.get_json()
        if data:
            t_matrix = data.get('matrix')
        else:
            t_matrix = None
    
        if t_matrix is None:
            return jsonify({'error': 'Матрица отсутствует'}), 400
        
        n, m = get_n_m(t_matrix)
        maxlen = max_length(n, m, t_matrix) + 2

        print("Транспонированная матрица ->")
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
    
        return jsonify({'status': 'Успешно выведено'}), 200

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5002)
