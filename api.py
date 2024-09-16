import requests

API_KEY = ''
URL = 'https://api.freecurrencyapi.com/v1/latest?currencies=&apikey='


def get_actual_currencies():
    url = URL + API_KEY
    response = requests.get(url)
    return response.json()
