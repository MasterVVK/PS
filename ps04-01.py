from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Подключаем драйвер браузера с автоматической установкой через ChromeDriverManager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org")

    try:
        initial_query = input("Введите ваш запрос для Википедии: ")
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(initial_query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        first_link = driver.find_element(By.CSS_SELECTOR, ".mw-search-results .mw-search-result-heading a")
        first_link.click()

        while True:
            action = input("Выберите действие: (1) Листать параграфы, (2) Перейти на связанную страницу, (3) Выйти: ")
            if action == '1':
                paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
                for i, paragraph in enumerate(paragraphs[:5]):
                    print(f"{i + 1}. {paragraph.text}\n")
            elif action == '2':
                links = driver.find_elements(By.CSS_SELECTOR, "p a")
                for i, link in enumerate(links[:5]):
                    print(f"{i + 1}. {link.get_attribute('href')}")

                link_choice = int(input("Выберите страницу для перехода: ")) - 1
                links[link_choice].click()
                time.sleep(2)
            elif action == '3':
                print("Завершение программы.")
                break
            else:
                print("Неверный ввод, попробуйте снова.")
    finally:
        driver.quit()

main()
