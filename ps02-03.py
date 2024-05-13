# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа

import requests

# URL API для создания новых постов
url = 'https://jsonplaceholder.typicode.com/posts'

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Печать статус-кода ответа
print("Статус-код ответа:", response.status_code)

# Печать содержимого ответа
print("Содержимое ответа:")
print(response.json())
