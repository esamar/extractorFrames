from moviepy.editor import VideoFileClip
import os

video_path = 'cropped_11_12_2023_de_00-00_a_07-03.mp4'
video_nombre = os.path.basename(video_path)

nuevo_fps = 1
video = VideoFileClip(video_path)
# video_cinco_minutos = video.subclip(0, 5*60)
video_con_nuevo_fps = video.set_fps(nuevo_fps)

video_con_nuevo_fps.write_videofile("downfps_"+video_nombre, audio=False)