import unittest
from urllib import response
import requests

class MatrixTranspositionTestCase(unittest.TestCase):

    # проверка доступности сервера обработки
    def test_proc_connection(self):
        self.proc_url = 'http://localhost:5001/transpose'
        try:
            response = requests.post(
                self.proc_url
                )
        except:
            print("сервер не отвечает")   # проверяем, отвечает ли сервер
        else:
            self.assertEqual(response.status_code, 405, "сервер доступен")   # проверяем, отвечает ли сервер в принципе


    # проверка доступности сервера обработки
    def test_output_connection(self):
        self.out_url = 'http://localhost:5002/output'
        try:
            response = requests.post(
                self.out_url
                )
        except:
            print("сервер не отвечает")   # проверяем, отвечает ли сервер
        else:
            self.assertEqual(response.status_code, 405, "сервер доступен")   # проверяем, отвечает ли сервер в принципе

    # проверка корректности передачи данных в модуль
    def test_proc_connection(self):
        self.out_url = 'http://localhost:5002/output'
        test_matrix = [[1, 55], [2, -4]]
        try:
            response = requests.post(
                self.out_url,
                json={'matrix':test_matrix}
                )
        except:
            print("сервер не отвечает")
        else:
            self.assertEqual(response.status_code, 200, "успешный вывод результата")   # проверяем, отвечает ли сервер в принципе

    
    # проверка возврата данных модулем обработки матрицы
    def test_proc_return(self):
        self.proc_url = 'http://localhost:5001/transpose'
        test_matrix = [[1, 55], [2, -4]]
        try:
            response = requests.post(
                self.proc_url,
                json={'matrix': test_matrix}
                )
        except:
            print("сервер не отвечает")   # проверяем, отвечает ли сервер
        else:
            self.assertEqual(response.status_code, 200, "сервер доступен и вывел результат")   # проверяем, возвращается ли значение (если main )

   

        

if __name__ == '__main__':
    unittest.main()