import requests

def test_home():
    response = requests.get("http://localhost:5001")
    assert response.status_code == 200