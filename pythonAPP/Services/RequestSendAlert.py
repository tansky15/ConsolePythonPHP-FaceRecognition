import requests
from Domain.Camera import *
from Domain.GeoMap import *


def EnvoyerSignalement(nom_complet, nom_camera, ip, geomap):
    url = 'http://localhost:8080/myprojects/iisprotect-AI/projet-AI-Face-Recognition-To-Server/backendPHP/Services/sendName.php'
    res = requests.post(
        url, params={"nom_du_suspect": nom_complet, "ip": ip, "longitude": geomap._longitude, "latitude": geomap._latitude, "nom_camera": nom_camera})
    print(res.text)
