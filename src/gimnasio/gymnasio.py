import json

with open('Datos/usuarios.json') as f:
  data = json.load(f)

print(data)

def printUsuarios():
    print(data)

def accessUsuario(id):
    if id in data["usId"]:
        for i in data["usuarios"]:
            if i["Id"] == id:
                print(i)

def altaUsuario(id, nombre):
    pass

def bajaUsuario(id):
    pass

if __name__=="__main__":
    pass
