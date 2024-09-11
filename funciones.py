from creds import credenciales
import pandas as pd
gc = credenciales()
def personalgrupo(mes):
    # Abrimos la hoja de Google y cargamos los datos
    grupo = gc.open('GRUPO DE EMPRESAS NUEVA').worksheet('EVALUACIONES')
    datos = grupo.get_all_records()
    datos = pd.DataFrame(datos)

    # Formateamos la fecha y extraemos el mes
    datos['FECHA'] = pd.to_datetime(datos['FECHA'], format='%d/%m/%Y')
    datos['MES'] = datos['FECHA'].dt.month

    # Filtramos los datos para el mes solicitado
    mes = datos[datos['MES'] == mes].copy()

    # Calculamos los porcentajes de cada columna de evaluación
    mes['cumplimiento_horario'] = mes["CUMPLIENTO DE HORARIO"] / 4
    mes['discrecion_politicas'] = mes["DISCRECION POLITICAS INTERNAS"] / 4
    mes['clima_organizacional'] = mes["CLIMA ORGANIZACIONAL"] / 4
    mes['cumplimiento_actividades'] = mes["CUMPLIMIENTO DE ACTIVIDADES "] / 4

    # Calculamos el resultado promedio global usando los valores normalizados
    mes['Resultado final'] = (mes['cumplimiento_horario'] + 
                        mes['discrecion_politicas'] + 
                        mes['clima_organizacional'] + 
                        mes['cumplimiento_actividades']) / 4

    # Agrupamos los resultados por el personal y calculamos el promedio
    mes = mes.groupby('PERSONAL')[["PERSONAL", 
                                   "cumplimiento_horario", 
                                   "discrecion_politicas", 
                                   "clima_organizacional", 
                                   "cumplimiento_actividades", 
                                   "Resultado final"]].mean(numeric_only=True).reset_index()

    # Cargamos la lista del personal
    personal = gc.open('GRUPO DE EMPRESAS NUEVA').worksheet('LISTADO DEL PERSONAL')
    personal = personal.get_all_records()
    personal = pd.DataFrame(personal)
    personal = personal[['NOMBRES Y APELLIDOS','CEDULA','CARGO','CORREO','SUPERVISOR INMEDIATO']]
    personal = personal.rename(columns={'NOMBRES Y APELLIDOS':'PERSONAL'})

    # Realizamos el merge con los resultados del personal
    merge = pd.merge(personal, mes, on="PERSONAL", how="inner")
    merge = merge.sort_values(by='PERSONAL', ascending=True)
    merge = merge.round(2)
    columnas=['cumplimiento_horario', 'discrecion_politicas', 'clima_organizacional', 'cumplimiento_actividades','Resultado final']
    for columna in columnas:
      merge[columna] = merge[columna].apply(lambda x: f'{x * 100}'.replace('.', ',') + '%')
    return merge