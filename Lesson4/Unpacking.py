def login(username,password):
    print(username,password)

data = ["admin","254646"]
login(data[0],data[1])

login(*data)

user = {
    "username":"admin",
    "password":"35353535"
}

login(**user)

# user2 = {
#     "username":"admin",
#     "password":"25255",
#     "remember_me":True
# }
#
# login(**user2)

