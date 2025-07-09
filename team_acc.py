from reid1 import detect_team
import cv2
import os

correct = 0
total = 0

with open("labels.csv", "r") as f:
    lines = f.readlines()

for line in lines[1:]:  # skip header
    fname, actual = line.strip().split(",")
    img_path = os.path.join("labeled_crops", fname)
    img = cv2.imread(img_path)

    if img is None:
        print(f"⚠️ Could not read {img_path}")
        continue

    pred = detect_team(img)
    print(f"Image: {fname} | Predicted: {pred} | Actual: {actual}")  # 👈 Debug output

    if pred == actual:
        correct += 1
    total += 1

if total > 0:
    print(f"✅ Team Classification Accuracy: {correct / total * 100:.2f}%")
else:
    print("⚠️ No valid labeled samples found.")
