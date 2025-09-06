# Invisibility Cloak (OpenCV Computer Vision Project)

This project creates a real-life **invisibility cloak effect** using **Computer Vision and OpenCV**.
By detecting a specific color (green/blue cloth), it replaces that region with the background, creating the illusion of invisibility.

---

## ✨ Features

* Detects green color in real-time using HSV color space
* Creates a mask to segment the cloth region
* Replaces the cloth with the background captured earlier
* Works with a simple webcam

---

## 🛠️ Requirements

* Python 3.x
* OpenCV
* NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

---

## ▶️ How to Run

1. Clone this repo

   ```bash
   git clone https://github.com/your-username/invisibility-cloak-opencv.git
   cd invisibility-cloak-opencv
   ```

2. Run the script

   ```bash
   python invisibility_cloak.py
   ```

3. Hold a **green cloth** in front of your webcam, and watch the magic happen! You can also change color - use bright colors
   Press **Q** or **ctrl+c** to quit.

---

---

## 📚 Concepts Used

* **Color detection in HSV space**
* **Image masking and segmentation**
* **Background replacement**
* **Basic Computer Vision with OpenCV**

---

## 📌 Future Improvements

* Support multiple colors
* Add custom background images or videos
* Improve mask refinement for smoother output

---

## 👨‍💻 Author

Raviranjan Kumar (Shaurya) - 

---

