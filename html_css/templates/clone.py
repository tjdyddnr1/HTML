import requests

url = "https://api.bithumb.com/public/ticker/ALL_KRW"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)