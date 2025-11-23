import pandas as pd

url_dataset = 'https://raw.githubusercontent.com/mzc07/Analisis-de-datos/refs/heads/main/Datos/dataset.csv'

dataset_global = None   # variable global compartida

def cargar_dataset():
    global dataset_global
    try:
        # Intentar cargar desde URL
        dataset_global = pd.read_csv(url_dataset)
        print("Dataset cargado desde la URL con éxito.")
    
    except Exception as error:
        print(f"Error al cargar desde URL: {error}")
        print("Intentando acceder localmente al archivo...")
        try:
            dataset_global = pd.read_csv(r'data\dataset.csv')
            print("Dataset cargado localmente con éxito.")
        except Exception as err_local:
            print(f"Error al cargar localmente: {err_local}")
            dataset_global = None
    
    return dataset_global
