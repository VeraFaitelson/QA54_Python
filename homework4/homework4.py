print("Task 1")
print("")

# 1. Save a book list
# Напишите функцию save_books(books).
# Функция принимает список строк и создаёт файл books.txt,
# в который сохраняет названия книг.
# Каждая книга должна быть записана с новой строки.
# Пример:
# books = [
#  	"Harry Potter",
#  	"The Hobbit",
#  	"1984",
#  	"The Little Prince"
#  ]
# save_books(books)
# После выполнения программы файл books.txt должен выглядеть так:
# Harry Potter
#  The Hobbit
#  1984
#  The Little Prince
# Используйте:
# with open(...)
# режим "w"
# цикл for

def save_books(books:list):
    with open("books.txt", "w", encoding="utf-8") as file:
        for line in books:
            file.write(f"{line}\n")
    return

save_books(["Harry Potter", "The Hobbit", "1984", "The Little Prince"])


print("Task 2")
print("")

# 2. Read data from a CSV file
# Создайте файл products.csv со следующим содержимым:
# product,price
#  Coffee,25
#  Tea,18
#  Chocolate,12
# Напишите функцию:
# read_products(filename)
# Функция должна прочитать данные из файла
# и вывести информацию в следующем формате:
# Product: Coffee (25)
#  Product: Tea (18)
#  Product: Chocolate (12)
# Используйте:
# csv.DictReader()

import csv
from os import write

with open("products.csv", "w", encoding="utf-8") as init_file:
    init_file.write("product,price\nCoffee,25\nTea,18\nChocolate,12\n")

def read_products(filename):
    with open(filename,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")
    return

read_products("products.csv")

print("")
print("Task 3")

# 3. Save user information to a JSON file
# Напишите функцию:
# save_user(username, email, country)
# Функция должна создать файл user.json и сохранить
# в него информацию о пользователе.
# Пример вызова:
# save_user("anna21", "anna@example.com", "Israel")
# Ожидаемое содержимое файла user.json:
# {
#  	"username": "anna21",
#  	"email": "anna@example.com",
#  	"country": "Israel"
#  }
# Используйте:
# ·       словарь dict
# ·       json.dump()

import json


def save_user(username, email, country):
    user_data = {
        "username": username,
        "email": email,
        "country": country
    }
    with open("user.json", "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=4)  # indent=4 - отступы
    return

save_user("anna21", "anna@example.com", "Israel")

print("Task 4")
print("")

# 4. Advanced ★
# Напишите функцию:
# create_logs_folder()
# Функция должна:
# 1.     Создать папку logs.
# 2.     Создать внутри неё файл app.txt.
# 3.     Записать в файл строку:
# Application started successfully!
# Используйте:
# ·       pathlib.Path
# ·       mkdir()
# ·       with open(...)
# General Requirements
# ·       Используйте encoding='utf-8' при работе с текстовыми файлами.
# ·       Проверьте работу каждой функции на примерах из задания.
# ·       Используйте названия функций, указанные в задании.
# ·       Код должен быть читаемым и аккуратно оформленным.
# ·       После выполнения программы проверьте содержимое созданных файлов.
#

from pathlib import Path

def create_logs_folder():
    # 1. Создаём объект Path для папки logs
    logs_dir = Path("logs")
    # 2. Создаём папку
    # parents=True позволяет создавать вложенные папки, если нужно
    # exist_ok=True защищает от ошибки, если папка logs уже создана
    logs_dir.mkdir(parents=True, exist_ok=True)
    # 3. Объединяем путь к папке с именем файла app.txt
    file_path = logs_dir / "app.txt"
    # 4. Открываем файл внутри созданной папки - для записи
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Application started successfully!\n")
    return

create_logs_folder()