
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# appending headers in place of the proxy
# acting as ACL proxy
headers = {
    "X-OBLV-USER-NAME": "Alice",
    "X-OBLV-USER-ROLE": "admin",
}

def test_settings():
    response = client.get(
        "/hello",
        headers = headers
    )

    assert response.content.decode("utf-8") == \
        f'"Hello {headers["X-OBLV-USER-NAME"]}, your role is {headers["X-OBLV-USER-ROLE"]}"'
