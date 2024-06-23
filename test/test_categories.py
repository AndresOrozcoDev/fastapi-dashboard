from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)

def test_create_category():
    headers = {'api-key': 'development'}
    data = {"name": "name"}
    response = client.post('/api/category', headers=headers, json=data)
    assert response.status_code == 201
    assert response.json() == {'status_code': 201, 'message': 'Category created', 'data': "name"}