import json

file = open("clientes.json", "r")
data = json.loads(file.read())
file.close()
id = 1
datos = []
for item in data["clientes"]:
    item["id"] = str(id)
    datos.append(item)
    id = id + 1

f = open("clientes_id.json", "a")
json.dump(datos, f)
f.close()