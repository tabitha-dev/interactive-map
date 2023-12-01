from flask import Flask
import folium
import os

app = Flask(__name__)


@app.route('/')
def show_map():
  # Create a map centered on Washington State
  map = folium.Map(location=[47.7511, -120.7401], zoom_start=7)

  # Add markers for various places
  locations = {
      "Seattle": [47.6062, -122.3321],
      "Olympia": [47.0458, -122.896],
      "Redmond": [47.6740, -122.1215],
      "Bellevue": [47.6101, -122.2015],
      "Sammamish": [47.6163, -122.0356],
      "Issaquah": [47.5301, -122.0326],
      "Bothell": [47.7601, -122.2054],
      "Mercer Island": [47.5707, -122.2221],
      "Kenmore": [47.7573, -122.2440],
      "Woodinville": [47.7543, -122.1635],
      "Mount Baker": [48.7769, -121.8144],
      "Mount Rainier": [46.8523, -121.7603],
      "Olympic National Park": [47.8021, -123.6044],
      "Seattle Center and the Space Needle": [47.6205, -122.3493],
      "San Juan Islands": [48.6099, -122.9554]
  }

  for place, coords in locations.items():
    # Differentiate iconic locations with unique icons
    if place in [
        "Mount Baker", "Mount Rainier", "Olympic National Park",
        "Seattle Center and the Space Needle", "San Juan Islands"
    ]:
      folium.Marker(coords,
                    popup=f'<strong>{place}</strong>',
                    icon=folium.Icon(color='green', icon='tree')).add_to(map)
    else:
      folium.Marker(coords,
                    popup=f'<strong>{place}</strong>',
                    icon=folium.Icon(color='blue',
                                     icon='info-sign')).add_to(map)

  # Return the HTML representation of the map
  return map._repr_html_()


if __name__ == '__main__':
  # Get the port from the environment variable or use 5000 as default
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port)
