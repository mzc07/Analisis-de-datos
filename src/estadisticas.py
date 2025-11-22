import pandas as pd
import src.data_loader as dl

def calcular_estadisticas():
    if dl.dataset_global is None:
        print("El dataset no ha sido cargado.")
        return

    df = dl.dataset_global

    minimo = df["Suicide Rate"].min()
    maximo = df["Suicide Rate"].max()
    media = df["Suicide Rate"].mean()
    mediana = df["Suicide Rate"].median()
    desviacion = df["Suicide Rate"].std()

    print("=== Estadísticas Globales de Suicide Rate ===")
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desviación estándar: {desviacion}\n")

    print("=== País con mayor y menor tasa por año ===")
    por_anio = df.groupby("Year")

    for year, group in por_anio:
        max_row = group.loc[group["Suicide Rate"].idxmax()]
        min_row = group.loc[group["Suicide Rate"].idxmin()]

        print(f"Año {year}:")
        print(f"  Mayor tasa: {max_row['Country Name']} ({max_row['Suicide Rate']})")
        print(f"  Menor tasa: {min_row['Country Name']} ({min_row['Suicide Rate']})")
        print()
