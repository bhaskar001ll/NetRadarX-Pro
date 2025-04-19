cat << 'EOF' > README.md
# NetRadarX-Pro

**NetRadarX-Pro** is a GUI-based network visualization tool built using PyQt5 and matplotlib. It features an interactive radar chart to display nearby devices and perform simulated actions on them.

---

## 📦 Required Libraries

- `PyQt5`: For GUI components
- `matplotlib`: For plotting the radar chart
- `numpy`: For calculations

### ✅ Installation

```bash
sudo apt update
sudo apt install python3-pyqt5
pip install -r requirements.txt

🚀 How to Run

cd NetRadarX-Pro
python3 main.py

🖥️ Features

    Radar Chart Visualization: Displays devices on a radar chart based on range.

    Add Device: Manually add devices with name, MAC address, and range.

    Hover Functionality: Shows context menu when hovering over a device.

    Attack Option: Simulated “Attack [Device Name]” action from context menu.

🛠️ Future Plans

    Implement real attack logic (educational purpose only)

    Save device data using a database

    Improve UI experience

🤝 Contributing

Feel free to fork the repo and submit pull requests. All contributions are welcome!
📄 License

This project is licensed under the MIT License.
👨‍💻 Maintainers

    bhaskar001ll EOF

echo -e "matplotlib\nnumpy\nPyQt5" > requirements.txt

git add README.md requirements.txt git commit -m "Added README and requirements.txt" git push

