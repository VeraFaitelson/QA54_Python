books = {
    'Lev Tolstoy': 'Anna Karenina',
    'Anton Chekhov': 'Thr Cherry Orchard'
}

books2 = {
    'Lev Tolstoy',
    'Anton Chekhov'
}

print(books)
print(type(books))

print(books2)
print(type(books2))

response = {
    'StatusCode': 200,
    'user': {
    'id':1, 'name': 'Kristina'
            }
}

print(response['user']['name'])

data = [1,2,3]
print(isinstance(data,list))

value = 22
print(type(value))
print(isinstance(value,(int, float)))

value = 22.4
print(type(value))
print(isinstance(value,(int)))

value = 22
print(type(value))
print(isinstance(value,(int)))

team_ages = {

    "Kristina": 39,

    "Alex":40,

    "Tatiana": 54,

    "Andrey": 44,

    "Vladimir":65

}

print(

    team_ages.keys()

)

print(

    team_ages.values()

)

team_names = "Kristina", "Alex", "Tatiana", "Andrey", "Vladimir"
team_num = [39,40,54,44,65]

team_ages = {name: age for name, age in zip(team_names,team_num)}

print(team_ages)


team_names1 = "Kristina", "Alex", "Tatiana", "Andrey", "Vladimir"
team_num1 = [39,40,54,44]

team_ages1 = {name: age for name, age in zip(team_names1,team_num1)}

print(team_ages1)