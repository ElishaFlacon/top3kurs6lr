import os
import time

from dotenv import load_dotenv
import requests
import pytest


@pytest.fixture(scope="module")
def api_data():
    load_dotenv()

    username = os.getenv('GITHUB_USERNAME')
    token = os.getenv('GITHUB_TOKEN')
    repo_name = "TESTREPOS2"

    if not all([username, token, repo_name]):
        pytest.fail("Required environment variables not found")

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    base_url = 'https://api.github.com'

    return {
        "username": username,
        "token": token,
        "repo_name": repo_name,
        "headers": headers,
        "base_url": base_url
    }


def test_create_repository(api_data):
    create_url = f"{api_data['base_url']}/user/repos"
    create_data = {
        'name': api_data['repo_name'],
        'description': 'Test repository created via API',
        'private': False
    }

    create_response = requests.post(
        create_url,
        headers=api_data['headers'],
        json=create_data
    )

    assert create_response.status_code == 201, f"Ошибка создания репозитория: {create_response.text}"

    time.sleep(2)


def test_verify_repository(api_data):
    verify_url = f"{api_data['base_url']}/repos/{api_data['username']}/{api_data['repo_name']}"
    verify_response = requests.get(verify_url, headers=api_data['headers'])

    assert verify_response.status_code == 200, f"Ошибка проверки репозитория: {verify_response.text}"
    repo_info = verify_response.json()
    assert repo_info['name'] == api_data['repo_name'], f"Ошибка проверки репозитория названия не совпадают"


def test_delete_repository(api_data):
    delete_url = f"{api_data['base_url']}/repos/{api_data['username']}/{api_data['repo_name']}"
    delete_response = requests.delete(delete_url, headers=api_data['headers'])

    assert delete_response.status_code == 204, f"Ошибка удаления репозитория: {delete_response.text}"
    print(f"Репозиторий '{api_data['repo_name']}' был успешно удален")
