import requests
import folium

response = requests.get("http://ckan2.multimediagdansk.pl/gpsPositions?v=2")
position = response.json()

m = folium.Map(location=[54.352025, 18.646638], zoom_start=13)

for bus in position['vehicles']:
    latitude = bus['lat']
    longitude = bus['lon']
    popup = f"Bus ID: {bus['vehicleCode']}, Line Number: {bus['routeShortName']}"
    marker = folium.Marker(location=[latitude, longitude], popup=popup)
    marker.add_to(m)

m.save('mapa.html')


# import requests
#
# response = requests.get("http://ckan2.multimediagdansk.pl/gpsPositions?v=2")
#
# position = response.json()
#
# data = {}
#
# for bus in position['vehicles']:
#     latitude = bus['lat']
#     longitude = bus['lon']
#
# import folium
#
#
# # Create a Folium map centered at a specific location
# m = folium.Map(location=[51.5074, 0.1278], zoom_start=12)
#
# # Add markers for each bus
# for index, row in bus_data.iterrows():
# folium.Marker([row['lat'], row['lon']], popup=row['bus_id']).add_to(m)

# Display the map
#m

    # for _id in payload_ids:
    #     response2 = requests.get(f"https://api.spacexdata.com/v4/payloads/{_id}")
    #     payload = response2.json()
    #     mass_kg = payload['mass_kg']
    #     # print(date, _id, mass_kg)
    #     if mass_kg is None:
    #         mass_kg = 0
    #     if date in data:
    #         data[date] = mass_kg + data[date]
    #     else:
    #         data[date] = mass_kg

