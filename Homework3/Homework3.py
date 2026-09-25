"""
1. Написать функцию print_list_reverse(lst)
Функция принимает список и выводит этот список в консоль
в обратном порядке.
Если lst равен None, пустой список,
или если аргумент не является объектом типа list,
функция должна вывести:
Wrong list
Пример:
print_list_reverse([1, 2, 3, 4, 5])
Вывод в консоль:
[5, 4, 3, 2, 1]
"""
print("Task1")

def print_list_reverse(lst: list):
    if (lst is None) or (type(lst) is not list) or (len(lst) == 0):
        print ("Wrong list")
    else:
        print(lst[::-1])

print_list_reverse([])
print_list_reverse(([1, 2, 3, 4, 5]))

print("____________")

"""
2. Написать функцию is_valid_point(point)
Функция принимает кортеж и проверяет, 
является ли он корректной точкой на плоскости.
Условия корректной точки:
 • аргумент должен быть кортежем (tuple), 
 а не списком или другим типом;
 • кортеж состоит ровно из 2 элементов;
 • оба элемента являются числами (int или float).
Если кортеж соответствует всем условиям, 
функция возвращает True.
Если аргумент не соответствует условиям, 
функция возвращает False.

Примеры:
is_valid_point((3, 5))      # True
is_valid_point((3, "5"))    # False
is_valid_point([3, 5])      # False
is_valid_point((1, 2, 3))   # False
is_valid_point(())          # None
is_valid_point(None)        # None
"""
print("Task2")

def is_valid_point(point:tuple):
    if point is None:
        return None
    if type(point) is not tuple:
        return False
    if len(point) == 0:
        return None
    if len(point) != 2:
        return False
    if not isinstance(point[0], (int, float)) or not isinstance(point[1], (int, float)):
        return False
    else:
        return True


print(is_valid_point((3, 5)))      # True
print(is_valid_point((3, "5")))    # False
print(is_valid_point([3, 5]))      # False
print(is_valid_point((1, 2, 3)))   # False
print(is_valid_point(()))          # None
print(is_valid_point(None))        # None

print("____________")


"""
3. Написать функцию print_sublist_reverse(lst, start, finish)
Функция принимает список, стартовый индекс и финишный индекс.
Нужно вывести в консоль список, в котором элементы 
от индекса start до индекса finish включительно 
расположены в обратном порядке, а остальные элементы 
остаются в обычном порядке.
Пример:
print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
Исходный список:
[10, 20, 30, 40, 50, 60]
Часть списка от индекса 1 до индекса 3 включительно:
[20, 30, 40]
После реверса:
[40, 30, 20]
Вывод в консоль:
[10, 40, 30, 20, 50, 60]
Если lst равен None, пустой список, 
не является списком, если start / finish не являются целыми 
числами, если индексы start / finish выходят за пределы списка, 
или start > finish, функция должна вывести:
Wrong args
Пример:
print_sublist_reverse([1, 2, 3], "0", 2)  
# Wrong args (start не является целым числом)
"""
print("Task3")

def print_sublist_reverse(lst:list, start:int, finish: int):
    result=[]
    if ((lst == None) or (lst==[]) or (type(lst) is not list)):
        return "Wrong args"
    if ((type(start) is not int) or (type(finish) is not int)):
        return "Wrong args"
    if ((start<0) or (start >= len(lst))
        or (finish<0) or (finish >= len(lst))
        or (start>finish)):
        return "Wrong args"
    result = lst[:start] + lst[start:finish + 1][::-1] + lst[finish + 1:]
    return result




print(print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3))
print(print_sublist_reverse([1, 2, 3], "0", 2))

print("____________")



"""
4. Advanced — Написать функцию get_students_by_grade(students)
Функция принимает словарь, где ключ — имя студента, 
а значение — его оценка.
Нужно вернуть новый словарь, где ключ — оценка, 
а значение — список имён студентов, получивших эту оценку.
Пример:
get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85})
Результат:
{90: ["Alice", "Diana"], 85: ["Bob", "Charlie"]}
Если students равен None, 
является пустым словарём или аргумент не является словарём, 
функция должна вернуть пустой словарь:
{}
"""
print("Task4")

def get_students_by_grade(students:dict)-> dict:
    result={}
    if ((students == None) or (students=={}) or (type(students) is not dict)):
        return result
    for name, grade in students.items():
        if not isinstance(name, str) or not isinstance(grade, int):
            return result
        if grade not in result:
            result[grade] = []
        result[grade].append(name)

    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))
print("____________")
