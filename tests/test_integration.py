import requests
from main import main

# тестовые клиенты тут, тк без этого возникает ошибка в тесте (конфликты при закрытии)
from matrix_processing import app as processing_app
from matrix_output import app as output_app


# вспомогательный класс для подмены ответа сервера
class Response:
    def __init__(self, flask_response):
        self.status_code = flask_response.status_code
        self._data = flask_response.get_json()

    def json(self):
        return self._data


def test_integration(monkeypatch, capsys):
    proc_client = processing_app.test_client()
    out_client = output_app.test_client()

    def route_post(url, json=None, timeout=5):
        if "5001/transpose" in url:
            resp = proc_client.post("/transpose", json=json)
        elif "5002/output" in url:
            resp = out_client.post("/output", json=json)
        else:
            raise requests.exceptions.ConnectionError()

        return Response(resp)

    user_inputs = iter(["2", "3", "1", "2", "3", "4", "5", "6", "н"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    monkeypatch.setattr(requests, "post", route_post)

    main()

    captured = capsys.readouterr()
    assert "Транспонированная матрица ->" in captured.out
    assert "| 1.0  4.0  |" in captured.out
    assert "| 2.0  5.0  |" in captured.out
    assert "| 3.0  6.0  |" in captured.out
