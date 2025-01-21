import json
# import os
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


# Абстрактный класс для хранения вакансий
class AbstractStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict):
        pass

    @abstractmethod
    def remove_vacancy(self, title: str):
        pass


# Класс для хранения вакансий в JSON-файле
class JSONStorage(AbstractStorage):
    def __init__(self, filename: str):
        self.filename = filename
        self.vacancies = []
        self._load()

    def _load(self):
        """Загружает вакансии из JSON-файла. Если файл не найден, инициализирует пустой список вакансий"""

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.vacancies = [Vacancy(**item) for item in json.load(f)]
        except FileNotFoundError:
            self.vacancies = []

    def _save(self):
        """Сохраняет текущий список вакансий в JSON-файл"""

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                [vacancy.to_dict() for vacancy in self.vacancies],
                f,
                ensure_ascii=False,
                indent=4,
            )

    def add_vacancy(self, vacancy: Vacancy):
        """Метод для добавления новой вакансии в хранилище. Сначала валидирует вакансию, затем добавляет её в список
        и сохраняет изменения в файле"""

        vacancy.validate()
        self.vacancies.append(vacancy)
        self._save()

    def get_vacancies(self, criteria: dict):
        """Метод для получения списка вакансий, соответствующих указанным критериям. Возвращает вакансии, которые
        удовлетворяют всем параметрам в словаре критериев"""

        return [
            vacancy
            for vacancy in self.vacancies
            if all(getattr(vacancy, k) == v for k, v in criteria.items())
        ]

    def remove_vacancy(self, title: str):
        """Метод для удаления вакансии из хранилища по заданному заголовку. После удаления обновляет сохранённый файл
        с текущим списком вакансий"""

        self.vacancies = [
            vacancy for vacancy in self.vacancies if vacancy.title != title
        ]
        self._save()
