import subprocess


# Вспомогательная функция для запуска основного скрипта и передачи данных через stdin
def run_main_script(input_data):
    process = subprocess.Popen(
        ['python', 'task9.py'],  # Запуск основного скрипта
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

    # Тест 1: Ввод двузначных чисел, делящихся на 3
    print("\nТест 1: Ввод двузначных чисел, делящихся на 3")
    total_tests += 1
    if check_output("5\n12\n15\n22\n30\n45\n",
                    expected_output="Минимальное двузначное число, делящееся на 3: 12\nМаксимальное двузначное число, делящееся на 3: 45"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 2: Нет двузначных чисел, делящихся на 3
    print("\nТест 2: Нет двузначных чисел, делящихся на 3")
    total_tests += 1
    if check_output("5\n10\n11\n22\n23\n44\n", expected_output="нет"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 3: Смешанные числа, включая двузначные, не делящиеся на 3
    print("\nТест 3: Смешанные числа")
    total_tests += 1
    if check_output("6\n8\n9\n99\n100\n15\n13\n",
                    expected_output="Минимальное двузначное число, делящееся на 3: 15\nМаксимальное двузначное число, делящееся на 3: 99"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")

    # Тест 4: Ввод только однозначных чисел
    print("\nТест 4: Ввод только однозначных чисел")
    total_tests += 1
    if check_output("5\n1\n2\n3\n4\n5\n", expected_output="нет"):
        print("Пройден!")
        tests_passed += 1
    else:
        print("Провален!")


    # Итоги
    print(f"\nРезультаты: {tests_passed}/{total_tests} тестов пройдено.")


# Запуск всех тестов
if __name__ == "__main__":
    run_tests()
