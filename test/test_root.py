from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)

def test_read_root():
    headers = {'API_KEY': 'development'}
    response = client.get('/', headers=headers)
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}