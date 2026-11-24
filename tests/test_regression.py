from main import size_input
from matrix_processing import app as processing_app
from matrix_output import app as output_app


# тест 1
# проверка исправления ошибки при json=None
def test_none_json():
    with processing_app.test_client() as p_client, output_app.test_client() as o_client:
        r1 = p_client.post("/transpose", json=None)
        r2 = o_client.post("/output", json=None)

        assert r1.status_code == 400
        assert r2.status_code == 400


# тест 2
# проверка исправления логической ошибки при вводе некорректного значения
def test_size_input(monkeypatch):
    inputs = iter(["0", "-5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert size_input() == 3
