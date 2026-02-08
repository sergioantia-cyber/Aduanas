import pandas as pd
import os
import glob

def limpiar_datos():
    archivos = glob.glob('impos*.*')
    if not archivos:
        print("❌ ERROR: No veo el archivo en C:\\Users\\DerEine\Desktop\\bot chamba papa")
        return

    file_name = archivos[0]
    try:
        if file_name.endswith('.xlsx'):
            df = pd.read_excel(file_name)
        else:
            df = pd.read_csv(file_name, low_memory=False)
        
        df.columns = ['CLIENTE', 'CONTROL', 'ADUANA', 'FECHA', 'REFERENCIA', 'ANTIDROGA', 'CHOFER']
        df = df[df['ADUANA'].notna()]
        df = df[df['ADUANA'].str.contains('TIENDITAS', na=False, case=False)]

        # NUEVO: Extraer el mes para el desglose detallado
        df['FECHA_DT'] = pd.to_datetime(df['FECHA'], dayfirst=True, errors='coerce')
        # Mapeo de meses en español
        meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 
                 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
        df['MES'] = df['FECHA_DT'].dt.month.map(meses).fillna('Sin Fecha')

        df.to_json('datos_finales.json', orient='records', force_ascii=False)
        print(f"✅ ¡LISTO! Datos preparados con desglose mensual.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    limpiar_datos()