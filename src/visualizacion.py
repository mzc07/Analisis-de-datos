import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import src.data_loader as data_loader   # Importar módulo completo


def mostrar_visualizaciones():
    df = data_loader.dataset_global

    if df is None:
        df = data_loader.cargar_dataset()

    # HISTOGRAMA
    plt.figure(figsize=(8,5))
    plt.hist(df["Suicide Rate"], bins=30)
    plt.title("Distribución de la Tasa de Suicidio (Histograma)")
    plt.xlabel("Tasa de suicidio")
    plt.ylabel("Frecuencia")
    plt.show()

    # BOXPLOT
    plt.figure(figsize=(7,5))
    sns.boxplot(x=df["Suicide Rate"])
    plt.title("Dispersión y Valores Atípicos (Boxplot)")
    plt.xlabel("Tasa de suicidio")
    plt.show()

    # LÍNEA POR AÑO
    tasas_por_anio = df.groupby("Year")["Suicide Rate"].mean()
    plt.figure(figsize=(9,5))
    plt.plot(tasas_por_anio.index, tasas_por_anio.values)
    plt.title("Tasa de Suicidio Promedio por Año")
    plt.xlabel("Año")
    plt.ylabel("Tasa promedio")
    plt.show()

    # HEATMAP
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.title("Mapa de Calor de Correlaciones")
    plt.show()

    # BARRAS
    ranking = df.groupby("Country Name")["Suicide Rate"].mean().sort_values(ascending=False)
    plt.figure(figsize=(10,12))
    ranking.plot(kind="bar")
    plt.title("Promedio Histórico por País")
    plt.xlabel("País")
    plt.ylabel("Tasa promedio")
    plt.tight_layout()
    plt.show()

    # DISPERSIÓN
    plt.figure(figsize=(8,5))
    plt.scatter(df["Year"], df["Suicide Rate"])
    plt.title("Año vs Tasa de Suicidio")
    plt.xlabel("Año")
    plt.ylabel("Tasa de suicidio")
    plt.show()
