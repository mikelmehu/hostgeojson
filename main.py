import csv, os, json, requests
print(os.getcwd())

with open("datos_nuevos.csv", encoding="UTF-8", errors="ignore") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line = 0
    clientes = []
    for row in csv_reader:
        if (line == 0):
            print(f'Column names are {", ".join(row)}')
            line = line + 1
        else:
            line = line + 1
            print(row)
            calle = str(row[0])
            if calle == "#N/A":
                print("Ignorando línea: #N/A")
                continue
    
            cp = str(row[1])
            ciudad = str(row[2])
            pais = str(row[3])
            datos_21 = str(row[4])
            datos_22 = str(row[5])
            datos_23 = str(row[6])
            nombre = str(row[7])
            direccion = "{}, {} {} ({})" .format(calle, ciudad, cp, pais)
            url = "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token=pk.eyJ1IjoibWlrZWxtIiwiYSI6ImNsaHN4aXR4cjBkZ3Yza3Fwdm1iY3p4NTgifQ.1zj0w4X4BJ1D6qzG-xozRA".format(str(direccion))
            try:
                data = requests.get(url)
                data = json.loads(data.content)
                c = data["features"][0]["center"]
                coordenadas = str(c[0]) + "," + str(c[1])
                print("Analizando línea: " + str(line) + " coordenadas obtenidas: " + str(coordenadas))
                object = {"nombre":nombre, "direccion":direccion,"coordenadas":str(coordenadas) ,"datos":{"2021":datos_21, "2022":datos_22, "2023":datos_23, "id":line}}
                pass
            except Exception as e:
                print("Error al obtener coordenadas: " + str(e))
            clientes.append(object)

    print( line, " líneas")
    
    print({"clientes":clientes})
    f = open("clientes_nuevo.json", "a")
    json.dump({"clientes":clientes}, f)
    f.close()