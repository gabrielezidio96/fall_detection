import os
import numpy as np
from PIL import Image
import pandas as pd
import cv2

PATH = 'full_dataset_100f'
OUT_PATH = 'full_image_dataset_100f'

if not os.path.exists(OUT_PATH):
    os.makedirs(OUT_PATH)

def process_video_to_img(path, file_name):
    backSub = cv2.createBackgroundSubtractorMOG2()
    cap = cv2.VideoCapture(path)
    first_frame = True
    imgDiff = None
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = backSub.apply(frame)
            if first_frame:
                first_frame = False
                imgDiff = cv2.absdiff(frame, frame)
            else:
                imgDiff = cv2.absdiff(imgDiff, frame)
                #cv2.imshow('image', imgDiff)

    finally:
        cv2.imwrite(os.path.join(OUT_PATH, file_name + '.jpg'), imgDiff)
        cap.release()
    return imgDiff

df = pd.read_csv('full_dataset.csv', index_col=0)

for index, row in df.iterrows():
    process_video_to_img(os.path.join(PATH, row['video_name']), row['video_name'][:-4])