import requests


class TestCreateJoke:
    def __init__(self):
        self.types = None
        self.number_of_type = None
        self.categories = None

    def get_categories(self):
        self.categories = requests.get("https://api.chucknorris.io/jokes/categories").json() #Получение категорий
        print("Категории получены")
        return self.categories

    def choose_category(self):
        print(f"Введите категорию: ") #Выбор категории
        self.types = input()
        print(f"Выбрали категорию {self.types}")
        return self.types

    def check_choose_category(self, types, categories):
        if types in categories:
            print("Выбранная категория есть")
            return True
        else:
            print("Такой категории нет")
            return False

    def get_joke(self, types):
        response = requests.get(f"https://api.chucknorris.io/jokes/random?category={types}")  # Get запрос (запрос шутки по категории)
        print(response.json())
        return response


if __name__ == "__main__":
    joke_tester = TestCreateJoke()

    choose_category = joke_tester.choose_category() #Выбор категории
    categories = joke_tester.get_categories() #Получение имеющихся категорий

    while True:
        if joke_tester.check_choose_category(choose_category, categories):  # Проверка наличия категории
            response = joke_tester.get_joke(joke_tester.types)
            break
        else:
            choose_category = joke_tester.choose_category()  # Выбор категории

    assert response.status_code == 200, "Статус код не 200"  # Проверка статуса ответа
    print("Статус код верен")

    assert response.json()["categories"][0] == joke_tester.types, "Выбранная категория не совпадает"  # Проверка категории шутки
    print("Категория шутки верная")

    print("Тест завершен")