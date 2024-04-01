import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
def credenciales():
    credenciales = st.secrets["google_sheets_credentials"]

    creds_dict = eval(credenciales)  # Evalúa la cadena JSON para convertirla en un diccionario
    scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    # Asegurar que las credenciales incluyan el alcance necesario
    credentials = Credentials.from_service_account_info(creds_dict, scopes=scopes)

    # Usar gspread para autenticar con Google Sheets
    gc = gspread.authorize(credentials)
    return gc
