import requests

api_key = "****"
text = "****"
sender = "****" # the line number that shows in sender_lines.py
recipient = "****"

url = f"https://api.sms-webservice.com/api/V3/Send?ApiKey={api_key}&Text={text}&Sender={sender}&Recipients={recipient}"

payload = {}
headers = {}

try:
    response = requests.get(url, headers=headers, data=payload)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.HTTPError as err:
    print(err)
