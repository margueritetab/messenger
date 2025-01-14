import requests

response = requests.get('https://eleves.mines-paris.eu')

print(response.status_code, response.text[:300])