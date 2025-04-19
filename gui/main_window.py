import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox, QInputDialog
from core.network_scanner import scan_network  # Only import scan_network
from attacks.ddos_simulator import simulate_ddos
from attacks.deauth_module import deauth_attack
from gui.radar_window import RadarWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NetRadarX-Pro")
        self.setGeometry(200, 100, 400, 400)

        layout = QVBoxLayout()
        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)

        self.scan_button = QPushButton("Scan Network")
        self.scan_button.clicked.connect(self.run_scan)

        self.ddos_button = QPushButton("Start DDoS Attack")
        self.ddos_button.clicked.connect(self.start_ddos)

        self.deauth_button = QPushButton("Start Deauth Attack")
        self.deauth_button.clicked.connect(self.start_deauth)

        self.radar_button = QPushButton("Open Radar View")
        self.radar_button.clicked.connect(self.open_radar)

        layout.addWidget(self.scan_button)
        layout.addWidget(self.ddos_button)
        layout.addWidget(self.deauth_button)
        layout.addWidget(self.radar_button)
        layout.addWidget(self.text_output)
        self.setLayout(layout)

    def run_scan(self):
        self.scan_button.setEnabled(False)
        self.text_output.clear()
        try:
            result = scan_network()
            self.text_output.setPlainText(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        finally:
            self.scan_button.setEnabled(True)

    def start_ddos(self):
        target_ip, ok = QInputDialog.getText(self, "DDoS Attack", "Enter target IP:")
        if ok and target_ip:
            result = simulate_ddos(target_ip)
            self.text_output.append(result)

    def start_deauth(self):
        target_mac, ok = QInputDialog.getText(self, "Deauth Attack", "Enter target MAC:")
        if ok and target_mac:
            result = deauth_attack(target_mac)
            self.text_output.append(result)

    def open_radar(self):
        self.radar_window = RadarWindow()
        self.radar_window.show()