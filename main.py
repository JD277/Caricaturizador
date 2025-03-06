from modules.modules import *

# Función para inicializar 
def initialize_state():
    if 'imagen_cargada' not in st.session_state:
        st.session_state.imagen_cargada = None
    if 'imagen_caricaturizada' not in st.session_state:
        st.session_state.imagen_caricaturizada = None
    if 'mostrar_confirmacion' not in st.session_state:
        st.session_state.mostrar_confirmacion = False
    if 'file' not in st.session_state:
        st.session_state.file = None
    if 'reiniciar' not in st.session_state:
        st.session_state.reiniciar = False

# Barra de progreso
def mostrar_progreso(progress_bar):
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)

# Caricaturización con Mediapipe 
def warping_con_mediapipe(imagen):
    # Aqui va el codigo para esta funcion
    img_name = f"images/cartoon{datetime.now().strftime("%d_%m_%Y, %H_%M_%S")}.jpg"
    warping_mediapipe(imagen,img_name)
    return img_name

# Método de Deep Learning 
def metodo_deep_learning(imagen):
    # Aquí va el codigo para esta funcion
    img_name = f"images/cartoon{datetime.now().strftime("%d_%m_%Y, %H_%M_%S")}.jpg"
    cartoonizer.cartoonize(imagen, img_name)
    return img_name

# Función para seleccionar y aplicar el método de caricaturización
def caricaturizar_imagen(imagen, metodo):
    progress_bar = st.progress(0)   
    mostrar_progreso(progress_bar) 

    if metodo == 'Caricaturización con Mediapipe':
        return warping_con_mediapipe(imagen)
    elif metodo == 'Caricaturización con Dlib':
        return warping_dlib(imagen, f"images/cartoon{datetime.now().strftime("%d_%m_%Y, %H_%M_%S")}.jpg")
    elif metodo == 'AI':
        return metodo_deep_learning(imagen)
    
    elif metodo == 'Realista simple':
        mostrar_progreso(progress_bar)
        return apply_effects(imagen,f"images/cartoon{datetime.now().strftime("%d_%m_%Y, %H_%M_%S")}.jpg")

# Función para limpiar el directorio 'images'
def limpiar_directorio_images():
    for filename in os.listdir("images"):
        file_path = os.path.join("images", filename)
        try:
            if os.path.isfile(file_path):  # Verificar que sea un archivo
                os.remove(file_path)  # Eliminar el archivo
                # print(f"Archivo eliminado: {file_path}")
        except Exception as e:
            pass
            # st.error(f"No se pudo eliminar {file_path}: {e}")

# Función para limpiar todo
def limpiar_todo():
    # Limpiar el directorio 'images'
    limpiar_directorio_images()
    st.session_state.reiniciar = True

    # st.success("Directorio 'images' limpiado y estado restablecido.")

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
    st.session_state.file = st.file_uploader('Arrastra y suelta una imagen aquí', type=['jpg', 'png', 'jpeg'])
   
    if st.session_state.file is not None:
        try:
            imagen_original = Image.open(st.session_state.file)
            st.session_state.imagen_cargada = imagen_original
            st.session_state.imagen_caricaturizada = None
            os.makedirs("images", exist_ok=True)
            file_path = os.path.join("images", st.session_state.file.name)
            with open(file_path, "wb") as f:
                f.write(st.session_state.file.getbuffer())
        except Exception as e:
            st.error(f'Error al cargar la imagen: {e}. Por favor, sube un archivo de imagen válido (JPG, PNG, JPEG).')
    else:
        st.info('Por favor, sube un archivo de imagen.')

    # Selección del método de caricaturización
    metodo = st.selectbox('Elige un método:', ['Caricaturización con Mediapipe', 'Caricaturización con Dlib', 'AI', 'Realista simple'])

    if st.session_state.imagen_cargada is not None:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="animated-image">', unsafe_allow_html=True)
            st.image(st.session_state.imagen_cargada, caption='Imagen Original', use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Botón para caricaturizar la imagen
        if st.button('Caricaturizar imagen'):
            # try:
                imagen_caricaturizada = caricaturizar_imagen(os.path.join("images",st.session_state.file.name), metodo)
                st.session_state.imagen_caricaturizada = Image.open(imagen_caricaturizada)
                st.success('¡Imagen caricaturizada con exito!')
            # except Exception as e:
                # st.error(f'Error al caricaturizar la imagen: {e}')

        with col2:
            if st.session_state.imagen_caricaturizada is not None:
                st.markdown('<div class="animated-image">', unsafe_allow_html=True)
                st.image(st.session_state.imagen_caricaturizada, caption='Imagen Caricaturizada', use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)


        # Botón de descarga
        if st.session_state.imagen_caricaturizada is not None:
            buffered = io.BytesIO()
            st.session_state.imagen_caricaturizada.save(buffered, format="PNG")
            st.download_button(
                label="Descargar Imagen",
                data=buffered.getvalue(),
                file_name="caricatura.png",
                mime="image/png",
                on_click=lambda: limpiar_todo()
            )
        if st.session_state.reiniciar:
            # Restablecer el estado de la aplicación
            st.session_state.imagen_cargada = None
            st.session_state.imagen_caricaturizada = None
            st.session_state.file = None
            imagen_original = None
            st.session_state.reiniciar = False

            # Forzar re-renderizado
            st.rerun()
            

# Ejecutar la interfaz del caricaturizador
interfaz_caricaturizador()