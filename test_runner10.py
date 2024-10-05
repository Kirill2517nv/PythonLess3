import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task10.py'],  # Запуск основного скрипта
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
def check_output(input_data, expected_output):
    output = run_main_script(input_data)

    if expected_output in output:
        return True
    else:
        print(f"Ожидалось:\n{expected_output}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Ввод простых чисел
    print("\nТест 1: Ввод простых чисел")
    total_tests += 1
    if check_output("5\n2\n3\n5\n7\n11\n",
                    expected_output="Минимальное простое число: 2\nМаксимальное простое число: 11"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Нет простых чисел
    print("\nТест 2: Нет простых чисел")
    total_tests += 1
    if check_output("5\n4\n6\n8\n9\n10\n", expected_output="нет"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Смешанные числа с простыми
    print("\nТест 3: Смешанные числа")
    total_tests += 1
    if check_output("6\n1\n4\n5\n10\n13\n17\n",
                    expected_output="Минимальное простое число: 5\nМаксимальное простое число: 17"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Все числа составные
    print("\nТест 4: Все составные числа")
    total_tests += 1
    if check_output("5\n9\n15\n21\n25\n27\n", expected_output="нет"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
