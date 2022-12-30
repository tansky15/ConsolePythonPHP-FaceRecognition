from Services.RequestSendAlert import EnvoyerSignalement
import requests


class Camera:
    def __init__(self, nom_camera, ip, geomap):
        self._ip = ip
        self._geomap = geomap
        self._nom_camera = nom_camera

    def getCameraName(self):
        return self._nom_camera

    def SignalerSuspect(self, nom_complet):
        EnvoyerSignalement(
            nom_complet, self._nom_camera, self._ip, self._geomap)
