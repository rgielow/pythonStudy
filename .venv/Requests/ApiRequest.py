from pip._vendor import requests
import json

url = 'https://dc1-2021.glitch.me/getHash'
myobj = {'rm': '87978', 'senha': 'BLn8Fh8sGA'}

response = requests.post(url, data = myobj)
response_dict = json.loads(response.text)

for i in response_dict:
    if i == "hash":
        print(response_dict[i])


