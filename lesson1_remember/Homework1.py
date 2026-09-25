print("Task 1")

#Task 1. Clean a Name
#Write a function clean_name(name).
#•	Remove spaces from the beginning and end of the string.
#•	Return the name in title case.
#Example:
#print(clean_name("   anna smith   "))
# #Anna Smith
#print(clean_name("DAVID COHEN"))
# #David Cohen
#Hint: Think about strip() and title().

def clean_name(name: str) -> str:
    return name.strip().title()

print(clean_name("   anna smith   "))
print(clean_name("DAVID COHEN"))

print("""------------------------------------------------""")

print("Task 2")
#Task 2. Normalize an Email
#Write a function normalize_email(email).
#•	Remove spaces from the beginning and end.
#•	Convert all letters to lowercase.
#•	Return the cleaned email.
#Example:
#print(normalize_email("  Anna.Smith@Example.COM  "))
## anna.smith@example.com
#Hint: Use strip() and lower().

def normalize_email(email: str) -> str:
    return email.strip().lower()

print(normalize_email("Anna.Smith@Example.COM"))

print("""------------------------------------------------""")

print("Task 3")

#Task 3. Check a File Name
#Write a function is_python_file(filename).
#•	Return True if the file name ends with .py.
#•	The check must work for .py, .PY, .Py, etc.
#Example:
#print(is_python_file("lesson.py"))
# #True
#print(is_python_file("HOMEWORK.PY"))
# #True
#print(is_python_file("notes.txt"))
# #False
#Hint: Normalize the case first, then use endswith().

def is_python_file(filename: str) -> bool:
    return filename.strip().lower().endswith(".py")

print(is_python_file("lesson.py"))
print(is_python_file("HOMEWORK.PY"))
print(is_python_file("notes.txt"))

print("""------------------------------------------------""")

print("Task 4")

#Task 4. Replace Words
#Write a function fix_message(message).
#•	Replace every occurrence of the word "bad" with "good".
#•	Return the new string.
#•	Remember: strings are immutable, so the original string itself is not changed.
#Example:
#message = "bad weather, bad mood"
#result = fix_message(message)
#print(result)
# #good weather, good mood
#print(message)
# #bad weather, bad mood
#Hint: Use replace().


def fix_message(message: str) -> str:
    cleaned_message = message.strip().lower()
    if ("bad" in cleaned_message):
        return cleaned_message.replace("bad","good")
    elif ("good" in cleaned_message):
        return cleaned_message.replace("good","bad")
    else:
        return cleaned_message

print(fix_message("bad weather, bad mood"))
print(fix_message("good weather, good mood"))
print(fix_message("hello world!"))


print("""------------------------------------------------""")

print("Task 5")

#Task 5. Count a Letter
#Write a function count_letter(text, letter).
#•	Count how many times letter appears in text.
#•	The check must be case-insensitive.
#Example:
#print(count_letter("Programming", "g"))
# #2
#print(count_letter("Mississippi", "I"))
# #4
#Hint: Convert both values to the same case and use count().

def count_letter(text: str, letter:str) -> int:
    cleaned_message = text.strip().lower()
    cleaned_letter = letter.strip().lower()
    return cleaned_message.count(cleaned_letter)

print(count_letter("Programming", "g"))
print(count_letter("Mississippi", " I "))


print("""------------------------------------------------""")

print("Task 6")

#Task 6. Create a Short Login
#Write a function create_login(first_name, last_name).
#•	Remove unnecessary spaces from both names.
#•	Convert both names to lowercase.
#•	Create a login in the format: first_name.last_name
#•	Return the result.
#Example:
#print(create_login("  Anna ", " SMITH  "))
## anna.smith
#Hint: You can combine several string methods in one task.

def create_login(first_name: str, last_name:str) -> str:
    cleaned_name = first_name.strip().lower()
    cleaned_last_name = last_name.strip().lower()
    return f"{cleaned_name}.{cleaned_last_name}"

print(create_login("  Anna ", " SMITH  "))


print("""------------------------------------------------""")

print("Bonus 1 - Task Split Full Name")

#Bonus 1. Split Full Name
#Write a function split_name(full_name).
# Assume the string contains exactly a first name
# and a last name separated by spaces.
#print(split_name("  Anna   Smith  "))
# #["Anna", "Smith"]
#Hint: strip() first, then split().


def split_name(full_name:str) -> list:
    parts = full_name.split()
    return parts

print(split_name("  Anna   Smith  "))


print("""------------------------------------------------""")

print("Bonus 2 - Simple Password Check")

#Write a function check_password(password).
#Return True only if all conditions are met:
#•	the password has at least 8 characters;
#•	it contains no spaces;
#•	it is not made only of letters;
#print(check_password("python123"))
# #True
#print(check_password("python"))
# #False
#print(check_password("python 123"))
# #False
#Hint: Remember len(), isspace()/the in operator, and isalpha().
#Before submitting
#•	All functions return a result with return.
#•	Add at least 2 of your own calls for each function.
#•	Try different letter cases and strings with extra spaces.
#•	Be ready to explain which string method you used and why.



def check_password(password:str) -> bool:
    if len(password) >= 8 and " " not in password:
                if password.isalnum() and not password.isalpha() and not password.isdigit():
                    return True
    else:
        return False

print(check_password("python123"))
print(check_password("python"))
print(check_password("python 123"))



#Variant 2

def check_password2(password:str) -> bool:
    if len(password) < 8:
        return False
    for char in password:
        if char.isspace():
            return False
    return True

print(check_password2("python123"))
print(check_password2("python"))
print(check_password2("python 123"))

#Variant 3

def check_password3(password:str) -> bool:
    return len(password)>=8 and " " not in password and not password.isalpha()


print(check_password3("python123"))
print(check_password3("python"))
print(check_password3("python 123"))

