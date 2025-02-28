import cv2
import numpy as np
import steamlib

imagen = None


#Permite que el usuario seleccione una imagen para cargar a su gusto, posteriormente redimensionandola
#verificando que realmente se haya cargado la imagen antes de hacerlo, de lo contrario muestra un error
def cargar(tamano = (500,500)):
    global imagen
    ruta = steamlib.open_file_dialog("Seleccione una imagen")
    if ruta:
        imagen = cv2.imread(ruta)
        if imagen is None:
            steamlib.show_message_box("Error", "No se encontró la imagen especificada")
        else:
            imagen = redimensionar(imagen, tamano)

#Redimensiona la imagen para que tenga las medidas correctas para su uso
def redimensionar(imagen, ancho= 500, largo=500):
    return cv2.resize(imagen,(ancho,largo))

#Revisa que se haya cargado una imagen, en ese caso, la transforma a escala de grises y extrae sus bordes
def procesar():
    global imagen
    if imagen is None:
        steamlib.show_message_box("Error", "Fallo al cargar la imagen, debe seleccionar una imagen para cargar")
        return

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    bordes = cv2.Canny(gris, 30, 100)