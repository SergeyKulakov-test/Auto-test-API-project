from home_work import MapApi


if __name__ == "__main__":
    test_put_request = MapApi()
    new_address = "10 Artelnaya street"  # Новый адрес
    print(new_address)

    place_id = test_put_request.get_place_id_in_file()[0]  # Получение ID из файла
    print(place_id)

    body = test_put_request.create_body_put_request(place_id, new_address)  # Добавление ID в тело запроса
    print(body)

    url = test_put_request.url + test_put_request.put_resource + test_put_request.key  # Ссылка для PUT запроса
    print(url)

    result_put = test_put_request.put_request(body, url)
    print(result_put.json())
    print(result_put.status_code)

    assert result_put.status_code == 200, "Статус код не верен"  # Проверка PUT запроса
    print(f"Статус код PUT запроса: {result_put.status_code}")

    get_url = test_put_request.url + test_put_request.get_resource + test_put_request.key + "&place_id=" + place_id  # Ссылка для GET запроса

    get_result = test_put_request.get_request(get_url)  # Получение данных для проверки
    print(get_result.json())

    assert get_result.status_code == 200, "Статус код верен"  # Проверка GET запроса
    print(f"Статус код GET запроса: {get_result.status_code}")

    assert get_result.json()["address"] == new_address, "Адресс не изменен"
    print("Данные успешно обновлены")

    print("Тест завершен")
