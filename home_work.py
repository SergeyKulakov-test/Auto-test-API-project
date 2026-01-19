import requests


class MapApi:
    def __init__(self):
        self.url = "https://rahulshettyacademy.com" #Базовая ссылка
        self.post_resource = "/maps/api/place/add/json" #Чать для POST запроса
        self.get_resource = "/maps/api/place/get/json" #Чать для GET запроса
        self.put_resource = "/maps/api/place/update/json"  #Чать для PUT запроса
        self.delete_resource = "/maps/api/place/delete/json"  #Часть для DELETE запроса
        self.key = "?key=qaclick123"                    #Ключ
        #Тело POST запроса
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
                "language": "French-IN"
                }
        # Тело PUT запроса
        self.put_body = {
            "place_id": "",
            "address": "",
            "language": "RU_ru",
            "key": "qaclick123"
        }
    #POST запрос
    # Создание локации
    @staticmethod
    def create_location(body, post_url):
        request_post = requests.post(post_url, json=body)
        print(request_post.json())
        return request_post

    # Get запрос
    @staticmethod
    def get_request(get_url):
        request_get = requests.get(get_url)
        return request_get

    # PUT запрос
    @staticmethod
    def put_request(body, url):
        request_put = requests.put(url, json=body)
        return request_put

    #DELETE запрос
    @staticmethod
    def delete_request(body, url):
        request_delete = requests.delete(url, json=body)
        return request_delete

    # Создание тела PUT запроса
    def create_body_put_request(self, place_id, address):
        self.put_body['place_id'] = place_id
        self.put_body['address'] = address
        return self.put_body

    # Работа с фалом
    # Сохранение в файл ID
    def save_place_id(self, request_post):
        with open('test_place_id.txt', 'a', encoding='utf-8') as file:
            file.write(request_post.json()["place_id"] + "\n")
        self.delete_place_id_in_file()

    # Удаление лишних ID
    @staticmethod
    def delete_place_id_in_file():
        with open('test_place_id.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if len(lines) > 5:
            lines = lines[-5:]
            with open('test_place_id.txt', 'w', encoding='utf-8') as file:
                file.writelines(lines)
        print("ID записан в файл")

    # Получение ID из файла
    @staticmethod
    def get_place_id_in_file():
        with open('test_place_id.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [s.strip("\n") for s in lines]
        return lines