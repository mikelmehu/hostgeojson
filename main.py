import csv, os, json, requests
print(os.getcwd())
with open("datos.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    clientes = []
    for row in csv_reader:
        if (line == 0):
            print(f'Column names are {", ".join(row)}')
            line = line + 1
        else:
            line = line + 1
            direccion = str(row[2]) + ", ", str(row[3]) + ", " + str(row[4]) + " " + str(row[5]) + " (" + str(row[6]) + ")"
            direccion = str(direccion)
            direccion = direccion.replace("'", "")
            direccion = direccion.replace('"', '')
            direccion = direccion.replace("(", "")
            direccion = direccion.replace(")", "")
            coordenadas = None
            url = "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token=pk.eyJ1IjoibWlrZWxtIiwiYSI6ImNsaHN4aXR4cjBkZ3Yza3Fwdm1iY3p4NTgifQ.1zj0w4X4BJ1D6qzG-xozRA".format(str(direccion))
            try:
                data = requests.get(url)
                data = json.loads(data.content)
                c = data["features"][0]["center"]
                coordenadas = str(c[0]) + "," + str(c[1])
                print("Analizando línea {d}. Coordenadas obtenidas: {c}" .format(d=str(line), c=str(coordenadas)))
            except Exception as e:
                print("Error al obtener coordenadas: " + str(e))
            object = {"direccion":direccion, "coordenadas":coordenadas, "nombre":str(row[1]), "telefono":str(row[7]), "email":str(row[9])}
            clientes.append(object)

    print( line, " líneas")
    
    print({"clientes":clientes})
    f = open("clientes_nuevo.json", "a")
    json.dump({"clientes":clientes}, f)
    f.close()