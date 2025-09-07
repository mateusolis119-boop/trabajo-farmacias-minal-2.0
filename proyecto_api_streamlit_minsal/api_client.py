import requests

URL_LOCALES = 'https://midas.minsal.cl/farmacia_v2/WS/getLocales.php'
URL_TURNOS = 'https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php'

def get_locales(timeout=60):
    r = requests.get(URL_LOCALES, timeout=timeout)
    r.raise_for_status()
    return r.json()

def get_turnos(timeout=60):
    r = requests.get(URL_TURNOS, timeout=timeout)
    r.raise_for_status()
    return r.json()
