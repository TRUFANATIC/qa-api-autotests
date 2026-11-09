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
    """TC-04: Создание поста и удаление его по полученному id."""
    payload = {
        "title": "Post to delete",
        "body": "Created for TC-04 delete flow",
        "userId": 1,
    }

    create_response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert create_response.status_code == 201

    post_id = create_response.json()["id"]
    assert post_id is not None

    delete_response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert delete_response.status_code == 200
