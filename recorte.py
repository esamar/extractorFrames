from moviepy.editor import VideoFileClip
import os

video_path = '11_12_2023_de_00-00_a_07-03.mp4'
video_nombre = os.path.basename(video_path)

x1, y1, x2, y2 = 25, 40, 365, 58
video = VideoFileClip(video_path)
#video_cinco_minu
tos = video.subclip(0, 5*60)
video_recortado =   video.crop(x1=x1, y1=y1, x2=x2, y2=y2)
video_recortado.write_videofile("cropped_"+video_nombre, audio=False)