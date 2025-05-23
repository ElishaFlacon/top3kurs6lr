import time
import requests


def run_github_repo_tests():
    username = ''  # Заполните своими данными
    token = ''     # Заполните своими данными
    repo_name = "TESTREPOS2asd"

    if not all([username, token, repo_name]):
        print("Error: Required configuration values not found")
        return False

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    base_url = 'https://api.github.com'

    api_data = {
        "username": username,
        "token": token,
        "repo_name": repo_name,
        "headers": headers,
        "base_url": base_url
    }

    # Test 1: Create repository
    print(f"Test 1: Creating repository '{repo_name}'...")
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

    if create_response.status_code != 201:
        print(f"Failed to create repository: {create_response.text}")
        return False
    else:
        print("Repository created successfully")

    time.sleep(2)

    # Test 2: Verify repository
    print(f"Test 2: Verifying repository '{repo_name}'...")
    verify_url = f"{api_data['base_url']}/repos/{api_data['username']}/{api_data['repo_name']}"
    verify_response = requests.get(verify_url, headers=api_data['headers'])

    if verify_response.status_code != 200:
        print(f"Failed to verify repository: {verify_response.text}")
        return False

    repo_info = verify_response.json()
    if repo_info['name'] != api_data['repo_name']:
        print(
            f"Repository name mismatch. Expected: {api_data['repo_name']}, Actual: {repo_info['name']}")
        return False
    else:
        print("Repository verified successfully")

    # Test 3: Delete repository
    print(f"Test 3: Deleting repository '{repo_name}'...")
    delete_url = f"{api_data['base_url']}/repos/{api_data['username']}/{api_data['repo_name']}"
    delete_response = requests.delete(delete_url, headers=api_data['headers'])

    if delete_response.status_code != 204:
        print(f"Failed to delete repository: {delete_response.text}")
        return False
    else:
        print(f"Repository '{api_data['repo_name']}' was successfully deleted")

    print("All tests passed successfully!")
    return True


if __name__ == "__main__":
    run_github_repo_tests()
