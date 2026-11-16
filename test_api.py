import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
created_post_id = None


def test_api1_get_user_by_id():
    #API-01: Получение пользователя GET /users/1.
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1
    assert user["username"] == "Bret"


def test_api2_get_nonexistent_user():
    #API-2: Запрос несуществующего пользователя GET /users/99999.
    response = requests.get(f"{BASE_URL}/users/99999")

    assert response.status_code == 404


def test_api3_create_post():
    #API-3: Создание нового поста POST /posts.
    global created_post_id

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
    created_post_id = post["id"]


def test_api4_delete_post():
    #API-4: Удаление поста, созданного в API-3.
    assert created_post_id is not None
    response = requests.delete(f"{BASE_URL}/posts/{created_post_id}")

    assert response.status_code == 200
