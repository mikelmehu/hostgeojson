import json, requests
f = open("clientes.geojson", "r")

data = json.loads(f.read())
f.close()

for cliente in data["features"]:
    features = cliente
    propertites = features["properties"]
    lat = float(str(cliente["geometry"]["coordinates"][0]).replace(",","."))
    long = float(str(cliente["geometry"]["coordinates"][1]).replace(",","."))
    direccion = str(propertites["direccion"])
    nombre = str(propertites["nombre"])
    f21 = float(str(propertites["2021"]).replace(",","."))
    f22 = float(str(propertites["2022"]).replace(",","."))
    f23 = float(str(propertites["2023"]).replace(",","."))
    obj = {"nombre":nombre, "direccion":direccion, "lat":lat, "long":long, "f21":f21, "f22":f22, "f23":f23}
    requests.post("https://39923278.servicio-online.net/appmapa/subir.php", headers={"User-agent":"Firefox"}, data=obj)