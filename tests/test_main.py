import requests
from main import size_input, post_data, main


# вспомогательный класс для подмены ответа сервера
class Response:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self._json_data = json_data or {}

    def json(self):
        return self._json_data


# тест 1
def test_valid_number_input(monkeypatch):
    # подмена ввода
    monkeypatch.setattr("builtins.input", lambda _: "4")
    result = size_input()
    assert result == 4


# тест 2
def test_invalid_number_input(monkeypatch, capsys):
    inputs = iter(["abc", "-1", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = size_input()
    # перехват вывода (print)
    captured = capsys.readouterr()

    assert "Недопустимый ввод, повторите попытку" in captured.out
    assert "Ввод должен быть больше 0!" in captured.out
    assert result == 2


# тест 3
def test_server_status_200(monkeypatch):
    # подмена requests.post
    expected_matrix = [[1, 4], [2, 5], [3, 6]]
    monkeypatch.setattr(
        requests,
        "post",
        lambda *args, **kwargs: Response(200, {"matrix": expected_matrix}),
    )

    result = post_data(
        "http://localhost:5001/transpose",
        [[1, 2, 3], [4, 5, 6]],
        "matrix_processing.py",
        get=1,
    )
    assert result == expected_matrix


# тест 4
def test_missing_module_error(monkeypatch, capsys):
    def raise_connection_error(*args, **kwargs):
        raise requests.exceptions.ConnectionError()  # принудительная генерация исключений

    monkeypatch.setattr(requests, "post", raise_connection_error)

    post_data(
        "http://localhost:5001/transpose",
        [[1, 2], [3, 4]],
        "matrix_processing.py",
        get=1,
    )

    captured = capsys.readouterr()
    assert "Модуль matrix_processing.py не отвечает" in captured.out


# тест 5
def test_main_full_cycle(monkeypatch, capsys):
    inputs = iter(["1", "1", "abc", "5", "х", "н"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(
        requests,
        "post",
        lambda *args, **kwargs: Response(200, {"matrix": []}),
    )

    main()

    captured = capsys.readouterr()
    assert "Ввод должен быть вещественным числом" in captured.out
    assert "Такого варианта ответа нет" in captured.out


# тест 6
def test_main_full_cycle_repeat(monkeypatch):
    """ТК-16 (Белый ящик): Покрытие ветки повторного запуска цикла ('Д')."""
    inputs = iter(["1", "1", "5", "Д", "1", "1", "9", "н"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(
        requests,
        "post",
        lambda *args, **kwargs: Response(200, {"matrix": []}),
    )

    main()
