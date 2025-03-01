import numpy as np
import cv2 as cv


# Convierte la imagen a gris, la difumina (blur) y le saca los bordes 
# (El blur debe tener un valor positivo e impar)
def edge_detection(img,blur= 5, line_size= 5):
    grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    grayscale_blur = cv.medianBlur(grayscale, blur)

    edges = cv.adaptiveThreshold(grayscale_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,line_size,blur)

    return edges

# Segmenta los colores de la imagen, y devuelve una versión caricaturizada con la cantidad de colores
# especificados
def color_segmentation(img, colors= 8, iterations= 20):
    bgr_to_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    #Se convierte la imagen en un arreglo numpy de tipo flotante (32 bits) y se reduce el mismo a una columna
    #(ya que es el tipo de dato que admite la funcion de clusters)
    np_array = np.float32(bgr_to_rgb)
    np_array = np_array.reshape((-1,3))

    # Especificaciones para terminar el proceso de clustering en la imagen
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, iterations, 0.02)


    _, label, center = cv.kmeans(np_array, colors, None, criteria, iterations, cv.KMEANS_RANDOM_CENTERS)

    result_image = center[label.flatten()].reshape(bgr_to_rgb.shape).astype(np.uint8)
    
    return result_image

# Caricaturiza la imagen. Recibe de parámetros: una imagen, el blur (determina que tan clara se ve la imagen
# y debe ser impar), numero de colores que se utilizaran en el proceso y el tamaño de la linea usado al
# caricaturizar
def cartoonize(img: cv.Mat, BLUR= 5, COLORS= 8, SIZE= 11):
    
    img_edges = edge_detection(img, BLUR, SIZE)
    img_colors = color_segmentation(img, COLORS)

    img_blur = cv.bilateralFilter(img_colors, 7, 200, 200)
    img_cartoon = cv.bitwise_and(img_blur, img_blur, mask= img_edges)
    return img_cartoon
