import numpy as np
import cv2 as cv
import matplotlib as plt
import mediapipe as mp
from mediapipe import solutions
from mediapipe.tasks import python as tk
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2 as pb

blue = (255,0,0)
path = "Test images/james-person-1.jpg"

#Recibe la ruta de una imagen y el tamaño de la misma, devolviendo la imagen leida y modificada
def image_manager( file: str, size = (360,480)):

    image = cv.imread(file)


    try:
        new_image = cv.resize(image,size)

    #Excepción en el caso de que se ingrese un tamaño invalido para la imagen 
    except:
        print("Upsi dupsi")
        size = (360,480)
        new_image = cv.resize(image,size)

    return new_image

#Dibuja los puntos que se usarán para la triangulación de Delaunay
def draw_points(rgb_image: mp.Image, configuration):
    face_landmarks = configuration.face_landmarks
    image_landmarked = np.copy(rgb_image)

    #Variables para asignar fácilmente las especificaciones al dibujo de landmarks
    mp_style = solutions.drawing_styles
    mp_mesh = solutions.face_mesh
    
    for faces in face_landmarks:
        actual_landmark = faces

        landmark_list = pb.NormalizedLandmarkList()
        landmark_list.landmark.extend([
            pb.NormalizedLandmark(x= landmark.x, y= landmark.y, z= landmark.z) 
            for landmark in actual_landmark
        ])

        solutions.drawing_utils.draw_landmarks(image= image_landmarked,
                                               landmark_list= landmark_list,
                                               landmark_drawing_spec= None,
                                               connections= mp_mesh.FACEMESH_TESSELATION,
                                               connection_drawing_spec=  mp_style.get_default_face_mesh_tesselation_style()
                                               )
    
    return image_landmarked



#Recibe la imagen que se utilizará para el warping, 
# y crea un landmark (como un análisis de las caras)
def landmark_startup(og: cv.Mat):

    model = "1.6 Warping/face_landmarker.task"

    #Variables que se utilizan para asignarle a la configuración del landmark
    mp_base = tk.BaseOptions(model_asset_path= model)
    mp_running_mode = vision.RunningMode

    #Configuración para el análisis de las caras (landmark)
    #TODO: Hacer modificable el número máximo de caras (me da fastidio hacerlo ahora)
    mp_lm_options = vision.FaceLandmarkerOptions(mp_base, num_faces = 5,
                                                running_mode= mp_running_mode.IMAGE,
                                                output_face_blendshapes=True,
                                                output_facial_transformation_matrixes=True)

    #Crea el landmark a partir de la configuración anterior
    mp_lm = vision.FaceLandmarker.create_from_options(mp_lm_options)

    #Cambia el formato de la imagen a uno compatible para el "detect" (de BGR A RGB)
    #y, posteriormente, detecta el landmark de la imagen dada
    image_lm = mp.Image(image_format= mp.ImageFormat.SRGB, data= og)
    detector = mp_lm.detect(image_lm)

    detected_image = draw_points(image_lm.numpy_view(),detector)
    cv.cvtColor(detected_image, cv.COLOR_RGB2BGR)

    return detected_image


#Detecta la cara dentro de la imagen dada, para posteriormente poder distorsionarla
def face_detection(img: cv.Mat) -> cv.Mat:
    gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

    classifier = cv.CascadeClassifier("1.6 Warping/haarcascade_frontalface_default.xml")
    face = classifier.detectMultiScale(gray_scale, minSize= (80,80))

    #Dibuja un rectangulo alrededor de la cara (x/y es el punto izquierdo superior del rectangulo
    #de las caras encontradas, y h/k es lo que se le suma paa hallar el final/derecho inferior)
    for (x,y,h,k) in face:
        rect = cv.rectangle(img,( x, y),(x + h, y + k),color= blue)

    new_image = landmark_startup(img)
    cv.imshow("Test", new_image)



if __name__ == '__main__':

    img = image_manager(path)

    face_detection(img)
    cv.waitKey(0)