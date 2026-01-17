import requests


class TestMapApi:
    def __init__(self):
        self.url = "https://rahulshettyacademy.com" #Базовая ссылка
        self.post_resource = "/maps/api/place/add/json" #Чать для POST запроса
        self.get_resource = "/maps/api/place/get/json" #Чать для GET запроса
        self.key = "?key=qaclick123"                    #Ключ
        #Тело запроса
        self.body = {"location": {
                "lat": -38.383494,
                "lng": 33.427362
                        }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number":
                "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": ["shoe park", "shop"],
                "website": "http://google.com",
                "language": "French-IN"}

    # Создание локации
    def create_location(self, body, post_url):
        request_post = requests.post(post_url, json=body)
        print(request_post.json())
        return request_post

    # Сохранение в файл ID
    def save_place_id(self, request_post):
        with open('test_place_id.txt', 'a', encoding='utf-8') as file:
            file.write(request_post.json()["place_id"] + "\n")
        self.delete_place_id_in_file()

    # Удаление лишних ID
    def delete_place_id_in_file(self):
        with open('test_place_id.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if len(lines) > 5:
            lines = lines[-5:]
            with open('test_place_id.txt', 'w', encoding='utf-8') as file:
                file.writelines(lines)
        print("ID записан в файл")

    # Get запрос
    def get_request(self, get_url):
        request_get = requests.get(get_url)
        print(request_get)
        return request_get

    # Получение ID из файла
    def get_place_id_in_file(self):
        with open('test_place_id.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [s.strip("\n") for s in lines]
        return lines


if __name__ == "__main__":
    create_location = TestMapApi()  # Создаие экземпляра класса
    post_url = create_location.url + create_location.post_resource  # Ссылка для POST запроса
    get_url = create_location.url + create_location.get_resource + create_location.key + "&place_id="  # Часть для GET запроса
    # Отправка 5-ти POST запросов
    for i in range(5):
        post_result = create_location.create_location(create_location.body, post_url)
        print(post_result.json().get("status"))

        assert post_result.json().get("status") == "OK", "Статус код не верен"  # Проверка, что запрос отправлен корректно
        print("Запрос POST успешен")

        create_location.save_place_id(post_result)  #Добавление ID в файл

    lines = create_location.get_place_id_in_file()   # Получение ID из файла
    print(lines)

    for line in lines:   # Отправка запросов по ID из файла
        print(get_url + line)
        get_result = create_location.get_request(get_url + line)
        print(get_result.json())

        assert get_result.status_code == 200, "Статус код не верен"  # Проверка, что запрос верен
        print("Запрос GET успешен")

    print("Тест завершен")


