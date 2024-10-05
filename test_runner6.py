import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task6.py'],  # Запуск основного скрипта
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

    # Тест 1: Ввод нескольких положительных чисел
    print("\nТест 1: Ввод нескольких положительных чисел")
    total_tests += 1
    if check_output("3\n5\n10\n2\n0\n", expected_output="Минимальное число: 2\nМаксимальное число: 10"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Ввод нескольких отрицательных чисел
    print("\nТест 2: Ввод нескольких отрицательных чисел")
    total_tests += 1
    if check_output("-1\n-5\n-3\n-10\n0\n", expected_output="Минимальное число: -10\nМаксимальное число: -1"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Ввод смешанных положительных и отрицательных чисел
    print("\nТест 3: Ввод смешанных положительных и отрицательных чисел")
    total_tests += 1
    if check_output("-3\n5\n-1\n10\n0\n", expected_output="Минимальное число: -3\nМаксимальное число: 10"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Ввод только нуля
    print("\nТест 4: Ввод только нуля")
    total_tests += 1
    if check_output("0\n", expected_output="Нет чисел для анализа."):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
