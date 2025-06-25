import requests

# SpaceX API endpoint
url = "https://api.spacexdata.com/v4/launches/upcoming"

# Fetch upcoming launches
response = requests.get(url)
launches = response.json()

# Display details
print("Upcoming SpaceX Launches:")
for launch in launches[:5]:
    print(f"Mission: {launch['name']}")
    print(f"Date: {launch['date_utc']}")
    print(f"Rocket: {launch['rocket']}")
    print("-" * 20)
