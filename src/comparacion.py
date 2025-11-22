import matplotlib.pyplot as plt
import src.data_loader as dl
import pandas as pd

def menu_comparaciones():
    if dl.dataset_global is None:
        print("El dataset no ha sido cargado.")
        return

    print("=== Comparación entre países ===")
    print("1. Ranking anual (mayor a menor tasa).")
    print("2. Ranking histórico (promedio global por país).")
    print("3. Dispersión entre países.")
    print("0. Volver.")

    try:
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Opción inválida.")
        return

    match opcion:
        case 1:
            ranking_anual()
        case 2:
            ranking_historico()
        case 3:
            dispersion_paises()
        case 0:
            return
        case _:
            print("Opción inválida.")


def ranking_anual():
    df = dl.dataset_global

    # Mostrar años disponibles
    years = sorted(df["Year"].unique())
    print("Años disponibles:")
    for i, y in enumerate(years, start=1):
        print(f"{i}. {y}")

    try:
        opcion = int(input("Seleccione un año: "))
        year = years[opcion - 1]
    except:
        print("Opción inválida.")
        return

    df_year = df[df["Year"] == year].copy()

    ranking = df_year.sort_values("Suicide Rate", ascending=False)

    print(f"=== Ranking de países en el año {year} ===")
    print(ranking[["Country Name", "Suicide Rate"]].to_string(index=False))


def ranking_historico():
    df = dl.dataset_global

    ranking = (
        df.groupby("Country Name")["Suicide Rate"]
        .mean()
        .sort_values(ascending=False)
    )

    print("=== Ranking histórico (promedio por país) ===")
    print(ranking.to_frame().to_string())


def dispersion_paises():
    df = dl.dataset_global

    # Calcular promedios por país para representar dispersión
    promedios = df.groupby("Country Name")["Suicide Rate"].mean().reset_index()

    plt.figure(figsize=(10, 5))
    plt.scatter(promedios["Country Name"], promedios["Suicide Rate"])
    plt.xticks(rotation=90)
    plt.title("Dispersión de tasas promedio entre países")
    plt.xlabel("País")
    plt.ylabel("Tasa promedio de suicidio")
    plt.tight_layout()
    plt.show()
