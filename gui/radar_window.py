import sys
import math
import json
from PyQt5.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem,
    QGraphicsTextItem, QVBoxLayout, QWidget, QPushButton, QInputDialog, QMenu
)
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

class RadarWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NetRadarX-Pro: Radar View")
        self.setGeometry(100, 100, 600, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.view = QGraphicsView()
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.view.setRenderHint(self.view.viewport().Antialiasing)
        self.view.setSceneRect(-250, -250, 500, 500)
        self.layout.addWidget(self.view)

        self.add_button = QPushButton("Add Device")
        self.add_button.clicked.connect(self.add_device)
        self.layout.addWidget(self.add_button)

        self.devices = []
        self.draw_radar_background()
        self.plot_radar()

    def draw_radar_background(self):
        pen = QPen(QColor("green"))
        for r in range(50, 251, 50):
            circle = QGraphicsEllipseItem(-r, -r, r*2, r*2)
            circle.setPen(pen)
            self.scene.addItem(circle)

        for angle in range(0, 360, 30):
            x = 250 * math.cos(math.radians(angle))
            y = 250 * math.sin(math.radians(angle))
            self.scene.addLine(0, 0, x, y, pen)

    def plot_radar(self):
        self.scene.clear()
        self.draw_radar_background()

        for i, device in enumerate(self.devices):
            angle = (i * 360 / len(self.devices)) % 360
            radius = device["range"] * 50
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))

            color = QColor("green") if device.get("is_new", False) else QColor("white")
            dot = self.scene.addEllipse(x-5, y-5, 10, 10, QPen(Qt.NoPen), QBrush(color))
            dot.setData(0, json.dumps(device))
            dot.setToolTip(f"{device['name']}\n{device['mac']}")

            label = QGraphicsTextItem(device["name"])
            label.setDefaultTextColor(color)
            label.setPos(x + 10, y)
            self.scene.addItem(label)

        self.view.viewport().installEventFilter(self)

    def add_device(self):
        name, ok1 = QInputDialog.getText(self, "Device Name", "Enter device name:")
        mac, ok2 = QInputDialog.getText(self, "MAC Address", "Enter MAC address:")
        range_val, ok3 = QInputDialog.getInt(self, "Range (1-5)", "Enter device range (1-5):", min=1, max=5)

        if ok1 and ok2 and ok3:
            device = {
                "name": name,
                "mac": mac,
                "range": range_val,
                "is_new": True
            }
            self.devices.append(device)
            self.plot_radar()

    def eventFilter(self, source, event):
        if event.type() == event.MouseMove:
            pos = self.view.mapToScene(event.pos())
            for item in self.scene.items():
                if isinstance(item, QGraphicsEllipseItem):
                    if item.contains(item.mapFromScene(pos)):
                        self.show_context_menu(item, event.globalPos())
                        break
        return super().eventFilter(source, event)

    def show_context_menu(self, item, global_pos):
        data = json.loads(item.data(0))
        menu = QMenu()
        action = menu.addAction(f"Attack {data['name']}")
        action.triggered.connect(lambda: self.perform_attack(data))
        menu.exec_(global_pos)

    def perform_attack(self, device):
        print(f"[!] Attack launched on {device['name']} ({device['mac']})")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    radar = RadarWindow()
    radar.show()
    sys.exit(app.exec_())
