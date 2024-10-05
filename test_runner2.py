import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task2.py'],  # Запуск основного скрипта
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
def check_output(input_data, expected_two_digit, expected_other):
    output = run_main_script(input_data)
    two_digit_check = f"Двузначных чисел: {expected_two_digit}"
    other_check = f"Других чисел: {expected_other}"

    if two_digit_check in output and other_check in output:
        return True
    else:
        print(f"Ожидалось: {two_digit_check} и {other_check}, но получили:\n{output}")
        return False


# Функция для запуска всех тестов
def run_tests():
    tests_passed = 0
    total_tests = 0

    # Тест 1: Все двузначные числа
    print("\nТест 1: Все двузначные числа")
    total_tests += 1
    if check_output("12\n34\n56\n78\n99\n0\n", expected_two_digit=5, expected_other=0):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Все другие числа (однозначные и трехзначные)
    print("\nТест 2: Все другие числа")
    total_tests += 1
    if check_output("1\n2\n100\n101\n9\n0\n", expected_two_digit=0, expected_other=5):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Смешанные числа
    print("\nТест 3: Смешанные числа")
    total_tests += 1
    if check_output("9\n23\n99\n150\n8\n0\n", expected_two_digit=2, expected_other=3):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Ввод только нуля
    print("\nТест 4: Ввод только нуля")
    total_tests += 1
    if check_output("0\n", expected_two_digit=0, expected_other=0):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
