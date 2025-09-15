# 🔫 Gun Detection using OpenCV  

## 📖 Overview  
This project implements a **firearm detection system** using **Python and OpenCV**.  
It leverages a **Haar Cascade Classifier** (`cascade.xml`) to identify guns in both **images** and **videos**.  

The scripts can process static pictures or live/recorded video streams, highlighting detected firearms with bounding boxes and alert messages.  
The goal of this project is to explore **Computer Vision techniques for object detection**, focusing on **security and surveillance applications**.  

---

## 🖼️ Features  
- ✅ Firearm detection in **images and videos**  
- ✅ Real-time **bounding box visualization**  
- ✅ Alert message **"Firearm detected!"** overlay  
- ✅ Date & time stamp in video feed  
- ✅ Simple to use and extend  

---

## ⚙️ Installation  
### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/Gun-Detection-OpenCV.git
cd Gun-Detection-OpenCV
```

### 2. Install Dependencies
```
pip install opencv-python imutils numpy
```

---

## 📚 Future Improvements
-🔹Train a deep learning model (YOLO / SSD / Faster R-CNN) for higher accuracy
-🔹 Build a web interface for real-time monitoring
-🔹 Deploy on Raspberry Pi / Jetson Nano for edge computing

---

## ⚠️ Disclaimer
This project is for educational and research purposes only.
The Haar Cascade model is prone to false positives/negatives and must not be used for real-world firearm detection in critical security environments.
---
