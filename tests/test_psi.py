from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# appending headers in place of the proxy
# acting as ACL proxy
headers = [
    {"X-OBLV-USER-NAME": "Alice"},
    {"X-OBLV-USER-NAME": "Bob"}
]

def test_settings():
    response = client.post(
        "/psi/submit_list",
        headers = headers[0],
        files = {'csv_file': open('tests/data/psi/alice.csv','rb')}
    )

    response = client.post(
        "/psi/submit_list",
        headers = headers[1],
        files = {'csv_file': open('tests/data/psi/bob.csv','rb')}
    )

    response = client.get(
        "/psi/compare",
        headers = headers[0]
    )

    assert response.content.decode("utf-8") == '"Alice and Bob have 5 values in common"'