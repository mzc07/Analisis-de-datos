import pandas as pd

url_dataset = 'https://raw.githubusercontent.com/mzc07/Analisis-de-datos/refs/heads/main/Datos/dataset.csv'

dataset_global = None   # variable global compartida

def cargar_dataset():
    global dataset_global
    try:
        dataset_global = pd.read_csv(url_dataset)
    except Exception as error:
        print(f'Error: {error}')
        return None
    else:
        print("Dataset cargado con exito.")
        return dataset_global
