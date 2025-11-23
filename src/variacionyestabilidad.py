import pandas as pd
import numpy as np


df = pd.read_csv("D:/USUARIO/Mis documentos/Hogar/Analisis-de-datos-main/data/dataset.csv")

print("Vista inicial del dataset:")
print(df.head(), "\n")


#  Limpieza, Se asegura que el año sea entero y que la tasa sea numérica y se ordenan los registros por país y año 

df['Year'] = df['Year'].astype(int)
df['Suicide Rate'] = pd.to_numeric(df['Suicide Rate'], errors='coerce')

df = df.sort_values(by=["Country Name", "Year"]).reset_index(drop=True)




# Variación interna
variation_df = df.groupby("Country Name").agg(
    mean_rate=("Suicide Rate", "mean"),# valor promedio
    min_rate=("Suicide Rate", "min"),
    max_rate=("Suicide Rate", "max"),
    std_rate=("Suicide Rate", "std") # desviación estándar 
)
# cuánto varía la tasa entre su máximo y mínimo.
variation_df["range"] = variation_df["max_rate"] - variation_df["min_rate"]

# CV bajo = país estable CV alto = país inestable

variation_df["CV"] = variation_df["std_rate"] / variation_df["mean_rate"]

print(">>> Variación interna (primeros países):")
print(variation_df.head(), "\n")



# estabilidad

# mayor estabilidad = CV bajo

estability_rank = variation_df.sort_values(by="CV")

print(">>> Países más estables (menor CV):")
print(estability_rank.head(10), "\n")

print(">>> Países menos estables (mayor CV):")
print(estability_rank.tail(10), "\n")



# cambio entre un año y el siguiente para cada país.

df["yearly_change"] = df.groupby("Country Name")["Suicide Rate"].diff()

# Identificar valores anómalos un cambio anormalmente grande.

threshold = df["yearly_change"].abs().std() * 3
outliers = df[df["yearly_change"].abs() > threshold]

print(">>> Años con cambios atípicos (shocks):")
print(outliers.head(10), "\n")



# estabilidad global por año desviación estándar mundial para cada año.

global_stability = df.groupby("Year")["Suicide Rate"].std()

print(">>> Estabilidad global (desviación estándar por año):")
print(global_stability, "\n")


# Variación interna y estabilidad


# Ordenar por variación 
least_variation = variation_df.sort_values("range").head(10)
most_variation = variation_df.sort_values("range", ascending=False).head(10)

print("\n>>> Países con menor variación interna (rango más bajo):")
print(least_variation)

print("\n>>> Países con mayor variación interna (rango más alto):")
print(most_variation)