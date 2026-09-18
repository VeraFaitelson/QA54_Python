#Task 1. Shopping cart
#Write a function clean_cart(cart). The list contains product names.
# Remove all occurrences of the string "sold out" and return
# the updated list.
#print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
#  #["milk", "bread", "coffee"]
#Hint: Be careful when removing elements while iterating through a list.

print ("Task 1")

def clean_cart(cart: list) -> list:
    clean = []
    for item in cart:
        if item != "sold out":
            clean.append(item)
    return clean

print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))

print ("___________")



#Write a function temperature_report(temperatures).
# Return a NEW list containing only temperatures greater than 25.
# print(temperature_report([21, 28, 19, 31, 25, 27]))
# #[28, 31, 27]
#Hint: Create an empty result list and add
# suitable values with append().

print ("Task 2")

def temperature_report(temperature: list) -> list:
    result = []
    for i in temperature:
        if i>25:
            result.append(i)
    return result

print(temperature_report([21, 28, 19, 31, 25, 27]))

print ("___________")

print ("Task 3")

#Write a function fix_balances(balances).
# Replace every negative value in the SAME
# list with 0. Return the list.
# print(fix_balances([120, -30, 50, -5, 0, 200]))
# [120, 0, 50, 0, 0, 200]
#Hint: Here you need indexes because you are changing list elements.

def fix_balances(balances: list) -> list:
    for i in range (len(balances)):
        if balances[i]<0:
            balances[i] = 0
    return balances

print(fix_balances([120, -30, 50, -5, 0, 200]))

print ("___________")

print ("Task 4")

#Write a function unique_items(items).
# Return a new list containing each value
# only once, preserving the original order. Do not use set().
#print(unique_items(["red", "blue", "red", "green", "blue"]))
# #["red", "blue", "green"]
#Hint: Before append(), check whether the
# value is already in the result list.


def unique_items(items: list) -> list:
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(unique_items(["red", "blue", "red", "green", "blue"]))

print ("___________")

print ("Task 5")

#Write a function longest_word(words).
#Find and return the longest word in the list.
#If several words have the same maximum length,
#return the first one. Do not use max().
#print(longest_word(["cat", "elephant", "python", "coffee"]))
# #"elephant"
#Hint: Keep the best word found so far and compare len().


def longest_word(words: list) -> str:
    a = ""
    for word in words:
        if len(words) > len(a):
            a = word
    return a

print(longest_word(["cat", "elephant", "python", "coffee"]))

