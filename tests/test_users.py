from flask import url_for
import pytest
from flask import url_for

def test_users_response(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json.keys()) == 2
    assert set(response.json) - set(["data", "total_items"]) == set()


@pytest.mark.parametrize('id', [1, 2])
def test_users_response_search(client, id):
    response = client.get(f"/users/{id}")
    assert response.status_code == 200

    assert len(response.json.keys()) == 8 

    compare_keys = set(response.json) - set(["id", "name", "username", "email", "address", "phone", "website", "company"])
    assert compare_keys == set() 


@pytest.mark.parametrize('id', [1, 2, 11, 400])
def test_tasks_response_search_data(client, id):

    response = client.get(f"/users/{id}/tasks")
    
    if response.status_code == 200:
        assert len(response.json["data"]) > 0
    else:
        assert response.json == []
