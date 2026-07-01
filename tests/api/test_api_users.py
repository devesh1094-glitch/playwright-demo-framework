import pytest
from utils.config import Config


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_user_returns_200_and_correct_id(api_client):
    response = api_client.get(f"{Config.api_base_url()}/users/2")
    assert response.status_code == 200

    body = response.json()
    assert body["data"]["id"] == 2
    assert "email" in body["data"]


@pytest.mark.api
def test_get_nonexistent_user_returns_404(api_client):
    response = api_client.get(f"{Config.api_base_url()}/users/23")
    assert response.status_code == 404


@pytest.mark.api
def test_create_user_returns_201_with_expected_payload(api_client):
    payload = {"name": "Devesh", "job": "Senior QA Engineer"}
    response = api_client.post(f"{Config.api_base_url()}/users", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body and "createdAt" in body


@pytest.mark.api
@pytest.mark.parametrize("page_num", [1, 2])
def test_list_users_pagination(api_client, page_num):
    response = api_client.get(f"{Config.api_base_url()}/users", params={"page": page_num})
    assert response.status_code == 200
    body = response.json()
    assert body["page"] == page_num
    assert len(body["data"]) > 0
