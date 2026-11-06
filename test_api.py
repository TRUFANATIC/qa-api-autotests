import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_by_id():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["username"] == "Bret"

def test_create_new_post():
    payload = {"title": "QA AutoTest", "body": "Testing API with pytest", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "QA AutoTest"
