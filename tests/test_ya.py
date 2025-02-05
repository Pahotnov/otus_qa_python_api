import requests


def test_address(base_url, status_code):
    headers = {"Content-Type": "application/json"}
    response = requests.get(url=base_url, headers=headers)
    assert response.status_code == int(status_code)
