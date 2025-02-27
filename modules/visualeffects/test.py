# The main code will be here

import cv2
import numpy as np
from modules.visualeffects.visual_effects import aplicar_filtros_artisticos, estilizar_imagen

def main():
    ruta_imagen = 'prueba.jpg'  # Si quieres realizar pruebas, coloca tu imagen en la raíz del proyecto.
    imagen = cv2.imread(ruta_imagen)

    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
        return

    suavizada, bordes = aplicar_filtros_artisticos(imagen)
    cartoon = estilizar_imagen(imagen, suavizada, bordes)

    cv2.imshow('Original', imagen)
    cv2.imshow('Caricatura', cartoon)
    cv2.imwrite('caricatura.jpg', cartoon)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()