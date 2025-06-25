import folium
from geopy.geocoders import Nominatim
import webbrowser

location_name = input("Enter a location: ")

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:
    latitude = location.latitude
    longitude = location.longitude
    clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)

    marker = folium.Marker([latitude, longitude], popup=location_name)
    marker.add_to(clcoding)

    # Save the map to an HTML file
    map_file = "map.html"
    clcoding.save(map_file)

    # Open the map in the default web browser
    webbrowser.open(map_file)
else:
    print("Location not found. Please try again.")