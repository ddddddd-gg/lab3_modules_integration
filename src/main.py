try:
    import requests
except:
    print("Критическая ошибка")
else:



    # создание пустой матрицы
    def e_matrix_create(n, m):
        e_matrix = []
        for i in range(n):
            e_matrix.append(list())
            for j in range(m):
                e_matrix[i].append(0)
        return e_matrix    # возвращем пустую (заполненную нулями) матрицу


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


    def post_data(url, data, module_name, get):    # get = 1, нужно получить данные
        try:
            response_proc = requests.post(
                url,
                json={'matrix': data}, 
                timeout=5
            )
            if response_proc.status_code == 200 and get == 1:
                return response_proc.json().get('matrix')
            else:
                print(f"Ошибка в {module_name}")
        except requests.exceptions.ConnectionError:
            print(f"Модуль {module_name} не отвечает")



    # управляющая функция
    def main():
        run = True
        while run:
            # создание матрицы
            print("*Размер матрицы задается в виде целого положительного числа")
            print("Введите количество строк ->")
            n = size_input()
            print("Введите количество столбцов ->")
            m = size_input()

            e_matrix = e_matrix_create(n, m)
            matrix = matrix_filling(e_matrix, n, m)
            

            # отправка запроса на транспонирование
            t_matrix = post_data('http://localhost:5001/transpose', matrix, "matrix_processing.py", 1)
            

            # отправка запроса на вывод результата
            post_data('http://localhost:5002/output', t_matrix, "matrix_output.py", 0)
        

            # запрос на повторный запуск
            answ = ""
            while (answ != 'Д' and answ != 'д' and answ != 'Н' and answ != 'н'):
                answ = input("\nПовторить запуск?\n[Д] - да, [Н] - нет: ")
                if (answ == 'Н' or answ == 'н'):
                    run = False
                elif (answ == 'Д' or answ == 'д'):
                    run = True
                    print("\n")
                    n = 0
                    m = 0
                else:
                    print("Такого варианта ответа нет, повторите ввод")

if __name__ == '__main__':
    main()
