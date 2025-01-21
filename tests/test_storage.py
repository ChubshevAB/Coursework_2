import os
import pytest
import json
from src.vacancy import Vacancy
from src.storage import JSONStorage


@pytest.fixture
def temporary_json_file(tmp_path):
    """Фикстура для создания временного JSON-файла."""
    return tmp_path / "test_vacancies.json"


def test_add_vacancy(temporary_json_file):
    """Тест добавления вакансии."""
    storage = JSONStorage(temporary_json_file)

    vacancy = Vacancy(title="Программист", url="http://example.com", salary=1000,
                      description="Программирование на Python")

    storage.add_vacancy(vacancy)

    vacancies = storage.get_vacancies({})
    assert len(vacancies) == 1
    assert vacancies[0].title == "Программист"
    assert vacancies[0].salary == 1000


def test_get_vacancies(temporary_json_file):
    """Тест получения вакансий."""
    storage = JSONStorage(temporary_json_file)

    vacancy1 = Vacancy(title="Программист", url="http://example.com/1", salary=1000, description="Разработка")
    vacancy2 = Vacancy(title="Тестировщик", url="http://example.com/2", salary=800, description="Тестирование")
    storage.add_vacancy(vacancy1)
    storage.add_vacancy(vacancy2)

    vacancies = storage.get_vacancies({})
    assert len(vacancies) == 2


def test_remove_vacancy(temporary_json_file):
    """Тест удаления вакансии."""
    storage = JSONStorage(temporary_json_file)

    vacancy = Vacancy(title="Программист", url="http://example.com", salary=1000,
                      description="Программирование на Python")
    storage.add_vacancy(vacancy)

    storage.remove_vacancy(vacancy.title)

    vacancies = storage.get_vacancies({})
    assert len(vacancies) == 0
