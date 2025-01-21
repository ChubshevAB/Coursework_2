import os
from src.api import HHAPI
from src.vacancy import Vacancy
from src.storage import JSONStorage


def user_interface():
    '''Осуществляет взаимодействие с пользователем через консоль'''

    api = HHAPI()
    storage_path = os.path.join("Data", "vacancies.json")
    storage = JSONStorage(storage_path)

    while True:
        print("\n1. Запрос вакансий по запросу")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии по ключевому слову")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            query = input("Введите поисковый запрос: ")
            try:
                vacancies = api.fetch_vacancies(query)
                for item in vacancies:
                    vacancy = Vacancy(
                        title=item['name'],
                        url=item['alternate_url'],
                        salary=item['salary']['from'] if item['salary'] else 0,
                        description=item['snippet']['requirement']
                    )
                    storage.add_vacancy(vacancy)
                print("Вакансии успешно добавлены.")

            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            n = int(input("Введите количество вакансий: "))
            top_vacancies = sorted(storage.vacancies, key=lambda v: v.salary, reverse=True)[:n]
            for vacancy in top_vacancies:
                print(f"{vacancy.title}, Зарплата: {vacancy.salary}, Ссылка: {vacancy.url}")

        elif choice == "3":
            keyword = input("Введите ключевое слово: ")
            results = [vacancy for vacancy in storage.vacancies if keyword.lower() in vacancy.description.lower()]
            for vacancy in results:
                print(f"{vacancy.title}, Зарплата: {vacancy.salary}, Ссылка: {vacancy.url}")

        elif choice == "4":
            break

        else:
            print("Некорректный выбор, повторите попытку.")

if __name__ == "__main__":
    user_interface()
