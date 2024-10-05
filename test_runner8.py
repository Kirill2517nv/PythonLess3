import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task8.py'],  # Запуск основного скрипта
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

    # Тест 1: Все положительные числа
    print("\nТест 1: Все положительные числа")
    total_tests += 1
    if check_output("5\n1\n2\n3\n4\n5\n", expected_output="Положительных чисел: 5\nОтрицательных чисел: 0"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Все отрицательные числа
    print("\nТест 2: Все отрицательные числа")
    total_tests += 1
    if check_output("5\n-1\n-2\n-3\n-4\n-5\n", expected_output="Положительных чисел: 0\nОтрицательных чисел: 5"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Смешанные положительные и отрицательные числа
    print("\nТест 3: Смешанные положительные и отрицательные числа")
    total_tests += 1
    if check_output("6\n-1\n2\n-3\n4\n0\n5\n", expected_output="Положительных чисел: 3\nОтрицательных чисел: 2"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Все нули
    print("\nТест 4: Все нули")
    total_tests += 1
    if check_output("3\n0\n0\n0\n", expected_output="Положительных чисел: 0\nОтрицательных чисел: 0"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
