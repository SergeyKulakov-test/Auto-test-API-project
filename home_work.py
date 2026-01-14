import requests


url = "https://api.chucknorris.io/jokes/random" #Запрашиваемый url
print(url)

response = requests.get(url) #Get запрос (запрос шутки)
print("Статус код: " + str(response.status_code)) #Вывод статуса ответа

assert 200 == response.status_code, "Статус код не 200" #Проверка статуса ответа
print("Статус код верен")

print(response.json()) #Вывод ответа
