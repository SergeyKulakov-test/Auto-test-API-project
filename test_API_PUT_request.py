from home_work import MapApi


if __name__ == "__main__":
    test_map_api_request = MapApi()

    place_id_list = test_map_api_request.get_place_id_in_file()  # Получение списка ID из файла
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
    for list in place_id_list:
        print(get_url + list)
        get_result = test_map_api_request.get_request(get_url + list)
        print(get_result.status_code)
        print(get_result.json())

        #Отбор существующих локаций
        if get_result.status_code == 200:
            with open('current_locations.txt', 'a', encoding='utf-8') as file:
                file.write(list + "\n")
                print()
        else:
            assert get_result.status_code == 404, "Статус код не верен"
            print(f"Запись с ID={list} не найдена")

    print("Тест завершен")
