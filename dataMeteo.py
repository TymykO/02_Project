import requests
import json

#352200375, WARSZAWA-OKĘCIE id_Warszawa 12375

meteo = requests.get('https://danepubliczne.imgw.pl/pl/datastore?product=Meteo')

dane_meteo = meteo.json()

print(dane_meteo)

for x in dane_meteo:

    line = x
    print(line)

