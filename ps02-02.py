# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

import requests

# URL API для получения постов
url = 'https://jsonplaceholder.typicode.com/posts'

# Параметры для запроса
params = {
    'userId': 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    # Вывод полученных записей
    posts = response.json()  # Преобразование ответа из формата JSON
    for post in posts:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
