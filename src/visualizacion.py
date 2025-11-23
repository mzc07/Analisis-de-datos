import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import dataset_global, cargar_dataset

def mostrar_visualizaciones():
    # Si el dataset no está cargado, lo cargamos
    df = dataset_global
    if df is None:
        df = cargar_dataset()

    # HISTOGRAMA: muestra cómo se distribuyen los valores de la tasa de suicidio
    plt.figure(figsize=(8,5))
    plt.hist(df["Suicide Rate"], bins=30)
    plt.title("Distribución de la Tasa de Suicidio (Histograma)")
    plt.xlabel("Tasa de suicidio")
    plt.ylabel("Frecuencia")
    plt.show()

    # BOXPLOT: permite ver valores atípicos y la dispersión general
    plt.figure(figsize=(7,5))
    sns.boxplot(x=df["Suicide Rate"])
    plt.title("Dispersión y Valores Atípicos de la Tasa de Suicidio (Boxplot)")
    plt.xlabel("Tasa de suicidio")
    plt.show()

    # LÍNEA POR AÑO: cómo cambia la tasa de suicidio promedio a través del tiempo
    tasas_por_anio = df.groupby("Year")["Suicide Rate"].mean()
    plt.figure(figsize=(9,5))
    plt.plot(tasas_por_anio.index, tasas_por_anio.values)
    plt.title("Tasa de Suicidio Promedio por Año")
    plt.xlabel("Año")
    plt.ylabel("Tasa promedio")
    plt.show()

    # MAPA DE CALOR: correlación entre columnas numéricas del dataset
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.title("Mapa de Calor de Correlaciones del Dataset")
    plt.show()

    # BARRAS: ranking del promedio histórico por país
    ranking = df.groupby("Country Name")["Suicide Rate"].mean().sort_values(ascending=False)
    plt.figure(figsize=(10,12))
    ranking.plot(kind="bar")
    plt.title("Promedio Histórico de Tasa de Suicidio por País")
    plt.xlabel("País")
    plt.ylabel("Promedio de tasa de suicidio")
    plt.tight_layout()
    plt.show()

    # DISPERSIÓN: relación entre el año y la tasa de suicidio
    plt.figure(figsize=(8,5))
    plt.scatter(df["Year"], df["Suicide Rate"])
    plt.title("Relación entre Año y Tasa de Suicidio (Dispersión)")
    plt.xlabel("Año")
    plt.ylabel("Tasa de suicidio")
    plt.show()

if __name__ == "__main__":
    mostrar_visualizaciones()
