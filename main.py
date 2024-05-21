import time
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер (устанавливаем путь к драйверу, если требуется)
driver = webdriver.Chrome()  # Используем Chrome

# Указываем URL веб-страницы
url = "https://tomsk.hh.ru/vacancies/programmist"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)

# Находим все карточки с вакансиями по названию класса
vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')

# Выводим количество найденных вакансий на экран
print(f"Найдено {len(vacancies)} вакансий")

# Создаём список для сохранения данных
parsed_data = []

# Функция для удаления непечатных символов из строки
def remove_non_printable(s):
    # Используем регулярное выражение для удаления непечатных символов, включая неразрывные пробелы
    return re.sub(r'[\x00-\x1F\x7F\u200B-\u200D\uFEFF]', '', s)

# Перебираем коллекцию вакансий
for vacancy in vacancies:
    try:
        # Находим элементы внутри вакансий по значению CSS селекторов
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')

        # Удаляем непечатные символы из строки зарплаты
        salary_cleaned = remove_non_printable(salary)

        # Вносим найденную информацию в список
        parsed_data.append([title, company, salary_cleaned, link])

    except Exception as e:
        print(f"Произошла ошибка при парсинге вакансии: {e}")
        continue

# Закрываем браузер
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)

print("Данные успешно сохранены в файл hh.csv")
