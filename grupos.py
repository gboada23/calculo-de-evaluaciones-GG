import streamlit as st
from PIL import Image
from funciones import serviplus, dapreca, inversiones, transporte, galpego, ferregal, admin
import pandas as pd

def centrar_titulos(titulo):
    st.markdown(f"<h1 style='text-align: center;'>{titulo}</h1>", unsafe_allow_html=True)

def meses_del_año():
    meses_a_numero = {"Enero": "1",
        "Febrero": "2",
        "Marzo": "3",
        "Abril": "4",
        "Mayo": "5",
        "Junio": "6",
        "Julio": "7",
        "Agosto": "8",
        "Septiembre": "9",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"}
    meses = list(meses_a_numero.keys())
    # Widget para seleccionar el mes
    mes_seleccionado = st.sidebar.selectbox('Selecciona el mes a obtener las evaluaciones:', meses)
    # Obtener el número de mes correspondiente
    numero_mes = int(meses_a_numero[mes_seleccionado])
    return numero_mes, mes_seleccionado

def home():    
    centrar_titulos("BIENVENIDOS")
    centrar_titulos("AL GRUPO DE EMPRESAS GHALMACA")
    st.markdown("---")
    col1, col2,col3  = st.columns((2,4,2))
# Texto a justificar
    texto = """
    En la barra lateral de la izquierda podrán encontrar las opciones a manipular para descargar 
    las evaluaciones procesadas del personal por empresa y por mes, lo primero que deben hacer es seleccionar la
    empresa correspondiente a cada gerente y luego les aparecerá el mes donde desean obtener la evaluación, se le
    mostrará una tabla con vista preliminar antes de descargar para que puedan chequear la información, una vez
    chequeada presionan el botón descargar para proceder a bajar el excel con las evaluaciones correspondientes al mes seleccionado.
    """
    # Usando HTML y CSS para justificar el texto
    col2.markdown(f"<h5 style='text-align: justify;'>{texto}</h5>", unsafe_allow_html=True)

def Serviplus():
    st.image(r'logos/SERVIPLUS.png',width=150)
    centrar_titulos("GESTION DE EVALUACIONES MULTISERVICIOS SERVIPLUS")
    centrar_titulos("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    mes, mes_letras= meses_del_año()
    df = serviplus(mes)
    st.dataframe(df,width=800)
    with pd.ExcelWriter('evaluaciones.xlsx') as writer:
        df.to_excel(writer, index=False)
    with open('evaluaciones.xlsx', 'rb') as f:
        bytes_data = f.read()
    if df.empty == True:
        st.sidebar.write("No hay informacion para descargar")
    else:
        st.sidebar.download_button(label="Descargar evaluaciones", data=bytes_data, file_name=f'evaluaciones serviplus {mes_letras}.xlsx', mime='application/vnd.ms-excel', key='descargar_excel_serv')
def Dapreca():
    st.image(r'logos/DAPRECA.png',width=150)
    centrar_titulos("GESTION DE EVALUACIONES DAPRECA")
    centrar_titulos("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    mes, mes_letras= meses_del_año()
    df = dapreca(mes)
    st.write(df)
    with pd.ExcelWriter('evaluaciones.xlsx') as writer:
        df.to_excel(writer, index=False)
    with open('evaluaciones.xlsx', 'rb') as f:
        bytes_data = f.read()
    if df.empty == True:
        st.sidebar.write("No hay informacion para descargar")
    else:
        st.sidebar.download_button(label="Descargar evaluaciones", data=bytes_data, file_name=f'evaluaciones dapreca {mes_letras}.xlsx', mime='application/vnd.ms-excel', key='descargar_excel_dapreca')
def Inversiones():
    st.image(r'logos/INVERSIONES GHALMACA.png',width=300)
    centrar_titulos("GESTION DE EVALUACIONES INVERSIONES GHALMACA")
    centrar_titulos("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    mes, mes_letras= meses_del_año()
    df = inversiones(mes)
    st.write(df)
    with pd.ExcelWriter('evaluaciones.xlsx') as writer:
        df.to_excel(writer, index=False)
    with open('evaluaciones.xlsx', 'rb') as f:
        bytes_data = f.read()
    if df.empty == True:
        st.sidebar.write("No hay informacion para descargar")
    else:
        st.sidebar.download_button(label="Descargar evaluaciones", data=bytes_data, file_name=f'evaluaciones inversiones {mes_letras}.xlsx', mime='application/vnd.ms-excel', key='descargar_excel_inv')
def Transporte():
    st.image(r'logos/GHALMACA TRANSPORTE.png',width=300)
    centrar_titulos("GESTION DE EVALUACIONES INVERSIONES GHALMACA")
    centrar_titulos("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    mes, mes_letras= meses_del_año()
    df = transporte(mes)
    st.write(df)
    with pd.ExcelWriter('evaluaciones.xlsx') as writer:
        df.to_excel(writer, index=False)
    with open('evaluaciones.xlsx', 'rb') as f:
        bytes_data = f.read()
    if df.empty == True:
        st.sidebar.write("No hay informacion para descargar")
    else:
        st.sidebar.download_button(label="Descargar evaluaciones", data=bytes_data, file_name=f'evaluaciones multiservicios {mes_letras}.xlsx', mime='application/vnd.ms-excel', key='descargar_excel_trans')
def Galpego():
    st.image(r'logos/GALPEGO.png',width=300)
    centrar_titulos("GESTION DE EVALUACIONES GALPEGO")
    centrar_titulos("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    mes, mes_letras= meses_del_año()
    df = galpego(mes)
    st.write(df)
    with pd.ExcelWriter('evaluaciones.xlsx') as writer:
        df.to_excel(writer, index=False)
    with open('evaluaciones.xlsx', 'rb') as f:
        bytes_data = f.read()
    if df.empty == True:
        st.sidebar.write("No hay informacion para descargar")
    else:
        st.sidebar.download_button(label="Descargar evaluaciones", data=bytes_data, file_name=f'evaluaciones galpego {mes_letras}.xlsx', mime='application/vnd.ms-excel', key='descargar_excel_GAL')
def Ferregal():
    st.image(r'logos/FERREGAL.png',width=300)
    centrar_titulos("GESTION DE EVALUACIONES FERREGAL")
    centrar_titulos("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    mes, mes_letras= meses_del_año()
    df = ferregal(mes)
    st.write(df)
    with pd.ExcelWriter('evaluaciones.xlsx') as writer:
        df.to_excel(writer, index=False)
    with open('evaluaciones.xlsx', 'rb') as f:
        bytes_data = f.read()
    if df.empty == True:
        st.sidebar.write("No hay informacion para descargar")
    else:
        st.sidebar.download_button(label="Descargar evaluaciones", data=bytes_data, file_name=f'evaluaciones ferregal{mes_letras}.xlsx', mime='application/vnd.ms-excel', key='descargar_excel_FER')

def Admin():
    st.image(r'logos/Admin-contab.jpg',width=300)
    centrar_titulos("GESTION DE EVALUACIONES CONTABILIDAD Y ADMINISTRACION")
    centrar_titulos("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    mes, mes_letras= meses_del_año()
    df = admin(mes)
    st.write(df)
    with pd.ExcelWriter('evaluaciones.xlsx') as writer:
        df.to_excel(writer, index=False)
    with open('evaluaciones.xlsx', 'rb') as f:
        bytes_data = f.read()
    if df.empty == True:
        st.sidebar.write("No hay informacion para descargar")
    else:
        st.sidebar.download_button(label="Descargar evaluaciones", data=bytes_data, file_name=f'evaluaciones ferregal{mes_letras}.xlsx', mime='application/vnd.ms-excel', key='descargar_excel_adm')

def Global21():
    st.warning("En Mantenimiento")