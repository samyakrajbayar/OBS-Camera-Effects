# 🎥 OBS Camera Effects

A real-time camera effects application built with Python and OpenCV. Apply cool visual effects to your webcam or OBS virtual camera feed with simple keyboard controls.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![OpenCV](https://img.shields.io/badge/opencv-4.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **8 Real-time Effects:**
  - 🎬 Normal - Original camera feed
  - ✏️ Edge Detection - Sketch-like line art
  - 🎨 Cartoonify - Turn yourself into a cartoon
  - 🔴 Color Pop - Highlight red colors only
  - 🟦 Pixelate - Retro 8-bit style
  - 🪞 Mirror - Symmetrical face effect
  - 🌡️ Thermal - Heat vision camera
  - 📺 Glitch - Digital corruption effect

- **Easy Controls:** Switch effects with a single key press
- **Screenshot Support:** Save your favorite moments
- **Low Latency:** Real-time processing with minimal delay

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- A working webcam or OBS virtual camera

### Install Dependencies

```bash
pip install opencv-python numpy
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

## 📖 Usage

1. Run the program:
```bash
python obs_camera_effects.py
```

2. Use keyboard controls:
   - `SPACE` - Cycle through effects
   - `S` - Save screenshot (saved as `screenshot_YYYYMMDD_HHMMSS.png`)
   - `Q` - Quit application

3. The current effect name is displayed at the top of the window

## 🎮 Controls

| Key | Action |
|-----|--------|
| `SPACE` | Switch to next effect |
| `S` | Save screenshot |
| `Q` | Quit program |

## 🔧 Configuration

### Change Camera Source

By default, the program uses camera index `0`. To use a different camera:

```python
cap = cv2.VideoCapture(0)  # Change 0 to your camera index
```

### Adjust Effect Parameters

You can modify effect intensity by changing parameters in the code:

- **Pixelate size:** Change `pixel_size=15` in `apply_pixelate()`
- **Edge detection sensitivity:** Adjust threshold values in `apply_edge_detection()`
- **Glitch intensity:** Modify random ranges in `apply_glitch()`

## 📸 Screenshots

Screenshots are automatically saved to the current directory with timestamps.

Format: `screenshot_YYYYMMDD_HHMMSS.png`

## 🛠️ Requirements

```
opencv-python>=4.5.0
numpy>=1.19.0
```

## 🐛 Troubleshooting

**Camera not found:**
- Ensure your webcam is connected and not being used by another application
- Try different camera indices (0, 1, 2, etc.)

**Slow performance:**
- Close other applications using the camera
- Reduce your camera resolution
- Try simpler effects like Edge Detection or Mirror

**Import errors:**
- Reinstall OpenCV: `pip install --upgrade opencv-python`

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new effects
- Improve existing effects
- Optimize performance
- Fix bugs
- Improve documentation

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Future Ideas

- [ ] Add face detection effects
- [ ] Background removal/replacement
- [ ] Custom color filters
- [ ] Video recording capability
- [ ] GUI for effect parameters
- [ ] Multiple camera support
- [ ] Real-time filters combination
