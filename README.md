# ⚽ Soccer Player Re-Identification using YOLOv11 🧠

This project tracks and re-identifies soccer players in match footage using object detection and simple spatial tracking. It also classifies teams based on jersey color! 🚀

---

## 📌 Project Highlights

- ✅ **Detects players** using a trained YOLOv11 model  
- 🎽 **Classifies team color** (Red, White/Blue, Yellow - referee)  
- 🔁 **Re-identifies players** across frames by position  
- 📺 **Draws bounding boxes + names** on output video  
- 🗺️ Live **tactical map** showing player positions  
- 📊 **Accuracy evaluation** of team classification  

---

## 🛠️ Setup Instructions

### 🔧 1. Clone or Download the Repository
```bash
  git clone https://github.com/nitya70/Object_Reidentification-using-YOLO.git
  cd Object_Reidentification-using-YOLO
```

###🐍 2. Create & Activate a Virtual Environment (optional but recommended)
```  bash
  python -m venv venv
  # On Windows:
  venv\Scripts\activate
  # On macOS/Linux:
  source venv/bin/activate
```
###📦 3. Install Dependencies
```  bash
  pip install -r requirements.txt
```
####📂 4. Add Required Files
```  bash
  models/
  └── best.pt              # Your trained YOLO model
assets/
  └── input_video.mp4      # The match video to process

```
###▶️ Running the Project
🎬 1. Run the Main Script Running
    python main.py


| Label | Meaning         | Color        |
| ----- | --------------- | ------------ |
| `R`   | Red team        | 🔴 Red       |
| `W`   | White/Blue team | ⚪ Blue/White |
| `Y`   | Referee         | 🟡 Yellow    |
| `?`   | Unknown         | ❓ Gray       |

![image](https://github.com/user-attachments/assets/636db9ab-1370-401d-a7e9-a10ad7a93c54)

![image](https://github.com/user-attachments/assets/abd69d85-938f-47b3-9135-b5735e3aae30)

###🧪 Evaluating Team Classification Accuracy
🏷️ Step 1: Label some crops
      Run main.py to generate cropped images in labeled_crops/.

      Then open labels.csv and fill in actual labels like:

        cs
        filename,actual_team
        frame12_id0_R.jpg,R
        frame12_id1_W.jpg,W
📊 Step 2: Run Accuracy Script
        bash
        python team_accuracy.py


