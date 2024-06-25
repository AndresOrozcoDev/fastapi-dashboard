import pytest

from main import app
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.api.services.categories import CategoriesService


client = TestClient(app)

@pytest.fixture
def session_mock():
    with patch('app.core.db.Session', return_value=MagicMock()) as mock:
        yield mock

@pytest.fixture
def service_mock():
    with patch.object(CategoriesService, 'delete_category') as mock:
        yield mock


def test_delete_category_success(session_mock, service_mock):
    headers = {'API-KEY': 'development'}
    service_mock.return_value = (True, {'id': 1, 'name': 'Category 1'})
    response = client.delete('/api/category/1', headers=headers)
    assert response.status_code == 200
    assert response.json() == {
        'status_code': 200,
        'message': 'Category deleted',
        'data': {'id': 1, 'name': 'Category 1'}
    }

def test_delete_category_not_found(session_mock, service_mock):
    headers = {'API-KEY': 'development'}
    service_mock.return_value = False, None
    response = client.delete('/api/category/2', headers=headers)
    assert response.status_code == 404
    assert response.json() == {
        'status_code': 404,
        'message': 'Not found category',
        'data': None
    }
