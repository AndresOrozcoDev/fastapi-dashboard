import pytest

from main import app
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.api.services.products import ProductService


client = TestClient(app)

productMock = {
    "id": 1,
    "price": 0,
    "unit": "string",
    "supermarket_id": 1,
    "name": "string",
    "value": 0,
    "created": "2024-06-25 17:52:51.472904",
    "category_id": 1
}


@pytest.fixture
def session_mock():
    with patch('app.core.db.Session', return_value=MagicMock()) as mock:
        yield mock

@pytest.fixture
def service_mock():
    with patch.object(ProductService, 'delete_product') as mock:
        yield mock



def test_delete_product_success(session_mock, service_mock):
    headers = {'API_KEY': 'development'}
    service_mock.return_value = (True, productMock)
    response = client.delete('/api/product/1', headers=headers)
    assert response.status_code == 200
    assert response.json() == {
  "status_code": 200,
  "message": "Product deleted",
  "data": productMock
}

def test_delete_product_not_found(session_mock, service_mock):
    headers = {'API_KEY': 'development'}
    service_mock.return_value = False, None
    response = client.delete('/api/product/2', headers=headers)
    assert response.status_code == 404
    assert response.json() == {
        'status_code': 404,
        'message': 'Not found product',
        'data': None
    }
