import streamlit as st
from PIL import Image
import io
import base64
import time

# Función para inicializar 
def initialize_state():
    if 'imagen_cargada' not in st.session_state:
        st.session_state.imagen_cargada = None
    if 'imagen_caricaturizada' not in st.session_state:
        st.session_state.imagen_caricaturizada = None
    if 'mostrar_confirmacion' not in st.session_state:
        st.session_state.mostrar_confirmacion = False

# Barra de progreso
def mostrar_progreso(progress_bar):
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)

# Método Clásico 
def metodo_clasico(imagen):
    # Aqui va el codigo para esta funcion
    return imagen

# Método de Deep Learning 
def metodo_deep_learning(imagen):
    # Aquí va el codigo para esta funcion
    return imagen

# Función para seleccionar y aplicar el método de caricaturización
def caricaturizar_imagen(imagen, metodo):
    progress_bar = st.progress(0)
    mostrar_progreso(progress_bar)

    if metodo == 'Método Clásico':
        return metodo_clasico(imagen)
    elif metodo == 'Deep Learning':
        return metodo_deep_learning(imagen)

# Función principal para la interfaz del caricaturizador
def interfaz_caricaturizador():
    
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to right, #282D88, #6F74CB); /* Gradiente aún más oscuro */
        }
        .animated-title {
            animation: fadeIn 2s ease-in-out;
        }
        .animated-image {
            animation: bounceIn 1s ease;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <script>
        window.onload = function() {
            const captions = document.querySelectorAll('figcaption');
            captions.forEach(caption => {
                caption.style.color = 'white';
            });
        }
        </script>
        """,
        unsafe_allow_html=True
    )

    # Título de la aplicación
    st.markdown('<h1 class="animated-title">Caricaturizador de Imágenes</h1>', unsafe_allow_html=True)
    st.write('¡Carga una imagen y convierte tu foto en una caricatura!')

    initialize_state()

    # Cargar imagen desde el sistema del usuario
    uploaded_file = st.file_uploader('Arrastra y suelta una imagen aquí', type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        try:
            imagen_original = Image.open(uploaded_file)
            st.session_state.imagen_cargada = imagen_original
            st.session_state.imagen_caricaturizada = None
        except Exception as e:
            st.error(f'Error al cargar la imagen: {e}. Por favor, sube un archivo de imagen válido (JPG, PNG, JPEG).')
    else:
        st.info('Por favor, sube un archivo de imagen.')

    # Selección del método de caricaturización
    metodo = st.selectbox('Elige un método:', ['Método Clásico', 'Deep Learning'])

    if st.session_state.imagen_cargada is not None:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="animated-image">', unsafe_allow_html=True)
            st.image(st.session_state.imagen_cargada, caption='Imagen Original', use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Botón para caricaturizar la imagen
        if st.button('Caricaturizar imagen'):
            try:
                imagen_caricaturizada = caricaturizar_imagen(st.session_state.imagen_cargada, metodo)
                st.session_state.imagen_caricaturizada = imagen_caricaturizada
                st.success('¡Imagen caricaturizada con exito!')
            except Exception as e:
                st.error(f'Error al caricaturizar la imagen: {e}')

        with col2:
            if st.session_state.imagen_caricaturizada is not None:
                st.markdown('<div class="animated-image">', unsafe_allow_html=True)
                st.image(st.session_state.imagen_caricaturizada, caption='Imagen Caricaturizada', use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

        # Botón para borrar la imagen
        if st.button('Borrar imagen'):
            st.session_state.mostrar_confirmacion = True

        # Confirmación de borrado
        if st.session_state.mostrar_confirmacion:
            st.write('¿Estás seguro de que deseas borrar la imagen?')
            col1, col2 = st.columns(2)
            if col1.button('Sí'):
                st.session_state.imagen_cargada = None
                st.session_state.imagen_caricaturizada = None
                st.session_state.mostrar_confirmacion = False
                st.success('Imagen borrada con éxito.')
            if col2.button('No'):
                st.session_state.mostrar_confirmacion = False
                st.info('Operación cancelada. La imagen no ha sido borrada.')

        # Botón de descarga
        if st.session_state.imagen_caricaturizada is not None:
            buffered = io.BytesIO()
            st.session_state.imagen_caricaturizada.save(buffered, format="PNG")
            st.download_button(
                label="Descargar Imagen",
                data=buffered.getvalue(),
                file_name="caricatura.png",
                mime="image/png"
            )

# Ejecutar la interfaz del caricaturizador
interfaz_caricaturizador()