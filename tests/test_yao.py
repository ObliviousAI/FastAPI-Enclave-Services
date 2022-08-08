from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# appending headers in place of the proxy
# acting as ACL proxy
headers = [
    {"X-OBLV-USER-NAME": "Alice"},
    {"X-OBLV-USER-NAME": "Bob"}
]

params = [
    {"value": 5},
    {"value": 6}
]

def test_settings():
    response = client.get(
        "/yao/submit_value",
        headers = headers[0],
        params = params[0]
    )

    response = client.get(
        "/yao/submit_value",
        headers = headers[1],
        params = params[1]
    )

    response = client.get(
        "/yao/compare",
        headers = headers[0]
    )

    assert response.content.decode("utf-8") == f'"Alice < Bob"'