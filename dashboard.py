import sys
import io
import json
import folium

from PyQt5.QtWidgets import QApplication, QGridLayout, QTextEdit, QWidget, QLabel, QToolBar, QStatusBar, QPlainTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from window import Window


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window("Audio Logger Dashboard")

    geo_json_map_1 = json.load(open('k2g_output/Tiles.json'))
    geo_json_map_2 = json.load(open('k2g_output/Team.json'))
    # print(geo_json_map_1)

    m = folium.Map(location=[38.8542, -78.5850],
                   zoom_start=10, max_bounds=True)

    # folium.GeoJson(geo_json_map_1, name="Tiles",
    #                style_function=lambda x: style1).add_to(m)
    # folium.GeoJson(geo_json_map_2, name='Team Split',
    #                style_function=lambda x: style2).add_to(m)

    folium.GeoJson(geo_json_map_1, name="Tiles",
                   style_function=lambda x: style1).add_to(m)
    folium.GeoJson(geo_json_map_2, name='Team Split',
                   style_function=lambda x: style3 if x["properties"]["styleUrl"] == "#Team1" else style2).add_to(m)

    folium.LayerControl().add_to(m)

    data = io.BytesIO()
    # m.save(data, close_file=False)
    # browser.setHtml(data.getvalue().decode())

    m.save("index.html")
    browser = QWebEngineView()

    browser.setHtml(open("index.html", "r").read())

    # browser.setHtml(open("index.html", "r", encoding="utf-8").read())
    # browser.setHtml(open("google_maps_1.html", "r").read())
    # browser.setHtml(open("google_maps_2.html", "r").read())

    central_widget = QWidget()
    window._addCentralWidget(central_widget)

    lay = QGridLayout(central_widget)
    # lay.addWidget(browser, 0, 0, 2, 1)
    # lay.addWidget(QTextEdit(), 0, 1)
    # lay.addWidget(QTextEdit(), 1, 1)
    lay.addWidget(browser, 0, 0, 2, 2)
    lay.addWidget(QTextEdit(), 0, 2, 1, 2)
    lay.addWidget(QTextEdit(), 1, 2, 1, 1)
    lay.addWidget(QPlainTextEdit(), 1, 3, 1, 1)

    # lay.setColumnStretch(0, 1)
    # lay.setColumnStretch(1, 1)

    # lay.setRowStretch(0, 1)
    # lay.setRowStretch(1, 1)

    lay.setColumnStretch(0, 2)
    lay.setColumnStretch(1, 2)

    lay.setRowStretch(0, 2)
    lay.setRowStretch(1, 2)

    window.showMaximized()
    sys.exit(app.exec())
