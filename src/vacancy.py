class Vacancy:
    def __init__(self, title: str, url: str, salary: float, description: str):
        self._title = title
        self._url = url
        self._salary = salary
        self._description = description
        self._validate()

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def salary(self):
        return self._salary

    @property
    def description(self):
        return self._description

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def _validate(self):
        """Метод валидации для проверки корректности значений атрибутов вакансии."""
        self._validate_salary(self._salary)
        self._validate_string(self._title, "Title")
        self._validate_string(self._url, "URL")
        self._validate_string(self._description, "Description")

    def _validate_salary(self, salary):
        """Проверяет, что зарплата является числом."""
        if not isinstance(salary, (int, float)):
            raise ValueError(f"Invalid salary: '{salary}'. Salary must be a number.")

    def _validate_string(self, value, name):
        """Проверяет, что значение является строкой."""
        if not isinstance(value, str):
            raise ValueError(f"Invalid {name}: '{value}'. {name} must be a string.")

    def to_dict(self):
        """Преобразует объект вакансии в словарь с ключами для названия, URL, зарплаты и описания"""
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }
