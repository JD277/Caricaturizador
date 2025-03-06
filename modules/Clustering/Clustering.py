import numpy as np
import cv2 as cv
import matplotlib as plt
import mediapipe as mp
import os
import pandas as pd
from mediapipe import solutions
import modules.Clustering.Caricature as car
from mediapipe.tasks import python as tk
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2 as pb
from modules.Landmarks.Landmarks import extract_landmarks_dlib
blue = (255,0,0)


# Recibe la ruta de una imagen y el tamaño de la misma, devolviendo la imagen leida y modificada
def image_manager( file: str, size = (360,480)):

    image = cv.imread(file)


    try:
        new_image = cv.resize(image,size)

    # Excepción en el caso de que se ingrese un tamaño invalido para la imagen 
    except:
        
        size = (360,480)
        new_image = cv.resize(image,size)
    old_size = image.shape[:2]
    return [new_image, old_size]

# Dibuja los puntos que se usarán para la triangulación de Delaunay
def draw_points(rgb_image: mp.Image, configuration, draw_face= True, draw_eyes_mouth= True, draw_iris= True, draw_nose= True):
    face_landmarks = configuration.face_landmarks
    image_landmarked = np.copy(rgb_image)

    # Variables para asignar fácilmente las especificaciones al dibujo de landmarks
    mp_style = solutions.drawing_styles
    mp_mesh = solutions.face_mesh
    
    # Dibuja los landmarks a cada cara detectada
    for faces in face_landmarks:

        actual_landmark = faces
  
        #Especificaciones para que el modelo ubique los landmarks
        landmark_list = pb.NormalizedLandmarkList()
        landmark_list.landmark.extend([
            pb.NormalizedLandmark(x= landmark.x, y= landmark.y, z= landmark.z) 
            for landmark in actual_landmark
        ])

        # Dibuja los landmarks en las zonas especificadas
        if draw_face:
            #Dibuja los landmarks de la cara
            solutions.drawing_utils.draw_landmarks(image= image_landmarked,
                                                    landmark_list= landmark_list,
                                                    landmark_drawing_spec= None,
                                                    connections= mp_mesh.FACEMESH_TESSELATION,
                                                    connection_drawing_spec= mp_style.get_default_face_mesh_tesselation_style()
                                                    )
        # Dibuja las pupilas
        if draw_iris:
            solutions.drawing_utils.draw_landmarks(image= image_landmarked,
                                                landmark_list= landmark_list,
                                                landmark_drawing_spec= None,
                                                connections= mp_mesh.FACEMESH_IRISES,
                                                connection_drawing_spec=  mp_style.get_default_face_mesh_iris_connections_style()
                                                )
        # dibuja los ojos y boca
        if draw_eyes_mouth:
            solutions.drawing_utils.draw_landmarks(image= image_landmarked,
                                                landmark_list= landmark_list,
                                                landmark_drawing_spec= None,
                                                connections= mp_mesh.FACEMESH_CONTOURS,
                                                connection_drawing_spec=  mp_style.get_default_face_mesh_contours_style()
                                                )
        
        # Dibuja la nariz
        if draw_nose:
            solutions.drawing_utils.draw_landmarks(image= image_landmarked,
                                                landmark_list= landmark_list,
                                                landmark_drawing_spec= None,
                                                connections= mp_mesh.FACEMESH_NOSE,
                                                connection_drawing_spec=  mp_style.get_default_face_mesh_tesselation_style()
                                                )
        
    return image_landmarked



# Recibe la imagen que se utilizará para el warping, 
# y crea un landmark (como un análisis de las caras)
def landmark_startup(og: cv.Mat, face: bool, eyes: bool, iris: bool, nose: bool):

    model = "modules/Warping/face_landmarker.task"

    # Variables que se utilizan para asignarle a la configuración del landmark
    mp_base = tk.BaseOptions(model_asset_path= model)
    mp_running_mode = vision.RunningMode

    # Configuración para el análisis de las caras (landmark)
    mp_lm_options = vision.FaceLandmarkerOptions(mp_base, num_faces = 5,
                                                running_mode= mp_running_mode.IMAGE,
                                                output_face_blendshapes=True,
                                                output_facial_transformation_matrixes=True)

    # Crea el landmark a partir de la configuración anterior
    mp_lm = vision.FaceLandmarker.create_from_options(mp_lm_options)

    # Cambia el formato de la imagen a uno compatible para el "detect" (de BGR A RGB)
    # y, posteriormente, detecta el landmark de la imagen dada
    image_lm = mp.Image(image_format= mp.ImageFormat.SRGB, data= og)
    results = mp_lm.detect(image_lm)

    detected_image = draw_points(image_lm.numpy_view(),results, face, eyes, iris, nose)
    cv.cvtColor(detected_image, cv.COLOR_RGB2BGR)

    return detected_image


# Detecta la cara dentro de la imagen dada, para darle un efecto de caricatura.
# En caso de que no se quiera una caricatura, devuelve la imagen regular
def face_detection(img: cv.Mat, img_blur, img_lsize, img_colork, cartoonish: bool = False) -> cv.Mat:
    gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

    copy_image= img.copy()

    #Detecta el area de la cara
    classifier = cv.CascadeClassifier("modules/Clustering/haarcascade_frontalface_default.xml")
    face = classifier.detectMultiScale(gray_scale, minSize= (80,80))
    numpy_array = None
    # Crea un rectangulo de identificación para la cara y extrae dicha parte de la imagen
    if cartoonish:    
        for (x,y,h,k) in face:
     
            # Se crea un arreglo de ceros del mismo tamaño que la imagen original
            numpy_array = np.zeros(img.shape)

            # Se caricaturiza la imagen original y se toma la sección de la cara
            # (para usarla como filtro)

            cartoon = car.cartoonize(img, img_blur, img_colork, img_lsize)
            cropped_image = cartoon[y:(y+k),x:(x+h)]

            # Se introduce dicha sección en el arreglo (en su posición original) 
            # para poder realizar operaciones matriciales
            numpy_array[y:y+k, x: x+ h] = cropped_image
            numpy_array = numpy_array.astype(np.uint8)
        
        copy_image = cv.addWeighted(copy_image.astype(np.uint8), 0.6, numpy_array, 0.4,0)
        
        return copy_image

    return img

# Colocando todo el proceso junto para integrarlo a la interfaz
def warping_mediapipe(img_input:str, output_path, blur= 5, colors= 8,img_lsize = 11, cartoonish = True):
    img = image_manager(img_input)
    landmarked_image = landmark_startup(img[0], False, False, False, False)
    warped_image = face_detection(landmarked_image, blur, img_lsize, colors, cartoonish)
    resized_image = cv.resize(warped_image,(img[1][1],img[1][0]))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv.imwrite(output_path, resized_image)
    return output_path

# Colocando todo el proceso junto para integrarlo a la interfaz
def warping_dlib(img_input:str, output_path):
    img = image_manager(img_input)
    landmarked_and_warped_image = extract_landmarks_dlib(img[0])
    resized_image = cv.resize(landmarked_and_warped_image,(img[1][1],img[1][0]))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv.imwrite(output_path, resized_image)
    return output_path
