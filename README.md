# Caricaturizador

## Descripción del Proyecto
El "Caricaturizador" es un software de procesamiento de imágenes que transforma rostros en caricaturas aplicando técnicas de computación gráfica y aprendizaje profundo. El objetivo del proyecto es desarrollar un sistema capaz de detectar rostros en imágenes, extraer sus características faciales y aplicar transformaciones para darles una apariencia caricaturesca.

Este proyecto se inspira en el enfoque de **Cartoon-World** (https://github.com/khaHesham/Cartoon-World/tree/main), el cual utiliza redes neuronales y procesamiento de imágenes para la transformación de rostros en caricaturas. Nuestro sistema integra técnicas como detección de puntos clave faciales y triangulación para lograr el efecto deseado.

## Funcionalidades del Sistema
El programa se compone de varios módulos que cumplen diferentes funciones en el proceso de caricaturización:

### 1.1 Carga de imagen
- Permite al usuario seleccionar una imagen desde su computadora.
- Convierte la imagen a un formato adecuado para el procesamiento.

### 1.2 Preprocesamiento de la imagen
- Convierte la imagen a escala de grises.
- Realiza filtrado y ajuste de brillo/contraste para mejorar la detección.

### 1.3 Detección de rostros
- Utiliza modelos de detección facial como **Haar Cascades** para identificar la posición del rostro en la imagen.

### 1.4 Extracción de características
- Se identifican puntos clave del rostro utilizando **MediaPipe Face Mesh**.
- Los puntos detectados servirán para la transformación geométrica de la caricatura.

### 1.5 Transformación geométrica
- Aplica la **triangulación de Delaunay** sobre los puntos clave detectados.
- Distorsiona la imagen basándose en la información de los puntos faciales.

### 1.6 Warping (Deformación facial)
Este módulo se encarga de deformar la imagen del rostro aplicando **detección de puntos faciales y distorsión geométrica**.

#### Explicación del archivo `Warping.py`
El archivo **Warping.py** implementa los siguientes procesos:
1. **Carga de la imagen**: Utiliza `cv.imread()` para leer la imagen y la ajusta a un tamaño fijo.
2. **Detección de puntos faciales**:
   - Usa la biblioteca **MediaPipe** para identificar landmarks en el rostro.
   - Aplica la **triangulación de Delaunay** para crear una malla sobre la cara.
3. **Detección de rostros**:
   - Emplea el clasificador `haarcascade_frontalface_default.xml` para encontrar caras.
   - Dibuja un rectángulo alrededor de las caras detectadas.
4. **Aplicación de la transformación**:
   - Se sobrepone la malla de triangulación sobre el rostro detectado.
   - Se realiza el warping geométrico para exagerar las proporciones de la cara.

### 1.7 Aplicación de filtros y efectos
- Se agregan filtros de dibujo para dar un efecto de caricatura a la imagen.
- Se pueden aplicar distintos estilos según las preferencias del usuario.

### 1.8 Generación de la caricatura final
- Se combinan los efectos aplicados para crear la imagen final en estilo caricaturesco.

### 1.9 Interfaz de usuario
- Se desarrolla una interfaz sencilla para cargar imágenes y visualizar los resultados.

### 1.10 Pruebas y despliegue
- Se ejecutan pruebas unitarias para verificar la correcta detección y transformación.
- Se prepara el sistema para su ejecución final y presentación.

## Tecnologías utilizadas
- **Python**
- **OpenCV** (Procesamiento de imágenes)
- **MediaPipe** (Detección de puntos faciales)
- **Numpy** (Manipulación de datos)
- **Matplotlib** (Visualización de resultados)

## Instrucciones de uso
1. Clona el repositorio en tu computadora:
   ```bash
   git clone https://github.com/JD277/Caricaturizador.git
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install opencv-python mediapipe numpy matplotlib
   ```
3. Ejecuta el programa principal:
   ```bash
   python main.py
   ```
4. Carga una imagen y observa el resultado de la caricaturización.

## Contribución
Cada colaborador debe trabajar en su módulo correspondiente y hacer commits siguiendo la estructura:
- **Nuevo cambio**: `Feat(feature): description`
- **Refactorización**: `Refactor(feature): description`
- **Eliminación**: `Delete(feature): description`
- **Pull Request**: `Merge(feature): description`

## Contacto
Si tienes dudas o sugerencias, abre un issue en el repositorio o contacta al equipo vía GitHub.

---

**Nota**: Este README es una guía inicial, se recomienda actualizarlo a medida que el proyecto avance y se integren nuevas funcionalidades.

