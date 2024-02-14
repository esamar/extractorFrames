import numpy as np
import csv
import cv2
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# Función para preprocesar la imagen
def preproc(img):
    gray_roi = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    total_pixels = thresh.shape[0] * thresh.shape[1]
    white_pixels = cv2.countNonZero(thresh)
    black_pixels = total_pixels - white_pixels

    percentage_white = (white_pixels / total_pixels) * 100
    percentage_black = (black_pixels / total_pixels) * 100

    return thresh, percentage_white, percentage_black

# Ruta de la carpeta que contiene las imágenes
output = 'output'
# video_nombre = 'salida_19-12-2023'

# Obtener la lista de archivos en la carpeta
folders_output = os.listdir(output)

for folder in folders_output:
    # print(folder)
    folder_path = output + "/" + folder
    image_files = os.listdir(folder_path)

    total_frames = len(image_files)
    frame_count = 1

    for image_file in image_files:
        # print( folder_path )
        # import sys
        # sys.exit()
        image_path = os.path.join(folder_path, image_file)
        frame = cv2.imread(image_path)

        binary, percentage_white, percentage_black = preproc(frame)
        # print("Porcentaje de píxeles blancos:", percentage_white)
        # print("Porcentaje de píxeles negros:", percentage_black)

        # cv2.imshow(f'Imagen -> w: {percentage_white:.2f}% b: {percentage_black:.2f}%', binary)

        porcentaje_procesado = (frame_count / total_frames) * 100
        porcentaje_procesado_redondeado = round(porcentaje_procesado, 3)

        print(f"procesado {porcentaje_procesado_redondeado:.2f}%: "+image_file)

        with open(folder_path + '.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([image_file, percentage_white, percentage_black])
        
        frame_count += 1

        # if cv2.waitKey(0) & 0xFF == ord('q'):
        #     break

    cv2.destroyAllWindows()
