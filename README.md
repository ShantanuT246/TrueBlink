# 👁️ TrueBlink

**TrueBlink** is a Python-based utility that extracts eye landmarks from video frames using MediaPipe and computes the Eye Aspect Ratio (EAR) for blink detection. This forms the core of a deepfake detection pipeline, inspired by the DeepVision research methodology. Designed for modularity, clarity, and experimentation, this project is ideal for researchers, developers, and students exploring facial dynamics and biometric authenticity.

---

## 🚀 Features

- 🎯 Accurate eye landmark detection via **MediaPipe Face Mesh**
- 📏 EAR computation for both left and right eyes
- 🎥 Frame extraction from video input
- 🧪 Ideal for testing blink-based biometric analysis or deepfake forensics

---

## 🧠 How It Works

TrueBlink uses the six key landmarks around each eye to compute the **Eye Aspect Ratio (EAR)**:

- For each eye:
  - 2 horizontal landmarks: outer & inner corners
  - 4 vertical landmarks: upper and lower eyelids

The EAR is calculated as:

```
EAR = (‖p2−p6‖ + ‖p3−p5‖) / (2 × ‖p1−p4‖)
```

This value drops sharply when the eye blinks, making it a reliable indicator of eye state.

---

## 🛠️ Requirements

Install the dependencies using pip:

```bash
pip install opencv-python mediapipe numpy
```

---

## 📁 Project Structure

```bash
TrueBlink/
├── main.py               # Main script to run EAR extraction
├── test.mov              # Sample video input
└── README.md             # Documentation
```

---

## ▶️ Usage

1. Place your input video (e.g., `test.mov`) in the project directory.
2. Run the script:

```bash
python main.py
```

3. Output will display:
   - Pixel coordinates of key eye landmarks
   - EAR values for the left and right eye

Example output:
```
Right Eye Points: [[x1, y1], [x2, y2], ...]
Left Eye Points: [[x1, y1], [x2, y2], ...]
Right EAR: 0.293
Left EAR: 0.287
```

---

## 📊 Applications

- Deepfake detection via blink pattern irregularities
- Eye blink-based liveness detection for authentication
- Academic experimentation in human-computer interaction (HCI)
- Real-time alertness monitoring systems (when extended)

---

## 🧩 Next Steps

- ⏱ Extend to track EAR over time for full blink detection
- 📈 Visualize EAR vs. time using Matplotlib
- 🎯 Classify videos as “Likely Real” or “Likely Fake” based on blink metrics

---

## 🧑‍💻 Author

**Shantanu Tapole**  

