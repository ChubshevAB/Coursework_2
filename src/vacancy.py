class Vacancy:
    def __init__(self, title: str, url: str, salary: float, description: str):
        self._title = title
        self._url = url
        self._salary = salary
        self._description = description
        self.validate()

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

    def validate(self):
        """Метод валидации для проверки корректности значений атрибутов вакансии. Проверяет, что зарплата является
        числом и что название, URL и описание — строки. Если проверки не пройдены, выбрасывает исключение ValueError
        """

        if not isinstance(self._salary, (int, float)):
            raise ValueError("Salary must be a number.")
        if (
            not isinstance(self._title, str)
            or not isinstance(self._url, str)
            or not isinstance(self._description, str)
        ):
            raise ValueError("Title, URL, and description must be strings.")

    def to_dict(self):
        """Преобразует объект вакансии в словарь с ключами для названия, URL, зарплаты и описания"""

        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }
