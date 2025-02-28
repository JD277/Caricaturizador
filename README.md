# Caricaturizador

## Descripción del Proyecto

El "Caricaturizador" es un software de procesamiento de imágenes que transforma rostros en caricaturas aplicando técnicas de computación gráfica y aprendizaje profundo. Su objetivo es detectar rostros en imágenes, extraer sus características faciales y aplicar transformaciones para darles una apariencia caricaturesca.

Este proyecto se basa en enfoques como [Cartoon-World](https://github.com/khaHesham/Cartoon-World/tree/main), que utiliza redes neuronales y procesamiento de imágenes para la transformación de rostros en caricaturas. Nuestro sistema integra técnicas como detección de puntos clave faciales, triangulación y warping geométrico para lograr el efecto deseado.

## Funcionalidades del Sistema

El programa se compone de varios módulos, cada uno con una función específica en el proceso de caricaturización:

### 1. Carga y Preprocesamiento de Imágenes
- Permite al usuario seleccionar una imagen desde su computadora.
- Convierte la imagen a un formato adecuado para el procesamiento.
- Ajusta la iluminación y normaliza la imagen para mejorar la detección facial.

### 2. Detección de Rostros y Características Faciales
- Utiliza modelos de detección facial como Haar Cascades o Dlib para identificar la posición del rostro en la imagen.
- Extrae puntos clave faciales utilizando MediaPipe Face Mesh.
- Los puntos detectados servirán para la transformación geométrica de la caricatura.

### 3. Transformaciones Geométricas (Warping)
- Aplica la triangulación de Delaunay sobre los puntos clave detectados.
- Distorsiona la imagen basándose en la información de los puntos faciales.
- Se encarga de deformar la imagen del rostro aplicando detección de puntos faciales y distorsión geométrica.

### 4. Aplicación de Filtros y Estilización
- Se agregan filtros de dibujo para dar un efecto de caricatura a la imagen.
- Se pueden aplicar distintos estilos según las preferencias del usuario, incluyendo enfoques basados en redes neuronales.

### 5. Interfaz de Usuario
- Se desarrolla una interfaz sencilla para cargar imágenes y visualizar los resultados.
- Permite seleccionar entre distintos estilos de caricatura.

### 6. Pruebas y Despliegue
- Se ejecutan pruebas unitarias para verificar la correcta detección y transformación.
- Se prepara el sistema para su ejecución final y presentación.

## Tecnologías Utilizadas
- **Python**
- **OpenCV** (Procesamiento de imágenes)
- **MediaPipe** (Detección de puntos faciales)
- **NumPy** (Manipulación de datos)
- **Matplotlib** (Visualización de resultados)

## Instrucciones de Uso

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

## Cómo Subir Cambios al Proyecto en GitHub

### Haciendo Commits mediante la Web de GitHub
1. Ve al repositorio del proyecto en GitHub.
2. Dirígete al archivo que deseas modificar y haz clic en el ícono de edición (lápiz).
3. Realiza los cambios necesarios en el archivo.
4. Escribe un mensaje de commit claro en el campo "Commit changes".
5. Selecciona "Commit directly to the main branch" si los cambios no requieren revisión, o crea un nuevo branch y un Pull Request.
6. Haz clic en "Commit changes".

## Convenciones para Commits
Cada colaborador debe trabajar en su módulo correspondiente y hacer commits siguiendo la estructura:

- **Nuevo cambio:** `Feat(feature): description`
- **Refactorización:** `Refactor(feature): description`
- **Eliminación:** `Delete(feature): description`
- **Pull Request:** `Merge(feature): description`

Ejemplo:
```bash
Feat(deteccion_rostros): Implementación de MediaPipe para detección de puntos clave
```

## Contacto
Si tienes dudas o sugerencias, abre un issue en el repositorio o contacta al equipo vía GitHub.

**Nota:** Este README es una guía inicial, se recomienda actualizarlo a medida que el proyecto avance y se integren nuevas funcionalidades.

