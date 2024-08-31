#!/usr/bin/env python
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import subprocess
import moviepy.editor
# Replace the filename below.
            
def get_length(filename):
    video = moviepy.editor.VideoFileClip(filename)
    video_duration = int(video.duration)
    return video_duration
  

directory = os.path.abspath(os.path.curdir)
for filename in os.listdir(directory):
    starttime=0
    with open("times.txt") as f:
        for line in f:
            data = line.split()
            times=int(data[0])  
    if filename.endswith(".mp4"):
        endtime = get_length(os.path.join(directory, filename))
        i=1;
        while starttime+times<= endtime:
             with VideoFileClip(os.path.join(directory, filename)) as video:
                 new= video.subclip(starttime,starttime+times)
                 new.write_videofile(str(os.path.join(directory, filename))+ str(i)+".mp4")
                 starttime+=times
                 i=i+1
        timeRemaining = endtime-starttime
        if timeRemaining > 0 :
             with VideoFileClip(os.path.join(directory, filename)) as video:
                 new= video.subclip(starttime,endtime)
                 new.write_videofile(str(os.path.join(directory, filename))+ str(i)+".mp4")
           
       


         






