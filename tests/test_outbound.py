from fastapi.testclient import TestClient
from app import app

# to intercept requests
import responses

# to pattern match on query urls
import re

client = TestClient(app)

@responses.activate
def test_call():
    #intended to mock a dns timeout
    responses.add_passthru("http://192.0.2.10")

    # to catch everything not allowed (acting as DNS fails)
    responses.add(
        responses.GET,
        re.compile("http://(?!example.com|192.0.2.10).*"),
        status=301,
        headers={"Location": "http://192.0.2.10"}
    )

    # to mock the allowed url endpoint
    responses.add(
        responses.GET,
        "http://example.com",
        json={"example":"result"},
        status=200
    )

    # case where the request should pass
    response = client.get(
        "/outbound",
        params={"url": "http://example.com"},
        headers={"X-OBLV-USER-NAME": "Alice"}
    )

    assert response.status_code == 200

    # case where the request should pass
    response = client.get(
        "/outbound",
        params={"url": "http://negative_example.com"},
        headers={"X-OBLV-USER-NAME": "Alice"}
    )

    assert response.status_code != 200