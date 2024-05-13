import requests
import pprint

# URL для API GitHub
url = 'https://api.github.com/search/repositories'

# Параметры для запроса
params = {
    'q': 'language:html'
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Печать статус-кода ответа
print("Статус-код:", response.status_code)

# Печать содержимого ответа в JSON формате
print("total_count в JSON:")
pprint.pprint(response.json()["total_count"])
