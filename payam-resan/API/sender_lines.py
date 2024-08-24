import requests

url = "https://api.sms-webservice.com/api/V3/AccountInfo"

payload = {
    "ApiKey": "****"
}

headers = {
    'Content-Type': 'application/json'
}

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.HTTPError as err:
    print(err)