import requests

API_KEY = "AIzaSyA5sJdTuzthrQkJgAZwFMURWtynWcGqRXE"
CSE_ID = "c240fe0982ba44fae"
query = "data scientist jobs in india"

url = "https://www.googleapis.com/customsearch/v1"
params = {
    "key": API_KEY,
    "cx": CSE_ID,
    "q": query,
    "num": 5
}

response = requests.get(url, params=params)
data = response.json()

for item in data.get("items", []):
    print(item["title"], item["link"], item["snippet"])