# DOCUMENTACIÓN DE QA Y DESPLIEGUE

## Introducción

Este documento detalla los procedimientos para la realización de pruebas del sistema (QA), la documentación técnica, el manual de usuario y el despliegue del proyecto "Caricaturizador". Su objetivo es garantizar la funcionalidad del software y facilitar su implementación en un entorno de producción.

---

## 1. QA (Pruebas del Sistema)

Antes de realizar el despliegue, es fundamental probar el sistema para detectar errores y asegurarse de que todas las funcionalidades operan correctamente.

### **1.1 Requisitos Previos**

- Tener instaladas las dependencias del proyecto (ver `requirements.txt`).
- Un entorno de desarrollo con Python 3.9 o superior.
- Acceso al repositorio del proyecto.

### **1.2 Pruebas Unitarias**

Para ejecutar pruebas unitarias sobre los módulos del sistema, usa `pytest` (si está disponible en `requirements.txt`).

```bash
pytest tests/
```

Si no hay tests implementados, se recomienda crearlos en una carpeta `tests/` con pruebas para cada módulo.

Ejemplo de prueba unitaria para detección de rostros:

```python
import cv2
from modules.face_detection import detect_face  

def test_face_detection():
    image = cv2.imread("prueba.jpg")
    result = detect_face(image)
    assert result is not None, "La detección de rostro falló"
```

### **1.3 Pruebas Manuales**

Ejecutar el programa con una imagen de prueba:

```bash
python main.py --input prueba.jpg
```

Verificar que:

- Se detecta el rostro correctamente.
- Se aplica el efecto de caricaturización.
- Se genera la imagen de salida sin errores.

---

### 1.4 Pruebas de Integración
Validar la comunicación entre los módulos clave ejecutando `integration_tests.py`.
```bash
python integration_tests.py
```

## 2. Documentación Técnica

### **2.1 Descripción de los Módulos**

Este proyecto sigue una arquitectura modular. Cada módulo tiene funciones específicas:
- `preprocessing.py`: Procesamiento de imágenes.
- `face_detection.py`: Detección de rostros.
- `landmarks.py`: Extracción de puntos faciales.
- `warp.py`: Transformaciones geométricas.
- `effects.py`: Filtros artísticos y ajustes visuales.
- `deep_learning.py`: Implementación de redes neuronales para estilización.
- `gui.py`: Interfaz gráfica con PyQt.


### **2.2 Algoritmos Utilizados**

- **Detección de Rostros**: Se usa OpenCV con haarcascades para identificar rostros en la imagen.
- **Filtrado Bilateral**: Suaviza la imagen manteniendo los bordes para lograr un efecto de dibujo.
- **Detección de Bordes con Canny**: Identifica los contornos para resaltar las características del rostro.

---

## 3. Manual de Usuario

### **3.1 Instalación**

1. Clonar el repositorio:

```bash
git clone https://github.com/usuario/caricaturizador.git
```

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar el programa:

```bash
python main.py --input imagen.jpg
```

El usuario debe:
1. Ejecutar `python main.py`.
2. Cargar una imagen desde su equipo.
3. Elegir el método de caricaturización (clásico o deep learning).
4. Guardar el resultado.

### **3.2 Resolución de Problemas Comunes**

- **Error: No se detectan rostros.**
  - Verificar que la imagen tenga rostros visibles y bien iluminados.
- **Error: No se genera la imagen de salida.**
  - Revisar permisos de escritura en el directorio de ejecución.

---

## 4. Despliegue

### 4.1 Creación de un Ejecutable
Se recomienda `PyInstaller` para generar un `.exe` en Windows.
```bash
pyinstaller --onefile --windowed main.py
```

### 4.2 Despliegue en Web
El proyecto puede adaptarse a `Streamlit` para correr en web:
```bash
streamlit run app.py
```

Con estos pasos, se asegura un correcto funcionamiento del sistema.


## 5. Mantenimiento y Soporte

### **5.1 Reporte de Errores**

Para reportar errores, abrir un issue en el repositorio de GitHub.

### **5.2 Recomendaciones para Nuevas Funcionalidades**

- Implementar una interfaz gráfica con Tkinter o PyQt.
- Optimizar la detección de rostros con modelos de Machine Learning.
- Crear una versión web con una API más robusta.

---

## 6. Conclusión

Este documento proporciona las pautas necesarias para la validación, documentación y despliegue del sistema. Siguiendo estos pasos, se garantiza que el software o programa funciona correctamente tanto en desarrollo como en producción.

