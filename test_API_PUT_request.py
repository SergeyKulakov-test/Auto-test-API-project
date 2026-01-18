from API_PUT_request import TestMapApiPutRequest
from home_work import TestMapApi


if __name__ == "__main__":
    test_put_request = TestMapApiPutRequest()
    new_address = test_put_request.put_body["address"]  # Новый адрес
    print(new_address)

    place_id = test_put_request.get_place_id_in_file()[0]  # Получение ID из файла
    print(place_id)

    body = test_put_request.create_body_put_request(place_id)  # Добавление ID в тело запроса
    print(body)

    url = test_put_request.url + test_put_request.put_resource + test_put_request.key  # Ссылка для PUT запроса
    print(url)

    result_put = test_put_request.put_request(body, url)
    print(result_put.json())
    print(result_put.status_code)

    assert result_put.status_code == 200, "Статус код не верен"  # Проверка PUT запроса
    print(f"Статус код PUT запроса: {result_put.status_code}")

    create_location = TestMapApi()
    get_url = create_location.url + create_location.get_resource + create_location.key + "&place_id=" + place_id  # Ссылка для GET запроса

    get_result = create_location.get_request(get_url)  # Получение данных для проверки
    print(get_result.json())

    assert get_result.status_code == 200, "Статус код верен"  # Проверка GET запроса
    print(f"Статус код GET запроса: {get_result.status_code}")

    assert get_result.json()["address"] == new_address, "Адресс не изменен"
    print("Данные успешно обновлены")

    print("Тест завершен")
