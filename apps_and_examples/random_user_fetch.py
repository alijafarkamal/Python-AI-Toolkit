import requests

url = "https://randomuser.me/api/"
response = requests.get(url)
user = response.json()["results"][0]
print(f"{user['name']['first']} {user['name']['last']} from {user['location']['country']}")
