import streamlit as st
from PIL import Image
from grupos import home, Serviplus, Dapreca, Inversiones, Transporte
import pandas as pd

st.set_page_config(
    page_title="EVALUACIONES | PERSONAL ",
    page_icon="📈",
    layout="wide")
logo = Image.open(r'logos/GRUPO GHALMACA.jpg')
st.sidebar.image(logo, width=150)
# Define tus páginas como funciones

def main():
    pagina = st.sidebar.selectbox("Selecciona la empresa correspondiente", ["Inicio", "Serviplus", "Dapreca","Inv Ghalmaca","Mult Ghalmaca", "Galpego", "Ferregal","Global a21"])

    if pagina == "Inicio":
        home()
    elif pagina == "Serviplus":
        Serviplus()
    elif pagina == "Dapreca":
        Dapreca()
    elif pagina == "Inv Ghalmaca":
        Inversiones()
    elif pagina == "Mult Ghalmaca":
        Transporte()
    elif pagina == "Galpego":
        pass
    elif pagina == "Ferregal":
        pass
    else:
        pass
if __name__ == "__main__":
    main()
