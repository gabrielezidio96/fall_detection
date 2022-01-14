#pip install --force-reinstall imageio-ffmpeg==0.2.0

import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import pandas as pd

FPS=2
frame_rate = 24
path_dataset = './full_dataset/'
#path_dataset_75f = './full_dataset_75f/'
path_dataset_100f = 'full_dataset_100f'
if not os.path.exists(path_dataset_100f):
    os.makedirs(path_dataset_100f)
df = pd.read_csv('full_dataset.csv')

for index, row in df.iterrows():
    start, end = int(row['start']), int(row['end'])
    #print((start/frame_rate, end/frame_rate))

    input = os.path.join(path_dataset, row['video_name'])
    target = os.path.join(path_dataset_100f, row['video_name'])
    # loading video dsa gfg intro video 
    clip = VideoFileClip(input) 
    
    # getting only first 5 seconds
    new_clip = clip.subclip(start/frame_rate, end/frame_rate)
    
    # new clip with new fps
    new_clip.write_videofile(target,fps=FPS, codec="libxvid")