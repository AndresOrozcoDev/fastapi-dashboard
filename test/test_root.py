from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)

def test_read_root():
    headers = {'api-key': 'development'}
    response = client.get('/', headers=headers)
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}