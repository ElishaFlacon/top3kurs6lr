import os
import requests
from dotenv import load_dotenv
import unittest
import time


class GitHubAPITest(unittest.TestCase):
    def setUp(self):
        load_dotenv()

        self.username = os.getenv('GITHUB_USERNAME')
        self.token = os.getenv('GITHUB_TOKEN')
        self.repo_name = "TESTREPOS2"

        if not all([self.username, self.token, self.repo_name]):
            self.fail("нет енв")

        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = 'https://api.github.com'

    def test_github_repo_operations(self):
        create_url = f"{self.base_url}/user/repos"
        create_data = {
            'name': self.repo_name,
            'description': 'Test repository created via API',
            'private': False
        }

        create_response = requests.post(
            create_url,
            headers=self.headers,
            json=create_data
        )

        self.assertEqual(
            create_response.status_code,
            201,
            f"Ошибка создания репозитория: {create_response.text}"
        )
        print(f"Репозиторий '{self.repo_name}' был создан")

        time.sleep(3)

        verify_url = f"{self.base_url}/repos/{self.username}/{self.repo_name}"
        verify_response = requests.get(verify_url, headers=self.headers)
        self.assertEqual(
            verify_response.status_code,
            200,
            f"Ошибка проверки репозитория: {verify_response.text}"
        )
        repo_info = verify_response.json()
        self.assertEqual(repo_info['name'], self.repo_name)
        print(f"Репозиторий '{self.repo_name}' существует")

        time.sleep(3)

        delete_url = f"{self.base_url}/repos/{self.username}/{self.repo_name}"
        delete_response = requests.delete(delete_url, headers=self.headers)
        self.assertEqual(
            delete_response.status_code,
            204,
            f"Ошибка удаления репозитория: {delete_response.text}"
        )
        print(f"Репозиторий '{self.repo_name}' был удален")


if __name__ == '__main__':
    unittest.main()
