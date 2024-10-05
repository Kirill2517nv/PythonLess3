import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task4.py'],  # Запуск основного скрипта
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
def check_output(input_data, expected_sum):
    output = run_main_script(input_data)
    expected_output = f"Сумма чисел, делящихся на 5: {expected_sum}"

    if expected_output in output:
        return True
    else:
        print(f"Ожидалось: {expected_output}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Все числа делятся на 5
    print("\nТест 1: Все числа делятся на 5")
    total_tests += 1
    if check_output("5\n10\n15\n20\n25\n0\n", expected_sum=75):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Ни одно число не делится на 5
    print("\nТест 2: Ни одно число не делится на 5")
    total_tests += 1
    if check_output("1\n2\n3\n4\n6\n0\n", expected_sum=0):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Смешанные числа (некоторые делятся на 5)
    print("\nТест 3: Смешанные числа")
    total_tests += 1
    if check_output("3\n5\n10\n22\n35\n0\n", expected_sum=50):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Ввод только нуля
    print("\nТест 4: Ввод только нуля")
    total_tests += 1
    if check_output("0\n", expected_sum=0):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
