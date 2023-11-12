import gspread
from oauth2client.service_account import ServiceAccountCredentials

def credenciales():
    credenciales = r"Credenciales/cred.json"
    # Definir las credenciales de la cuenta de servicio de Google Sheets
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credenciales, scope)
    gc = gspread.authorize(creds)
    return gc
