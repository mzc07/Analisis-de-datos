import pandas as pd
from data_loader import dataset_global

def obtener_estadisticas():
    def estadisticos_globales(df: dataset_global) -> dict:
        """
        Calcula mínimo, máximo, media, mediana y desviación estándar
        de la columna 'tasa' para todo el dataset.

        Returns:
            dict: valores estadísticos.
        """
        tasa = df["tasa"]

        return {
            "min": tasa.min(),
            "max": tasa.max(),
            "media": tasa.mean(),
            "mediana": tasa.median(),
            "desviacion_estandar": tasa.std()
        }


    def extremos_por_anio(df: pd.DataFrame) -> pd.DataFrame:
        """
        Identifica el país con mayor y menor tasa en cada año.

        Returns:
            DataFrame con columnas:
            anio | pais_max | max_tasa | pais_min | min_tasa
        """

        # Obtener índice de máximo y mínimo por año
        idx_max = df.groupby("anio")["tasa"].idxmax()
        idx_min = df.groupby("anio")["tasa"].idxmin()

        df_max = df.loc[idx_max, ["anio", "pais", "tasa"]].rename(
            columns={"pais": "pais_max", "tasa": "max_tasa"}
        )

        df_min = df.loc[idx_min, ["anio", "pais", "tasa"]].rename(
            columns={"pais": "pais_min", "tasa": "min_tasa"}
        )

        # Combinar por año
        df_extremos = df_max.merge(df_min, on="anio")

        return df_extremos
