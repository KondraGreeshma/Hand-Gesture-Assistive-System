# Hand Gesture–Based Assistive System

## 📌 Overview
A real-time hand gesture recognition system that detects finger counts using a webcam and triggers corresponding assistive actions with audio and visual feedback.

## 🚀 Features
- Real-time hand tracking using MediaPipe (via CVZone)
- Finger count detection
- Action-based image display
- Audio feedback for gestures
- Assistive and accessibility-focused system
- Prevents repeated audio playback

## 🧠 Use Cases
- Assistive technology for differently-abled users
- Healthcare and hospital assistance systems
- Touch-free communication
- Emergency alert systems

## 🛠 Tech Stack
- Python
- OpenCV
- CVZone
- MediaPipe
- Pygame

## ▶️ How to Run
```bash
pip install opencv-python cvzone mediapipe pygame
python hand_gesture_assistive_system.py

📁 Project Structure
Hand-Gesture-Assistive-System/
├── FingerImages/
├── ActionImages/
├── Audio/
├── hand_gesture_assistive_system.py
└── README.md
