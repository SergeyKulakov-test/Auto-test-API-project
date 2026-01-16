import requests


class TestCreateJoke:
    def __init__(self):
        self.categories = None

    def get_categories(self):
        self.categories = requests.get("https://api.chucknorris.io/jokes/categories").json() #Получение категорий
        print("Категории получены")
        return self.categories

    def get_joke(self, types):
        response = requests.get(f"https://api.chucknorris.io/jokes/random?category={types}")  # Get запрос (запрос шутки по категории)
        print(response.json())
        return response


if __name__ == "__main__":
    joke_tester = TestCreateJoke()
    categories = joke_tester.get_categories()
    print(categories)

    for category in categories:                   # Перебор категорий
        print(f"Категория {category}")
        response = joke_tester.get_joke(category) # Запрос шутки по категории

        assert response.status_code == 200, "Статус код не 200" #Проверка статуса ответа
        print("Статус код верен")

        assert response.json()["categories"][0] == category, "Выбранная категория не совпадает"  # Проверка категории шутки
        print("Категория шутки верная")

        print(response.json()["value"]) # Вывод шутки

    print("Тест завершен")


