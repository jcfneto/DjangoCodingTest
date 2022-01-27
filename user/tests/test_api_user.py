import requests


USER_URL = "http://localhost:8000/user/register/"


class TestAPIEmployee:

    """To run the tests it is necessary to create a token in Django Admin."""

    # Authorization params.
    TOKEN = "bcbc09e06be7319627706090c797571da2e7a30c"
    headers = {"Authorization": f"Token {TOKEN}"}

    # Payload paramns.
    data = {
        "email": "jose@igs-software.com.br",
        "full_name": "José Carlos",
        "password": "senhaForte",
        "password_confirm": "senhaForte"
    }

    # Test funcs.
    def test_post_user(self):

        response = requests.post(url=USER_URL, headers=self.headers, data=self.data)
        assert response.status_code == 201
