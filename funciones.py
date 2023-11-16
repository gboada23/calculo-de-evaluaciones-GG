from creds import credenciales
import pandas as pd
gc = credenciales()
def gsheet():
    ID = "1VAzhIBSoWo6KoeZmQJoydNw16ucNusU44rdqhgnxFqs"
    return ID
ID = gsheet()
def serviplus(mes):
    pd.set_option('display.max_colwidth', None)
    tabla = gc.open_by_key(ID).worksheet('EVA SERVIPLUS').get_all_records()
    BD = gc.open_by_key(ID).worksheet('SERVIPLUS').get_all_records()
    df = pd.DataFrame(tabla)
    df2 = pd.DataFrame(BD)
    df["FECHA"] = pd.to_datetime(df["FECHA"], format = "%d/%m/%Y")
    df["MES"] = df['FECHA'].dt.month
    df = df[df['MES'] == mes].copy()
    numericas = ['CUMPLIENTO DE HORARIO','DISCRECION POLITICAS INTERNAS', 'CLIMA ORGANIZACIONAL','CUMPLIMIENTO DE ACTIVIDADES ']
    df = df.groupby("PERSONAL").mean(numeric_only=True)[numericas].reset_index()
    for columna in numericas:
        df[columna] = round(df[columna]/4,2)
    df["DESEMPEÑO DEL MES"] = df['CUMPLIENTO DE HORARIO']*0.25 + df['DISCRECION POLITICAS INTERNAS']*0.25+ df['CLIMA ORGANIZACIONAL']*0.25 +df['CUMPLIMIENTO DE ACTIVIDADES ']*0.25
    df["DESEMPEÑO DEL MES"] = round(df["DESEMPEÑO DEL MES"],2)
    df.drop(columns = numericas, inplace = True)
    df2 = df2.copy()
    df2 = df2[['NOMBRE', 'CEDULA','CARGO']]
    new_df = pd.merge(df, df2, left_on = 'PERSONAL',right_on='NOMBRE', how= 'left')
    new_df = new_df[['PERSONAL',  'CEDULA',  'CARGO','DESEMPEÑO DEL MES']]
    new_df['DESEMPEÑO DEL MES'] = new_df['DESEMPEÑO DEL MES'].apply(lambda x: f'{x * 100}'.replace('.', ',') + '%')
    return new_df
def dapreca(mes):
    tabla = gc.open_by_key(ID).worksheet('EVA DAPRECA').get_all_records()
    BD = gc.open_by_key(ID).worksheet('DAPRECA').get_all_records()
    df = pd.DataFrame(tabla).copy()
    df2 = pd.DataFrame(BD).copy()
    df["FECHA"] = pd.to_datetime(df["FECHA"], format = "%d/%m/%Y")
    df["MES"] = df['FECHA'].dt.month
    df = df[df['MES'] == mes]
    numericas = ['CUMPLIENTO DE HORARIO','DISCRECION POLITICAS INTERNAS','CUMPLIMIENTO DE ACTIVIDADES ']
    df = df.groupby("PERSONAL").mean(numeric_only=True)[numericas].reset_index()
    for columna in numericas:
        df[columna] = round(df[columna]/4,2)
    df["DESEMPEÑO DEL MES"] = round((df['CUMPLIENTO DE HORARIO'] + df['DISCRECION POLITICAS INTERNAS'] +df['CUMPLIMIENTO DE ACTIVIDADES '])/3,2)
    df.drop(columns = numericas, inplace = True)
    df2 = df2
    df2 = df2[['NOMBRE', 'CEDULA','CARGO']]
    new_df = pd.merge(df, df2, left_on = 'PERSONAL',right_on='NOMBRE', how= 'left')
    new_df = new_df[['PERSONAL',  'CEDULA',  'CARGO','DESEMPEÑO DEL MES']]
    new_df['DESEMPEÑO DEL MES'] = new_df['DESEMPEÑO DEL MES'].apply(lambda x: f'{x * 100}'.replace('.', ',') + '%')
    return new_df

