import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    assert response.status_code == 200, "Ошибка получения todos"
    assert isinstance(response.json(), list), "Ответ должен быть списком"
    assert len(response.json()) > 0, "Список задач не должен быть пустым"


def test_get_todo_by_id():
    response = requests.get(f"{BASE_URL}/todos/1")
    assert response.status_code == 200, "Ошибка получения todo"
    data = response.json()
    assert "id" in data, "Ошибка получения todo"
    assert "title" in data, "Ошибка получения todo"
    assert "completed" in data, "Ошибка получения todo"
    assert data["id"] == 1, "Ошибка получения todo"


def test_create_todo():
    payload = {
        "title": "Тестовая задача",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/todos", json=payload)
    assert response.status_code == 201, "Ошибка создания todo"
    data = response.json()
    assert "id" in data, "Ошибка создания todo"
    assert data["title"] == "Тестовая задача", "Ошибка создания todo"
    assert data["completed"] is False, "Ошибка создания todo"


def test_update_todo():
    payload = {
        "title": "Обновленная задача",
        "completed": True
    }
    response = requests.put(f"{BASE_URL}/todos/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Обновленная задача", "Ошибка обновления todo"
    assert data["completed"] is True, "Ошибка обновления todo"


def test_delete_todo():
    response = requests.delete(f"{BASE_URL}/todos/1")
    assert response.status_code == 200


def test_invalid_todo_id():
    response = requests.get(f"{BASE_URL}/todos/9999")
    assert response.status_code == 404, "Ошибка несуществующего id"
    assert response.json() == {}, "Ошибка несуществующего id"


def test_invalid_payload_format():
    payload = "Это не JSON"
    response = requests.post(
        f"{BASE_URL}/todos",
        data=payload,
        headers={"Content-Type": "text/plain"}
    )
    assert response.status_code in [
        400, 201, 200
    ], "Ошибка ввода невалидных данных"
