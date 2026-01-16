import requests


class TestCreateJoke:
    def __init__(self):
        self.types = None
        self.number_of_type = None

    def get_categories(self):
        print("123")
        self.categories = requests.get("https://api.chucknorris.io/jokes/categories").json() #Получение категорий
        print("Категории получены")
        return self.categories

    def choose_category(self):
        categories = self.get_categories()
        print(f"Введите число от 0 до 15, соответствующее выбранной категории") #Выбор категории
        for index, category in enumerate(categories):
            print(f"{index} - {category}")
        while True:
            try:
                self.number_of_type = int(input())
                if 0 <= self.number_of_type <= 15:
                    print(f"Выбрана категория {categories[self.number_of_type]}")
                    self.types = categories[self.number_of_type]    #выбранная категория
                    return self.types
                else:
                    print("Введите число от 0 до 15")
            except ValueError:
                print("Введено не чиcло")

    def get_joke(self):
        types = self.choose_category()
        response = requests.get(f"https://api.chucknorris.io/jokes/random?category={types}")  # Get запрос (запрос шутки по категории)
        print(response.json())
        return response


if __name__ == "__main__":
    joke_tester = TestCreateJoke()
    response = joke_tester.get_joke()

    assert response.status_code == 200, "Статус код не 200" #Проверка статуса ответа
    print("Статус код верен")

    assert response.json()["categories"][0] == joke_tester.types, "Выбранная категория не совпадает"  # Проверка категории шутки
    print("Категория шутки верная")

    assert "Chuck" in response.json()["value"], "Шутка не содержит Chuck"  # Проверка категории шутки
    print(response.json()["value"])