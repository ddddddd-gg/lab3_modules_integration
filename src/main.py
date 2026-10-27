# лаба 3 "интегрирование модулей"
# вариант 19
# модули:
# модуль ввода - ввод размерности матрицы, создание и заполнение матрицы
# модуль транспонирования - транспонирование матрицы
# модуль вывода - вывод результата
# интеграция - нисходящая
# протокол - rest api

try:
    import matrix_input
    import matrix_output
except:
    print("Критическая ошибка")
else:
    run = True

    while (run):
        # создание матрицы
        matrix = matrix_input.matrix_create()
        if matrix == "Error":
            print("Критическая ошибка")
            run = False

        # вывод результата
        matrix_output.matrix_output(matrix) 
    
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


