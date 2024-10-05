import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task1.py'],  # Запуск основного скрипта
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Используем строки для ввода/вывода
        encoding='utf-8'
    )

    stdout, stderr = process.communicate(input=input_data)

    if stderr:
        raise Exception(f"Ошибка: {stderr}")

    return stdout


# Проверка результата на соответствие
def check_output(input_data, expected_pos, expected_neg):
    output = run_main_script(input_data)
    pos_check = f"Положительных чисел: {expected_pos}"
    neg_check = f"Отрицательных чисел: {expected_neg}"

    if pos_check in output and neg_check in output:
        return True
    else:
        print(f"Ожидалось: {pos_check} и {neg_check}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Все положительные числа
    print("\nТест 1: Все положительные числа")
    total_tests += 1
    if check_output("1\n2\n3\n4\n5\n0\n", expected_pos=5, expected_neg=0):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Все отрицательные числа
    print("\nТест 2: Все отрицательные числа")
    total_tests += 1
    if check_output("-1\n-2\n-3\n-4\n-5\n0\n", expected_pos=0, expected_neg=5):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Смешанные числа
    print("\nТест 3: Смешанные положительные и отрицательные числа")
    total_tests += 1
    if check_output("-1\n2\n-3\n4\n0\n", expected_pos=2, expected_neg=2):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Ввод только нуля
    print("\nТест 4: Ввод только нуля")
    total_tests += 1
    if check_output("0\n", expected_pos=0, expected_neg=0):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
