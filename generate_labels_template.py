import os
import csv

CROPS_FOLDER = "labeled_crops"
OUTPUT_CSV = "labels.csv"

if not os.path.exists(CROPS_FOLDER):
    print("❌ Folder 'labeled_crops/' not found.")
    exit()

image_files = sorted([
    f for f in os.listdir(CROPS_FOLDER)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

if not image_files:
    print("⚠️ No image files found in 'labeled_crops/'. Check the folder.")
else:
    with open(OUTPUT_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "actual_team"])
        for fname in image_files:
            writer.writerow([fname, ""])

    print(f"✅ {len(image_files)} image entries written to {OUTPUT_CSV}")
    print("👉 Fill in actual_team column with R, W, Y, or ?")
