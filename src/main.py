try:
    import requests
except:
    print("Критическая ошибка")
else:
    run = True
    while run:
        # создание матрицы
        matrix = None
        try:
            response_input = requests.get(
                'http://localhost:5000/input'
            )
            if response_input.status_code == 200:
                matrix = response_input.json().get('matrix')
            else:
                print("Ошибка ввода")
        except requests.exceptions.ConnectionError:
            print("Модуль ввода matrix_input.py не отвечает")

        # отправка запроса на транспонирование
        t_matrix = None
        try:
            response_proc = requests.post(
                'http://localhost:5001/transpose',
                json={'matrix': matrix}, 
                timeout=5
            )
            if response_proc.status_code == 200:
                t_matrix = response_proc.json().get('transposed_matrix')
            else:
                print("Ошибка транспонирования")
        except requests.exceptions.ConnectionError:
            print("Модуль транспонирования matrix_processing.py не отвечает")

        # отправка запроса на вывод результата
        try:
            response_out = requests.post(
                'http://localhost:5002/output',
                json={'matrix': t_matrix}, 
                timeout=5
            )
            if response_out.status_code != 200:
                print("Ошибка вывода результата")
        except requests.exceptions.ConnectionError:
            print("Модуль вывода результата matrix_output.py не отвечает")
        

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
