# 1.Напишите три функции
# ⁠1.1 save_test_ids(test_ids) — принимает список
# ID тестов и сохраняет их в tests.txt.
# Каждый ID должен находиться на отдельной строке.
# 1.2⁠  ⁠add_test_id(test_id) — добавляет один новый
# ID в конец существующего файла, не удаляя предыдущие записи.
# 1.3  ⁠load_test_ids(filename) — читает файл и возвращает список ID.
# Пустые строки нужно пропускать, пробелы по краям удалять.
# Пример исходного списка->["QA-1001", "QA-1002", "QA-1003"]
# После вызова add_test_id("QA-1004") функция load_test_ids("tests.txt")
# должна вернуть:
# ["QA-1001", "QA-1002", "QA-1003", "QA-1004"]
# Используйте: def, return, for, list, append(), with open(),
# режимы w, a, r, strip().
# Проверьте пустой список, повторное добавление записи и чтение файла
# с пустыми строками.

print("Task 1")

def save_test_ids(test_ids):
    with open("tests.txt", "w", encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(f"{test_id}\n")
    return

def add_test_id(test_id):
    with open("tests.txt", "a", encoding="utf-8") as file:
        file.write(f"{test_id}\n")
    return

def load_test_ids(filename):
    ids_list = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line != "":
                ids_list.append(cleaned_line)
    return ids_list

initial_tests = ["QA-1001", "QA-1002", "QA-1003"]
save_test_ids(initial_tests)
print("Исходный список сохранен")

add_test_id("QA-1004")
print("Новый ID добавлен.")

loaded_tests = load_test_ids("tests.txt")
print("Результат чтения из файла:", loaded_tests)

print("Task 2")

# 2.Создайте файл results.csv test_id,status,duration_ms
# QA-1001,PASSED,120
# QA-1002,FAILED,230
# QA-1003,PASSED,150
# Напишите функцию get_test_statistics(filename)
# Функция должна:
# 1.⁠ ⁠Прочитать данные из CSV.
# 2.⁠ ⁠Посчитать общее количество тестов.
# 3.⁠ ⁠Посчитать количество PASSED и FAILED.
# 4.⁠ ⁠Найти суммарное время выполнения тестов в миллисекундах.
# 5.⁠ ⁠Собрать в список ID всех проваленных тестов.
# 6.Вернуть словарь с результатом
# Ожидаемый резальт->
# {
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500,
#     "failed_ids": ["QA-1002"]
# }
# Используйте: csv.DictReader(), for, if, dict, list, int(), append(),
# return.
# Считайте, что в корректном входном файле статусы могут быть только
# PASSED и FAILED, а время — целое неотрицательное число.
# Дополнительно проверьте файл, содержащий только заголовки.
# Все счётчики должны быть равны нулю, список ошибок — пустой.

import csv
with open("results.csv", "w", encoding="utf-8") as file:
    file.write("test_id,status,duration_ms\n")
    file.write("QA-1001,PASSED,120\n")
    file.write("QA-1002,FAILED,230\n")
    file.write("QA-1003,PASSED,150\n")

with open("empty_results.csv", "w", encoding="utf-8") as file:
    file.write("test_id,status,duration_ms\n")

def get_test_statistics(filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])
            if row["status"] == "PASSED":
                passed += 1
            elif row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

    result = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms,
        "failed_ids": failed_ids
    }

    return result

stats = get_test_statistics("results.csv")
print("Статистика по основному файлу:")
print(stats)

print("\n--- Дополнительная проверка ---")

empty_stats = get_test_statistics("empty_results.csv")
print("Статистика по пустому файлу (только заголовки):")
print(empty_stats)


print("Task 3")

