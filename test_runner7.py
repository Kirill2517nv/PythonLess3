import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task7.py'],  # Запуск основного скрипта
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

    # Тест 1: Ввод нескольких чисел Фибоначчи
    print("\nТест 1: Ввод нескольких чисел Фибоначчи")
    total_tests += 1
    if check_output("3\n5\n8\n2\n13\n0\n", expected_output="Минимальное число Фибоначчи: 2"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Ввод чисел без чисел Фибоначчи
    print("\nТест 2: Ввод чисел без чисел Фибоначчи")
    total_tests += 1
    if check_output("4\n6\n9\n10\n0\n", expected_output="нет"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Ввод смешанных чисел, некоторые из которых являются числами Фибоначчи
    print("\nТест 3: Ввод смешанных чисел")
    total_tests += 1
    if check_output("4\n1\n2\n6\n10\n0\n", expected_output="Минимальное число Фибоначчи: 1"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Ввод только нуля
    print("\nТест 4: Ввод только нуля")
    total_tests += 1
    if check_output("0\n", expected_output="нет"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
