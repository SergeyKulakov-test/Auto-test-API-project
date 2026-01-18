import requests


class TestMapApiPutRequest:
    def __init__(self):
        self.url = "https://rahulshettyacademy.com" #Базовая ссылка
        self.put_resource = "/maps/api/place/update/json" #Чать для POST запроса
        self.key = "?key=qaclick123"
        # Тело для PUT запроса
        self.put_body = {
                "place_id" : "",
                "address" : "80 Beketov street",
                "language" : "RU_ru",
                "key" : "qaclick123"
                }

    def create_body_put_request(self, place_id):
        self.put_body['place_id'] = place_id
        return self.put_body

    def put_request(self, body, url):
        request_put = requests.put(url, json=body)
        print(request_put.status_code)
        return request_put

    def get_place_id_in_file(self):
        with open('test_place_id.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [s.strip("\n") for s in lines]
        return lines





