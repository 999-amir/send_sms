import requests
import json

url = "https://gateway.ghasedak.me/rest/api/v1/WebService/SendSingleSMS"

payload = json.dumps({
  "lineNumber": "*****",
  "receptor": "*****",
  "message": "تست. لغو11",
})
headers = {
  'Content-Type': 'application/json',
  'ApiKey': "*******************************"
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
