# print("Hello World")
# result = 10/0
# print(result)
#
# print("Bye World")
#
# def div_int(a,b):
#     return a/b
# print("start program")
# result = div_int(10,0)
#
# print(result)
# print("end program")


# # try exeption
# print("Hello World")
# try:
#     result = 10/0
#     print(result)
# except Exception as e:
#     print("An error occured: e")
#
# print("bye")
#
# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print("result:", result)
#
# except ValueError:
#     print("ValueError")
#
# except ZeroDivisionError:
#     print("Zero Error")


def calculator(a:float, b:float,operator:str):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    raise ValueError("Invalid operator")

# parsing convert string into numbers
def pars(a_str:str, b_str: str, operator:str):
    a = float(a_str)
    b = float(b_str)
    return calculator(a,b,operator)

#dialog

def run():
   try:
      a = input("Enter first number: ")
      b = input("Enter second number: ")
      operator = input("Enter Action operator (+,-,*,/):  ")
      result = pars(a,b,operator)
      print(f"Result: {result}")
   except ValueError as e:
      print(f"Invalid input: {e}")
   except ZeroDivisionError:
      print(f"Cannot divide by zero")

run()


