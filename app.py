import streamlit as st
from PIL import Image
from grupos import home, Admin
import pandas as pd

st.set_page_config(
    page_title="EVALUACIONES | PERSONAL ",
    page_icon="📈",
    layout="wide")
logo = Image.open(r'logos/GRUPO GHALMACA.jpg')
st.sidebar.image(logo, width=150)
# Define tus páginas como funciones

def main():
    pagina = st.sidebar.selectbox("Selecciona la empresa correspondiente", ["Inicio","Personal evaluado" ])

    if pagina == "Inicio":
        home()
    elif pagina == "Personal evaluado":
        Admin()
if __name__ == "__main__":
    main()
