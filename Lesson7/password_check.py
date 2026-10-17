import re


def has_digits(password):
    return bool(re.search(r"\d",password))

print(has_digits("123"))
print(has_digits("qwerty"))

