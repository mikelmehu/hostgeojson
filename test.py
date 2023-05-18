import json
from json import JSONDecodeError
file = open("clientes_id.json", "r")
try:
    json.loads(file.read())
    print("Json loaded successfully")
except JSONDecodeError as e:
    print("Error occurred: " + str(e))
file.close()