import json

import requests

headers = {
"Content-Type": "application/json"
}

payload = {
        "name": "Test Movie",
        "price": 500,
        "description": "Описание тестового фильма",
        "location": "MSK",  # Исправлено значение location
        "published": True,
        "genreId": 1  # Исправлено значение genreId
    }
response = requests.post(url='https://webhook.site/f863c403-5276-4b7f-9128-5491383ac7b8', data=json.dumps(payload))

print(response.status_code)
