import cv2
import numpy as np


def aplicar_filtros_artisticos(imagen):

    suavizada = cv2.bilateralFilter(imagen, d=9, sigmaColor=75, sigmaSpace=75)
    bordes = cv2.Canny(suavizada, threshold1=50, threshold2=150)
    return suavizada, bordes


def estilizar_imagen(imagen, suavizada, bordes):
    # Convertir los bordes a una máscara
    bordes = cv2.cvtColor(bordes, cv2.COLOR_GRAY2BGR)

    # Combinar la imagen suavizada con los bordes resaltados
    cartoon = cv2.bitwise_and(suavizada, 255 - bordes)
    return cartoon
