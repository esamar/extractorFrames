import numpy as np
import cv2
import sys
import pytesseract
import csv
import os
# from IPython.display import display, clear_output
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# video_path = 'downfps_cropped_11_12_2023_de_00-00_a_07-03.mp4'
# video_nombre = os.path.basename(video_path)

def preproc(img):
    alto, ancho = img.shape[:2]

    nuevo_alto = alto * 1
    nuevo_ancho = ancho * 1

    imagen_duplicada = cv2.resize(img, (nuevo_ancho, nuevo_alto))

    gray_roi = cv2.cvtColor(imagen_duplicada, cv2.COLOR_BGR2GRAY)
    #gray_roi = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    

    #cv2_imshow(thresh)

    #text = pytesseract.image_to_string(thresh)
    # custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789-/ :'
    custom_config = r'--psm 6'

    return pytesseract.image_to_string(thresh, lang='eng', config=custom_config)

# video = cv2.VideoCapture(video_path)

# frame_count = 0
# fps = int(video.get(cv2.CAP_PROP_FPS))

# print("FPS del video:", fps)

# total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# print("El video tiene", total_frames, "fotogramas.")

frame_count = 1

#while(frame_count < 100):
# while(video.isOpened()):
folder_path = 'D:\Video\salida_19-12-2023'
video_nombre = 'salida_19-12-2023'

image_files = os.listdir(folder_path)
total_frames = len(image_files)

for image_file in image_files:
        #if frame_count % fps == 0:
        # roi = frame[40:58, 25:100]
        # roi2 = frame[40:58, 240:365]
        image_path = os.path.join(folder_path, image_file)
        frame = cv2.imread(image_path)

        # roi = frame[1:56, 0:74]
        roi2 = frame[40:56, 240:363]

        # cv2.imshow("prueba 1", roi2)
        # cv2_imshow("prueba 2", roi2)
        # cv2.waitKey(0)

        # sys.exit()

        # fecha = preproc(roi)
        hora = preproc(roi2)
        # fecha = preproc(frame)

        #print("Fecha", fecha )
        #print("Hora", hora )

        with open(video_nombre+'.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([image_file, frame_count, hora])

        frame_count += 1
        
        porcentaje_procesado = (frame_count / total_frames) * 100
        porcentaje_procesado_redondeado = round(porcentaje_procesado, 3)

        print(f"Porcentaje procesado: {porcentaje_procesado_redondeado:.2f}%")

cv2.waitKey(0)
cv2.destroyAllWindows()
