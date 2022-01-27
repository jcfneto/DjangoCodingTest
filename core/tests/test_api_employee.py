import requests


DEPARTMENT_URL = "http://localhost:8000/department/"
EMPLOYEE_URL = "http://localhost:8000/employee/"


class TestAPIEmployee:

    """To run the tests it is necessary to create a token in Django Admin."""

    # Authorization params.
    TOKEN = "bcbc09e06be7319627706090c797571da2e7a30c"
    headers = {"Authorization": f"Token {TOKEN}"}

    # Payload paramns.
    department_data = {
        "name": "Tech",
        "created_at": "2022-01-01"
    }
    employee_data = {
        "name": "Jose Carlos",
        "email": "jose@igs-software.com.br",
        "department": "1",
        "birth_date": "1994-02-25",
        "salary": "9500",
        "first_day": "2022-02-01"
    }

    # Test funcs.
    def test_post_department(self):

        response = requests.post(url=DEPARTMENT_URL, headers=self.headers, data=self.department_data)
        assert response.status_code == 201

    def test_post_employee(self):

        last_department_id = requests.get(url=DEPARTMENT_URL).json()[-1]['id']
        self.employee_data['department'] = last_department_id
        response = requests.post(url=EMPLOYEE_URL, headers=self.headers, data=self.employee_data)
        assert response.status_code == 201
        assert response.json()['name'] == self.employee_data['name']

    def test_get_employees(self):

        response = requests.get(url=EMPLOYEE_URL)
        assert response.status_code == 200

    def test_get_employee(self):

        last_employee_id = requests.get(url=EMPLOYEE_URL).json()[-1]['id']
        response = requests.get(url=f"{EMPLOYEE_URL}{last_employee_id}/")
        assert response.status_code == 200

    def test_delete_employee(self):

        last_employee_id = requests.get(url=EMPLOYEE_URL).json()[-1]['id']
        response = requests.delete(url=f"{EMPLOYEE_URL}{last_employee_id}/", headers=self.headers)
        assert response.status_code == 200

    def test_delete_department(self):

        last_department_id = requests.get(url=DEPARTMENT_URL).json()[-1]['id']
        response = requests.delete(url=f'{DEPARTMENT_URL}{last_department_id}/', headers=self.headers)
        assert response.status_code == 200
