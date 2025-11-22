import matplotlib.pyplot as plt
import src.data_loader as dl

def ver_tendencias():
    if dl.dataset_global is None:
        print("El dataset no ha sido cargado.")
        return

    df = dl.dataset_global

    # Lista de países disponibles
    paises = sorted(df["Country Name"].unique())

    print("=== Paises disponibles ===")
    for i, p in enumerate(paises, start=1):
        print(f"{i}. {p}")

    try:
        opcion = int(input("\nElija un país por número: "))
        pais_seleccionado = paises[opcion - 1]
    except Exception:
        print("Opción inválida.")
        return

    # Filtrar por país
    df_pais = df[df["Country Name"] == pais_seleccionado].sort_values("Year")

    if df_pais.empty:
        print("No hay datos para ese país.")
        return

    # Gráfico de tendencia
    plt.figure(figsize=(10, 5))
    plt.plot(df_pais["Year"], df_pais["Suicide Rate"])
    plt.title(f"Tendencia anual de Suicide Rate en {pais_seleccionado}")
    plt.xlabel("Año")
    plt.ylabel("Tasa de suicidio")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
