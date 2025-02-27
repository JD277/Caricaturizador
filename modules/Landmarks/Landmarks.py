import cv2
import dlib
import numpy as np

def extract_landmarks_dlib(image_path, predictor_path="shape_predictor_68_face_landmarks.dat"):
    
    # Carga la imagen y la convierte a escala de grises
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Inicializa el detector de rostros y predictor de landmarks
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)
    
    # Detecta rostros en la imagen
    faces = detector(gray)
    if len(faces) == 0:
        print("No se detectaron rostros en la imagen.")
        return image, []
    
    landmarks_list = []
    # Itera sobre cada rostro detectado
    for face in faces:
        # Predictor de los 68 puntos de referencia
        shape = predictor(gray, face)
        # Convierte un array de numpy con formato (68, 2)
        landmarks = np.array([[p.x, p.y] for p in shape.parts()])
        landmarks_list.append(landmarks)
    
    return image, landmarks_list

def visualize_landmarks(image, landmarks_list, radius=2, color=(0, 255, 0)):
    
    annotated_image = image.copy()
    for landmarks in landmarks_list:
        for (x, y) in landmarks:
            cv2.circle(annotated_image, (x, y), radius, color, -1)
    return annotated_image

if __name__ == "__main__":
    # Acá especifiqué la ruta imagen de testeo y del modelo de landmarks con el
    # test 4 se muestra que es fregao que obtenga caras con poco detalle pero con los otros test
    # Si se nota que agarra distintos angulos (mas no completamente de lado como se ve en Test5)
    IMAGE_PATH = "Test3.jpg"
    PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
    
    # Extrae landmarks
    image, landmarks_list = extract_landmarks_dlib(IMAGE_PATH, PREDICTOR_PATH)
    
    # Visualiza resultados
    annotated_image = visualize_landmarks(image, landmarks_list)
    cv2.imshow("Landmarks Faciales", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


from paquete_analisis import modulo_analisis
modulo_analisis.procesar_landmarks(landmarks)