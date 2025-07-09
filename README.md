# Soccer Player Re-Identification using YOLOv11

This project performs real-time soccer player detection, team classification, and re-identification using a YOLOv11 model and custom logic.

## 🚀 Features
- Player detection using YOLOv11
- Jersey color-based team classification (Red, White, Yellow)
- Player Re-identification using spatial matching
- Live tactical map visualization
- Team classification accuracy reporting

---

## 🛠️ Setup Instructions
![image](https://github.com/user-attachments/assets/636db9ab-1370-401d-a7e9-a10ad7a93c54)

![image](https://github.com/user-attachments/assets/abd69d85-938f-47b3-9135-b5735e3aae30)


1. Clone the repo or unzip the folder
  bash
  git clone https://github.com/nitya70/Object_Reidentification-using-YOLO.git
  cd Object_Reidentification-using-YOLO

2. Create a virtual environment and activate it
  bash
  python -m venv venv
  source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install requirements
  bash
  pip install -r requirements.txt

4. Place your files
  bash
  models/best.pt           ← Trained YOLO model
  assets/input_video.mp4   ← Input match video

5. Running
    python main.py
