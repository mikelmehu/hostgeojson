import json

def convert_to_geojson(json_array):
    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }
    
    for item in json_array:
        coordinates = False
        if "coordenadas" not in item:
            pass
        try:
            coordinates = item.get("coordenadas")
        except AttributeError:
            print("Error: " + item)
            pass
        if coordinates:
            lat, lon = coordinates.split(",")
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(lat), float(lon)]
                },
                "properties": {
                    "id":str(item.get("id")),
                    "direccion":str(item.get("direccion")),
                    "nombre":str(item.get("nombre")),
                    "2021":str(item.get("datos")["2021"]),
                    "2022":str(item.get("datos")["2022"]),
                    "2023":str(item.get("datos")["2023"])
                }
            }
            geojson_data["features"].append(feature)
    
    return geojson_data


# Example usage
file = open("clientes_nuevo.json", "r")
out = open("clientes.geojson", "a")
geojson = convert_to_geojson(json.loads(file.read())["clientes"])

# Print the GeoJSON data
json.dump(geojson, out, indent=4)
out.close()
file.close()