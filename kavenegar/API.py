import requests

API_KEY = '****'

url = f"https://api.kavenegar.com/v1/{API_KEY}/sms/send.json"

data = {
    'receptor': '****',
    'message': '****',
    'sender': '****'
}

response = requests.post(url, data)
print(response)
