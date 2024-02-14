import cv2

video_path = '11_12_2023_de_00-00_a_07-03.mp4'

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error al abrir el archivo de video.")
    exit()

fps = video.get(cv2.CAP_PROP_FPS)

frame_count = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame_count += 1

    time_seconds = frame_count / fps

    if time_seconds >= 1:
        cv2.imwrite(f"frame_{frame_count}.jpg", frame)
        print(f"Guardado frame_{frame_count}.jpg")

        frame_count = 0

video.release()
