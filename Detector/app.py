import cv2
import numpy as np

class FaceDetector:
    def __init__(self, model_path="yunet_n_640_640.onnx", input_size=(320, 320), conf_threshold=0.8):
        self.detector = cv2.FaceDetectorYN_create(
            model=model_path,
            config="",
            input_size=input_size,
            score_threshold=conf_threshold,
            nms_threshold=0.3,
            top_k=5000
        )
        self.input_size = input_size

    def preprocess(self, image):
        # Mejorar contraste con CLAHE (para condiciones de luz pobres)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        return cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)

    def detect(self, image):
        # Preprocesar y redimensionar
        processed = self.preprocess(image)
        h, w = image.shape[:2]
        self.detector.setInputSize((w, h))
        
        # Detección de rostros
        _, faces = self.detector.detect(processed)
        return faces if faces is not None else []

# Función principal para ser llamada desde otro módulo
def detect_faces_in_image(image, model_path="yunet_n_640_640.onnx", input_size=(640, 640), conf_threshold=0.85):
    """
    Detecta rostros en una imagen recibida como parámetro.
    
    Parámetros:
        image (numpy.ndarray): La imagen en formato BGR (como la que devuelve cv2.imread).
        model_path (str): Ruta al modelo ONNX.
        input_size (tuple): Tamaño de entrada para el detector.
        conf_threshold (float): Umbral de confianza para la detección.
    
    Retorna:
        list: Lista de rostros detectados, donde cada rostro es un array con las coordenadas y la confianza.
    """
    detector = FaceDetector(model_path=model_path, input_size=input_size, conf_threshold=conf_threshold)
    faces = detector.detect(image)
    return faces