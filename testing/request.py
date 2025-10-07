import requests
from json import loads


url = "http://localhost:5000/generate"

p = input()

prompt = {
    "input_text" : f"{p}"
}

response = requests.post(url, json=prompt)

print(response.json()["generated_text"])