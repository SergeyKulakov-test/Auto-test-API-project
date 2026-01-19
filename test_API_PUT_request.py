from home_work import MapApi


if __name__ == "__main__":
    test_map_api_request = MapApi()

    post_url = test_map_api_request.url + test_map_api_request.post_resource + test_map_api_request.key  # Ссылка для POST запроса
    for i in range(5):
        result_post = test_map_api_request.create_location(post_url, test_map_api_request.body)
        print(result_post.json().get("status"))

        test_map_api_request.save_place_id(result_post) # Запись ID  в файл

    place_id_list = test_map_api_request.get_place_id_in_file('test_place_id.txt')  # Получение списка ID из файла
    print(place_id_list)

    url = test_map_api_request.url + test_map_api_request.delete_resource + test_map_api_request.key  # Ссылка для DELETE запроса
    print(url)

    # Удаление 2 и 4 локаций
    for i in range(len(place_id_list)):
        body = {"place_id": place_id_list[i]}
        if i == 1 or i == 3:
            result_delete = test_map_api_request.delete_request(body, url)
            print(result_delete.status_code)
            assert result_delete.status_code == 200, "Статус код не верен"
            print(f"Локация с ID - {place_id_list[i]} удалена")

    get_url = test_map_api_request.url + test_map_api_request.get_resource + test_map_api_request.key + "&place_id="  # Ссылка для GET запроса

    #GET запросы по ID
    for line in place_id_list:
        print(get_url + line)
        get_result = test_map_api_request.get_request(get_url + line)
        print(get_result.status_code)

        #Отбор существующих локаций
        if get_result.status_code == 200:
            get_result.json()
            with open('current_locations.txt', 'a', encoding='utf-8') as file:
                file.write(line + "\n")
        else:
            print(f"Запись с ID={line} не найдена")

    current_place_id_list = test_map_api_request.get_place_id_in_file('current_locations.txt')  # Получение списка ID из файла
    print(current_place_id_list)

    test_map_api_request.check_current_location(place_id_list, current_place_id_list) # Проверка наличия 2 и 4 ID в новом фале

    test_map_api_request.clear_file() # Очистка нового файла

    print("Тест завершен")
