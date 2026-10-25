import streamlit as st
import random
import time

st.title("The Crew App")

palos = ["♠️ Picas", "♣️ Tréboles", "♦️ Diamantes", "♥️ Corazones"]
numeros = list(range(1, 10))
mazo = [(numero, palo) for palo in palos for numero in numeros]
random.shuffle(mazo)


if "fichas_guardadas" not in st.session_state:
    st.session_state.fichas_guardadas = []

def pulsar_ficha(ficha):
    if ficha in st.session_state.fichas_guardadas:
        st.session_state.fichas_guardadas.remove(ficha)
    else:
        st.session_state.fichas_guardadas.append(ficha)

fichas_fila_1 = ["1", "2", "3", "4", "5"]
fichas_fila_2 = [">", ">>", ">>>", ">>>>", "Ω"]

# Fila 1
cols1 = st.columns(5)
for i, ficha in enumerate(fichas_fila_1):
    with cols1[i]:
        # Comprobamos si esta ficha en concreto está en nuestro array de memoria
        esta_pulsada = ficha in st.session_state.fichas_guardadas
        
        st.button(
            ficha, 
            key=f"btn_{ficha}", # Clave única obligatoria si generamos botones en bucle
            type="primary" if esta_pulsada else "secondary", # Aquí ocurre la magia del color
            on_click=pulsar_ficha, 
            args=(ficha,), # Le pasamos el nombre de la ficha a la función
            use_container_width=True
        )

# Fila 2
cols2 = st.columns(5)
for i, ficha in enumerate(fichas_fila_2):
    with cols2[i]:
        esta_pulsada = ficha in st.session_state.fichas_guardadas
        st.button(
            ficha, 
            key=f"btn_{ficha}",
            type="primary" if esta_pulsada else "secondary",
            on_click=pulsar_ficha, 
            args=(ficha,),
            use_container_width=True
        )



num_misiones = st.number_input("NÚMERO DE MISIONES:", min_value=0,max_value=36,step=1)
lon_fichas = len(st.session_state.fichas_guardadas)
st.divider()
if st.button("GENERAR MISIÓN",use_container_width=True, type="primary"):
    with st.spinner('Asignando misión...'):
        time.sleep(1.2)
    columnas = st.columns(3)
    
    for i in range(num_misiones):
        carta = mazo.pop()
        indice_col = i % 3
        with columnas[indice_col]:
            with st.container(border=True):
                
                if i < lon_fichas:
                    st.write(carta[1])
                    st.header(carta[0])
                    st.warning(f"FICHA: {st.session_state.fichas_guardadas[i]}")
                else:
                    st.write(carta[1])
                    st.header(carta[0])


