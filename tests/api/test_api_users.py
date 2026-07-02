import pytest
from utils.config import Config


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_user_returns_200_and_correct_id(api_client):
    response = api_client.get(f"{Config.api_base_url()}/users/2")
    assert response.status_code == 200

    body = response.json()
    assert body["id"] == 2
    assert "email" in body


@pytest.mark.api
def test_get_nonexistent_user_returns_404(api_client):
    response = api_client.get(f"{Config.api_base_url()}/users/999")
    assert response.status_code == 404


@pytest.mark.api
def test_create_post_returns_201_with_expected_payload(api_client):
    payload = {"title": "Devesh QA Post", "body": "Senior QA Engineer test", "userId": 1}
    response = api_client.post(f"{Config.api_base_url()}/posts", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2])
def test_get_user_posts(api_client, user_id):
    response = api_client.get(f"{Config.api_base_url()}/posts", params={"userId": user_id})
    assert response.status_code == 200
    body = response.json()
    assert len(body) > 0
    assert all(post["userId"] == user_id for post in body)