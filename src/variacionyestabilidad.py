import pandas as pd
import numpy as np
import src.data_loader as data_loader   # importar el módulo completo


def analizar_suicidios():
    """
    Analiza variación interna, estabilidad y outliers del dataset global.
    Usa el dataset cargado previamente en data_loader.
    """

    if data_loader.dataset_global is None:
        print("Error: el dataset no está cargado. Use la opción 1 del menú primero.")
        return

    df = data_loader.dataset_global.copy()

    # Limpieza
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    df["Suicide Rate"] = pd.to_numeric(df["Suicide Rate"], errors="coerce")

    df = df.sort_values(["Country Name", "Year"]).reset_index(drop=True)

    # Variación interna por país
    variation_df = df.groupby("Country Name").agg(
        mean_rate=("Suicide Rate", "mean"),
        min_rate=("Suicide Rate", "min"),
        max_rate=("Suicide Rate", "max"),
        std_rate=("Suicide Rate", "std"),
    )
    variation_df["range"] = variation_df["max_rate"] - variation_df["min_rate"]
    variation_df["CV"] = variation_df["std_rate"] / variation_df["mean_rate"]

    stability_rank = variation_df.sort_values("CV")

    # Cambios interanuales
    df["yearly_change"] = df.groupby("Country Name")["Suicide Rate"].diff()

    threshold = df["yearly_change"].abs().std() * 3
    yearly_outliers = df[df["yearly_change"].abs() > threshold]

    # Estabilidad global
    global_stability = df.groupby("Year")["Suicide Rate"].std()

    # Variación interna mínima y máxima
    least_variation = variation_df.sort_values("range").head(10)
    most_variation = variation_df.sort_values("range", ascending=False).head(10)

    print("\n>>> Países más estables (menor CV):")
    print(stability_rank.head(10))

    print("\n>>> Países menos estables (mayor CV):")
    print(stability_rank.tail(10))

    print("\n>>> Cambios atípicos (shocks):")
    print(yearly_outliers.head(10))

    print("\n>>> Estabilidad global por año (std):")
    print(global_stability)

    print("\n>>> Países con menor variación interna:")
    print(least_variation)

    print("\n>>> Países con mayor variación interna:")
    print(most_variation)