def inversiones(mes):
    tabla = gc.open_by_key(ID).worksheet('EVA INV GHALMACA').get_all_records()
    BD = gc.open_by_key(ID).worksheet('INV GHALMACA').get_all_records()
    df = pd.DataFrame(tabla).copy()
    df2 = pd.DataFrame(BD).copy()
    df["FECHA"] = pd.to_datetime(df["FECHA"], format = "%d/%m/%Y")
    df["MES"] = df['FECHA'].dt.month
    df = df[df['MES'] == mes]
    numericas = ['CUMPLIENTO DE HORARIO','DISCRECION POLITICAS INTERNAS','CUMPLIMIENTO DE ACTIVIDADES ']
    df = df.groupby("PERSONAL").mean(numeric_only=True)[numericas].reset_index()
    for columna in numericas:
        df[columna] = round(df[columna]/4,2)
    df["DESEMPEÑO DEL MES"] = round((df['CUMPLIENTO DE HORARIO'] + df['DISCRECION POLITICAS INTERNAS'] +df['CUMPLIMIENTO DE ACTIVIDADES '])/3,2)
    df.drop(columns = numericas, inplace = True)
    df2 = df2
    df2 = df2[['NOMBRE', 'CEDULA','CARGO']]
    new_df = pd.merge(df, df2, left_on = 'PERSONAL',right_on='NOMBRE', how= 'left')
    new_df = new_df[['PERSONAL',  'CEDULA',  'CARGO','DESEMPEÑO DEL MES']]
    new_df['DESEMPEÑO DEL MES'] = new_df['DESEMPEÑO DEL MES'].apply(lambda x: f'{x * 100}'.replace('.', ',') + '%')
    return new_df

def transporte(mes):
    tabla = gc.open_by_key(ID).worksheet('EVA MULT GHALMACA').get_all_records()
    BD = gc.open_by_key(ID).worksheet('MULT GHALMACA').get_all_records()
    df = pd.DataFrame(tabla).copy()
    df2 = pd.DataFrame(BD).copy()
    df["FECHA"] = pd.to_datetime(df["FECHA"], format = "%d/%m/%Y")
    df["MES"] = df['FECHA'].dt.month
    df = df[df['MES'] == mes]
    numericas = ['TRABAJO EN EQUIPO','DESENVOLVIMIENTO EN EL AREA DE TRABAJO','CUMPLIMIENTO DEL DESPACHO','CUMPLIMIENTO DE HORARIO','PRESENCIA EN SU PUESTO DE TRABAJO']
    df = df.groupby("PERSONAL").mean(numeric_only=True)[numericas].reset_index()
    for columna in numericas:
        df[columna] = round(df[columna]/4,2)
    df["DESEMPEÑO DEL MES"] = round((df['TRABAJO EN EQUIPO'] + df['DESENVOLVIMIENTO EN EL AREA DE TRABAJO'] +df['CUMPLIMIENTO DEL DESPACHO']) +df['CUMPLIMIENTO DE HORARIO']+df['PRESENCIA EN SU PUESTO DE TRABAJO']/5,2)
    df.drop(columns = numericas, inplace = True)
    df2 = df2[['NOMBRE', 'CEDULA','CARGO']]
    new_df = pd.merge(df, df2, left_on = 'PERSONAL',right_on='NOMBRE', how= 'left')
    new_df = new_df[['PERSONAL',  'CEDULA',  'CARGO','DESEMPEÑO DEL MES']]
    new_df['DESEMPEÑO DEL MES'] = new_df['DESEMPEÑO DEL MES'].apply(lambda x: f'{x * 100}'.replace('.', ',') + '%')
    return new_df

def galpego(mes):
    tabla = gc.open_by_key(ID).worksheet('EVA GALPEGO').get_all_records()
    BD = gc.open_by_key(ID).worksheet('GALPEGO').get_all_records()
    df = pd.DataFrame(tabla).copy()
    df2 = pd.DataFrame(BD).copy()
    df["FECHA"] = pd.to_datetime(df["FECHA"], format = "%d/%m/%Y")
    df["MES"] = df['FECHA'].dt.month
    df = df[df['MES'] == mes]
    numericas = ['ORDEN Y LIMPIEZA','PUNTUALIDAD','TRABAJO EN EQUIPO','CONOCIMIENTO E INICIATIVA']
    df = df.groupby("PERSONAL").mean(numeric_only=True)[numericas].reset_index()
    for columna in numericas:
        df[columna] = round(df[columna]/4,2)
    df["DESEMPEÑO DEL MES"] = round((df['ORDEN Y LIMPIEZA'] + df['PUNTUALIDAD'] +df['TRABAJO EN EQUIPO']+df['CONOCIMIENTO E INICIATIVA'])/4,2)
    df.drop(columns = numericas, inplace = True)
    df2 = df2[['NOMBRE', 'CEDULA','CARGO']]
    new_df = pd.merge(df, df2, left_on = 'PERSONAL',right_on='NOMBRE', how= 'left')
    new_df = new_df[['PERSONAL',  'CEDULA',  'CARGO','DESEMPEÑO DEL MES']]
    new_df['DESEMPEÑO DEL MES'] = new_df['DESEMPEÑO DEL MES'].apply(lambda x: f'{x * 100}'.replace('.', ',') + '%')
    return new_df