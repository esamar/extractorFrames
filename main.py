import numpy as np
import cv2
import sys
import pytesseract
import csv
import os
# from IPython.display import display, clear_output
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

video_path = 'downfps_cropped_11_12_2023_de_00-00_a_07-03.mp4'
video_nombre = os.path.basename(video_path)

def preproc(img):
    alto, ancho = img.shape[:2]

    # Duplicar el tamaño de la imagen
    nuevo_alto = alto * 1
    nuevo_ancho = ancho * 1

    # Redimensionar la imagen
    imagen_duplicada = cv2.resize(img, (nuevo_ancho, nuevo_alto))

    gray_roi = cv2.cvtColor(imagen_duplicada, cv2.COLOR_BGR2GRAY)
    #gray_roi = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    

    #cv2_imshow(thresh)

    #text = pytesseract.image_to_string(thresh)
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789-/ :'

    return pytesseract.image_to_string(thresh, lang='eng', config=custom_config)

video = cv2.VideoCapture(video_path)

frame_count = 0
fps = int(video.get(cv2.CAP_PROP_FPS))

print("FPS del video:", fps)

total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print("El video tiene", total_frames, "fotogramas.")

frame_count = 0

#while(frame_count < 100):
while(video.isOpened()):

    current_frame = int(video.get(cv2.CAP_PROP_POS_FRAMES))

    tiempo_transcurrido_segundos = current_frame / fps
    hora_transcurrida = int(tiempo_transcurrido_segundos // 3600)
    minutos_transcurridos = int((tiempo_transcurrido_segundos % 3600) // 60)
    segundos_transcurridos = int(tiempo_transcurrido_segundos % 60)

    tiempo_vivo = f"{hora_transcurrida:02d}:{minutos_transcurridos:02d}:{segundos_transcurridos:02d}"


    ret, frame = video.read()

    if ret:
        #if frame_count % fps == 0:
        # roi = frame[40:58, 25:100]
        # roi2 = frame[40:58, 240:365]
        
        # roi = frame[1:56, 0:74]
        roi2 = frame[1:56, 217:335]

        # cv2.imshow("prueba 1", roi)
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
            writer.writerow([frame_count, tiempo_vivo, hora])
            # writer.writerow([frame_count, tiempo_vivo, fecha])

        #video.set(cv2.CAP_PROP_POS_FRAMES, frame_count + fps)
        
        porcentaje_procesado = (frame_count / total_frames) * 100
        porcentaje_procesado_redondeado = round(porcentaje_procesado, 3)

        # Imprime el porcentaje procesado en el mismo lugar
        print(f"Porcentaje procesado: {porcentaje_procesado_redondeado:.2f}%")

        # clear_output(wait=True)

        #frame_count += fps
        frame_count += 1

    else:
        print("Finalizó")
        break


video.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
