from src.vacancy import Vacancy

def test_vacancy_initialization():
    vacancy = Vacancy(title="Программист", url="http://example.com", salary=120000, description="Разработка приложений на Python")

    assert vacancy.title == "Программист"
    assert vacancy.url == "http://example.com"
    assert vacancy.salary == 120000
    assert vacancy.description == "Разработка приложений на Python"
