# Caricaturizador

## Descripción del Proyecto

El "Caricaturizador" es un software de procesamiento de imágenes que transforma rostros en caricaturas aplicando técnicas de computación gráfica y aprendizaje profundo. Su objetivo es detectar rostros en imágenes, extraer sus características faciales y aplicar transformaciones para darles una apariencia caricaturesca.

Este proyecto se basa en enfoques como [Cartoon-World](https://github.com/khaHesham/Cartoon-World/tree/main), que utiliza redes neuronales y procesamiento de imágenes para la transformación de rostros en caricaturas. Nuestro sistema integra técnicas como detección de puntos clave faciales, triangulación y warping geométrico para lograr el efecto deseado.

## Funcionalidades del Sistema

El programa se compone de varios módulos, cada uno con una función específica en el proceso de caricaturización:

### 1. Carga y Preprocesamiento de Imágenes
- Permite al usuario seleccionar una imagen desde su computadora.
- Convierte la imagen a escala de grises y la normaliza si es necesario.
- Ajusta el tamaño de la imagen para un procesamiento más eficiente.

### 2. Detección de Rostros
- Emplea OpenCV o Dlib para detectar rostros en la imagen.
- Extrae la región de interés (ROI) correspondiente al rostro detectado.

### 3. Extracción de Landmarks Faciales
- Usa el predictor de 68 puntos faciales de Dlib para identificar las características clave del rostro.

### 4. Exageración de Rasgos
- Modifica las coordenadas de los landmarks para enfatizar características distintivas como ojos, nariz y boca.

### 5. Transformaciones Geométricas
- Aplica triangulación de Delaunay para modificar la imagen basada en los landmarks ajustados.

### 6. Aplicación de Efectos Visuales
- Utiliza filtros artísticos para dar un acabado más caricaturesco.
- Ajusta el color y los bordes para resaltar la transformación.

### 7. Estilización con Deep Learning
- Permite la opción de aplicar modelos como CartoonGAN para una caricaturización más avanzada.

### 8. Pruebas y Despliegue
- Se ejecutan pruebas unitarias para verificar la correcta detección y transformación.
- Se prepara el sistema para su ejecución final y presentación.

## Instalación y Uso

### Requisitos Previos
- Python 3.9 o superior
- Dependencias listadas en `requirements.txt`


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

## Documentación y Soporte
Para detalles técnicos, revisa `DOCUMENTATION.md`. Para soporte, abre un issue en el repositorio.

**Nota:** Este README es una guía inicial, se recomienda actualizarlo a medida que el proyecto avance y se integren nuevas funcionalidades.

