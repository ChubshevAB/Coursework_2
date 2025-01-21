import pytest
import requests
from src.api import HHAPI


@pytest.fixture
def mock_api(monkeypatch):

    class MockResponse:
        @staticmethod
        def json():
            return {"items": [{"name": "Программист", "alternate_url": "http://example.com", "salary": {"from": 1000}}]}

        @property
        def status_code(self):
            return 200

    monkeypatch.setattr(requests, "get", lambda url, *args, **kwargs: MockResponse())


def test_fetch_vacancies_success(mock_api):
    api = HHAPI()
    vacancies = api.fetch_vacancies("Программист")

    assert len(vacancies) == 1
    assert vacancies[0]['name'] == "Программист"
    assert vacancies[0]['alternate_url'] == "http://example.com"
    assert vacancies[0]['salary']['from'] == 1000


def test_fetch_vacancies_failure(monkeypatch):
    class MockResponse:
        @property
        def status_code(self):
            return 404

    monkeypatch.setattr(requests, "get", lambda url, *args, **kwargs: MockResponse())

    api = HHAPI()

    with pytest.raises(Exception) as exc_info:
        api.fetch_vacancies("Программист")

    assert str(exc_info.value) == "Error fetching data from HH API: 404"
