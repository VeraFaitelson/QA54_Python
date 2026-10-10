with open("user.txt","w",encoding="utf-8") as file:
    file.write("Kristina\n")
    file.write("Alex\n ")

with open("user.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(len(content))


with open("user.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)

for line in lines:
    print(line.strip())

print()

with open("user.txt", "r", encoding="utf-8") as file:
    for line in lines:
        print(line.strip())

print()