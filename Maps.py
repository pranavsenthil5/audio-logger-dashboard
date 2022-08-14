from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QGridLayout, QTextEdit, QWidget, QLabel, QToolBar, QStatusBar, QPlainTextEdit
import folium
import map_config as mc
import json
from window import Window
import sys


class Folium_Map():
    def __init__(self, tile_json_location, team_json_location):
        self.map = folium.Map(location=[38.8542, -78.5850],
                              zoom_start=10, max_bounds=True)
        self.tile_geojson = json.load(open(tile_json_location))
        self.team_geojson = json.load(open(team_json_location))

        print(self.team_geojson)
        print(self.tile_geojson)

        self.add_default_maps()
        # self.add_custom_maps()
        self.add_map_style()
        self.add_layer_control()

        self.save_map("index.html")

    def add_map_style(self):
        folium.GeoJson(self.tile_geojson, name="Tiles",
                       style_function=lambda x: mc.style1).add_to(self.map)
        folium.GeoJson(self.team_geojson, name='Team Split',
                       style_function=lambda x: mc.style3 if x["properties"]["styleUrl"] == "#Team1" else mc.style2).add_to(self.map)

    def add_default_maps(self):
        for map_name in mc.default_maps:
            folium.TileLayer(map_name).add_to(self.map)
        print(1)

    def add_custom_maps(self):
        for map_name in mc.custom_maps:
            folium.TileLayer(map_name).add_to(self.map)
        print(2)

    def add_layer_control(self):
        folium.LayerControl().add_to(self.map)
        print(3)

    def save_map(self, filename):
        self.map.save(filename)
        print(4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window("Audio Logger Dashboard")
    map = Folium_Map("k2g_output/Tiles.json", "k2g_output/Team.json")

    map_view = QWebEngineView()

    map_view.setHtml(open("index.html", "r").read())

    # browser.setHtml(open("index.html", "r", encoding="utf-8").read())
    # browser.setHtml(open("google_maps_1.html", "r").read())
    # browser.setHtml(open("google_maps_2.html", "r").read())

    central_widget = QWidget()
    window._addCentralWidget(central_widget)

    lay = QGridLayout(central_widget)
    # lay.addWidget(browser, 0, 0, 2, 1)
    # lay.addWidget(QTextEdit(), 0, 1)
    # lay.addWidget(QTextEdit(), 1, 1)
    lay.addWidget(map_view, 0, 0, 2, 2)
    lay.addWidget(QTextEdit(), 0, 2, 1, 2)
    lay.addWidget(QTextEdit(), 1, 2, 1, 1)
    lay.addWidget(QPlainTextEdit(), 1, 3, 1, 1)

    # lay.setColumnStretch(0, 1)
    # lay.setColumnStretch(1, 1)

    # lay.setRowStretch(0, 1)
    # lay.setRowStretch(1, 1)

    lay.setColumnStretch(0, 1)
    lay.setColumnStretch(1, 1)
    lay.setColumnStretch(2, 1)
    lay.setColumnStretch(3, 1)

    lay.setRowStretch(0, 3)
    lay.setRowStretch(1, 2)

    window.showMaximized()
    sys.exit(app.exec())
