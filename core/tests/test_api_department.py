import requests


DEPARTMENT_URL = "http://localhost:8000/department/"


class TestAPIDepartment:

    """To run the tests it is necessary to create a token in Django Admin."""

    # Authorization params.
    TOKEN = "bcbc09e06be7319627706090c797571da2e7a30c"
    headers = {"Authorization": f"Token {TOKEN}"}

    # Payload param.
    data = {
        "name": "Tech",
        "created_at": "2022-01-01"
    }

    # Test funcs.
    def test_post_department(self):

        response = requests.post(url=DEPARTMENT_URL, headers=self.headers, data=self.data)
        assert response.status_code == 201
        assert response.json()['name'] == self.data['name']

    def test_get_departments(self):

        response = requests.get(url=DEPARTMENT_URL)
        assert response.status_code == 200

    def test_get_department(self):

        last_department_id = requests.get(url=DEPARTMENT_URL).json()[-1]['id']
        response = requests.get(url=f'{DEPARTMENT_URL}{last_department_id}/')
        assert response.status_code == 200

    def test_put_department(self):

        data = {
            "name": "Tech",
            "created_at": "2022-02-01"
        }
        last_department_id = requests.get(url=DEPARTMENT_URL).json()[-1]['id']
        response = requests.put(url=f'{DEPARTMENT_URL}{last_department_id}/', headers=self.headers, data=data)
        assert response.status_code == 200
        assert response.json()['name'] == data['name']

    def test_delete_department(self):

        last_department_id = requests.get(url=DEPARTMENT_URL).json()[-1]['id']
        response = requests.delete(url=f'{DEPARTMENT_URL}{last_department_id}/', headers=self.headers)
        assert response.status_code == 200