# 3. Напишите две функции:
# •⁠  ⁠save_test_config(environment, base_url, timeout) —
# создаёт config.json и сохраняет параметры тестового окружения.
# •⁠  ⁠load_test_config(filename) — читает JSON и возвращает
# словарь с настройками.
# Пример вызова
# save_test_config(
#     "staging",
#     "https://example.com",
#     30
# )
# Ожидаемый JSON {
#     "environment": "staging",
#     "base_url": "https://example.com",
#     "timeout": 30
# }
# —-----------
# 1.⁠ ⁠Для сохранения используйте json.dump().
# 2.⁠ ⁠Для чтения используйте json.load().
# 3.⁠ ⁠Сохраняйте данные с отступами для удобного чтения.
# 4.⁠ ⁠Проверьте, что после загрузки тип timeout остаётся int.
# 5.⁠ ⁠Проверьте, что повторное сохранение заменяет старую
# конфигурацию.
#
# Используйте: dict, json.dump(), json.load(), with open(),
# type(), assert.

import json

def save_test_config(environment, base_url, timeout):
    config_data = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config_data, file, indent=4, ensure_ascii=False)
    return

def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        config_dict = json.load(file)
    return config_dict

save_test_config("staging", "https://example.com", 30)
print("Конфигурация успешно сохранена.")

loaded_config = load_test_config("config.json")
print("Загруженная конфигурация:", loaded_config)

print("Task 4")

# 4.Advanced
# Вы работаете QA Engineer. После
# запуска автоматизированных тестов необходимо создать
# отчёт для команды.
# Напишите функцию build_run_report(project_name, csv_filename)
# Функция получает название проекта и путь к CSV-файлу в формате
# из Task 2.
# Она должна
# 1.⁠ ⁠Прочитать все результаты тестирования.
# 2.⁠ ⁠Посчитать total, passed, failed, total_duration_ms.
# 3.⁠ ⁠Создать папку reports.
# 4.⁠ ⁠Внутри неё создать папку с названием проекта.
# 5.⁠ ⁠Создать файл summary.json с общей статистикой.
# 6.⁠ ⁠Создать файл failed_tests.txt, в который записать ID всех
# тестов со статусом FAILED.
# 7.⁠ ⁠Вернуть словарь с итоговой статистикой.
#
# Пример
# build_run_report("Shop", "results.csv")
# reports/
#     Shop/
#         summary.json
#         failed_tests.txt
# Содержимое summary.json:
# {
#     "project": "Shop",
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500
# }
# Содержимое failed_tests.txt QA-1002
# Если папки ещё нет, она должна создаваться автоматически.
# •⁠  ⁠Если папка уже существует, программа должна работать без ошибки.
# •⁠  ⁠Если проваленных тестов нет, failed_tests.txt должен существовать,
# но оставаться пустым.
# •⁠  ⁠При повторном запуске файлы должны обновляться, а не дублировать
# старые результаты.
#
# Используйте: pathlib.Path, mkdir(parents=True, exist_ok=True),
# csv.DictReader(), json.dump(), with open(), циклы, условия,
# списки и словари.

import csv
import json
from pathlib import Path

with open("results.csv", "w", encoding="utf-8") as file:
    file.write("test_id,status,duration_ms\n")
    file.write("QA-1001,PASSED,120\n")
    file.write("QA-1002,FAILED,230\n")
    file.write("QA-1003,PASSED,150\n")

def build_run_report(project_name, csv_filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(csv_filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])

            if row["status"] == "PASSED":
                passed += 1
            elif row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

    project_folder = Path("reports") / project_name
    project_folder.mkdir(parents=True, exist_ok=True)
    summary_path = project_folder / "summary.json"
    failed_txt_path = project_folder / "failed_tests.txt"

    summary_data = {
        "project": project_name,
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms
    }

    with open(summary_path, "w", encoding="utf-8") as json_file:
        json.dump(summary_data, json_file, indent=4, ensure_ascii=False)

    with open(failed_txt_path, "w", encoding="utf-8") as txt_file:
        for test_id in failed_ids:
            txt_file.write(f"{test_id}\n")
    return summary_data

report_result = build_run_report("Shop", "results.csv")

print("\nОтчёт успешно сгенерирован!")
print("Вернувшееся значение функции (статистика):")
print(report_result)

print("\nПроверка созданных файлов:")
print(f"Файл summary.json существует: {Path('reports/Shop/summary.json').exists()}")
print(f"Файл failed_tests.txt существует: {Path('reports/Shop/failed_tests.txt').exists()}")