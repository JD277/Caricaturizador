import numpy as np
import cv2 as cv
import matplotlib as plt
import mediapipe as mp
import mediapipe.python.solutions as solutions

blue = (255,0,0)

#Dibuja los puntos que se usarán para la triangulación de Delaunay
def draw_points(img, point):
    cv.circle(img, point, 3, blue, cv.FILLED)


def points_to_face(pf, gray, og):

    pass


#Detecta la cara dentro de la imagen dada, para posteriormente poder distorsionarla
def face_detection(img: cv.Mat) -> cv.Mat:
    gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

    classifier = cv.CascadeClassifier("1.6 Warping/haarcascade_frontalface_default.xml")
    face = classifier.detectMultiScale(gray_scale, minSize= (80,80))
    
    

    #Dibuja un rectangulo alrededor de la cara (x/y es el punto izquierdo superior del rectangulo
    #de las caras encontradas, y h/k es lo que se le suma paa hallar el final/derecho inferior)
    for (x,y,h,k) in face:
        rect = cv.rectangle(img,( x, y),(x + h, y + k),color= blue)

    points_to_face(face,gray_scale, img)
    cv.imshow("Test", img)


if __name__ == '__main__':

    mp_drawings = solutions.drawing_utils
    mp_style = solutions.drawing_styles
    mp_mesh = solutions.face_mesh

    image = cv.imread("Test images/james-person-1.jpg")

    new_image = cv.resize(image,(360,480))

    print(new_image.shape)

    rect = (0,0,new_image.shape[0],new_image.shape[1])

    face_detection(new_image)
    cv.waitKey(0)