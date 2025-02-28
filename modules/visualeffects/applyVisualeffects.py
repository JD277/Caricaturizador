# The main code will be here

import cv2
import numpy as np
from modules.visualeffects.visual_effects import aplicar_filtros_artisticos, estilizar_imagen
from datetime import datetime
import os
def apply_effects(image, output_path):
    ruta_imagen = image  # Si quieres realizar pruebas, coloca tu imagen en la raíz del proyecto.
    imagen = cv2.imread(ruta_imagen)

    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
        return

    suavizada, bordes = aplicar_filtros_artisticos(imagen)
    cartoon = estilizar_imagen(imagen, suavizada, bordes)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, cartoon)
    return output_path
