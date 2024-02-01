users = ["user", "user2", "user3"]
userspassword = ["nikita", "nikita2" , "nikita3"]

username = input("Vvedite login: ")
password = input("Vvedite parol: ")

if username in users:
    temp_index = users.index(username)
    temp_pass = userspassword[temp_index]
    print(temp_pass == password)
else:
    print(False)

