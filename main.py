def coroutine():
    print("Начало coroutine")
    try:
        while True:
            value = yield
            print(f"Получено: {value}")
    except GeneratorExit:
        print("Генератор закрыт")

# Создаем генератор
gen = coroutine()

# Запускаем генератор
next(gen)  # Вывод: Начало coroutine

# Отправляем значение в генератор
try:
    gen.send("Привет!")  # Вывод: Получено: Привет!
    gen.send("Как дела?")  # Вывод: Получено: Как дела?
except StopIteration:
    print("Генератор завершил выполнение")

# Закрываем генератор
gen.close()
