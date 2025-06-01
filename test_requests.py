import requests

# Отправляем GET-запрос на тестовый сайт
response = requests.get("https://jsonplaceholder.typicode.com/posts/1") 

# Выводим статус ответа (200 — всё хорошо!)
print("Статус:", response.status_code)

# Выводим содержимое ответа (данные в формате JSON)
print("Данные:", response.json())