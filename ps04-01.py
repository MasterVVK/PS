from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
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

        time.sleep(2)
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
        if paragraphs:
            print(f"1. {paragraphs[0].text}\n")

        paragraph_index = 1
        action = '1'

        while True:
            action = input("Выберите действие: (1) Листать параграфы, (2) Перейти на связанную страницу, (3) Выйти или нажмите Enter для продолжения с текущим выбором: ")
            if action == '1':
                if paragraph_index < len(paragraphs):
                    print(f"{paragraph_index + 1}. {paragraphs[paragraph_index].text}\n")
                    paragraph_index += 1
                else:
                    print("Больше нет параграфов.\n")
            elif action == '2':
                links = driver.find_elements(By.CSS_SELECTOR, "p a")
                if links:
                    for i, link in enumerate(links[:5]):
                        print(f"{i + 1}. {link.get_attribute('href')}")
                    try:
                        link_choice = int(input("Выберите страницу для перехода: ")) - 1
                        links[link_choice].click()
                        time.sleep(2)
                        paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
                        paragraph_index = 0
                    except ValueError:
                        print("Вы ввели недопустимый номер, попробуйте еще раз.")
                    except IndexError:
                        print("Вы ввели номер за пределами диапазона, попробуйте еще раз.")
                else:
                    print("Ссылки для перехода не найдены.")
            elif action == '3':
                print("Завершение программы.")
                break
            elif not action:
                continue  # Просто продолжаем цикл с последнего действия
            else:
                print("Неверный ввод, попробуйте снова.")

    finally:
        driver.quit()

main()
