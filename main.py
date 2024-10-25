import uuid

user = 'ph'
user2 = 'admin'
user3 = '7f'

password = 'admin'
users = {}

def identificador():
    return str(uuid.uuid4())

users = {
    user: {
        'User': user,
        'Password': password,
        'Identificador': identificador()
    },

    user2: {
        'User': user2,
        'Password': password,
        'Identificador': identificador()
    },

    user3: {
        'User': user3,
        'Password': password,
        'Identificador': identificador()
    },
}

print(users)