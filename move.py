import os, shutil
import pandas as pd

full_path = "full_image_dataset_100f"
nonfall_path = "nonfall"
fall_path = "fall"

if not os.path.exists(os.path.join(full_path, nonfall_path)):
    os.makedirs(os.path.join(full_path, nonfall_path))

if not os.path.exists(os.path.join(full_path, fall_path)):
    os.makedirs(os.path.join(full_path, fall_path))

files = os.listdir(full_path)

df = pd.read_csv('full_dataset.csv', index_col=0)

for index, row in df.iterrows():
    video_name = row['video_name'].replace(".avi", ".jpg")
    if row['tag'] in "fall":
        shutil.move(os.path.join(full_path, video_name), os.path.join(full_path, fall_path, video_name))
    else:
        shutil.move(os.path.join(full_path, video_name), os.path.join(full_path, nonfall_path, video_name))