import matplotlib.pyplot as plt
import src.data_loader as dl
import pandas as pd


def menu_outliers():
    if dl.dataset_global is None:
        print("El dataset no ha sido cargado.")
        return

    print("=== Análisis de Outliers ===")
    print("1. Outliers globales (todo el dataset).")
    print("2. Outliers por país.")
    print("3. Visualización (boxplot global).")
    print("4. Países con mayor cantidad de outliers.")
    print("0. Volver.")

    try:
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Opción inválida.")
        return

    match opcion:
        case 1:
            outliers_globales()
        case 2:
            outliers_por_pais()
        case 3:
            boxplot_global()
        case 4:
            paises_con_mas_outliers()
        case 0:
            return
        case _:
            print("Opción inválida.")


# ----------------------------------------------------------------------
# OUTLIERS GLOBALES
# ----------------------------------------------------------------------

def outliers_globales():
    df = dl.dataset_global

    Q1 = df["Suicide Rate"].quantile(0.25)
    Q3 = df["Suicide Rate"].quantile(0.75)
    IQR = Q3 - Q1

    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR

    outliers = df[
        (df["Suicide Rate"] < limite_inf) |
        (df["Suicide Rate"] > limite_sup)
    ]

    print("=== Outliers Globales ===")
    print(f"Límite inferior: {limite_inf}")
    print(f"Límite superior: {limite_sup}")
    print(f"Cantidad total de outliers: {len(outliers)}\n")

    if len(outliers) > 0:
        print(outliers[["Country Name", "Year", "Suicide Rate"]].to_string(index=False))
    else:
        print("No se detectaron valores atípicos.")


# ----------------------------------------------------------------------
# OUTLIERS POR PAÍS
# ----------------------------------------------------------------------

def outliers_por_pais():
    df = dl.dataset_global

    paises = sorted(df["Country Name"].unique())
    print("=== Países disponibles ===")
    for i, p in enumerate(paises, start=1):
        print(f"{i}. {p}")

    try:
        opcion = int(input("Seleccione un país: "))
        pais = paises[opcion - 1]
    except:
        print("Opción inválida.")
        return

    df_pais = df[df["Country Name"] == pais].copy()

    Q1 = df_pais["Suicide Rate"].quantile(0.25)
    Q3 = df_pais["Suicide Rate"].quantile(0.75)
    IQR = Q3 - Q1

    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR

    outliers = df_pais[
        (df_pais["Suicide Rate"] < limite_inf) |
        (df_pais["Suicide Rate"] > limite_sup)
    ]

    print(f"=== Outliers en {pais} ===")
    print(f"Límite inferior: {limite_inf}")
    print(f"Límite superior: {limite_sup}")
    print(f"Cantidad de outliers: {len(outliers)}\n")

    if len(outliers) > 0:
        print(outliers[["Year", "Suicide Rate"]].to_string(index=False))
    else:
        print("Sin outliers para este país.")


# ----------------------------------------------------------------------
# BOX PLOT GLOBAL
# ----------------------------------------------------------------------

def boxplot_global():
    df = dl.dataset_global

    plt.figure(figsize=(6, 6))
    plt.boxplot(df["Suicide Rate"], vert=True)
    plt.title("Boxplot global de Suicide Rate")
    plt.ylabel("Tasa de suicidio")
    plt.grid(True)
    plt.show()


# ----------------------------------------------------------------------
# PAISES CON MÁS OUTLIERS
# ----------------------------------------------------------------------

def paises_con_mas_outliers():
    df = dl.dataset_global

    lista = []

    for pais, grupo in df.groupby("Country Name"):
        Q1 = grupo["Suicide Rate"].quantile(0.25)
        Q3 = grupo["Suicide Rate"].quantile(0.75)
        IQR = Q3 - Q1

        limite_inf = Q1 - 1.5 * IQR
        limite_sup = Q3 + 1.5 * IQR

        outliers = grupo[
            (grupo["Suicide Rate"] < limite_inf) |
            (grupo["Suicide Rate"] > limite_sup)
        ]

        lista.append([pais, len(outliers)])

    resumen = pd.DataFrame(lista, columns=["País", "Cantidad Outliers"])
    resumen = resumen.sort_values("Cantidad Outliers", ascending=False)

    print("=== Países con más outliers detectados ===")
    print(resumen.to_string(index=False))

