s = "cat"
s = s.upper()
print(s)

s1 = "Hello"
s2 = 'Hello'
s3 = """Line one 
                Line two"""

print(s1)
print(s2)
print(s3)

print(s1, s2, s3, sep ="\n")


#len()

s = "Hello my group!"
print(len(s))

print(s[0])
print(s[4])
print(s[14])
print(s[-1])

#print(s[100])

#slicing -> my_string[start:end:step]
text = "automation"
       #0123456789
print(text[2:6])
print(text[:4])
print(text[4:])

print(text[:])

print(text[::2])

print(text[::-1])
print(text[:5:100])

name = "Mariia"
last_name = "Ivanova"
age = 25
print(name + " " + last_name + " - " + str(age))

print(f"Hi my name is {name} and my last name is {last_name} and i'm {age}")

#upper()___/lower()------
raw = "  Automation QA"
print(raw.upper())
print(raw.lower())

#strip() убирает пробелы в строке

print(raw.strip().upper())

#split()/join()
cvs_line = "Login,Cart,Chekout"
parts = cvs_line.split(",")
print(parts)

cvs_line = "Login:Cart,Chekout,Mama,Papa"
parts = cvs_line.split(",")
print(parts)

print(" - ".join(parts))


#replace()
msg = "Test failed: element not found"
print(msg.replace("failed", "passed"))

#find() and index()
#find()-->-1, if substring is not found
#index()-->ValueError, if substring is not found

s = "banana"
print(s.find("na"))
print(s.index("na"))

print(s.find("xyz"))
#print(s.index("xyz"))

#count()
print(s.count("na"))