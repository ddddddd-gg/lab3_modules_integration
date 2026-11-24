# тест 1
def test_output_success(output_client):
    matrix = {"matrix": [[1, 2, 3], [4, 5, 6]]}
    response = output_client.post("/output", json=matrix)
    assert response.status_code == 200
    assert response.get_json() == {"status": "Успешно выведено"}


# тест 2
def test_output_empty_matrix(output_client):
    response = output_client.post("/output", json={"matrix": []})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Матрица отсутствует"}


# тест 3
def test_output_missing_key(output_client):
    response = output_client.post("/output", json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Матрица отсутствует"}


# тест 4
def test_output_none_json(output_client):
    response = output_client.post("/output", json=None)
    assert response.status_code == 400
    assert response.get_json() == {"error": "Матрица отсутствует"}


# тест 5
def test_output_dynamic_space(output_client):
    matrix = [[1, 2, 55]]
    response = output_client.post("/output", json={"matrix": matrix})

    assert response.status_code == 200
    assert response.get_json() == {"status": "Успешно выведено"}
