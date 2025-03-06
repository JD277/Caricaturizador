import cv2
import dlib
import numpy as np
from modules.Clustering.Caricature import cartoonize
# Función para extraer landmarks y aplicar el filtro al rostro
def extract_landmarks_dlib(image):
    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Inicializa el detector de rostros y predictor de landmarks
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("modules/Landmarks/shape_predictor_68_face_landmarks.dat")

    # Detecta rostros en la imagen
    faces = detector(gray)
    if len(faces) == 0:
        print("No se detectaron rostros en la imagen.")
        return image

    # Itera sobre cada rostro detectado
    for face in faces:
        # Predictor de los 68 puntos de referencia
        shape = predictor(gray, face)
        landmarks = np.array([[p.x, p.y] for p in shape.parts()])

        # Encuentra el rectángulo que encierra el rostro
        x_min, y_min = np.min(landmarks, axis=0)
        x_max, y_max = np.max(landmarks, axis=0)

        # Extrae la región del rostro
        face_region = image[y_min:y_max, x_min:x_max]

        # Aplica el filtro de cartoonización a la región del rostro
        cartoon_face = cartoonize(face_region,5,8,11)

        # Mezcla la imagen original y la cartoonizada
        blended_face = cv2.addWeighted(face_region, 0.8, cartoon_face, 1 - 0.5, 0)

        # Reemplaza la región del rostro en la imagen original
        image[y_min:y_max, x_min:x_max] = blended_face
    return image





# if __name__ == "__main__":
    # Acá especifiqué la ruta imagen de testeo y del modelo de landmarks con el
    # test 4 se muestra que es fregao que obtenga caras con poco detalle pero con los otros test
    # Si se nota que agarra distintos angulos (mas no completamente de lado como se ve en Test5)
    # IMAGE_PATH = "modules/Landmarks/Test3.jpg"
    # PREDICTOR_PATH = "modules/Landmarks/shape_predictor_68_face_landmarks.dat"
    
    # Extrae landmarks
    # image, landmarks_list = extract_landmarks_dlib(IMAGE_PATH, PREDICTOR_PATH)
    
    # Visualiza resultados
    # annotated_image = visualize_landmarks(image, landmarks_list)
    # cv2.imshow("Landmarks Faciales", annotated_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


