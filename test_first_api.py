import requests
import pytest


class TestFirstAPI:
    names = [
        ("Gleb"),
        ("Konstantin"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong response status code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_result_text = "Hello, someone"
        else:
            expected_result_text = f"Hello, {name}"
        actual_result_text = response_dict.get("answer")
        assert actual_result_text == expected_result_text, "Actual text in the response in incorrect"
