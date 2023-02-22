import folium

# Create a map centered on the city coordinates
m = folium.Map(location=[45.0078322, 19.8187834], zoom_start=12)

# Add the city borders to the map
folium.GeoJson(f'https://data.cityofnewyork.us/api/geospatial/cpf4-rkhq?method=export&format=GeoJSON').add_to(m)

# Display the map
m
m.save('aee.html')