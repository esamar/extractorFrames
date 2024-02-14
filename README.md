Requisitos:
    ffmpeg: Se requiere la herramienta de línea de comandos ffmpeg
    Ubicación:
        C:\ffmpeg\bin

    tesseract_cmd:
    Módulos: Español
    Ubicación:
        C:\Program Files\Tesseract-OCR\tesseract

Paquetes:
    OpenCV
    Pytesseract
    
Generar binarios:
pyinstaller --onefile extractframe.py
pyinstaller --onefile proctocsv.py

Para trabajar con el scrip crear la carpeta "input"

Los videos en formato .mp4 se cargan directamente en /input/*.mp4