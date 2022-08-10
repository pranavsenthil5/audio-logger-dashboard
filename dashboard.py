import sys
import io
import json
import folium

from PyQt5.QtWidgets import QApplication, QGridLayout, QTextEdit, QWidget, QLabel, QToolBar, QStatusBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Window import Window


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window("Audio Logger Dashboard")

    geo_json_map_1 = json.load(open('input_files/actual 1.geojson'))
    geo_json_map_2 = json.load(open('input_files/actual 2.geojson'))
    geo_json_map_3 = json.load(open('shenandoah.geojson'))
    print(geo_json_map_1)

    m = folium.Map(location=[38.6694, -78.4987],  zoom_start=14)

    style1 = {'fillColor': '#000000',
              'color': '#000000',
              'weight': 1}

    style2 = {'fillColor': '#ff0000',
              'color': '#0096FF	',
              'weight': 3,
              'fillOpacity': 1,
              'dashArray': '5, 5'}

    folium.TileLayer('openstreetmap').add_to(m)
    folium.TileLayer('Stamen Toner').add_to(m)
    folium.TileLayer('Stamen Terrain').add_to(m)
    folium.TileLayer('Stamen Watercolor').add_to(m)
    folium.TileLayer('CartoDB positron').add_to(m)

    folium.GeoJson(geo_json_map_1, name="test1",
                   style_function=lambda x: style1).add_to(m)
    folium.GeoJson(geo_json_map_2, name='test2',
                   style_function=lambda x: style2).add_to(m)
    folium.GeoJson(geo_json_map_3, name="test1",
                   style_function=lambda x: style1).add_to(m)
    folium.LayerControl().add_to(m)

    data = io.BytesIO()
    # m.save(data, close_file=False)
    # browser.setHtml(data.getvalue().decode())

    m.save("index.html")
    browser = QWebEngineView()

    # browser.setHtml(open("index.html", "r", encoding="utf-8").read())
    browser.setHtml(open("index.html", "r").read())

    # browser.setHtml(open("google_maps_1.html", "r").read())
    # browser.setHtml(open("google_maps_2.html", "r").read())

    central_widget = QWidget()
    window._addCentralWidget(central_widget)

    lay = QGridLayout(central_widget)
    lay.addWidget(browser, 0, 0, 2, 1)
    lay.addWidget(QTextEdit(), 0, 1)
    lay.addWidget(QTextEdit(), 1, 1)

    lay.setColumnStretch(0, 1)
    lay.setColumnStretch(1, 1)

    lay.setRowStretch(0, 1)
    lay.setRowStretch(1, 1)

    window.show()
    sys.exit(app.exec())
