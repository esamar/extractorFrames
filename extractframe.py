import subprocess
import os

def extract_frames_ffmpeg(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    command = [
        "C:\\ffmpeg\\bin\\ffmpeg",
        "-i", video_path,
        "-vf", "fps=1", 
        os.path.join(output_folder, "frame_%d.jpg")
    ]
    subprocess.call(command)

if __name__ == "__main__":
    video_path = "19-12-2023/19_12_2023_de_04-49_a_09-37.mp4"
    videos_files = os.listdir('input')
    for video in videos_files:
        print("Se inició el procesamiento de: " + video)
        extract_frames_ffmpeg("input/"+ video , "output/" + video)
