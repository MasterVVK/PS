import requests
from bs4 import BeautifulSoup

# URL сайта для парсинга
url = "https://quotes.toscrape.com/"

# Отправляем HTTP запрос и получаем ответ
response = requests.get(url)

# Создаём объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Используем метод find_all для поиска всех тегов <span> с классом "text" для цитат
quotes = soup.find_all('span', class_='text')

# Используем метод find_all для поиска всех тегов <small> с классом "author" для авторов
authors = soup.find_all('small', class_='author')

# Проверяем, найдены ли цитаты и авторы
if quotes and authors:
    for quote, author in zip(quotes, authors):
        print(f"{quote.text} — {author.text}")
else:
    print("Цитаты или авторы не найдены")
