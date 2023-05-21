import json
from json import JSONDecodeError
file = open("prueba.geojson", "r")
try:
    data = json.loads(file.read())
    print("Json loaded successfully")
except JSONDecodeError as e:
    print("Error occurred: " + str(e))

file.close()