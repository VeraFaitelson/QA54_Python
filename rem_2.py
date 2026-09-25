for ch in "banana":
    print(ch)

#range(start,stop,step)

for i in range(3): #0 1 2
    print(i)

print("_____")

for i in range(2,5): #2 3 4
    print(i)

print("_____")

for i in range(2,13,2):  # 2 4 6 8 10 12
    print(i)

print("_____")

count = 0
while count<3:
    print(count)
    count += 1


#for fruit in fruits:
# append(), insert(), extend()

fruits = ["apple", "banana", "orange"]
print(fruits)


fruits.append("kiwi")
print(fruits)

fruits.append(["car","trak"])
print(fruits)

fruits.extend(["cat","dog"])
print(fruits)

fruits.insert(4,"pear")
print(fruits)

#удаление remove()-удалить объект который не знаю где,
# pop() - удаляет элемент из списка по индексу, он его возвращает
# del - не метод списка. оператор пайтона. удаляет элемент по индексу, но ничего не возвпащает
# clear() - удаление все содержимое - осается пустой список

print("del")
e = ["apple", "banana", "orange"]
print(e)

e.remove("banana")
print(e)

print("_________")

f = ["apple", "banana", "orange"]
print(f)

popped = f.pop(1)# удалит 1 по индексу
print(popped,f)

popped = f.pop() #удалит последний
print(popped,f)

print("_________")

h = ["apple", "banana", "orange"]
print(h)

del h[0]
print(h)

print("_________")

k = ["apple", "banana", "orange"]
print(k)

k.clear()
print(k)

# поиск и подсчет index(),count(),in, not in

m = ["apple", "banana","cherry", "orange"]
print(m.index("cherry"))
print(m.count("banana"))
print("apple" in m)
print("kiwi" not in m)

#сортировка sort(), sorted(), reverse()

numbers = [3,1,5,2,9,6]
result = numbers.sort()
print(numbers,result)

numbers_2 = [3,1,5,2,9,6]
new_list = sorted (numbers_2)
print(numbers_2,new_list)

numbers_3 = [3,1,5,2,9,6]
numbers_3.reverse()
print(numbers_3)


numbers_4 = [3,1,5,2,9,6]
print(sorted(numbers_4,reverse=True))

# перебор
items = ["apple", "banana", "orange"]

for item in items:
    print(item)

for i in range(len(items)):
    print(i,items[i])

numbers_5 = [-2,3,-1,5,0,-9]
result = []
for n in numbers_5:
    if n>0:
        result.append(n)
print(result)

result2 = [n for n in numbers_5 if n>0]
print(result2)
