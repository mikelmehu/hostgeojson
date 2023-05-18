import json
from json import JSONDecodeError
file = open("clientes_id_nuevo.json", "r")
try:
    data = json.loads(file.read())
    print("Json loaded successfully")
    print(data["clientes"])
except JSONDecodeError as e:
    print("Error occurred: " + str(e))

file.close()