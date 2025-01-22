import requests

# Base URL for SpaceX API
base_url = "https://api.spacexdata.com/v4"

# Fetch upcoming launches
launches_url = f"{base_url}/launches/upcoming"
response = requests.get(launches_url)
upcoming_launches = response.json()

print("Upcoming SpaceX Launches (Detailed):")
for launch in upcoming_launches[:5]:
    mission_name = launch.get("name", "N/A")
    launch_date = launch.get("date_utc", "N/A")
    rocket_id = launch.get("rocket", None)
    payload_ids = launch.get("payloads", [])
    
    # Fetch rocket details
    rocket_name = "Unknown"
    if rocket_id:
        rocket_response = requests.get(f"{base_url}/rockets/{rocket_id}")
        rocket_name = rocket_response.json().get("name", "Unknown")
    
    # Fetch payload details
    payload_names = []
    for payload_id in payload_ids:
        payload_response = requests.get(f"{base_url}/payloads/{payload_id}")
        payload_data = payload_response.json()
        payload_names.append(payload_data.get("name", "Unknown"))

    print(f"Mission: {mission_name}")
    print(f"Launch Date (UTC): {launch_date}")
    print(f"Rocket: {rocket_name}")
    print(f"Payloads: {', '.join(payload_names) if payload_names else 'N/A'}")
    print("-" * 40)
