import folium

custom_maps = {
    'Google Maps': folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='Google',
        name='Google Maps',
        # overlay=True,
        control=True
    ),
    'Google Satellite': folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='Google',
        name='Google Satellite',
        # overlay=True,
        control=True
    ),
    'Google Terrain': folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr='Google',
        name='Google Terrain',
        # overlay=True,
        control=True
    ),
    'Google Satellite Hybrid': folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr='Google',
        name='Google Satellite',
        # overlay=True,
        control=True
    ),
    'Esri Satellite': folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri Satellite',
        # overlay=True,
        control=True
    )
}

default_maps = ['openstreetmap', 'Stamen Toner', 'Stamen Terrain',
                'Stamen Watercolor', 'CartoDB positron', 'CartoDB dark_matter']

# default_maps = ['openstreetmap']

style1 = {'fillColor': '#000000',
          'color': '#000000',
          'weight': 1,
          'fillOpacity': 0.1,
          'fill': True}

style2 = {'fillColor': '#0096FF',
          'color': '#0096FF	',
          'weight': 1,
          'fillOpacity': 0.2,
          'fill': True}

style3 = {'fillColor': '#FF0000',
          'color': '#FF0000',
          'weight': 1,
          'fillOpacity': 0.2,
          'fill': True}
