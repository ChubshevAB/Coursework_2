from abc import ABC, abstractmethod

import requests


# Абстрактный класс для API
class AbstractAPI(ABC):
    @abstractmethod
    def fetch_vacancies(self, query: str):
        pass


# Реализация API для hh.ru
class HHAPI(AbstractAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def fetch_vacancies(self, query: str):
        """Извлекает список вакансий с API hh.ru на основе указанного поискового запроса"""

        response = requests.get(self.BASE_URL, params={"text": query, "area": 113})
        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            raise Exception(f"Error fetching data from HH API: {response.status_code}")
