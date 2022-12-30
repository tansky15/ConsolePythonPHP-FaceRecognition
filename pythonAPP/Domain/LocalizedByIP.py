import requests


def get_location(ip):
    ip_address = ip
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    return response


