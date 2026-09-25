from typing import assert_type


def greet(name):
    return f'Hello, {name}!'

result = greet("Vera")
print(result)

#result2 = greet()
#print(result2)

def create_user (name, role = "User"):
    return {"name": name, "role": role}

print(create_user("Alex"))
print(create_user("Vera","Admin"))

def cal_discount(price, discount=20):
    return price - (price * discount/100)

print(cal_discount(100))
print(cal_discount(3000,25))

#def foo(a=2,b):
#    return a+b
#print(foo(5,2))


def add_tests(name, results=[]):
    results.append(name)
    return results

print(add_tests("test_registration"))
print(add_tests("print_login"))


def add_tests(name, results=None):
    if results is None:
        results = []
    results.append(name)
    return results


print(add_tests("test_registration"))
print(add_tests("test_login"))

def create_user2(username, email, role):
    return f"{username} ({email})- {role}"

print(create_user2("Alex", "alex@gmail.com", "Admin"))
print(create_user2(role="Project",username="Alex",email="test2@gm.com"))

print(create_user2("Kristina",role="QA",email="qa@gm.com"))

def total(*args):
    print(type(args),args)
    return sum(args)
print(total(1,2,3,4,5,6))
print(total(10,20,30,40,50,60))
print(total())

def print_scores(students,*scores):
    print(f"Students: {students}")
    print("scores: ", scores)

print_scores("Kristina",30,20,45)
print_scores("Alex",60)


def check_status_codes(*codes):
    for code in codes:
        assert code == 200
    return True


print(check_status_codes(200, 200, 200))
#print(check_status_codes(200, 400, 200))

