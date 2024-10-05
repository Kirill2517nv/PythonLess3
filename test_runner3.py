import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task3.py'],  # Запуск основного скрипта
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Используем текстовый режим (строки)
        encoding='utf-8'  # Явно указываем кодировку UTF-8
    )

    stdout, stderr = process.communicate(input=input_data)

    if stderr:
        raise Exception(f"Ошибка: {stderr}")

    return stdout


# Проверка результата на соответствие
def check_output(input_data, expected_prime, expected_composite):
    output = run_main_script(input_data)
    prime_check = f"Простых чисел: {expected_prime}"
    composite_check = f"Составных чисел: {expected_composite}"

    if prime_check in output and composite_check in output:
        return True
    else:
        print(f"Ожидалось: {prime_check} и {composite_check}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Все простые числа
    print("\nТест 1: Все простые числа")
    total_tests += 1
    if check_output("2\n3\n5\n7\n11\n0\n", expected_prime=5, expected_composite=0):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Все составные числа
    print("\nТест 2: Все составные числа")
    total_tests += 1
    if check_output("4\n6\n8\n9\n10\n0\n", expected_prime=0, expected_composite=5):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Смешанные числа
    print("\nТест 3: Смешанные числа")
    total_tests += 1
    if check_output("2\n4\n5\n9\n10\n0\n", expected_prime=2, expected_composite=3):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Ввод только нуля
    print("\nТест 4: Ввод только нуля")
    total_tests += 1
    if check_output("0\n", expected_prime=0, expected_composite=0):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
