import hashlib as hash
import json

usuarios = []

usuario = {
    "name": "Clark Kent",
    "username": "kent",
    "password": "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"
}

usuarios.append(usuario)

usuario = {
    "name": "Bruce Wayne",
    "username": "wayne",
    "password": "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"
}

usuarios.append(usuario)

usuario = {
    "name": "Christopher Walker",
    "username": "walker",
    "password": "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"
}

usuarios.append(usuario)

def verificaSenha(usuario, hash):
    for item in usuarios:
        if usuario == item.get('username'):
            if hash == item.get('password'):
                print("{} logado!".format(item.get('name')))
            else:
                print("Usuário/senha inválidos")

def verificaSeExisteUser(usuario, senhaEmHash):
    user = 0
    for item in usuarios:
        if usuario == item.get('username'):
            user = 1
    if user == 0:
        print("Usuário não existe")
    else:
        verificaSenha(usuario, senhaEmHash)

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
senhaEmBytes = bytes(senha, 'utf-8')

hash = hash.sha256()
hash.update(senhaEmBytes)
senhaEmHash = hash.hexdigest()
verificaSeExisteUser(usuario, senhaEmHash)
