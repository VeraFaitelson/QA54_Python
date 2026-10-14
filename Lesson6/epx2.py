# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print("Result:", result)
# except ValueError:
#     print("Error: Please enter a valid number")
# except ZeroDivisionError:
#     print("Error: Cannot enter zero number")

def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False

print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Kris"))
print(is_number(None))

try:
    value = int("39")
except ValueError:
    print("An error occurred")
else:
    print("Successfully: ",value)
finally:
    print("End of try")