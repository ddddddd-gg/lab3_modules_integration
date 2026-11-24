# тест 1
def test_transpose_success(processing_client):
    matrix = {"matrix": [[1, 2, 3], [4, 5, 6]]}
    response = processing_client.post("/transpose", json=matrix)
    assert response.status_code == 200
    assert response.get_json() == {"matrix": [[1, 4], [2, 5], [3, 6]]}


# тест 2
def test_transpose_empty_matrix(processing_client):
    response = processing_client.post("/transpose", json={"matrix": []})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Данные матрицы отсутствуют"}


# тест 3
def test_transpose_missing_key(processing_client):
    response = processing_client.post("/transpose", json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Данные матрицы отсутствуют"}


# тест 4
def test_transpose_none_json(processing_client):
    response = processing_client.post("/transpose", json=None)
    assert response.status_code == 400
    assert response.get_json() == {"error": "Данные матрицы отсутствуют"}
