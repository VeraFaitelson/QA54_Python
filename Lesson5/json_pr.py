import json

#dumps() - pyton->json str
# loads() - json -> pyton object
# dump() save puton object -> file.json (file)
# load() file.json ->> pyton (file)

user = {"username":"vera","age": 27, "is_admin": True}
json_str = json.dumps(user)
print(json_str)
print(type(json_str))

user = json.loads(json_str)
print()
print(user)
print(type(user))
print(user["username"])

test_config = {
    "url": "http://localhost:8080",
    "username": "Anna",
    "password": "Aw!3344",
    "timeout": 10
}

with open ("config.json", "w", encoding = "utf-8") as file:
    json.dump(test_config, file, indent = 4, ensure_ascii=False)

with open ("config.json", "r", encoding = "utf-8") as file:

    config = json.load(file)
    print(config)
    print(config["url"])