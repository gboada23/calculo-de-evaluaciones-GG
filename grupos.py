import streamlit as st
from PIL import Image
from funciones import personalgrupo
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from streamlit import secrets

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
    las evaluaciones procesadas del personal por mes, lo primero que deben hacer es seleccionar la
    empresa correspondiente a cada gerente y luego les aparecerá el mes donde desean obtener la evaluación, se le
    mostrará una tabla con vista preliminar antes de descargar para que puedan chequear la información, una vez
    chequeada presionan el botón descargar para proceder a bajar el excel con las evaluaciones correspondientes al mes seleccionado.
    """
    # Usando HTML y CSS para justificar el texto
    col2.markdown(f"<h5 style='text-align: justify;'>{texto}</h5>", unsafe_allow_html=True)

def Admin():
    centrar_titulos("GESTION DE EVALUACIONES PERSONAL GRUPO")
    centrar_titulos("")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    mes, mes_letras= meses_del_año()
    df = personalgrupo(mes)
    st.write(df)
    with pd.ExcelWriter('evaluaciones.xlsx') as writer:
        df.to_excel(writer, index=False)
    with open('evaluaciones.xlsx', 'rb') as f:
        bytes_data = f.read()
    if df.empty:
        st.sidebar.write("No hay informacion para descargar")
    else:
        st.sidebar.download_button(label="Descargar evaluaciones", data=bytes_data, file_name=f'Evaluaciones personal mes {mes_letras}.xlsx', mime='application/vnd.ms-excel', key='descargar_excel_adm')
        # Botón para enviar correos electrónicos
    if st.button("Enviar correos electrónicos"):
        enviaremail(df,mes_letras)  # Llama a la función para enviar correos

def enviaremail(df, mes):
    for _, row in df.iterrows():
        nombre = row['PERSONAL'].title()
        correo = row['CORREO']
        cumplimiento_horario = row['cumplimiento_horario']
        discrecion_politicas = row['discrecion_politicas']
        clima_organizacional = row['clima_organizacional']
        cumplimiento_actividades = row['cumplimiento_actividades']
        resultado_final = row['Resultado final']
        supervisor = row['SUPERVISOR INMEDIATO'].title()

        # Creamos el mensaje de correo
        mensaje = MIMEMultipart()
        mensaje['From'] = secrets['CORREO']
        mensaje['To'] = correo
        mensaje['Subject'] = f'Evaluación del Mes de {mes} para {nombre}'

        # Formato del cuerpo del correo en HTML
        cuerpo_html = f"""
            <html>
                <body>
                    <div style='background: #efefef; margin: 10px auto; padding: 30px; text-align: center; width: 500px; box-sizing: border-box;'>
                        <img src='https://ghalmaca.com/wp-content/uploads/Admin-contab.jpg' style='width: 150px'>
                    </div>
                    <div style='width: 500px; margin: 0 auto; background-color: #FFF;'>
                        <h1 style='text-align: center;'>Hola, {nombre}</h1>
                        <h4>Aqui podras visualizar tú evaluación de desempeño del mes de {mes}:</h4>
                        <p><strong>Cumplimiento de Horario:</strong> {cumplimiento_horario}</p>
                        <p><strong>Discreción en Políticas Internas:</strong> {discrecion_politicas}</p>
                        <p><strong>Clima Organizacional:</strong> {clima_organizacional}</p>
                        <p><strong>Cumplimiento de Actividades:</strong> {cumplimiento_actividades}</p>
                        <h3 style='text-align: center;'>Resultado Final: {resultado_final}</h3>
                    </div>
                    <div style='width: 500px; background: #efefef; padding: 15px 30px; text-align: justify; margin: 10px auto; box-sizing: border-box;'>
                        <p style='margin: 0;'>Si tienes alguna duda o comentario, no dudes en comunicarte con tu supervisor inmediato
                            <strong>{supervisor}</strong>, quien es el encargado de evaluar tu desempeño.</p><br>
                        <p style='text-align: center; margin: 0;'>Saludos Atentamente,<br> <strong>Gustavo Boada <br>Coordinador de Tecnología</strong></p>
                    </div>
                </body>
            </html>

            """
        # Adjuntar el cuerpo HTML al mensaje
        mensaje.attach(MIMEText(cuerpo_html, 'html'))
            # Enviar el correo
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as servidor: 
                servidor.starttls()
                #loggin
                servidor.login(secrets['CORREO'], secrets['CONTRA'])
                servidor.sendmail(secrets['CORREO'], correo, mensaje.as_string())    
        except Exception as e:
            st.error(f'Error al enviar correo a {nombre} ({correo}): {e}')
    
    st.success(f'Correos del mes de {mes} enviados masivamente con éxito.')