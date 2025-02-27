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

## 2. Documentación Técnica

### **2.1 Descripción de los Módulos**

El proyecto está compuesto por los siguientes módulos:

- ``: Se encarga de detectar los rostros en la imagen de entrada utilizando OpenCV.
- ``: Aplica efectos de caricaturización mediante filtros bilaterales y detección de bordes con Canny.
- ``: Punto de entrada principal del programa, gestiona la entrada y salida de datos.

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

### **3.2 Resolución de Problemas Comunes**

- **Error: No se detectan rostros.**
  - Verificar que la imagen tenga rostros visibles y bien iluminados.
- **Error: No se genera la imagen de salida.**
  - Revisar permisos de escritura en el directorio de ejecución.

---

## 4. Despliegue del Sistema

El objetivo del despliegue es ejecutar el programa en un servidor en lugar de solo en local.

### **4.1 Instalación de Dependencias**

Si el proyecto se ejecuta en un servidor nuevo, instalar las dependencias:

```bash
pip install -r requirements.txt
```

### **4.2 Ejecución en un Servidor**

Para correr el sistema en un servidor Linux:

```bash
nohup python main.py --input imagen.jpg &
```

Esto permite que la ejecución continúe en segundo plano.

### **4.3 Opcional: Servir la Aplicación como una API**

Si se quiere exponer el servicio a través de una API con Flask:

```bash
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
```

Esto permitirá acceder al servicio desde un navegador o cliente HTTP.

### **4.4 Opcional: Empaquetado en un Ejecutable**

Para distribuir el programa como un ejecutable:

```bash
pyinstaller --onefile main.py
```

El archivo ejecutable generado estará en la carpeta `dist/`.

---

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

