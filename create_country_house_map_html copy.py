import folium
import pandas as pd

# Read the CSV file
data = pd.read_csv('data/recommended_houses_locations.csv')

# Create a map centered around the average latitude and longitude
center_lat = data['latitude'].mean()
center_lon = data['longitude'].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# Add markers to the map
for _, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['name']
    ).add_to(m)

# Save the map to an HTML file
m.save("data/recommended_houses_csv_map.html")

# Display the map in a Jupyter notebook (optional)
