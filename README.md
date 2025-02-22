# Caricaturizador - Proyecto de Computación Gráfica

## Descripción del Proyecto
Caricaturizador es un software de procesamiento de imágenes que transforma fotografías en caricaturas. Utiliza técnicas de **visión computacional, machine learning y procesamiento de imágenes** para modificar las facciones del rostro, generar efectos estilizados y mejorar la experiencia del usuario con una interfaz interactiva.

El proyecto se desarrolla en Python utilizando librerías como **OpenCV, Dlib, NumPy, Tkinter/PyQt/Kivy, TensorFlow/PyTorch** (según la sección) y herramientas de control de versiones como **Git y GitHub**.

## Funcionalidades Generales
1. **Carga de imagen**: El usuario puede subir una imagen desde su dispositivo.
2. **Detección de rostro**: Identificación automática de la cara en la imagen.
3. **Extracción de landmarks faciales**: Obtención de puntos clave del rostro.
4. **Exageración de rasgos faciales**: Modificación geométrica para resaltar características como ojos, nariz y boca.
5. **Transformaciones geométricas (Warping)**: Aplicación de técnicas para deformar suavemente el rostro.
6. **Efectos visuales y postprocesamiento**: Aplicación de filtros para dar un estilo artístico.
7. **Opción de Deep Learning**: Estilización avanzada mediante redes neuronales.
8. **Interfaz Gráfica**: Permite la interacción con el usuario y la visualización de los cambios en tiempo real.
9. **Despliegue y distribución**: Preparación del software para su instalación y uso final.

## Secciones del Proyecto y Responsabilidades
Cada parte del proyecto está dividida en módulos con responsabilidades específicas:

### 1.1. Interfaz Gráfica y Diseño de UX/UI
- Desarrollo de una GUI intuitiva.
- Integración de botones y opciones.
- Conexión con el backend para procesamiento.

### 1.2. Preprocesamiento de Imágenes
- Carga y ajuste de tamaño de imágenes.
- Conversión a escala de grises si es necesario.
- Optimización para la detección de rostros.

### 1.3. Visión Computacional para Detección de Rostros
- Implementación de detectores con OpenCV/Dlib.
- Optimización para distintos tipos de imágenes.

### 1.4. Extracción de Landmarks Faciales
- Uso de modelos de predicción para obtener puntos clave.
- Visualización de los landmarks en la imagen.

### 1.5. Análisis y Exageración de Rasgos Faciales
- Algoritmos matemáticos para modificar proporciones faciales.
- Control de parámetros para distintos niveles de exageración.

### 1.6. Transformaciones Geométricas (Warping)
- Uso de triangulación de Delaunay y TPS para deformar la imagen.
- Validación de la calidad de la deformación.

### 1.7. Efectos Visuales y Postprocesamiento
- Aplicación de filtros artísticos para mejorar la apariencia caricaturesca.

### 1.8. Deep Learning para Estilización
- Uso de modelos preentrenados (CartoonGAN, Style Transfer) para generar caricaturas de alta calidad.

### 1.9. Integración
- Ensamblaje de todos los módulos en un solo flujo de trabajo.
- Manejo de errores y optimización del rendimiento.

### 1.10. QA, Documentación y Despliegue
- **Pruebas unitarias y de integración**: Evaluar el funcionamiento de cada módulo.
- **Documentación**: Creación de informes técnicos y manuales de usuario.
- **Despliegue del software**: Empaquetado y distribución del programa.
- **Mantenimiento**: Planificación de mejoras futuras.

## Instalación y Uso
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/JD277/Caricaturizador.git
   ```
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar el programa**:
   ```bash
   python main.py
   ```

## Contribución y Control de Versiones
Cada miembro del equipo trabaja en una rama independiente y sube sus cambios con mensajes de commit estructurados:
- **Añadir nuevas funciones**: `Feat(NombreFuncionalidad): descripción breve`
- **Refactorizar código**: `Refactor(NombreFuncionalidad): descripción breve`
- **Eliminar código innecesario**: `Delete(NombreFuncionalidad): descripción breve`
- **Realizar pull request**: `Merge(NombreFuncionalidad): descripción breve`

## Créditos
Proyecto desarrollado por estudiantes de la **Universidad de Oriente** de la asignatura **Computación Gráfica**.
Cada módulo es responsabilidad de un miembro del equipo, asegurando un desarrollo colaborativo y eficiente.

---
Este documento se irá actualizando conforme avance el proyecto.

