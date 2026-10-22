import pytest
import requests



BASE_URL = "http://127.0.0.1:5000"

class TestModelAPI:
    def test_predict_returns_200(self):
        response = requests.post(f"{BASE_URL}/predict",json={'text':'这是一条测试数据'})
        assert response.status_code == 200

    def test_predict_has_required_fields(self):
        response = requests.post()