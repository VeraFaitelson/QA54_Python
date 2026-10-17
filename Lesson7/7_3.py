import re

def is_valid_id(order_id):

    return bool(re.search("^ORD-...$",order_id))

print(is_valid_id("ORD-123"))
print(is_valid_id("ORD-12"))
print(is_valid_id("OOO-123"))

print(re.search("gr[ae]y","grey"))
print(re.search("gr[ae]y","groy"))
print(re.search("gr[ae]y","green"))

print(re.search("[a-z]","Kristina"))
print(re.search("[0-9]","Order #34"))
print(re.search("[A-Z]","kristina"))
print(re.search("[A-Za-z]","kristina"))
print(re.search("[A-Za-z]","kristina"))

print(re.search("[^0-9]","123456a"))
print(re.search("[^0-9]","123456"))
print(re.search("[^0-9]","123.45.6"))


print(re.search('\\d',"Order #34"))
print(re.search('\\w',"!!!Kristina"))
print(re.search('\\s',"Kristina QA 54"))

print(re.search(r'\d',"Order #34"))
print(re.search(r'\w',"!!!Kristina"))
print(re.search(r'\s',"Kristina QA 54"))



print(re.search(r"ab*c","ac"))
print(re.search(r"ab*c","abc"))
print(re.search(r"ab*c","abccccc"))


print(re.search(r"ab+c","ac"))
print(re.search(r"ab+c","abc"))
print(re.search(r"ab+c","abc"))

print(re.search(r"cocon?t","cocont"))
print(re.search(r"cocon?t","coconut"))
print(re.search(r"cocon?t","coconuut"))


print(re.search(r"\d{4}","13"))
print(re.search(r"\d{4}","5666613"))


print(re.search(r"\d{2,4}","123456"))
print(re.search(r"\d{3,4}","323"))



