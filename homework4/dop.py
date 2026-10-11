from pathlib import Path


def create_test_report(project_name, tester_name, passed, failed):
    # 1. Создаём путь "reports/Имя_Проекта"
    project_folder = Path("reports") / project_name
    # Создаём папки на диске
    project_folder.mkdir(parents=True, exist_ok=True)
    # 2. Считаем значения
    total = passed + failed
    if failed == 0:
        status = "Passed"
    else:
        status = "Failed"
    # 3. ПРАВИЛЬНО собираем путь к файлу внутри созданной папки
    file_path = project_folder / "reports.txt"
    # 4. Открываем файл и заполняем f-строку (добавлена буква 'f' перед кавычками)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f'''Project: {project_name}
Tester: {tester_name}
Status: {status}
Passed tests: {passed}
Failed tests: {failed}
Total tests: {total}
''')
    return

create_test_report("Phonebook", "Vera", 88, 22)