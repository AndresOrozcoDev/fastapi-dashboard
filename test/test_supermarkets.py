import pytest

from main import app
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.api.services.supermarkets import SupermarketService


client = TestClient(app)

supermarketMock = {'id': 1, 'name': 'Supermarket 1'}


@pytest.fixture
def session_mock():
    with patch('app.core.db.Session', return_value=MagicMock()) as mock:
        yield mock

@pytest.fixture
def service_mock():
    with patch.object(SupermarketService, 'delete_supermarket') as mock:
        yield mock


def test_delete_supermarket_success(session_mock, service_mock):
    headers = {'API_KEY': 'development'}
    service_mock.return_value = (True, supermarketMock)
    response = client.delete('/api/supermarket/1', headers=headers)
    assert response.status_code == 200
    assert response.json() == {
        'status_code': 200,
        'message': 'Supermarket deleted',
        'data': supermarketMock
    }

def test_delete_supermarket_not_found(session_mock, service_mock):
    headers = {'API_KEY': 'development'}
    service_mock.return_value = False, None
    response = client.delete('/api/supermarket/2', headers=headers)
    assert response.status_code == 404
    assert response.json() == {
        'status_code': 404,
        'message': 'Not found supermarket',
        'data': None
    }
