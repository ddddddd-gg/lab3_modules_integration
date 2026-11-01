import unittest
from unittest.mock import patch    #для подмены ввода с клавиатуры
import requests

class MatrixTranspositionTestCase(unittest.TestCase):

    # проверяет взаимодействие между клиентом и сервером ввода
    @patch('matrix_input.input')
    def test_iconnection(self, mock_x):
        self.input = 'http://localhost:5000/input'
        mock_x.return_value = 2
        response = requests.get(self.input)
        self.assertEqual(response.status_code, 200)

        

if __name__ == '__main__':
    unittest.main()