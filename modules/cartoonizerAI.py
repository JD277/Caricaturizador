import os
import cv2
import numpy as np
import tensorflow as tf
from network import unet_generator  
from guided_filter import guided_filter 

class Cartoonizer:
    def __init__(self, model_path="saved_models"):
        self.model_path = model_path
        self.sess = None
        self.input_photo = None
        self.final_out = None
        self._load_model()

    def _load_model(self):
        """Carga el modelo preentrenado y configura la sesión de TensorFlow"""
        tf.compat.v1.disable_eager_execution()
        
        self.input_photo = tf.compat.v1.placeholder(tf.float32, [1, None, None, 3])
        network_out = unet_generator(self.input_photo)
        self.final_out = guided_filter(self.input_photo, network_out, r=1, eps=5e-3)
        
        config = tf.compat.v1.ConfigProto()
        config.gpu_options.allow_growth = True
        self.sess = tf.compat.v1.Session(config=config)
        
        # Cargar pesos entrenados
        saver = tf.compat.v1.train.Saver()
        saver.restore(self.sess, tf.train.latest_checkpoint(self.model_path))

    def _resize_crop(self, image):
        """Redimensiona y recorta la imagen para cumplir requisitos de la red"""
        h, w, _ = image.shape
        if min(h, w) > 720:
            ratio = 720.0 / min(h, w)
            h, w = int(h * ratio), int(w * ratio)
        h, w = h - h % 8, w - w % 8
        return image[:h, :w, :]

    def cartoonize(self, input_path, output_path):
        """Procesa una imagen y guarda el resultado en la ruta especificada"""
        # Validar archivo de entrada
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Archivo no encontrado: {input_path}")
        
        # Leer imagen
        image = cv2.imread(input_path)
        if image is None:
            raise ValueError("Formato de imagen no compatible")
        
        # Preprocesamiento
        image = self._resize_crop(image)
        image_normalized = (image.astype(np.float32) / 127.5) - 1
        image_batch = np.expand_dims(image_normalized, axis=0)
        
        # Inferencia
        output = self.sess.run(self.final_out, feed_dict={self.input_photo: image_batch})
        output = (np.squeeze(output) + 1) * 127.5
        output = np.clip(output, 0, 255).astype(np.uint8)
        
        # Guardar resultado
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, output)
        print(f"Imagen guardada en: {output_path}")


if __name__ == "__main__":
    # Configuración
    model_path = "modules/saved_models"  # Ruta al modelo entrenado
    input_image = "images/img.jpeg"    # Ruta de la imagen original
    output_image = "images/cartoon.jpg"  # Ruta donde guardar el resultado

    # Crear instancia y procesar
    cartoonizer = Cartoonizer(model_path)
    cartoonizer.cartoonize(input_image, output_image)