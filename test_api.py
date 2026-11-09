import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_tc01_get_user_by_id():
    """TC-01: Получение пользователя GET /users/1."""
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1
    assert user["username"] == "Bret"


def test_tc02_get_nonexistent_user():
    """TC-02: Запрос несуществующего пользователя GET /users/99999."""
    response = requests.get(f"{BASE_URL}/users/99999")

    assert response.status_code == 404


def test_tc03_create_post():
    """TC-03: Создание нового поста POST /posts."""
    payload = {
        "title": "QA Automation Post",
        "body": "Created by automated test",
        "userId": 1,
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    post = response.json()
    assert post["title"] == "QA Automation Post"
    assert "id" in post


def test_tc04_delete_post():
    """TC-04: Удаление поста DELETE /posts/1."""
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
