from flask import url_for
import pytest
from flask import url_for

def test_tasks_response(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json.keys()) == 2
    assert set(response.json) - set(["data", "total_items"]) == set()


def test_tasks_response_search(client):
    response = client.get("/tasks?completed=True")
    assert response.status_code == 200
    
    no_completed = list(filter(lambda x: x.get("completed") == False, response.json['data']))
    assert len(no_completed) == 0


def test_tasks_response_search(client):
    response = client.get("/tasks?completed=false")
    assert response.status_code == 200
    
    no_completed = list(filter(lambda x: x.get("completed") == False, response.json['data']))
    assert len(no_completed) == 0

@pytest.mark.parametrize('id', [1, 2, 11,"Joe"])
def test_tasks_response_search_data(client, id):

    response = client.get(f"/tasks/{id}")
    
    if isinstance(id, str):
        assert response.status_code != 200
    else:
        assert response.status_code == 200 and response.json
